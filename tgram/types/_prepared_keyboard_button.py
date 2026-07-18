import tgram
from .type_ import Type_

from typing import Optional


class PreparedKeyboardButton(Type_):
    """
    This object represents a keyboard button prepared by the bot to be sent by a user of a Mini App.

    Telegram Documentation: https://core.telegram.org/bots/api#preparedkeyboardbutton

    :param request_users: Optional. If specified, pressing the button will open a list of suitable users.
        Identifiers of selected users will be sent to the bot in a “users_shared” service message.
    :type request_users: :class:`tgram.types.KeyboardButtonRequestUsers`

    :param request_chat: Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will
        send its identifier to the bot in a “chat_shared” service message.
    :type request_chat: :class:`tgram.types.KeyboardButtonRequestChat`

    :param request_managed_bot: Optional. If specified, the user will be asked to create a managed bot and share its identifier.
    :type request_managed_bot: :class:`tgram.types.KeyboardButtonRequestManagedBot`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PreparedKeyboardButton`
    """

    def __init__(
        self,
        request_users: "tgram.types.KeyboardButtonRequestUsers" = None,
        request_chat: "tgram.types.KeyboardButtonRequestChat" = None,
        request_managed_bot: "tgram.types.KeyboardButtonRequestManagedBot" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_managed_bot = request_managed_bot

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PreparedKeyboardButton"]:
        return (
            PreparedKeyboardButton(
                me=me,
                json=d,
                request_users=tgram.types.KeyboardButtonRequestUsers._parse(
                    me=me, d=d.get("request_users")
                ),
                request_chat=tgram.types.KeyboardButtonRequestChat._parse(
                    me=me, d=d.get("request_chat")
                ),
                request_managed_bot=tgram.types.KeyboardButtonRequestManagedBot._parse(
                    me=me, d=d.get("request_managed_bot")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
