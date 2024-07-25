import tgram
from .type_ import Type_

from typing import Optional


class BotCommand(Type_):
    """
    This object represents a bot command.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommand

    :param command: Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and
        underscores.
    :type command: :obj:`str`

    :param description: Description of the command; 1-256 characters.
    :type description: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommand`
    """

    def __init__(
        self,
        command: "str" = None,
        description: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.command = command
        self.description = description

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BotCommand"]:
        return (
            BotCommand(
                me=me,
                json=d,
                command=d.get("command"),
                description=d.get("description"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
