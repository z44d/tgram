import tgram

from tgram.types import Message, SuggestedPostParameters

from typing import Union


class ForwardMessage:
    async def forward_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        video_start_timestamp: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        direct_messages_topic_id: int = None,
        suggested_post_parameters: SuggestedPostParameters = None,
        message_effect_id: str = None,
    ) -> Message:
        """
        Use this method to forward messages of any kind.

        Telegram documentation: https://core.telegram.org/bots/api#forwardmessage

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound
        :type disable_notification: :obj:`bool`

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :type from_chat_id: :obj:`int` or :obj:`str`

        :param message_id: Message identifier in the chat specified in from_chat_id
        :type message_id: :obj:`int`

        :param video_start_timestamp: New start timestamp for the forwarded video in the message
        :type video_start_timestamp: :obj:`int`

        :param protect_content: Protects the contents of the forwarded message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :type message_thread_id: :obj:`int`

        :param direct_messages_topic_id: Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
        :type direct_messages_topic_id: :obj:`int`

        :param suggested_post_parameters: A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.
        :type suggested_post_parameters: :class:`tgram.types.SuggestedPostParameters`

        :param message_effect_id: Unique identifier of the message effect to be added to the message
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self(
            "forwardMessage",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            message_thread_id=message_thread_id,
            video_start_timestamp=video_start_timestamp,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            direct_messages_topic_id=direct_messages_topic_id,
            suggested_post_parameters=suggested_post_parameters,
            message_effect_id=message_effect_id,
        )
        return Message._parse(me=self, d=result["result"])
