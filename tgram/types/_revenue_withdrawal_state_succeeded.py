from typing import Optional

import tgram

from .type_ import Type_


class RevenueWithdrawalStateSucceeded(Type_):
    """
    The withdrawal succeeded.

    Telegram documentation: https://core.telegram.org/bots/api#revenuewithdrawalstatesucceeded

    :param type: Type of the state, always “succeeded”
    :type type: :obj:`str`

    :param date: Date the withdrawal was completed in Unix time
    :type date: :obj:`int`

    :param url: An HTTPS URL that can be used to see transaction details
    :type url: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`RevenueWithdrawalStateSucceeded`
    """

    def __init__(
        self,
        date: "int | None" = None,
        url: "str | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = "succeeded"
        self.date = date
        self.url = url

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RevenueWithdrawalStateSucceeded"]:
        return (
            RevenueWithdrawalStateSucceeded(
                me=me, json=d, type=d.get("type"), date=d.get("date"), url=d.get("url")
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
