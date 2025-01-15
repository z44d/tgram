import tgram
from typing import List
from typing import Union
from tgram.types import MessageId


class ForwardMessages:
    async def forward_messages(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> List[MessageId]:
        """
        Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded,
        they are skipped. Service messages and messages with protected content can't be forwarded.
        Album grouping is kept for forwarded messages. On success, an array of MessageId of the sent messages is returned.

        Telegram documentation: https://core.telegram.org/bots/api#forwardmessages

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :type from_chat_id: :obj:`int` or :obj:`str`

        :param message_ids: Message identifiers in the chat specified in from_chat_id
        :type message_ids: :obj:`list`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound
        :type disable_notification: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the messages will be sent
        :type message_thread_id: :obj:`int`

        :param protect_content: Protects the contents of the forwarded message from forwarding and saving
        :type protect_content: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.MessageID`
        """

        result = await self(
            "forwardMessages",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_ids=message_ids,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
        )
        return [MessageId._parse(me=self, d=i) for i in result["result"]]
