import tgram

from tgram.types import MessageEntity, ParseMode
from typing import List


class SendGift:
    async def send_gift(
        self: "tgram.TgBot",
        user_id: int,
        gift_id: str,
        text: str = None,
        text_parse_mode: ParseMode = None,
        text_entities: List[MessageEntity] = None,
    ) -> bool:
        """
        Sends a gift to the given user. The gift can't be converted to Telegram Stars by the user. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#sendgift

        :param user_id: Unique identifier of the target user that will receive the gift
        :type user_id: :obj:`int`

        :param gift_id: Identifier of the gift
        :type gift_id: :obj:`str`

        :param text: Text that will be shown along with the gift; 0-255 characters
        :type text: :obj:`str`

        :param text_parse_mode: Mode for parsing entities in the text. See formatting options for more details.
        Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.
        :type text_parse_mode: :obj:`str`

        :param text_entities: A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of text_parse_mode. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.
        :type text_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """
        result = await self(
            "sendGift",
            user_id=user_id,
            gift_id=gift_id,
            text=text,
            text_parse_mode=text_parse_mode,
            text_entities=text_entities,
        )

        return result["result"]
