import tgram
from tgram.types import StarAmount


class GetMyStarBalance:
    async def get_my_star_balance(self: "tgram.TgBot") -> StarAmount:
        """
        Use this method to get the current Telegram Stars balance of the bot.
        On success, returns a StarAmount object.

        Telegram documentation: https://core.telegram.org/bots/api#getmystarbalance

        :return: Current Stars balance of the bot
        :rtype: :class:`tgram.types.StarAmount`
        """
        result = await self("getMyStarBalance")
        return StarAmount._parse(me=self, d=result["result"])
