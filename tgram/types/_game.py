import tgram
from .type_ import Type_

from typing import List, Optional


class Game(Type_):
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Telegram Documentation: https://core.telegram.org/bots/api#game

    :param title: Title of the game
    :type title: :obj:`str`

    :param description: Description of the game
    :type description: :obj:`str`

    :param photo: Photo that will be displayed in the game message in chats.
    :type photo: :obj:`list` of :class:`tgram.types.PhotoSize`

    :param text: Optional. Brief description of the game or high scores included in the game message. Can be
        automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited
        using editMessageText. 0-4096 characters.
    :type text: :obj:`str`

    :param text_entities: Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    :type text_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param animation: Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
    :type animation: :class:`tgram.types.Animation`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Game`
    """

    def __init__(
        self,
        title: "str" = None,
        description: "str" = None,
        photo: List["tgram.types.PhotoSize"] = None,
        text: "str" = None,
        text_entities: List["tgram.types.MessageEntity"] = None,
        animation: "tgram.types.Animation" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Game"]:
        return (
            Game(
                me=me,
                json=d,
                title=d.get("title"),
                description=d.get("description"),
                photo=[tgram.types.PhotoSize._parse(me=me, d=i) for i in d.get("photo")]
                if d.get("photo")
                else None,
                text=d.get("text"),
                text_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("text_entities")
                ]
                if d.get("text_entities")
                else None,
                animation=tgram.types.Animation._parse(me=me, d=d.get("animation")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
