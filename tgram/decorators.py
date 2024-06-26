import tgram

from typing import Callable
from .handlers import Handler, Handlers
from .filters import Filter, all


class Decorators:
    def on_all(self: "tgram.TgBot"):
        def decorator(func: Callable) -> Callable:
            self.add_handler(Handler(callback=func))
            return func

        return decorator

    def on_message(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(callback=func, type=Handlers.MESSAGE, filters=filters or all)
            )
            return func

        return decorator

    def on_edited_message(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func, type=Handlers.EDITED_MESSAGE, filters=filters or all
                )
            )
            return func

        return decorator

    def on_channel_post(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func, type=Handlers.CHANNEL_POST, filters=filters or all
                )
            )
            return func

        return decorator

    def on_edited_channel_post(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.EDITED_CHANNEL_POST,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_business_connection(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.BUSINESS_CONNECTION,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_business_message(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.BUSINESS_MESSAGE,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_edited_business_message(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.EDITED_BUSINESS_MESSAGE,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_deleted_business_messages(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.DELETED_BUSINESS_MESSAGES,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_message_reaction(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.MESSAGE_REACTION,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_message_reaction_count(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.MESSAGE_REACTION_COUNT,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_inline_query(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func, type=Handlers.INLINE_QUERY, filters=filters or all
                )
            )
            return func

        return decorator

    def on_chosen_inline_result(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.CHOSEN_INLINE_RESULT,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_callback_query(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func, type=Handlers.CALLBACK_QUERY, filters=filters or all
                )
            )
            return func

        return decorator

    def on_shipping_query(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func, type=Handlers.SHIPPING_QUERY, filters=filters or all
                )
            )
            return func

        return decorator

    def on_pre_checkout_query(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.PRE_CHECKOUT_QUERY,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_poll(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(callback=func, type=Handlers.POLL, filters=filters or all)
            )
            return func

        return decorator

    def on_poll_answer(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func, type=Handlers.POLL_ANSWER, filters=filters or all
                )
            )
            return func

        return decorator

    def on_my_chat_member(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func, type=Handlers.MY_CHAT_MEMBER, filters=filters or all
                )
            )
            return func

        return decorator

    def on_chat_member(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func, type=Handlers.CHAT_MEMBER, filters=filters or all
                )
            )
            return func

        return decorator

    def on_chat_join_request(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.CHAT_JOIN_REQUEST,
                    filters=filters or all,
                )
            )
            return func

        return decorator

    def on_chat_boost(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(callback=func, type=Handlers.CHAT_BOOST, filters=filters or all)
            )
            return func

        return decorator

    def on_removed_chat_boost(self: "tgram.TgBot", filters: Filter = None):
        def decorator(func: Callable) -> Callable:
            self.add_handler(
                Handler(
                    callback=func,
                    type=Handlers.REMOVED_CHAT_BOOST,
                    filters=filters or all,
                )
            )
            return func

        return decorator
