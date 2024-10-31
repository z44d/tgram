import tgram
from typing import List
from typing import Union
from tgram.types import InputMedia
from tgram.types import Message
from tgram.types import ReplyParameters

from tgram.utils import convert_input_media


class SendMediaGroup:
    async def send_media_group(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        media: List[InputMedia],
        business_connection_id: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        allow_paid_broadcast: bool = None,
    ) -> List[Message]:
        """
        Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files
        can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendmediagroup

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param media: A JSON-serialized array describing messages to be sent, must include 2-10 items
        :type media: :obj:`list` of :obj:`tgram.types.InputMedia`

        :param disable_notification: Sends the messages silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the messages will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :param allow_paid_broadcast: Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
            The relevant Stars will be withdrawn from the bot's balance
        :type allow_paid_broadcast: :obj:`bool`

        :return: On success, an array of Messages that were sent is returned.
        :rtype: List[types.Message]
        """
        arr, files = convert_input_media(media)
        result = await self._send_request(
            "sendMediaGroup",
            chat_id=chat_id,
            media=arr,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            allow_paid_broadcast=allow_paid_broadcast,
            **files,
        )
        return [Message._parse(me=self, d=i) for i in result["result"]]
