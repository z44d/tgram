import tgram

from tgram.types import MessageEntity, ParseMode
from typing import List, Union


class SendGift:
    async def send_gift(
        self: "tgram.TgBot",
        gift_id: str,
        user_id: int = None,
        chat_id: Union[int, str] = None,
        pay_for_upgrade: bool = None,
        text: str = None,
        text_parse_mode: ParseMode = None,
        text_entities: List[MessageEntity] = None,
    ) -> bool:
        """
        Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#sendgift

        :param user_id: Required if chat_id is not specified. Unique identifier of the target user who will receive the gift.
        :type user_id: :obj:`int`

        :param chat_id: Required if user_id is not specified. Unique identifier for the chat or username of the channel (in the format @channelusername) that will receive the gift.
        :type chat_id: :obj:`int` or :obj:`str`

        :param gift_id: Identifier of the gift
        :type gift_id: :obj:`str`

        :param pay_for_upgrade: Pass True to pay for the gift upgrade from the bot's balance,
            thereby making the upgrade free for the receiver
        :type pay_for_upgrade: :obj:`bool`

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
            chat_id=chat_id,
            gift_id=gift_id,
            pay_for_upgrade=pay_for_upgrade,
            text=text,
            text_parse_mode=text_parse_mode,
            text_entities=text_entities,
        )

        return result["result"]
