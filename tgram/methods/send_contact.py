import tgram
from typing import Union
from tgram.types import ForceReply
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message
from tgram.types import ReplyKeyboardMarkup
from tgram.types import ReplyKeyboardRemove
from tgram.types import ReplyParameters


class SendContact:
    async def send_contact(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        last_name: str = None,
        vcard: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
        allow_paid_broadcast: bool = None,
    ) -> Message:
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendcontact

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` or :obj:`str`

        :param phone_number: Contact's phone number
        :type phone_number: :obj:`str`

        :param first_name: Contact's first name
        :type first_name: :obj:`str`

        :param last_name: Contact's last name
        :type last_name: :obj:`str`

        :param vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes
        :type vcard: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard,
            custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if one of the specified
            replied-to messages is not found.
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: The thread to which the message will be sent
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

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendContact",
            chat_id=chat_id,
            phone_number=phone_number,
            first_name=first_name,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            last_name=last_name,
            vcard=vcard,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
            allow_paid_broadcast=allow_paid_broadcast,
        )
        return Message._parse(me=self, d=result["result"])
