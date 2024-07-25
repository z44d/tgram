import tgram


class DeleteWebhook:
    async def delete_webhook(
        self: "tgram.TgBot", drop_pending_updates: bool = None
    ) -> bool:
        """
        Use this method to remove webhook integration if you decide to switch back to getUpdates.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletewebhook

        :param drop_pending_updates: Pass True to drop all pending updates, defaults to None
        :type drop_pending_updates: :obj: `bool`, optional

        :param timeout: Request connection timeout, defaults to None
        :type timeout: :obj:`int`, optional

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteWebhook",
            drop_pending_updates=drop_pending_updates,
        )
        return result["result"]
