import tgram
from .type_ import Type_

from typing import Optional


class Story(Type_):
    """
    This object represents a story.

    Telegram documentation: https://core.telegram.org/bots/api#story

    :param chat: Chat that posted the story
    :type chat: :class:`tgram.types.Chat`

    :param id: Unique identifier for the story in the chat
    :type id: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`Story`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        id: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.id = id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Story"]:
        return (
            Story(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                id=d.get("id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
