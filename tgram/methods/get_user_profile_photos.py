import tgram
from tgram.types import UserProfilePhotos


class GetUserProfilePhotos:
    async def get_user_profile_photos(
        self: "tgram.TgBot", user_id: int, offset: int = None, limit: int = None
    ) -> UserProfilePhotos:
        """
        Use this method to get a list of profile pictures for a user.
        Returns a :class:`tgram.types.UserProfilePhotos` object.

        Telegram documentation: https://core.telegram.org/bots/api#getuserprofilephotos

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param offset: Sequential number of the first photo to be returned. By default, all photos are returned.
        :type offset: :obj:`int`

        :param limit: Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :type limit: :obj:`int`

        :return: `UserProfilePhotos <https://core.telegram.org/bots/api#userprofilephotos>`_
        :rtype: :class:`tgram.types.UserProfilePhotos`

        """

        result = await self._send_request(
            "getUserProfilePhotos",
            user_id=user_id,
            offset=offset,
            limit=limit,
        )
        return UserProfilePhotos._parse(me=self, d=result["result"])
