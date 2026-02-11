import tgram
from typing import Union


class SetMyProfilePhoto:
    async def set_my_profile_photo(
        self: "tgram.TgBot",
        photo: Union[
            "tgram.types.InputProfilePhotoStatic",
            "tgram.types.InputProfilePhotoAnimated",
        ],
    ) -> bool:
        """
        Use this method to change the profile photo of the bot. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setmyprofilephoto

        :param photo: New profile photo for the bot
        :type photo: :class:`tgram.types.InputProfilePhotoStatic` or :class:`tgram.types.InputProfilePhotoAnimated`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "setMyProfilePhoto",
            params={
                "photo": photo,
            },
        )
        return result["result"]
