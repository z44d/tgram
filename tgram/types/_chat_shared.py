import tgram
from .type_ import Type_

from typing import List, Optional


class ChatShared(Type_):
    """
    This object contains information about the chat whose identifier was shared with the bot using a
    `tgram.types.KeyboardButtonRequestChat` button.

    Telegram documentation: https://core.telegram.org/bots/api#Chatshared

    :param request_id: identifier of the request
    :type request_id: :obj:`int`

    :param chat_id: Identifier of the shared chat. This number may have more than 32 significant bits and some programming
        languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit
        integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat
        and could be unable to use this identifier, unless the chat is already known to the bot by some other means.
    :type chat_id: :obj:`int`

    :param title: Optional. Title of the shared chat
    :type title: :obj:`str`

    :param photo: Optional. Array of Photosize
    :type photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param username: Optional. Username of the shared chat
    :type username: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChatShared`
    """

    def __init__(
        self,
        request_id: "int" = None,
        chat_id: "int" = None,
        title: "str" = None,
        username: "str" = None,
        photo: List["tgram.types.PhotoSize"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChatShared"]:
        return (
            ChatShared(
                me=me,
                json=d,
                request_id=d.get("request_id"),
                chat_id=d.get("chat_id"),
                title=d.get("title"),
                username=d.get("username"),
                photo=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
