import tgram
import asyncio
from typing import Callable, Union
from tgram.types import Listener, Message, CallbackQuery, Update

from tgram.errors import CanceledListener


class Ask:
    async def ask(
        self: "tgram.TgBot",
        chat_id: int,
        update_type: str = None,
        user_id: int = None,
        sender_id: int = None,
        cancel: Callable[[Update], bool] = None,
        filters: "tgram.filters.Filter" = None,
        timeout: float = None,
    ) -> Union[Message, CallbackQuery, Update]:
        """
        Waits for a user response matching given filters within a time limit.

        Args:
            chat_id (int): The target chat to listen in.
            update_type (str, optional): Type of update to listen for ('message', 'callback_query', etc.).
            user_id (int, optional): Filter responses to a specific user.
            sender_id (int, optional): Filter responses to a specific sender chat (channel's speaker).
            cancel (Callable[[Update], bool], optional): A function that cancels the waiting when it returns True.
            filters (Filter, optional): Custom filters to match incoming updates.
            timeout (int): Timeout in seconds.

        Returns:
            Union[Message, CallbackQuery, Update]: The matched incoming update.

        Raises:
            TimeoutError: If the user doesn't respond within the timeout period.
        """
        loop = asyncio.get_event_loop()
        future = loop.create_future()

        listener = Listener(
            update_type=update_type,
            chat_id=chat_id,
            user_id=user_id,
            sender_id=sender_id,
            cancel=cancel,
            filters=filters,
            future=future,
        )

        self._listen_handlers.append(listener)

        future.add_done_callback(lambda _: self._listen_handlers.remove(listener))

        try:
            r = await asyncio.wait_for(future, timeout)
            if hasattr(r, "canceled"):
                raise CanceledListener(r)
            return r
        except asyncio.exceptions.TimeoutError:
            raise TimeoutError(
                f"Timeout of {timeout} seconds reached while waiting for user response."
            )
