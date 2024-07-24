import tgram

from typing import Callable
from tgram.handlers import Handler, Handlers
from tgram.filters import Filter, all


class OnInlineQuery:
    def on_inline_query(self=None, filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            handler = Handler(
                callback=func,
                type=Handlers.INLINE_QUERY,
                filters=self if isinstance(self, Filter) else (filters or all),
            )
            if isinstance(self, tgram.TgBot):
                self.add_handler(handler)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(handler)

            return func

        return decorator
