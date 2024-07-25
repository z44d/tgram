import tgram
from .type_ import Type_

from typing import Optional


class ForumTopicEdited(Type_):
    """
    This object represents a service message about an edited forum topic.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopicedited

    :param name: Optional, Name of the topic(if updated)
    :type name: :obj:`str`

    :param icon_custom_emoji_id: Optional. New identifier of the custom emoji shown as the topic icon, if it was edited;
        an empty string if the icon was removed
    :type icon_custom_emoji_id: :obj:`str`
    """

    def __init__(
        self,
        name: "str" = None,
        icon_custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ForumTopicEdited"]:
        return (
            ForumTopicEdited(
                me=me,
                json=d,
                name=d.get("name"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
