import tgram
from .type_ import Type_

from typing import List, Optional


class InputTextMessageContent(Type_):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inputtextmessagecontent

    :param message_text: Text of the message to be sent, 1-4096 characters
    :type message_text: :obj:`str`

    :param parse_mode: Optional. Mode for parsing entities in the message text. See formatting options for more
        details.
    :type parse_mode: :obj:`str`

    :param entities: Optional. List of special entities that appear in message text, which can be specified instead of
        parse_mode
    :type entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param disable_web_page_preview: deprecated
    :type disable_web_page_preview: :obj:`bool`

    :param link_preview_options: Optional. Link preview generation options for the message
    :type link_preview_options: :class:`tgram.types.LinkPreviewOptions`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputTextMessageContent`
    """

    def __init__(
        self,
        message_text: "str" = None,
        parse_mode: "str" = None,
        entities: List["tgram.types.MessageEntity"] = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputTextMessageContent"]:
        return (
            InputTextMessageContent(
                me=me,
                json=d,
                message_text=d.get("message_text"),
                parse_mode=d.get("parse_mode"),
                entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("entities")
                ]
                if d.get("entities")
                else None,
                link_preview_options=tgram.types.LinkPreviewOptions._parse(
                    me=me, d=d.get("link_preview_options")
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
