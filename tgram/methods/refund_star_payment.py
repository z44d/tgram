import tgram


class RefundStarPayment:
    async def refund_star_payment(
        self: "tgram.TgBot", user_id: int, telegram_payment_charge_id: str
    ) -> bool:
        """
        Refunds a successful payment in Telegram Stars. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#refundstarpayment

        :param user_id: Identifier of the user whose payment will be refunded
        :type user_id: :obj:`int`

        :param telegram_payment_charge_id: Telegram payment identifier
        :type telegram_payment_charge_id: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "refundStarPayment",
            user_id=user_id,
            telegram_payment_charge_id=telegram_payment_charge_id,
        )
        return result["result"]
