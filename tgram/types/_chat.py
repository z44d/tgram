import tgram
from .type_ import Type_

from typing import Optional


class Chat(Type_):
    """
    In BotAPI 7.3 Chat was reduced and full info moved to ChatFullInfo:
    "Split out the class ChatFullInfo from the class Chat and changed the return type of the method getChat to ChatFullInfo."

    https://core.telegram.org/bots/api#chatfullinfo

    Currently Chat is left as full copy of ChatFullInfo for compatibility.
    """

    def __init__(
        self,
        id: "int" = None,
        type: "str" = None,
        title: "str" = None,
        username: "str" = None,
        first_name: "str" = None,
        last_name: "str" = None,
        is_forum: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Chat"]:
        return (
            Chat(
                me=me,
                json=d,
                id=d.get("id"),
                type=d.get("type"),
                title=d.get("title"),
                username=d.get("username"),
                first_name=d.get("first_name"),
                last_name=d.get("last_name"),
                is_forum=d.get("is_forum"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
