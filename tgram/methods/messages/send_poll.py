
import tgram
from tgram.types import (
    ForceReply,
    InlineKeyboardMarkup,
    InputPollMedia,
    InputPollOption,
    Message,
    MessageEntity,
    ParseMode,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
)
from tgram.utils import convert_to_inline_keyboard_markup


class SendPoll:
    async def send_poll(
        self: "tgram.TgBot",
        chat_id: int | str,
        question: str,
        options: list[InputPollOption],
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        question_parse_mode: ParseMode = None,
        question_entities: list[MessageEntity] | None = None,
        is_anonymous: bool | None = None,
        type: str | None = None,
        allows_multiple_answers: bool | None = None,
        correct_option_ids: list[int] | None = None,
        explanation: str | None = None,
        explanation_parse_mode: ParseMode = None,
        explanation_entities: list[MessageEntity] | None = None,
        open_period: int | None = None,
        close_date: int | None = None,
        is_closed: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,
        allow_paid_broadcast: bool | None = None,
        allows_revoting: bool | None = None,
        shuffle_options: bool | None = None,
        allow_adding_options: bool | None = None,
        hide_results_until_closes: bool | None = None,
        description: str | None = None,
        description_parse_mode: ParseMode = None,
        description_entities: list[MessageEntity] | None = None,
        media: InputPollMedia = None,
        explanation_media: InputPollMedia = None,
        members_only: bool | None = None,
        country_codes: list[str] | None = None,
    ) -> Message:
        """
        Use this method to send a native poll.
        On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendpoll

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` | :obj:`str`

        :param question: Poll question, 1-300 characters
        :type question: :obj:`str`

        :param options: A JSON-serialized list of 2-10 answer options
        :type options: :obj:`list` of :obj:`InputPollOption`

        :param is_anonymous: True, if the poll needs to be anonymous, defaults to True
        :type is_anonymous: :obj:`bool`

        :param type: Poll type, “quiz” or “regular”, defaults to “regular”
        :type type: :obj:`str`

        :param allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
        :type allows_multiple_answers: :obj:`bool`

        :param correct_option_ids: 0-based identifiers of the correct answer options. Available only for polls in quiz mode,
            defaults to None
        :type correct_option_ids: :obj:`list` of :obj:`int`

        :param explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll,
            0-200 characters with at most 2 line feeds after entities parsing
        :type explanation: :obj:`str`

        :param explanation_parse_mode: Mode for parsing entities in the explanation. See formatting options for more details.
        :type explanation_parse_mode: :obj:`str`

        :param open_period: Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
        :type open_period: :obj:`int`

        :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed.
        :type close_date: :obj:`int` | :obj:`datetime`

        :param is_closed: Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.
        :type is_closed: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the poll allows multiple options to be voted simultaneously.
        :type allow_sending_without_reply: :obj:`bool`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard,
            instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`InlineKeyboardMarkup` | :obj:`ReplyKeyboardMarkup` | :obj:`ReplyKeyboardRemove` | :obj:`ForceReply`

        :param timeout: Timeout in seconds for waiting for a response from the user.
        :type timeout: :obj:`int`

        :param explanation_entities: A JSON-serialized list of special entities that appear in the explanation,
            which can be specified instead of parse_mode
        :type explanation_entities: :obj:`list` of :obj:`MessageEntity`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: The identifier of a message thread, in which the poll will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of the business connection to send the message through
        :type business_connection_id: :obj:`str`

        :param question_parse_mode: Mode for parsing entities in the question. See formatting options for more details. Currently, only custom emoji entities are allowed
        :type question_parse_mode: :obj:`str`

        :param question_entities: A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of question_parse_mode
        :type question_entities: :obj:`list` of :obj:`MessageEntity`

        :param message_effect_id: Identifier of the message effect to apply to the sent message
        :type message_effect_id: :obj:`str`

        :param allow_paid_broadcast: Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
            The relevant Stars will be withdrawn from the bot's balance
        :type allow_paid_broadcast: :obj:`bool`

        :param allows_revoting: Pass True to allow users to change their vote.
        :type allows_revoting: :obj:`bool`

        :param shuffle_options: Pass True to shuffle the options.
        :type shuffle_options: :obj:`bool`

        :param allow_adding_options: Pass True to allow users to add options.
        :type allow_adding_options: :obj:`bool`

        :param hide_results_until_closes: Pass True to hide results until the poll closes.
        :type hide_results_until_closes: :obj:`bool`

        :param description: Poll description, 0-512 characters.
        :type description: :obj:`str`

        :param description_parse_mode: Mode for parsing entities in the description.
        :type description_parse_mode: :obj:`str`

        :param description_entities: A JSON-serialized list of special entities that appear in the description.
        :type description_entities: :obj:`list` of :obj:`MessageEntity`

        :param media: A JSON-serialized object for a media to add to the poll
        :type media: :class:`tgram.types.InputPollMedia`

        :param explanation_media: A JSON-serialized object for a media to add to the quiz explanation
        :type explanation_media: :class:`tgram.types.InputPollMedia`

        :param members_only: Pass True, if only members of the chat can vote in the poll
        :type members_only: :obj:`bool`

        :param country_codes: A JSON-serialized list of country codes, for polls that are only available in certain countries
        :type country_codes: :obj:`list` of :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :obj:`tgram.types.Message`
        """

        result = await self(
            "sendPoll",
            chat_id=chat_id,
            question=question,
            options=options,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            question_parse_mode=question_parse_mode,
            question_entities=question_entities,
            is_anonymous=is_anonymous,
            type=type,
            allows_multiple_answers=allows_multiple_answers,
            correct_option_ids=correct_option_ids,
            explanation=explanation,
            explanation_parse_mode=explanation_parse_mode,
            explanation_entities=explanation_entities,
            open_period=open_period,
            close_date=close_date,
            is_closed=is_closed,
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
            allows_revoting=allows_revoting,
            shuffle_options=shuffle_options,
            allow_adding_options=allow_adding_options,
            hide_results_until_closes=hide_results_until_closes,
            description=description,
            description_parse_mode=description_parse_mode,
            description_entities=description_entities,
            media=media,
            explanation_media=explanation_media,
            members_only=members_only,
            country_codes=country_codes,
        )
        return Message._parse(me=self, d=result.get("result", {}))
