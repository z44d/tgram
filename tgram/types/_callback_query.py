import tgram
from .type_ import Type_

from typing import Optional


class CallbackQuery(Type_, tgram.types.CallbackB):
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    Telegram Documentation: https://core.telegram.org/bots/api#callbackquery

    :param id: Unique identifier for this query
    :type id: :obj:`str`

    :param from_user: Sender
    :type from_user: :class:`tgram.types.User`

    :param message: Optional. Message sent by the bot with the callback button that originated the query
    :type message: :class:`tgram.types.Message` or :class:`tgram.types.InaccessibleMessage`

    :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated the
        query.
    :type inline_message_id: :obj:`str`

    :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback
        button was sent. Useful for high scores in games.
    :type chat_instance: :obj:`str`

    :param data: Optional. Data associated with the callback button. Be aware that the message originated the query can
        contain no callback buttons with this data.
    :type data: :obj:`str`

    :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for the game
    :type game_short_name: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.CallbackQuery`
    """

    def __init__(
        self,
        id: "str" = None,
        from_user: "tgram.types.User" = None,
        chat_instance: "str" = None,
        message: "tgram.types.Message" = None,
        inline_message_id: "str" = None,
        data: "str" = None,
        game_short_name: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.CallbackQuery"]:
        return (
            CallbackQuery(
                me=me,
                json=d,
                id=d.get("id"),
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                chat_instance=d.get("chat_instance"),
                message=tgram.types.Message._parse(me=me, d=d.get("message")),
                inline_message_id=d.get("inline_message_id"),
                data=d.get("data"),
                game_short_name=d.get("game_short_name"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
