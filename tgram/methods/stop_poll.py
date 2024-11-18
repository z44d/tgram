import tgram
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import Poll

from tgram.utils import convert_to_inline_keyboard_markup


class StopPoll:
    async def stop_poll(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        business_connection_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Poll:
        """
        Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.

        Telegram documentation: https://core.telegram.org/bots/api#stoppoll

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` | :obj:`str`

        :param message_id: Identifier of the original message with the poll
        :type message_id: :obj:`int`

        :param reply_markup: A JSON-serialized object for a new message markup.
        :type reply_markup: :obj:`InlineKeyboardMarkup`

        :param business_connection_id: Identifier of the business connection to send the message through
        :type business_connection_id: :obj:`str`

        :return: On success, the stopped Poll is returned.
        :rtype: :obj:`tgram.types.Poll`
        """

        result = await self._send_request(
            "stopPoll",
            chat_id=chat_id,
            message_id=message_id,
            business_connection_id=business_connection_id,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
        )
        return Poll._parse(me=self, d=result["result"])
