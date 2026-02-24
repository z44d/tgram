import tgram
from typing import Optional


class DeclineSuggestedPost:
    async def decline_suggested_post(
        self: "tgram.TgBot",
        chat_id: int,
        message_id: int,
        comment: Optional[str] = None,
    ) -> bool:
        """
        Declines a suggested post in a direct messages chat.
        The bot must have the 'can_manage_direct_messages' administrator right in the corresponding channel chat.

        Telegram documentation: https://core.telegram.org/bots/api#declinesuggestedpost

        :param chat_id: Unique identifier for the target direct messages chat
        :type chat_id: :obj:`int`

        :param message_id: Identifier of a suggested post message to decline
        :type message_id: :obj:`int`

        :param comment: Comment for the creator of the suggested post; 0-128 characters
        :type comment: :obj:`str`, optional

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """

        result = await self(
            "declineSuggestedPost",
            chat_id=chat_id,
            message_id=message_id,
            comment=comment,
        )
        return result.get("result", {})
