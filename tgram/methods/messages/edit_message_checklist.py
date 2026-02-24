import tgram
from tgram.types import InlineKeyboardMarkup, Message, InputChecklist

from tgram.utils import convert_to_inline_keyboard_markup


class EditMessageChecklist:
    async def edit_message_checklist(
        self: "tgram.TgBot",
        business_connection_id: str,
        chat_id: int,
        message_id: int,
        checklist: InputChecklist,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        """
        Use this method to edit a checklist on behalf of a connected business account.
        On success, the edited Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#editmessagechecklist

        :param business_connection_id: Unique identifier of the business connection on behalf of which the message will be sent
        :type business_connection_id: :obj:`str`

        :param chat_id: Unique identifier for the target chat
        :type chat_id: :obj:`int`

        :param message_id: Unique identifier for the target message
        :type message_id: :obj:`int`

        :param checklist: A JSON-serialized object for the new checklist
        :type checklist: :class:`tgram.types.InputChecklist`

        :param reply_markup: A JSON-serialized object for the new inline keyboard for the message
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup`

        :return: On success, the edited Message is returned.
        :rtype: :class:`tgram.types.Message`
        """
        result = await self(
            "editMessageChecklist",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            checklist=checklist,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return Message._parse(me=self, d=result.get("result", {}))
