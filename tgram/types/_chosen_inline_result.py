import tgram
from .type_ import Type_

from typing import Optional

from tgram import bound


class ChosenInlineResult(Type_, bound.ChosenInlineResultB):
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.

    Telegram Documentation: https://core.telegram.org/bots/api#choseninlineresult

    :param result_id: The unique identifier for the result that was chosen
    :type result_id: :obj:`str`

    :param from: The user that chose the result
    :type from: :class:`tgram.types.User`

    :param location: Optional. Sender location, only for bots that require user location
    :type location: :class:`tgram.types.Location`

    :param inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline
        keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
    :type inline_message_id: :obj:`str`

    :param query: The query that was used to obtain the result
    :type query: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ChosenInlineResult`
    """

    def __init__(
        self,
        result_id: "str" = None,
        from_user: "tgram.types.User" = None,
        query: "str" = None,
        location: "tgram.types.Location" = None,
        inline_message_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.result_id = result_id
        self.from_user = from_user
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ChosenInlineResult"]:
        return (
            ChosenInlineResult(
                me=me,
                json=d,
                result_id=d.get("result_id"),
                from_user=tgram.types.User._parse(me=me, d=d.get("from")),
                query=d.get("query"),
                location=tgram.types.Location._parse(me=me, d=d.get("location")),
                inline_message_id=d.get("inline_message_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
