import tgram


class VerifyUser:
    async def verify_user(
        self: "tgram.TgBot", user_id: int, custom_description: str = None
    ) -> bool:
        """
        Verifies a user on behalf of the organization which is represented by the bot. Returns True on success.
        Telegram documentation: https://core.telegram.org/bots/api#verifyuser

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param custom_description: UCustom description for the verification; 0-70 characters.
            Must be empty if the organization isn't allowed to provide a custom verification description.
        :type custom_description: :obj:`str`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "verifyUser", user_id=user_id, custom_description=custom_description
        )
        return result.get("result", {})
