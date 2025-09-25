import tgram
from .type_ import Type_
from typing import Optional


class SuggestedPostPrice(Type_):
    """
    Describes the price of a suggested post.

    :param currency: Currency in which the post will be paid. Must be "XTR" for Telegram Stars or "TON" for toncoins.
    :type currency: :obj:`str`
    :param amount: The amount of the currency that will be paid for the post in the smallest units of the currency.
    :type amount: :obj:`int`
    """

    def __init__(
        self,
        currency: str = None,
        amount: int = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.currency = currency
        self.amount = amount

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuggestedPostPrice"]:
        return (
            SuggestedPostPrice(
                me=me,
                json=d,
                currency=d.get("currency"),
                amount=d.get("amount"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class SuggestedPostInfo(Type_):
    """
    Contains information about a suggested post.

    :param state: State of the suggested post. Can be "pending", "approved", or "declined".
    :type state: :obj:`str`
    :param price: Optional. Proposed price of the post.
    :type price: :class:`tgram.types.SuggestedPostPrice`
    :param send_date: Optional. Proposed send date of the post.
    :type send_date: :obj:`int`
    """

    def __init__(
        self,
        state: str = None,
        price: "tgram.types.SuggestedPostPrice" = None,
        send_date: int = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.state = state
        self.price = price
        self.send_date = send_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuggestedPostInfo"]:
        return (
            SuggestedPostInfo(
                me=me,
                json=d,
                state=d.get("state"),
                price=tgram.types.SuggestedPostPrice._parse(me=me, d=d.get("price")),
                send_date=d.get("send_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class SuggestedPostParameters(Type_):
    """
    Contains parameters of a post that is being suggested by the bot.

    :param price: Optional. Proposed price for the post.
    :type price: :class:`SuggestedPostPrice`
    :param send_date: Optional. Proposed send date of the post.
    :type send_date: :obj:`int`
    """

    def __init__(
        self,
        price: "tgram.types.SuggestedPostPrice" = None,
        send_date: int = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.price = price
        self.send_date = send_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuggestedPostParameters"]:
        return (
            SuggestedPostParameters(
                me=me,
                json=d,
                price=tgram.types.SuggestedPostPrice._parse(me=me, d=d.get("price")),
                send_date=d.get("send_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class SuggestedPostApproved(Type_):
    """
    Describes a service message about the approval of a suggested post.

    :param suggested_post_message: Optional. Message containing the suggested post.
    :type suggested_post_message: :class:`tgram.types.Message`
    :param price: Optional. Amount paid for the post.
    :type price: :class:`tgram.types.SuggestedPostPrice`
    :param send_date: Date when the post will be published.
    :type send_date: :obj:`int`
    """

    def __init__(
        self,
        suggested_post_message: "tgram.types.Message" = None,
        price: "tgram.types.SuggestedPostPrice" = None,
        send_date: int = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.suggested_post_message = suggested_post_message
        self.price = price
        self.send_date = send_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuggestedPostApproved"]:
        return (
            SuggestedPostApproved(
                me=me,
                json=d,
                suggested_post_message=tgram.types.Message._parse(
                    me=me, d=d.get("suggested_post_message")
                ),
                price=tgram.types.SuggestedPostPrice._parse(me=me, d=d.get("price")),
                send_date=d.get("send_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class SuggestedPostApprovalFailed(Type_):
    """
    Describes a service message about the failed approval of a suggested post.

    :param suggested_post_message: Optional. Message containing the suggested post whose approval has failed.
    :type suggested_post_message: :class:`tgram.types.Message`
    :param price: Expected price of the post.
    :type price: :class:`tgram.types.SuggestedPostPrice`
    """

    def __init__(
        self,
        suggested_post_message: "tgram.types.Message" = None,
        price: "tgram.types.SuggestedPostPrice" = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.suggested_post_message = suggested_post_message
        self.price = price

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuggestedPostApprovalFailed"]:
        return (
            SuggestedPostApprovalFailed(
                me=me,
                json=d,
                suggested_post_message=tgram.types.Message._parse(
                    me=me, d=d.get("suggested_post_message")
                ),
                price=tgram.types.SuggestedPostPrice._parse(me=me, d=d.get("price")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class SuggestedPostDeclined(Type_):
    """
    Describes a service message about the rejection of a suggested post.

    :param suggested_post_message: Optional. Message containing the suggested post.
    :type suggested_post_message: :class:`tgram.types.Message`
    :param comment: Optional. Comment with which the post was declined.
    :type comment: :obj:`str`
    """

    def __init__(
        self,
        suggested_post_message: "tgram.types.Message" = None,
        comment: str = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.suggested_post_message = suggested_post_message
        self.comment = comment

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuggestedPostDeclined"]:
        return (
            SuggestedPostDeclined(
                me=me,
                json=d,
                suggested_post_message=tgram.types.Message._parse(
                    me=me, d=d.get("suggested_post_message")
                ),
                comment=d.get("comment"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class SuggestedPostPaid(Type_):
    """
    Describes a service message about a successful payment for a suggested post.

    :param suggested_post_message: Optional. Message containing the suggested post.
    :type suggested_post_message: :class:`tgram.types.Message`
    :param currency: Currency in which the payment was made. "XTR" for Telegram Stars or "TON" for toncoins.
    :type currency: :obj:`str`
    :param amount: Optional. The amount of the currency that was received by the channel in nanotoncoins; for payments in toncoins only.
    :type amount: :obj:`int`
    :param star_amount: Optional. The amount of Telegram Stars that was received by the channel; for payments in Telegram Stars only.
    :type star_amount: :class:`tgram.types.StarAmount`
    """

    def __init__(
        self,
        suggested_post_message: "tgram.types.Message" = None,
        currency: str = None,
        amount: int = None,
        star_amount: "tgram.types.StarAmount" = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.suggested_post_message = suggested_post_message
        self.currency = currency
        self.amount = amount
        self.star_amount = star_amount

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuggestedPostPaid"]:
        return (
            SuggestedPostPaid(
                me=me,
                json=d,
                suggested_post_message=tgram.types.Message._parse(
                    me=me, d=d.get("suggested_post_message")
                ),
                currency=d.get("currency"),
                amount=d.get("amount"),
                star_amount=tgram.types.StarAmount._parse(
                    me=me, d=d.get("star_amount")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )


class SuggestedPostRefunded(Type_):
    """
    Describes a service message about a payment refund for a suggested post.

    :param suggested_post_message: Optional. Message containing the suggested post.
    :type suggested_post_message: :class:`tgram.types.Message`
    :param reason: Reason for the refund. "post_deleted" or "payment_refunded".
    :type reason: :obj:`str`
    """

    def __init__(
        self,
        suggested_post_message: "tgram.types.Message" = None,
        reason: str = None,
        me: "tgram.TgBot" = None,
        json: dict = None,
    ):
        super().__init__(me=me, json=json)
        self.suggested_post_message = suggested_post_message
        self.reason = reason

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.SuggestedPostRefunded"]:
        return (
            SuggestedPostRefunded(
                me=me,
                json=d,
                suggested_post_message=tgram.types.Message._parse(
                    me=me, d=d.get("suggested_post_message")
                ),
                reason=d.get("reason"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
