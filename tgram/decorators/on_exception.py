import tgram

from typing import Callable
from tgram.handlers import Handler


class OnException:
    def on_exception(self=None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            handler = Handler(callback=func, type="exception")
            if isinstance(self, tgram.TgBot):
                self.add_handler(handler, group)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((handler, group))

            return func

        return decorator
