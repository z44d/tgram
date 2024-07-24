import tgram
from tgram.types import BusinessConnection


class GetBusinessConnection:
    async def get_business_connection(
        self: "tgram.TgBot", business_connection_id: str
    ) -> BusinessConnection:
        """
        Use this method to get information about the connection of the bot with a business account.
        Returns a BusinessConnection object on success.

        Telegram documentation: https://core.telegram.org/bots/api#getbusinessconnection

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :return: Returns a BusinessConnection object on success.
        :rtype: :class:`tgram.types.BusinessConnection`
        """

        result = await self._send_request(
            "getBusinessConnection",
            business_connection_id=business_connection_id,
        )
        return BusinessConnection._parse(me=self, d=result["result"])
