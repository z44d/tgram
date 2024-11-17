import tgram
from typing import List
from tgram.types import LabeledPrice


class CreateInvoiceLink:
    async def create_invoice_link(
        self: "tgram.TgBot",
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        subscription_period: int = None,
        provider_token: str = None,
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
    ) -> str:
        """
        Use this method to create a link for an invoice.
        Returns the created invoice link as String on success.

        Telegram documentation:
        https://core.telegram.org/bots/api#createinvoicelink

        :param title: Product name, 1-32 characters
        :type title: :obj:`str`

        :param description: Product description, 1-255 characters
        :type description: :obj:`str`

        :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
            use for your internal processes.
        :type payload: :obj:`str`

        :param provider_token: Payments provider token, obtained via @Botfather; Pass None to omit the parameter
            to use "XTR" currency
        :type provider_token: :obj:`str`

        :param currency: Three-letter ISO 4217 currency code,
            see https://core.telegram.org/bots/payments#supported-currencies
        :type currency: :obj:`str`

        :param prices: Price breakdown, a list of components
            (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
        :type prices: :obj:`list` of :obj:`tgram.types.LabeledPrice`

        :param subscription_period: The number of seconds the subscription will be active for before the next payment.
        The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified.
        :type subscription_period: :obj:`int`

        :param max_tip_amount: The maximum accepted amount for tips in the smallest units of the currency
        :type max_tip_amount: :obj:`int`

        :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the smallest
            units of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip
            amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
        :type suggested_tip_amounts: :obj:`list` of :obj:`int`

        :param provider_data: A JSON-serialized data about the invoice, which will be shared with the payment provider.
            A detailed description of required fields should be provided by the payment provider.
        :type provider_data: :obj:`str`

        :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods
            or a photo of the invoice. People like it better when they see a photo of what they are paying for.
        :type photo_url: :obj:`str`

        :param photo_size: Photo size in bytes
        :type photo_size: :obj:`int`

        :param photo_width: Photo width
        :type photo_width: :obj:`int`

        :param photo_height: Photo height
        :type photo_height: :obj:`int`

        :param need_name: Pass True, if you require the user's full name to complete the order
        :type need_name: :obj:`bool`

        :param need_phone_number: Pass True, if you require the user's phone number to complete the order
        :type need_phone_number: :obj:`bool`

        :param need_email: Pass True, if you require the user's email to complete the order
        :type need_email: :obj:`bool`

        :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
        :type need_shipping_address: :obj:`bool`

        :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
        :type send_phone_number_to_provider: :obj:`bool`

        :param send_email_to_provider: Pass True, if user's email address should be sent to provider
        :type send_email_to_provider: :obj:`bool`

        :param is_flexible: Pass True, if the final price depends on the shipping method
        :type is_flexible: :obj:`bool`

        :return: Created invoice link as String on success.
        :rtype: :obj:`str`
        """

        result = await self._send_request(
            "createInvoiceLink",
            title=title,
            description=description,
            payload=payload,
            currency=currency,
            prices=prices,
            subscription_period=subscription_period,
            provider_token=provider_token,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            provider_data=provider_data,
            photo_url=photo_url,
            photo_size=photo_size,
            photo_width=photo_width,
            photo_height=photo_height,
            need_name=need_name,
            need_phone_number=need_phone_number,
            need_email=need_email,
            need_shipping_address=need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider,
            is_flexible=is_flexible,
        )
        return result["result"]
