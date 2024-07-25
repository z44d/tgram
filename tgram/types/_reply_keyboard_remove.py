import tgram
from .type_ import Type_

from typing import Optional


class ReplyKeyboardRemove(Type_):
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    Telegram Documentation: https://core.telegram.org/bots/api#replykeyboardremove

    :param remove_keyboard: Requests clients to remove the custom keyboard (user will not be able to summon this
        keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in
        ReplyKeyboardMarkup)
        Note that this parameter is set to True by default by the library. You cannot modify it.
    :type remove_keyboard: :obj:`bool`

    :param selective: Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets:
        1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has
        reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation
        message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options
        to users who haven't voted yet.
    :type selective: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ReplyKeyboardRemove`
    """

    def __init__(
        self,
        remove_keyboard: "bool" = None,
        selective: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.remove_keyboard = remove_keyboard
        self.selective = selective

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ReplyKeyboardRemove"]:
        return (
            ReplyKeyboardRemove(
                me=me,
                json=d,
                remove_keyboard=d.get("remove_keyboard"),
                selective=d.get("selective"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
