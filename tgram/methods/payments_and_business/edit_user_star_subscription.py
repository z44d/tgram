import tgram


class EditUserStarSubscription:
    async def edit_user_star_subscription(
        self: "tgram.TgBot",
        user_id: int,
        telegram_payment_charge_id: str,
        is_canceled: bool,
    ) -> bool:
        """
        Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns True on success.
        """
        result = await self(
            "editUserStarSubscription",
            user_id=user_id,
            telegram_payment_charge_id=telegram_payment_charge_id,
            is_canceled=is_canceled,
        )
        return result.get("result", {})
