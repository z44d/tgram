import tgram
import asyncio
import logging

from ..errors import MutedError
from ..storage.utils import check_update

from typing import Callable, Any, Union
from collections import OrderedDict

logger = logging.getLogger(__name__)


class Dispatcher:
    async def handler_worker(self: "tgram.TgBot", lock: asyncio.Lock):
        while True:
            update = await self.updates_queue.get()

            if update is None:
                break

            async with lock:
                try:
                    if isinstance(update, tgram.types.Update):
                        try:
                            await check_update(update)
                            await self._check_update(update)
                        except MutedError:
                            continue
                    elif isinstance(update, dict):
                        await self._process_exception(
                            update["e"], update["m"], **update["kwargs"]
                        )
                    elif isinstance(
                        update, (tgram.types.Message, tgram.types.MessageId)
                    ):
                        await self._process_outgoing_message(update)
                except Exception as e:
                    logger.exception(e)

    async def run_for_updates(self: "tgram.TgBot", skip_updates: bool = None) -> None:
        if self.plugins:
            self.load_plugins()

        # Determine offset, allowed updates, and limit based on skip_updates flag
        offset, allowed_updates, limit = (
            -1
            if (self.skip_updates if skip_updates is None else skip_updates)
            else None,
            self.allowed_updates,
            100,
        )
        self.is_running = True

        if not self._me:
            self._me = await self.get_me()

        # Create handler worker tasks
        for _ in range(self.workers):
            self.locks_list.append(asyncio.Lock())
            self.handler_worker_tasks.append(
                self.loop.create_task(self.handler_worker(self.locks_list[-1]))
            )

        logger.info("Started %s Handler Tasks", self.workers)

        while self.is_running:
            try:
                updates = await self.get_updates(
                    offset=offset,
                    limit=limit,
                    allowed_updates=allowed_updates,
                    timeout=55,
                )
                for update in updates:
                    offset = update.update_id + 1
                    self.updates_queue.put_nowait(update)
            except (asyncio.CancelledError, KeyboardInterrupt):
                self.is_running = False
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                logger.exception(e)

        session = await self._get_session()
        await session.close()

    async def _check_cancel(
        self: "tgram.TgBot", callback: Callable, update: Any
    ) -> bool:
        logger.debug("Checking listener in %s func", callback.__name__)
        try:
            if asyncio.iscoroutinefunction(callback):
                return await callback(self, update)
            else:
                return await self.loop.run_in_executor(
                    self.executor, callback, self, update
                )
        except Exception as e:
            logger.exception(e)

    async def _check_listener(
        self: "tgram.TgBot", update: "tgram.types.Update"
    ) -> None:
        for listener in self._listen_handlers:
            if (
                attr := getattr(update, listener.update_type)
                if listener.update_type
                else update
            ) and await listener.filters(self, attr):
                if listener.cancel is not None:
                    result = await self._check_cancel(listener.cancel, attr)
                    if result:
                        setattr(attr, "canceled", True)
                listener.future.set_result(attr)
                raise tgram.ContinuePropagation()

    async def _check_update(self: "tgram.TgBot", update: "tgram.types.Update") -> None:
        for group, group_items in self.groups.items():
            for handler in group_items:
                try:
                    await self._check_listener(update)
                    if handler.type == "all":
                        await self._process_update(update, handler.callback, group)
                    elif handler.type == "exception":
                        continue
                    elif (
                        attr := getattr(update, handler.type)
                    ) and await handler.filter(self, attr):
                        await self._process_update(attr, handler.callback, group)
                except tgram.StopPropagation:
                    return
                except tgram.ContinuePropagation:
                    continue
                except Exception as e:
                    logger.exception(e)
                    continue

    async def _process_update(
        self: "tgram.TgBot", update: Any, callback: Callable, group: int
    ) -> None:
        if hasattr(update, "_groups") and group in getattr(update, "_groups"):
            return
        if not hasattr(update, "_groups"):
            update._groups = []
        update._groups.append(group)
        logger.debug("Processing update to %s func", callback.__name__)
        try:
            if asyncio.iscoroutinefunction(callback):
                await callback(self, update)
            else:
                await self.loop.run_in_executor(self.executor, callback, self, update)
        except tgram.StopPropagation:
            raise
        except tgram.ContinuePropagation:
            update._groups.remove(group)
            raise
        except Exception as e:
            logger.exception(e)

    async def _process_exception(
        self: "tgram.TgBot", exception: Exception, method: str, **kwargs
    ) -> None:
        for group_items in self.groups.values():
            for handler in group_items:
                try:
                    if handler.type == "exception":
                        logger.debug(
                            "Processing exception to %s func", handler.callback.__name__
                        )
                        if asyncio.iscoroutinefunction(handler.callback):
                            await handler.callback(self, exception, method, **kwargs)
                        else:
                            await self.loop.run_in_executor(
                                self.executor,
                                handler.callback,
                                self,
                                exception,
                                method,
                                **kwargs,
                            )
                except Exception as e:
                    logger.exception(e)
                    continue

    async def _process_outgoing_message(
        self: "tgram.TgBot",
        message: Union["tgram.types.Message", "tgram.types.MessageId"],
    ) -> None:
        for group_items in self.groups.values():
            for handler in group_items:
                try:
                    if handler.type == "outgoing":
                        logger.debug(
                            "Processing outgoing to %s func", handler.callback.__name__
                        )
                        if asyncio.iscoroutinefunction(handler.callback):
                            await handler.callback(self, message)
                        else:
                            await self.loop.run_in_executor(
                                self.executor, handler.callback, self, message
                            )
                except Exception as e:
                    logger.exception(e)
                    continue

    async def _add_grouped_handler(
        self: "tgram.TgBot", handler: "tgram.handlers.Handler", group: int
    ):
        for lock in self.locks_list:
            await lock.acquire()

        try:
            if group not in self.groups:
                self.groups[group] = []
                self.groups = OrderedDict(sorted(self.groups.items()))

            self.groups[group].append(handler)
            logger.info(
                "(%s) added to %s handlers in group %s",
                handler.callback.__name__,
                "Update." + handler.type if handler.type != "all" else "all",
                group,
            )
        finally:
            for lock in self.locks_list:
                lock.release()

    async def _remove_grouped_handler(
        self: "tgram.TgBot", handler: "tgram.handlers.Handler", group: int
    ):
        for lock in self.locks_list:
            await lock.acquire()

        try:
            if group not in self.groups:
                raise ValueError(
                    f"Group {group} does not exist. Handler was not removed."
                )

            self.groups[group].remove(handler)
            logger.info(
                "(%s) removed from %s handlers from group %s",
                handler.callback.__name__,
                "Update." + handler.type if handler.type != "all" else "all",
                group,
            )
        finally:
            for lock in self.locks_list:
                lock.release()
