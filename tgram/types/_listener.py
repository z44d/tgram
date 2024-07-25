import tgram
from .type_ import Type_

from typing import Callable


class Listener(Type_):
    def __init__(
        self,
        update_type: str = None,
        next_step: Callable = None,
        data: dict = None,
        cancel: Callable = None,
        filters: "tgram.filters.Filter" = None,
    ) -> None:
        super().__init__(None, None)
        self.update_type = update_type
        self.next_step = next_step
        self.data = data
        self.cancel = cancel
        self.filters = filters
