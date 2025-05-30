import tgram


class SetBusinessAccountUsername:
    async def set_business_account_username(
        self: "tgram.TgBot",
        business_connection_id: str,
        username: str = None,
    ) -> bool:
        """
        Changes the username of a managed business account.
        Requires the can_change_username business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#setbusinessaccountusername

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param username: The new value of the username for the business account; 0-32 characters
        :type username: :obj:`str`, optional

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setBusinessAccountUsername",
            business_connection_id=business_connection_id,
            username=username,
        )
        return result["result"]
