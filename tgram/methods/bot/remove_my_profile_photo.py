import tgram


class RemoveMyProfilePhoto:
    async def remove_my_profile_photo(self: "tgram.TgBot") -> bool:
        """
        Use this method to remove the profile photo of the bot. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#removemyprofilephoto

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "removeMyProfilePhoto",
        )
        return result.get("result", {})
