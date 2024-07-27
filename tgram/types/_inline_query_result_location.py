import tgram
import random
from .type_ import Type_

from typing import Optional


class InlineQueryResultLocation(Type_):
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultlocation

    :param type: Type of the result, must be location
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 Bytes
    :type id: :obj:`str`

    :param latitude: Location latitude in degrees
    :type latitude: :obj:`float` number

    :param longitude: Location longitude in degrees
    :type longitude: :obj:`float` number

    :param title: Location title
    :type title: :obj:`str`

    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :type horizontal_accuracy: :obj:`float` number

    :param live_period: Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
    :type live_period: :obj:`int`

    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :type heading: :obj:`int`

    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :type proximity_alert_radius: :obj:`int`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the location
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param thumbnail_url: Optional. Url of the thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_width: Optional. Thumbnail width
    :type thumbnail_width: :obj:`int`

    :param thumbnail_height: Optional. Thumbnail height
    :type thumbnail_height: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultLocation`
    """

    def __init__(
        self,
        latitude: "float" = None,
        longitude: "float" = None,
        title: "str" = None,
        horizontal_accuracy: "float" = None,
        live_period: "int" = None,
        heading: "int" = None,
        proximity_alert_radius: "int" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
        input_message_content: "tgram.types.InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "location"
        self.id = random.randint(10000, 99999)
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InlineQueryResultLocation"]:
        return (
            InlineQueryResultLocation(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                horizontal_accuracy=d.get("horizontal_accuracy"),
                live_period=d.get("live_period"),
                heading=d.get("heading"),
                proximity_alert_radius=d.get("proximity_alert_radius"),
                reply_markup=tgram.types.InlineKeyboardMarkup._parse(
                    me=me, d=d.get("reply_markup")
                ),
                input_message_content=tgram.types.InputMessageContent._parse(
                    me=me, d=d.get("input_message_content")
                ),
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
