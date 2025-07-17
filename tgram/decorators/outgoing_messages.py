import tgram

from typing import Callable
from tgram.handlers import Handler


class OutgoingMessage:
    def outgoing_message(self=None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            handler = Handler(callback=func, type="outgoing")
            if isinstance(self, tgram.TgBot):
                self.add_handler(handler, group)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((handler, group))

            return func

        return decorator

    def edited_outgoing_message(self=None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            handler = Handler(callback=func, type="e-outgoing")
            if isinstance(self, tgram.TgBot):
                self.add_handler(handler, group)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((handler, group))

            return func

        return decorator
