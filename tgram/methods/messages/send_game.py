import tgram
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message
from tgram.types import ReplyParameters

from tgram.utils import convert_to_inline_keyboard_markup


class SendGame:
    async def send_game(
        self: "tgram.TgBot",
        chat_id: int,
        game_short_name: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup = None,
        allow_paid_broadcast: bool = None,
    ) -> Message:
        """
        Used to send the game.

        Telegram documentation: https://core.telegram.org/bots/api#sendgame

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param game_short_name: Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather.
        :type game_short_name: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`InlineKeyboardMarkup` or :obj:`ReplyKeyboardMarkup` or :obj:`ReplyKeyboardRemove` or :obj:`ForceReply`

        :param timeout: Timeout in seconds for waiting for a response from the bot.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if one of the specified replied-to messages is not found.
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Pass True, if content of the message needs to be protected from being viewed by the bot.
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of the thread to which the message will be sent.
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of the business connection.
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Identifier of the message effect.
        :type message_effect_id: :obj:`str`

        :param allow_paid_broadcast: Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
            The relevant Stars will be withdrawn from the bot's balance
        :type allow_paid_broadcast: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :obj:`tgram.types.Message`
        """

        result = await self(
            "sendGame",
            chat_id=chat_id,
            game_short_name=game_short_name,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=convert_to_inline_keyboard_markup(reply_markup)
            if isinstance(reply_markup, list)
            else reply_markup,
            allow_paid_broadcast=allow_paid_broadcast,
        )
        return Message._parse(me=self, d=result.get("result", {}))
