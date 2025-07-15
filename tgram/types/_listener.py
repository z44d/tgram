import asyncio
from .type_ import Type_

from typing import Callable
from tgram import filters as ff


class Listener(Type_):
    def __init__(
        self,
        chat_id: int,
        future: asyncio.Future,
        user_id: int = None,
        sender_id: int = None,
        update_type: str = None,
        cancel: Callable = None,
        filters: "ff.Filter" = "ff.all",
    ) -> None:
        super().__init__(None, None)
        self.update_type = update_type
        self.chat_id = chat_id
        self.future = future
        self.user_id = user_id
        self.sender_id = sender_id
        self.cancel = cancel
        self.filters = (
            (filters)
            & ff.chat(chat_id)
            & (ff.user(user_id) if user_id else ff.all)
            & (ff.sender(sender_id) if sender_id else ff.all)
        )
