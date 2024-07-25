import tgram
from .type_ import Type_

from typing import List, Optional


class InputInvoiceMessageContent(Type_):
    """
    Represents the content of an invoice message to be sent as the result of an inline query.

    Telegram Documentation: https://core.telegram.org/bots/api#inputinvoicemessagecontent

    :param title: Product name, 1-32 characters
    :type title: :obj:`str`

    :param description: Product description, 1-255 characters
    :type description: :obj:`str`

    :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your
        internal processes.
    :type payload: :obj:`str`

    :param provider_token: Payment provider token, obtained via @BotFather
    :type provider_token: :obj:`str`

    :param currency: Three-letter ISO 4217 currency code, see more on currencies
    :type currency: :obj:`str`

    :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery
        cost, delivery tax, bonus, etc.)
    :type prices: :obj:`list` of :class:`tgram.types.LabeledPrice`

    :param max_tip_amount: Optional. The maximum accepted amount for tips in the smallest units of the currency
        (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp
        parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the
        majority of currencies). Defaults to 0
    :type max_tip_amount: :obj:`int`

    :param suggested_tip_amounts: Optional. A JSON-serialized array of suggested amounts of tip in the smallest units
        of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip
        amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
    :type suggested_tip_amounts: :obj:`list` of :obj:`int`

    :param provider_data: Optional. A JSON-serialized object for data about the invoice, which will be shared with the
        payment provider. A detailed description of the required fields should be provided by the payment provider.
    :type provider_data: :obj:`str`

    :param photo_url: Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image
        for a service.
    :type photo_url: :obj:`str`

    :param photo_size: Optional. Photo size in bytes
    :type photo_size: :obj:`int`

    :param photo_width: Optional. Photo width
    :type photo_width: :obj:`int`

    :param photo_height: Optional. Photo height
    :type photo_height: :obj:`int`

    :param need_name: Optional. Pass True, if you require the user's full name to complete the order
    :type need_name: :obj:`bool`

    :param need_phone_number: Optional. Pass True, if you require the user's phone number to complete the order
    :type need_phone_number: :obj:`bool`

    :param need_email: Optional. Pass True, if you require the user's email address to complete the order
    :type need_email: :obj:`bool`

    :param need_shipping_address: Optional. Pass True, if you require the user's shipping address to complete the
        order
    :type need_shipping_address: :obj:`bool`

    :param send_phone_number_to_provider: Optional. Pass True, if the user's phone number should be sent to provider
    :type send_phone_number_to_provider: :obj:`bool`

    :param send_email_to_provider: Optional. Pass True, if the user's email address should be sent to provider
    :type send_email_to_provider: :obj:`bool`

    :param is_flexible: Optional. Pass True, if the final price depends on the shipping method
    :type is_flexible: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InputInvoiceMessageContent`
    """

    def __init__(
        self,
        title: "str" = None,
        description: "str" = None,
        payload: "str" = None,
        currency: "str" = None,
        prices: List["tgram.types.LabeledPrice"] = None,
        provider_token: "str" = None,
        max_tip_amount: "int" = None,
        suggested_tip_amounts: List["int"] = None,
        provider_data: "str" = None,
        photo_url: "str" = None,
        photo_size: "int" = None,
        photo_width: "int" = None,
        photo_height: "int" = None,
        need_name: "bool" = None,
        need_phone_number: "bool" = None,
        need_email: "bool" = None,
        need_shipping_address: "bool" = None,
        send_phone_number_to_provider: "bool" = None,
        send_email_to_provider: "bool" = None,
        is_flexible: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputInvoiceMessageContent"]:
        return (
            InputInvoiceMessageContent(
                me=me,
                json=d,
                title=d.get("title"),
                description=d.get("description"),
                payload=d.get("payload"),
                currency=d.get("currency"),
                prices=[
                    tgram.types.LabeledPrice._parse(me=me, d=i) for i in d.get("prices")
                ]
                if d.get("prices")
                else None,
                provider_token=d.get("provider_token"),
                max_tip_amount=d.get("max_tip_amount"),
                suggested_tip_amounts=d.get("suggested_tip_amounts"),
                provider_data=d.get("provider_data"),
                photo_url=d.get("photo_url"),
                photo_size=d.get("photo_size"),
                photo_width=d.get("photo_width"),
                photo_height=d.get("photo_height"),
                need_name=d.get("need_name"),
                need_phone_number=d.get("need_phone_number"),
                need_email=d.get("need_email"),
                need_shipping_address=d.get("need_shipping_address"),
                send_phone_number_to_provider=d.get("send_phone_number_to_provider"),
                send_email_to_provider=d.get("send_email_to_provider"),
                is_flexible=d.get("is_flexible"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
