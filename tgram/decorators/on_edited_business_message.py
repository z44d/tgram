from collections.abc import Callable

import tgram
from tgram.filters import Filter, all
from tgram.handlers import Handler, Handlers


class OnEditedBusinessMessage:
    def on_edited_business_message(self=None, filters: Filter = None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            handler = Handler(
                callback=func,
                type=Handlers.EDITED_BUSINESS_MESSAGE,
                filters=self if isinstance(self, Filter) else (filters or all),
            )
            if isinstance(self, tgram.TgBot):
                self.add_handler(handler, group)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((handler, group))

            return func

        return decorator
