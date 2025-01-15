import tgram
from typing import List
from tgram.types import Sticker


class GetForumTopicIconStickers:
    async def get_forum_topic_icon_stickers(self: "tgram.TgBot") -> List[Sticker]:
        """
        Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user.
        Requires no parameters. Returns an Array of Sticker objects.

        Telegram documentation: https://core.telegram.org/bots/api#getforumtopiciconstickers

        :return: On success, a list of StickerSet objects is returned.
        :rtype: List[:class:`tgram.types.StickerSet`]
        """

        result = await self(
            "getForumTopicIconStickers",
        )
        return [Sticker._parse(me=self, d=i) for i in result["result"]]
