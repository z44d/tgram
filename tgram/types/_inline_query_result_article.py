import tgram
import random
from .type_ import Type_

from typing import Optional


class InlineQueryResultArticle(Type_):
    """
    Represents a link to an article or web page.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultarticle

    :param type: Type of the result, must be article
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 Bytes
    :type id: :obj:`str`

    :param title: Title of the result
    :type title: :obj:`str`

    :param input_message_content: Content of the message to be sent
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param url: Optional. URL of the result
    :type url: :obj:`str`

    :param description: Optional. Short description of the result
    :type description: :obj:`str`

    :param thumbnail_url: Optional. Url of the thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_width: Optional. Thumbnail width
    :type thumbnail_width: :obj:`int`

    :param thumbnail_height: Optional. Thumbnail height
    :type thumbnail_height: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultArticle`
    """

    def __init__(
        self,
        title: "str" = None,
        input_message_content: "tgram.types.InputMessageContent" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
        url: "str" = None,
        description: "str" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "article"
        self.id = random.randint(10000, 99999)
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InlineQueryResultArticle"]:
        return (
            InlineQueryResultArticle(
                me=me,
                json=d,
                title=d.get("title"),
                input_message_content=tgram.types.InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
                reply_markup=tgram.types.InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                url=d.get("url"),
                description=d.get("description"),
                thumbnail_url=d.get("thumbnail_url"),
                thumbnail_width=d.get("thumbnail_width"),
                thumbnail_height=d.get("thumbnail_height"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
