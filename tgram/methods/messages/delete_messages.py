import tgram
from typing import List
from typing import Union


class DeleteMessages:
    async def delete_messages(
        self: "tgram.TgBot", chat_id: Union[int, str], message_ids: List[int]
    ) -> bool:
        """
        Use this method to delete multiple messages simultaneously.
        If some of the specified messages can't be found, they are skipped. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletemessages

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_ids: Identifiers of the messages to be deleted
        :type message_ids: :obj:`list` of :obj:`int`

        :return: Returns True on success.

        """

        result = await self(
            "deleteMessages",
            chat_id=chat_id,
            message_ids=message_ids,
        )
        return result["result"]
