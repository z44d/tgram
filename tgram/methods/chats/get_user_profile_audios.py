import tgram
from tgram.types import UserProfileAudios


class GetUserProfileAudios:
    async def get_user_profile_audios(
        self: "tgram.TgBot", user_id: int, offset: int = None, limit: int = None
    ) -> UserProfileAudios:
        """
        Use this method to get a list of profile audios for a user. Returns a UserProfileAudios object.

        Telegram documentation: https://core.telegram.org/bots/api#getuserprofileaudios

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param offset: Optional. Sequential number of the first audio to be returned. By default, all audios are returned.
        :type offset: :obj:`int`

        :param limit: Optional. Limits the number of audios to be retrieved. Values between 1–100 are accepted. Defaults to 100.
        :type limit: :obj:`int`

        :return: UserProfileAudios
        :rtype: :class:`tgram.types.UserProfileAudios`
        """

        result = await self(
            "getUserProfileAudios",
            params={
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
            },
        )
        return UserProfileAudios._parse(me=self, d=result.get("result", {}))
