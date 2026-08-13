from typing import Optional

import tgram

from .type_ import Type_


class ForumTopicClosed(Type_):
    """
    This object represents a service message about a forum topic closed in the chat. Currently holds no information.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopicclosed
    """

    def __init__(
        self,
        name: "str | None" = None,
        icon_custom_emoji_id: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.ForumTopicClosed"]:
        return (
            ForumTopicClosed(
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
