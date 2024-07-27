import tgram
from tgram.types import WebhookInfo


class GetWebhookInfo:
    async def get_webhook_info(self: "tgram.TgBot") -> WebhookInfo:
        """
        Use this method to get current webhook status. Requires no parameters.
        On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.

        Telegram documentation: https://core.telegram.org/bots/api#getwebhookinfo

        :param timeout: Request connection timeout
        :type timeout: :obj:`int`, optional

        :return: On success, returns a WebhookInfo object.
        :rtype: :class:`tgram.types.WebhookInfo`
        """

        result = await self._send_request(
            "getWebhookInfo",
        )
        return WebhookInfo._parse(me=self, d=result["result"])
