import tgram
from .type_ import Type_

from typing import Optional


class ForumTopicCreated(Type_):
    """
    This object represents a service message about a new forum topic created in the chat.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopiccreated

    :param name: Name of the topic
    :type name: :obj:`str`

    :param icon_color: Color of the topic icon in RGB format
    :type icon_color: :obj:`int`

    :param icon_custom_emoji_id: Optional. Unique identifier of the custom emoji shown as the topic icon
    :type icon_custom_emoji_id: :obj:`str`

    :param is_name_implicit: Optional. True, if the topic name was automatically set based on the sender's name
    :type is_name_implicit: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ForumTopicCreated`
    """

    def __init__(
        self,
        name: "str" = None,
        icon_color: "int" = None,
        icon_custom_emoji_id: "str" = None,
        is_name_implicit: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id
        self.is_name_implicit = is_name_implicit

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ForumTopicCreated"]:
        return (
            ForumTopicCreated(
                me=me,
                json=d,
                name=d.get("name"),
                icon_color=d.get("icon_color"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
                is_name_implicit=d.get("is_name_implicit"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
