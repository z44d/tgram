import tgram
from .type_ import Type_

from typing import Optional


class ForceReply(Type_):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Telegram Documentation: https://core.telegram.org/bots/api#forcereply

    :param force_reply: Shows reply interface to the user, as if they manually selected the bot's message and tapped
        'Reply'
    :type force_reply: :obj:`bool`

    :param input_field_placeholder: Optional. The placeholder to be shown in the input field when the reply is active;
        1-64 characters
    :type input_field_placeholder: :obj:`str`

    :param selective: Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users
        that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same
        chat and forum topic, sender of the original message.
    :type selective: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ForceReply`
    """

    def __init__(
        self,
        force_reply: "bool" = None,
        input_field_placeholder: "str" = None,
        selective: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ForceReply"]:
        return (
            ForceReply(
                me=me,
                json=d,
                force_reply=d.get("force_reply"),
                input_field_placeholder=d.get("input_field_placeholder"),
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
