import tgram
from .type_ import Type_

from typing import Optional


class PreparedInlineMessage(Type_):
    """
    Describes an inline message to be sent by a user of a Mini App.

    Telegram Documentation: https://core.telegram.org/bots/api#preparedinlinemessage

    :param id: Unique identifier of the prepared message
    :type id: :obj:`str`

    :param expiration_date: Expiration date of the prepared message, in Unix time.
    Expired prepared messages can no longer be used
    :type expiration_date: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PreparedInlineMessage`
    """

    def __init__(
        self,
        id: "str" = None,
        expiration_date: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.expiration_date = expiration_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PreparedInlineMessage"]:
        return (
            PreparedInlineMessage(
                me=me,
                json=d,
                id=d.get("id"),
                expiration_date=d.get("expiration_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
