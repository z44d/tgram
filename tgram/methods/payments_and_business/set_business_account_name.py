import tgram


class SetBusinessAccountName:
    async def set_business_account_name(
        self: "tgram.TgBot",
        business_connection_id: str,
        first_name: str,
        last_name: str = None,
    ) -> bool:
        """
        Changes the first and last name of a managed business account.
        Requires the can_change_name business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#setbusinessaccountname

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param first_name: The new value of the first name for the business account; 1-64 characters
        :type first_name: :obj:`str`

        :param last_name: The new value of the last name for the business account; 0-64 characters
        :type last_name: :obj:`str`, optional

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setBusinessAccountName",
            business_connection_id=business_connection_id,
            first_name=first_name,
            last_name=last_name,
        )
        return result["result"]
