import tgram
import random
from .type_ import Type_

from typing import Optional


class InlineQueryResultVenue(Type_):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinequeryresultvenue

    :param type: Type of the result, must be venue
    :type type: :obj:`str`

    :param id: Unique identifier for this result, 1-64 Bytes
    :type id: :obj:`str`

    :param latitude: Latitude of the venue location in degrees
    :type latitude: :obj:`float`

    :param longitude: Longitude of the venue location in degrees
    :type longitude: :obj:`float`

    :param title: Title of the venue
    :type title: :obj:`str`

    :param address: Address of the venue
    :type address: :obj:`str`

    :param foursquare_id: Optional. Foursquare identifier of the venue if known
    :type foursquare_id: :obj:`str`

    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example,
        “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :type foursquare_type: :obj:`str`

    :param google_place_id: Optional. Google Places identifier of the venue
    :type google_place_id: :obj:`str`

    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :type google_place_type: :obj:`str`

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

    :param input_message_content: Optional. Content of the message to be sent instead of the venue
    :type input_message_content: :class:`tgram.types.InputMessageContent`

    :param thumbnail_url: Optional. Url of the thumbnail for the result
    :type thumbnail_url: :obj:`str`

    :param thumbnail_width: Optional. Thumbnail width
    :type thumbnail_width: :obj:`int`

    :param thumbnail_height: Optional. Thumbnail height
    :type thumbnail_height: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineQueryResultVenue`
    """

    def __init__(
        self,
        latitude: "float" = None,
        longitude: "float" = None,
        title: "str" = None,
        address: "str" = None,
        foursquare_id: "str" = None,
        foursquare_type: "str" = None,
        google_place_id: "str" = None,
        google_place_type: "str" = None,
        reply_markup: "tgram.types.InlineKeyboardMarkup" = None,
        input_message_content: "tgram.types.InputMessageContent" = None,
        thumbnail_url: "str" = None,
        thumbnail_width: "int" = None,
        thumbnail_height: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "venue"
        self.id = random.randint(10000, 99999)
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InlineQueryResultVenue"]:
        return (
            InlineQueryResultVenue(
                me=me,
                json=d,
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                title=d.get("title"),
                address=d.get("address"),
                foursquare_id=d.get("foursquare_id"),
                foursquare_type=d.get("foursquare_type"),
                google_place_id=d.get("google_place_id"),
                google_place_type=d.get("google_place_type"),
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
