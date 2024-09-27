import tgram
from .type_ import Type_

from typing import Optional


class MessageEntity(Type_):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    Telegram Documentation: https://core.telegram.org/bots/api#messageentity

    :param type: Type of the entity. Currently, can be “mention” (@username), “hashtag” (#hashtag), “cashtag” ($USD),
        “bot_command” (/start@jobs_bot),“url” (https://telegram.org), “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123),
        “bold” (bold text), “italic” (italic text), “underline” (underlined text), “strikethrough” (strikethrough text),
        “spoiler” (spoiler message), “blockquote” (block quotation), “expandable_blockquote” (collapsed-by-default block quotation),
        “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs),
        “text_mention” (for users without usernames), “custom_emoji” (for inline custom emoji stickers)
    :type type: :obj:`str`

    :param offset: Offset in UTF-16 code units to the start of the entity
    :type offset: :obj:`int`

    :param length: Length of the entity in UTF-16 code units
    :type length: :obj:`int`

    :param url: Optional. For “text_link” only, URL that will be opened after user taps on the text
    :type url: :obj:`str`

    :param user: Optional. For “text_mention” only, the mentioned user
    :type user: :class:`tgram.types.User`

    :param language: Optional. For “pre” only, the programming language of the entity text
    :type language: :obj:`str`

    :param custom_emoji_id: Optional. For “custom_emoji” only, unique identifier of the custom emoji.
        Use get_custom_emoji_stickers to get full information about the sticker.
    :type custom_emoji_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.MessageEntity`
    """

    def __init__(
        self,
        type: "tgram.types.MessageEntityType" = None,
        offset: "int" = None,
        length: "int" = None,
        url: "str" = None,
        user: "tgram.types.User" = None,
        language: "str" = None,
        custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MessageEntity"]:
        return (
            MessageEntity(
                me=me,
                json=d,
                type=d.get("type"),
                offset=d.get("offset"),
                length=d.get("length"),
                url=d.get("url"),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                language=d.get("language"),
                custom_emoji_id=d.get("custom_emoji_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
