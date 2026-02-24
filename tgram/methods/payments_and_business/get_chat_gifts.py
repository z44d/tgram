import tgram
from tgram.types import OwnedGifts


class GetChatGifts:
    async def get_chat_gifts(
        self: "tgram.TgBot",
        chat_id: int,
        offset: str = "",
        limit: int = 100,
    ) -> OwnedGifts:
        """
        Use this method to get the list of gifts received by a chat.
        Returns an OwnedGifts object on success.

        Telegram documentation: https://core.telegram.org/bots/api#getchatgifts

        :param chat_id: Unique identifier of the target chat
        :type chat_id: :obj:`int`
        :param offset: Offset of the first entry to return; use empty string for first chunk
        :type offset: :obj:`str`, optional
        :param limit: Maximum number of gifts to return; 1-100, defaults to 100
        :type limit: :obj:`int`, optional

        :return: Returns an OwnedGifts object on success.
        :rtype: :class:`tgram.types.OwnedGifts`
        """
        result = await self(
            "getChatGifts",
            chat_id=chat_id,
            offset=offset,
            limit=limit,
        )
        return OwnedGifts._parse(me=self, d=result.get("result", {}))
