import asyncio
import functools
import inspect
import threading
import logging

logger = logging.getLogger(__name__)

def async_to_sync(obj, name):
    function = getattr(obj, name)
    main_loop = asyncio.get_event_loop()

    def async_to_sync_gen(agen, loop, is_main_thread):
        async def anext(agen):
            try:
                return await agen.__anext__(), False
            except StopAsyncIteration:
                return None, True
            except Exception as e:
                logger.error(f"Error in async generator: {e}")
                return None, True

        while True:
            try:
                if is_main_thread:
                    item, done = loop.run_until_complete(anext(agen))
                else:
                    item, done = asyncio.run_coroutine_threadsafe(
                        anext(agen), loop
                    ).result()

                if done:
                    break

                yield item
            except Exception as e:
                logger.error(f"Error while running async generator: {e}")
                break

    @functools.wraps(function)
    def async_to_sync_wrap(*args, **kwargs):
        coroutine = function(*args, **kwargs)

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        if threading.current_thread() is threading.main_thread() or not main_loop.is_running():
            if loop.is_running():
                return coroutine
            else:
                if inspect.iscoroutine(coroutine):
                    try:
                        return loop.run_until_complete(coroutine)
                    except (asyncio.CancelledError, KeyboardInterrupt):
                        logger.info(f"\nThe process {coroutine.__name__} got killed")
                    except Exception as e:
                        logger.error(f"Error in coroutine execution: {e}")
                        raise

                if inspect.isasyncgen(coroutine):
                    return async_to_sync_gen(coroutine, loop, True)
        else:
            if inspect.iscoroutine(coroutine):
                if loop.is_running():
                    async def coro_wrapper():
                        try:
                            return await asyncio.wrap_future(
                                asyncio.run_coroutine_threadsafe(coroutine, main_loop)
                            )
                        except Exception as e:
                            logger.error(f"Error in coroutine wrapper: {e}")
                            raise

                    return coro_wrapper()
                else:
                    try:
                        return asyncio.run_coroutine_threadsafe(
                            coroutine, main_loop
                        ).result()
                    except Exception as e:
                        logger.error(f"Error in coroutine thread-safe execution: {e}")
                        raise

            if inspect.isasyncgen(coroutine):
                if loop.is_running():
                    return coroutine
                else:
                    return async_to_sync_gen(coroutine, main_loop, False)

    setattr(obj, name, async_to_sync_wrap)


def wrap(source):
    for name in dir(source):
        method = getattr(source, name)

        if not name.startswith("_"):
            if inspect.iscoroutinefunction(method) or inspect.isasyncgenfunction(method):
                async_to_sync(source, name)
