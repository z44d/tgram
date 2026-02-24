import tgram
from typing import Union


class SendChatAction:
    async def send_chat_action(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        action: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
    ) -> bool:
        """
        Use this method when you need to tell the user that something is happening on the bot's side.
        The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).
        Returns True on success.

        Example: The ImageBot needs some time to process a request and upload the image. Instead of sending a text message along the lines of
        “Retrieving image, please wait…”, the bot may use sendChatAction with action = upload_photo. The user will see a “sending photo” status for the bot.

        Telegram documentation: https://core.telegram.org/bots/api#sendchataction

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` or :obj:`str`

        :param action: Type of action to broadcast. Choose one, depending on what the user is about
            to receive: typing for text messages, upload_photo for photos, record_video or upload_video
            for videos, record_voice or upload_voice for voice notes, upload_document for general files,
            choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes.
        :type action: :obj:`str`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param message_thread_id: The thread to which the message will be sent(supergroups only)
        :type message_thread_id: :obj:`int`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "sendChatAction",
            chat_id=chat_id,
            action=action,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
        )
        return result.get("result", {})
