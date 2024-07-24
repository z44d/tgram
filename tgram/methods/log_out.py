import tgram


class LogOut:
    async def log_out(self: "tgram.TgBot") -> bool:
        """
        Use this method to log out from the cloud Bot API server before launching the bot locally.
        You MUST log out the bot before running it locally, otherwise there is no guarantee
        that the bot will receive updates.
        After a successful call, you can immediately log in on a local server,
        but will not be able to log in back to the cloud Bot API server for 10 minutes.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#logout

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "logOut",
        )
        return result["result"]
