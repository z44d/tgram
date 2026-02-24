import tgram

from typing import List


class GiftPremiumSubscription:
    async def gift_premium_subscription(
        self: "tgram.TgBot",
        user_id: int,
        month_count: int,
        star_count: int,
        text: str = None,
        text_parse_mode: str = None,
        text_entities: List["tgram.types.MessageEntity"] = None,
    ) -> bool:
        """
        Gifts a Telegram Premium subscription to the given user.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#giftpremiumsubscription

        :param user_id: Unique identifier of the target user who will receive a Telegram Premium subscription
        :type user_id: :obj:`int`

        :param month_count: Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12
        :type month_count: :obj:`int`

        :param star_count: Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months
        :type star_count: :obj:`int`

        :param text: Text that will be shown along with the service message about the subscription; 0-128 characters
        :type text: :obj:`str`, optional

        :param text_parse_mode: Mode for parsing entities in the text
        :type text_parse_mode: :obj:`str`, optional

        :param text_entities: A JSON-serialized list of special entities that appear in the gift text
        :type text_entities: :obj:`list`, optional

        :return: True on success.
        :rtype: :obj:`bool`
        """
        result = await self(
            "giftPremiumSubscription",
            user_id=user_id,
            month_count=month_count,
            star_count=star_count,
            text=text,
            text_parse_mode=text_parse_mode,
            text_entities=text_entities,
        )
        return result.get("result", {})
