import tgram


class RemoveUserVerification:
    async def remove_user_verification(
        self: "tgram.TgBot",
        user_id: int,
    ) -> bool:
        """
        Removes verification from a user who is currently verified on behalf of the organization represented by the bot. Returns True on success.
        Telegram documentation: https://core.telegram.org/bots/api#removeuserverification

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "removeUserVerification",
            user_id=user_id,
        )
        return result.get("result", {})
