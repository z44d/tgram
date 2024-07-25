import tgram
from typing import List
from tgram.types import Sticker


class GetCustomEmojiStickers:
    async def get_custom_emoji_stickers(
        self: "tgram.TgBot", custom_emoji_ids: List[str]
    ) -> List[Sticker]:
        """
        Use this method to get information about custom emoji stickers by their identifiers.
        Returns an Array of Sticker objects.

        :param custom_emoji_ids: List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.
        :type custom_emoji_ids: :obj:`list` of :obj:`str`

        :return: Returns an Array of Sticker objects.
        :rtype: :obj:`list` of :class:`tgram.types.Sticker`
        """

        result = await self._send_request(
            "getCustomEmojiStickers",
            custom_emoji_ids=custom_emoji_ids,
        )
        return [Sticker._parse(me=self, d=i) for i in result["result"]]
