import tgram
from .type_ import Type_

from typing import Optional


class KeyboardButton(Type_):
    """
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive.

    Telegram Documentation: https://core.telegram.org/bots/api#keyboardbutton

    :param text: Text of the button. If none of the optional fields are used, it will be sent as a message when the button is
        pressed
    :type text: :obj:`str`

    :param request_contact: Optional. If True, the user's phone number will be sent as a contact when the button is
        pressed. Available in private chats only.
    :type request_contact: :obj:`bool`

    :param request_location: Optional. If True, the user's current location will be sent when the button is pressed.
        Available in private chats only.
    :type request_location: :obj:`bool`

    :param request_poll: Optional. If specified, the user will be asked to create a poll and send it to the bot when the
        button is pressed. Available in private chats only.
    :type request_poll: :class:`tgram.types.KeyboardButtonPollType`

    :param web_app: Optional. If specified, the described Web App will be launched when the button is pressed. The Web App
        will be able to send a “web_app_data” service message. Available in private chats only.
    :type web_app: :class:`tgram.types.WebAppInfo`

    :param request_user: deprecated
    :type request_user: :class:`tgram.types.KeyboardButtonRequestUser`

    :param request_users: Optional. If specified, pressing the button will open a list of suitable users.
        Identifiers of selected users will be sent to the bot in a “users_shared” service message. Available in private chats only.
    :type request_users: :class:`tgram.types.KeyboardButtonRequestUsers`

    :param request_chat: Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will
        send its identifier to the bot in a “chat_shared” service message. Available in private chats only.
    :type request_chat: :class:`tgram.types.KeyboardButtonRequestChat`

    :param icon_custom_emoji_id: Optional. Unique identifier of the custom emoji shown before the text of the button
    :type icon_custom_emoji_id: :obj:`str`

    :param style: Optional. Style of the button. Must be one of “danger”, “success”, or “primary”
    :type style: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.KeyboardButton`
    """

    def __init__(
        self,
        text: "str" = None,
        request_users: "tgram.types.KeyboardButtonRequestUsers" = None,
        request_chat: "tgram.types.KeyboardButtonRequestChat" = None,
        request_contact: "bool" = None,
        request_location: "bool" = None,
        request_poll: "tgram.types.KeyboardButtonPollType" = None,
        web_app: "tgram.types.WebAppInfo" = None,
        icon_custom_emoji_id: "str" = None,
        style: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app
        self.icon_custom_emoji_id = icon_custom_emoji_id
        self.style = style

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.KeyboardButton"]:
        return (
            KeyboardButton(
                me=me,
                json=d,
                text=d.get("text"),
                request_users=tgram.types.KeyboardButtonRequestUsers._parse(
                    me=me, d=d.get("request_users")
                ),
                request_chat=tgram.types.KeyboardButtonRequestChat._parse(
                    me=me, d=d.get("request_chat")
                ),
                request_contact=d.get("request_contact"),
                request_location=d.get("request_location"),
                request_poll=tgram.types.KeyboardButtonPollType._parse(
                    me=me, d=d.get("request_poll")
                ),
                web_app=tgram.types.WebAppInfo._parse(me=me, d=d.get("web_app")),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
                style=d.get("style"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
