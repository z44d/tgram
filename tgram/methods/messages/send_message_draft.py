import tgram
from typing import Union


class SendMessageDraft:
    async def send_message_draft(
        self: "tgram.TgBot",
        business_connection_id: str,
        chat_id: Union[int, str],
        text: str,
        message_thread_id: int = None,
    ) -> bool:
        """
        Use this method to send a draft message while it is being generated.
        This can be used to stream partial messages to a user while generating the content.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#sendmessagedraft

        :param business_connection_id: Unique identifier of the business connection on behalf
            of which the message will be sent
        :type business_connection_id: :obj:`str`
        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` or :obj:`str`
        :param text: Text of the message draft to be sent
        :type text: :obj:`str`
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum;
            for forum supergroups only
        :type message_thread_id: :obj:`int`, optional

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """
        result = await self(
            "sendMessageDraft",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            text=text,
            message_thread_id=message_thread_id,
        )
        return result.get("result", {})
