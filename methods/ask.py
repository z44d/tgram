import tgram
from typing import Callable
from tgram.types import Listener


class Ask:
    async def ask(
        self: "tgram.TgBot",
        update_type: str,
        next_step: Callable,
        data: dict = None,
        cancel: Callable = None,
        filters: "tgram.filters.Filter" = None,
    ) -> None:
        return self._listen_handlers.append(
            Listener(
                update_type=update_type,
                next_step=next_step,
                data=data if data is not None else {},
                cancel=cancel,
                filters=filters or tgram.filters.all,
            )
        )
