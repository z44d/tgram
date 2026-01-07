import tgram
from tgram.types import OwnedGifts


class GetUserGifts:
    async def get_user_gifts(
        self: "tgram.TgBot",
        user_id: int,
        offset: str = "",
        limit: int = 100,
    ) -> OwnedGifts:
        """
        Use this method to get the list of gifts received by a user.
        Returns an OwnedGifts object on success.

        Telegram documentation: https://core.telegram.org/bots/api#getusergifts

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`
        :param offset: Offset of the first entry to return; use empty string for first chunk
        :type offset: :obj:`str`, optional
        :param limit: Maximum number of gifts to return; 1-100, defaults to 100
        :type limit: :obj:`int`, optional

        :return: Returns an OwnedGifts object on success.
        :rtype: :class:`tgram.types.OwnedGifts`
        """
        result = await self(
            "getUserGifts",
            user_id=user_id,
            offset=offset,
            limit=limit,
        )
        return OwnedGifts._parse(me=self, d=result["result"])
