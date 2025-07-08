import tgram
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message
from tgram.types import ReplyParameters
from tgram.types import InputChecklist

from tgram.utils import convert_to_inline_keyboard_markup


class SendChecklist:
    async def send_checklist(
        self: "tgram.TgBot",
        business_connection_id: str,
        chat_id: int,
        checklist: InputChecklist,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        """
        Use this method to send a checklist on behalf of a connected business account.
        On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendchecklist

        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent
        :type business_connection_id: :obj:`str`

        :param chat_id: Unique identifier for the target chat
        :type chat_id: :obj:`int`

        :param checklist: A JSON-serialized object for the checklist to send
        :type checklist: :class:`tgram.types.InputChecklist`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound
        :type disable_notification: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_effect_id: Unique identifier of the message effect to be added to the message
        :type message_effect_id: :obj:`str`

        :param reply_parameters: A JSON-serialized object for description of the message to reply to
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param reply_markup: A JSON-serialized object for an inline keyboard
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """
        result = await self(
            "sendChecklist",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            checklist=checklist,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return Message._parse(me=self, d=result["result"])
