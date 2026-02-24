import tgram
from tgram.types import StarAmount


class GetBusinessAccountStarBalance:
    async def get_business_account_star_balance(
        self: "tgram.TgBot", business_connection_id: str
    ) -> StarAmount:
        """
        Returns the amount of Telegram Stars owned by a managed business account.

        Telegram documentation: https://core.telegram.org/bots/api#getbusinessaccountstarbalance

        :param business_connection_id: Unique identifier of the business connection
        :return: StarAmount object
        """
        result = await self(
            "getBusinessAccountStarBalance",
            business_connection_id=business_connection_id,
        )
        return StarAmount._parse(me=self, d=result.get("result", {}))
