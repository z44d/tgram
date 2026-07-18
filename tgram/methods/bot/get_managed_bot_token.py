import tgram


class GetManagedBotToken:
    async def get_managed_bot_token(
        self: "tgram.TgBot",
        managed_bot_user_id: int,
    ) -> str:
        """
        Use this method to get the current bot token for a managed bot.
        Returns the token on success.

        Telegram documentation: https://core.telegram.org/bots/api#getmanagedbottoken
        """

        result = await self(
            "getManagedBotToken",
            managed_bot_user_id=managed_bot_user_id,
        )
        return result.get("result", {})
