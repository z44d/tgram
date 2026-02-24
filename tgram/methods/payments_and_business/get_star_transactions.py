import tgram
from tgram.types import StarTransactions


class GetStarTransactions:
    async def get_star_transactions(
        self: "tgram.TgBot", offset: int = None, limit: int = None
    ) -> StarTransactions:
        """
        Returns the bot's Telegram Star transactions in chronological order.

        Telegram documentation: https://core.telegram.org/bots/api#getstartransactions

        :param offset: Number of transactions to skip in the response
        :type offset: :obj:`int`

        :param limit: The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :type limit: :obj:`int`

        :return: On success, returns a StarTransactions object.
        :rtype: :obj:`tgram.types.StarTransactions`
        """

        result = await self(
            "getStarTransactions",
            offset=offset,
            limit=limit,
        )
        return StarTransactions._parse(me=self, d=result.get("result", {}))
