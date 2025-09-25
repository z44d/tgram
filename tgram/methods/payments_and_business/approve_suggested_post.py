import tgram
from typing import Optional


class ApproveSuggestedPost:
    async def approve_suggested_post(
        self: "tgram.TgBot",
        chat_id: int,
        message_id: int,
        send_date: Optional[int] = None,
    ) -> bool:
        """
        Approves a suggested post in a direct messages chat.
        The bot must have the 'can_post_messages' administrator right in the corresponding channel chat.

        Telegram documentation: https://core.telegram.org/bots/api#approvesuggestedpost

        :param chat_id: Unique identifier for the target direct messages chat
        :type chat_id: :obj:`int`

        :param message_id: Identifier of a suggested post message to approve
        :type message_id: :obj:`int`

        :param send_date: Point in time (Unix timestamp) when the post is expected to be published;
                          omit if the date has already been specified when the suggested post was created.
                          If specified, then the date must be not more than 2678400 seconds (30 days) in the future
        :type send_date: :obj:`int`, optional

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """

        result = await self(
            "approveSuggestedPost",
            chat_id=chat_id,
            message_id=message_id,
            send_date=send_date,
        )
        return result["result"]
