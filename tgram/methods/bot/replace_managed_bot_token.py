import tgram


class ReplaceManagedBotToken:
    async def replace_managed_bot_token(
        self: "tgram.TgBot",
        managed_bot_user_id: int,
        reason: str = None,
    ) -> str:
        """
        Use this method to replace the current bot token for a managed bot.
        Returns the new token on success.

        Telegram documentation: https://core.telegram.org/bots/api#replacemanagedbottoken
        """

        result = await self(
            "replaceManagedBotToken",
            managed_bot_user_id=managed_bot_user_id,
            reason=reason,
        )
        return result.get("result", {})
