import tgram
from .type_ import Type_
from typing import Optional


class StoryAreaPosition(Type_):
    """
    Describes the position of a clickable area within a story.

    :param x_percentage: The abscissa of the area's center, as a percentage of the media width
    :type x_percentage: :obj:`float`
    :param y_percentage: The ordinate of the area's center, as a percentage of the media height
    :type y_percentage: :obj:`float`
    :param width_percentage: The width of the area's rectangle, as a percentage of the media width
    :type width_percentage: :obj:`float`
    :param height_percentage: The height of the area's rectangle, as a percentage of the media height
    :type height_percentage: :obj:`float`
    :param rotation_angle: The clockwise rotation angle of the rectangle, in degrees; 0-360
    :type rotation_angle: :obj:`float`
    :param corner_radius_percentage: The radius of the rectangle corner rounding, as a percentage of the media width
    :type corner_radius_percentage: :obj:`float`
    """

    def __init__(
        self,
        x_percentage: float = None,
        y_percentage: float = None,
        width_percentage: float = None,
        height_percentage: float = None,
        rotation_angle: float = None,
        corner_radius_percentage: float = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.x_percentage = x_percentage
        self.y_percentage = y_percentage
        self.width_percentage = width_percentage
        self.height_percentage = height_percentage
        self.rotation_angle = rotation_angle
        self.corner_radius_percentage = corner_radius_percentage

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["StoryAreaPosition"]:
        return (
            StoryAreaPosition(
                x_percentage=d.get("x_percentage"),
                y_percentage=d.get("y_percentage"),
                width_percentage=d.get("width_percentage"),
                height_percentage=d.get("height_percentage"),
                rotation_angle=d.get("rotation_angle"),
                corner_radius_percentage=d.get("corner_radius_percentage"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class StoryAreaTypeLocation(Type_):
    """
    Describes a story area pointing to a location.

    :param type: Type of the area, always "location"
    :type type: :obj:`str`
    :param latitude: Location latitude in degrees
    :type latitude: :obj:`float`
    :param longitude: Location longitude in degrees
    :type longitude: :obj:`float`
    :param address: Optional. Address of the location
    :type address: :obj:`LocationAddress`
    """

    def __init__(
        self,
        latitude: float = None,
        longitude: float = None,
        address: "tgram.types.LocationAddress" = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "location"
        self.latitude = latitude
        self.longitude = longitude
        self.address = address

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["StoryAreaTypeLocation"]:
        return (
            StoryAreaTypeLocation(
                latitude=d.get("latitude"),
                longitude=d.get("longitude"),
                address=tgram.types.LocationAddress._parse(me=me, d=d.get("address"))
                if d.get("address")
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


class StoryAreaTypeSuggestedReaction(Type_):
    """
    Describes a story area pointing to a suggested reaction.

    :param type: Type of the area, always "suggested_reaction"
    :type type: :obj:`str`
    :param reaction_type: Type of the reaction
    :type reaction_type: :obj:`ReactionType`
    :param is_dark: Optional. Pass True if the reaction area has a dark background
    :type is_dark: :obj:`bool`
    :param is_flipped: Optional. Pass True if reaction area corner is flipped
    :type is_flipped: :obj:`bool`
    """

    def __init__(
        self,
        reaction_type: "tgram.types.ReactionType" = None,
        is_dark: bool = None,
        is_flipped: bool = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "suggested_reaction"
        self.reaction_type = reaction_type
        self.is_dark = is_dark
        self.is_flipped = is_flipped

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["StoryAreaTypeSuggestedReaction"]:
        return (
            StoryAreaTypeSuggestedReaction(
                reaction_type=(
                    tgram.types.ReactionTypeCustomEmoji._parse(
                        me, d.get("reaction_type")
                    )
                    if d["reaction_type"]["type"] == "custom_emoji"
                    else tgram.types.ReactionTypeEmoji._parse(
                        me, d.get("reaction_type")
                    )
                    if d["reaction_type"]["type"] == "emoji"
                    else tgram.types.ReactionTypePaid._parse(me, d.get("reaction_type"))
                )
                if d.get("reaction_type")
                else None,
                is_dark=d.get("is_dark"),
                is_flipped=d.get("is_flipped"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class StoryAreaTypeLink(Type_):
    """
    Describes a story area pointing to an HTTP or tg:// link.

    :param type: Type of the area, always "link"
    :type type: :obj:`str`
    :param url: HTTP or tg:// URL to be opened when the area is clicked
    :type url: :obj:`str`
    """

    def __init__(
        self,
        url: str = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "link"
        self.url = url

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["StoryAreaTypeLink"]:
        return (
            StoryAreaTypeLink(
                url=d.get("url"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class StoryAreaTypeWeather(Type_):
    """
    Describes a story area containing weather information.

    :param type: Type of the area, always "weather"
    :type type: :obj:`str`
    :param temperature: Temperature, in degree Celsius
    :type temperature: :obj:`float`
    :param emoji: Emoji representing the weather
    :type emoji: :obj:`str`
    :param background_color: A color of the area background in the ARGB format
    :type background_color: :obj:`int`
    """

    def __init__(
        self,
        temperature: float = None,
        emoji: str = None,
        background_color: int = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "weather"
        self.temperature = temperature
        self.emoji = emoji
        self.background_color = background_color

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["StoryAreaTypeWeather"]:
        return (
            StoryAreaTypeWeather(
                temperature=d.get("temperature"),
                emoji=d.get("emoji"),
                background_color=d.get("background_color"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class StoryAreaTypeUniqueGift(Type_):
    """
    Describes a story area pointing to a unique gift.

    :param type: Type of the area, always "unique_gift"
    :type type: :obj:`str`
    :param name: Unique name of the gift
    :type name: :obj:`str`
    """

    def __init__(
        self,
        name: str = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "unique_gift"
        self.name = name

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["StoryAreaTypeUniqueGift"]:
        return (
            StoryAreaTypeUniqueGift(
                name=d.get("name"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class StoryArea(Type_):
    """
    Describes a clickable area on a story media.

    :param position: Position of the area
    :type position: :obj:`StoryAreaPosition`
    :param type: Type of the area
    :type type: :obj:`StoryAreaType`
    """

    def __init__(
        self,
        position: StoryAreaPosition = None,
        type: "tgram.types.StoryAreaType" = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.position = position
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["StoryArea"]:
        return (
            StoryArea(
                position=StoryAreaPosition._parse(me=me, d=d.get("position"))
                if d.get("position")
                else None,
                type=d.get("type"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
