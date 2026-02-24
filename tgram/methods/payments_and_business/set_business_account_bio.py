import tgram


class SetBusinessAccountBio:
    async def set_business_account_bio(
        self: "tgram.TgBot",
        business_connection_id: str,
        bio: str = None,
    ) -> bool:
        """
        Changes the bio of a managed business account.
        Requires the can_change_bio business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#setbusinessaccountbio

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param bio: The new value of the bio for the business account; 0-140 characters
        :type bio: :obj:`str`, optional

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setBusinessAccountBio",
            business_connection_id=business_connection_id,
            bio=bio,
        )
        return result.get("result", {})
