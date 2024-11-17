import tgram

from tgram.types import Gifts


class GetAvailableGifts:
    async def get_available_gifts(self: "tgram.TgBot") -> Gifts:
        """
        Returns the list of gifts that can be sent by the bot to users. Requires no parameters. Returns a Gifts object.

        Telegram documentation: https://core.telegram.org/bots/api#getavailablegifts
        """
        result = await self._send_request("getAvailableGifts")

        return Gifts._parse(self, result["result"])
