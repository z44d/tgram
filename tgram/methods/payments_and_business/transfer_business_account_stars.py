import tgram


class TransferBusinessAccountStars:
    async def transfer_business_account_stars(
        self: "tgram.TgBot",
        business_connection_id: str,
        star_count: int,
    ) -> bool:
        """
        Transfers Telegram Stars from the business account balance to the bot's balance.
        Requires the can_transfer_stars business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#transferbusinessaccountstars

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param star_count: Number of Telegram Stars to transfer; 1-10000
        :type star_count: :obj:`int`

        :return: On success, returns True.
        :rtype: :obj:`bool`

        :raises ValueError: If star_count is not in the range 1-10000.
        """
        if not (1 <= star_count <= 10000):
            raise ValueError("star_count must be between 1 and 10000")

        result = await self(
            "transferBusinessAccountStars",
            business_connection_id=business_connection_id,
            star_count=star_count,
        )
        return result["result"]
