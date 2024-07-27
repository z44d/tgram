import tgram
from typing import List
from typing import Union
from tgram.types import MessageId


class CopyMessages:
    async def copy_messages(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        remove_caption: bool = None,
    ) -> List[MessageId]:
        """
        Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped.
        Service messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied
        only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessages, but
        the copied messages don't have a link to the original message. Album grouping is kept for copied messages.
        On success, an array of MessageId of the sent messages is returned.

        Telegram documentation: https://core.telegram.org/bots/api#copymessages

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :type from_chat_id: :obj:`int` or :obj:`str`

        :param message_ids: Message identifiers in the chat specified in from_chat_id
        :type message_ids: :obj:`list` of :obj:`int`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound
        :type disable_notification: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the messages will be sent
        :type message_thread_id: :obj:`int`

        :param protect_content: Protects the contents of the forwarded message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param remove_caption: Pass True to copy the messages without their captions
        :type remove_caption: :obj:`bool`

        :return: On success, an array of MessageId of the sent messages is returned.
        :rtype: :obj:`list` of :class:`tgram.types.MessageID`
        """

        result = await self._send_request(
            "copyMessages",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_ids=message_ids,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            remove_caption=remove_caption,
        )
        return [MessageId._parse(me=self, d=i) for i in result["result"]]
