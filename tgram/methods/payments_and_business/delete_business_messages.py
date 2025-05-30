import tgram
from typing import List


class DeleteBusinessMessages:
    async def delete_business_messages(
        self: "tgram.TgBot",
        business_connection_id: str,
        message_ids: List[int],
    ) -> bool:
        """
        Deletes messages on behalf of a business account.
        Requires the can_delete_sent_messages business bot right to delete messages sent by the bot itself,
        or the can_delete_all_messages business bot right to delete any message.

        Telegram documentation: https://core.telegram.org/bots/api#deletebusinessmessages

        :param business_connection_id: Unique identifier of the business connection on behalf of which to delete the messages
        :type business_connection_id: :obj:`str`

        :param message_ids: A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat.
        :type message_ids: :obj:`list[int]`

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """

        result = await self(
            "deleteBusinessMessages",
            business_connection_id=business_connection_id,
            message_ids=message_ids,
        )
        return result["result"]
