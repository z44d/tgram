import tgram
from .type_ import Type_

from typing import List, Optional


class Poll(Type_):
    """
    This object contains information about a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#poll

    :param id: Unique poll identifier
    :type id: :obj:`str`

    :param question: Poll question, 1-300 characters
    :type question: :obj:`str`

    :param options: List of poll options
    :type options: :obj:`list` of :class:`tgram.types.PollOption`

    :param total_voter_count: Total number of users that voted in the poll
    :type total_voter_count: :obj:`int`

    :param is_closed: True, if the poll is closed
    :type is_closed: :obj:`bool`

    :param is_anonymous: True, if the poll is anonymous
    :type is_anonymous: :obj:`bool`

    :param type: Poll type, currently can be “regular” or “quiz”
    :type type: :obj:`str`

    :param allows_multiple_answers: True, if the poll allows multiple answers
    :type allows_multiple_answers: :obj:`bool`

    :param correct_option_id: Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    :type correct_option_id: :obj:`int`

    :param explanation: Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    :type explanation: :obj:`str`

    :param explanation_entities: Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    :type explanation_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param open_period: Optional. Amount of time in seconds the poll will be active after creation
    :type open_period: :obj:`int`

    :param close_date: Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    :type close_date: :obj:`int`

    :param question_entities: Optional. Special entities that appear in the question. Currently, only custom emoji entities are allowed in poll questions
    :type question_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Poll`
    """

    def __init__(
        self,
        id: "str" = None,
        question: "str" = None,
        options: List["tgram.types.PollOption"] = None,
        total_voter_count: "int" = None,
        is_closed: "bool" = None,
        is_anonymous: "bool" = None,
        type: "str" = None,
        allows_multiple_answers: "bool" = None,
        question_entities: List["tgram.types.MessageEntity"] = None,
        correct_option_id: "int" = None,
        explanation: "str" = None,
        explanation_entities: List["tgram.types.MessageEntity"] = None,
        open_period: "int" = None,
        close_date: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.question = question
        self.question_entities = question_entities
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Poll"]:
        return (
            Poll(
                me=me,
                json=d,
                id=d.get("id"),
                question=d.get("question"),
                options=[
                    tgram.types.PollOption._parse(me=me, d=i) for i in d.get("options")
                ]
                if d.get("options")
                else None,
                total_voter_count=d.get("total_voter_count"),
                is_closed=d.get("is_closed"),
                is_anonymous=d.get("is_anonymous"),
                type=d.get("type"),
                allows_multiple_answers=d.get("allows_multiple_answers"),
                question_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("question_entities")
                ]
                if d.get("question_entities")
                else None,
                correct_option_id=d.get("correct_option_id"),
                explanation=d.get("explanation"),
                explanation_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("explanation_entities")
                ]
                if d.get("explanation_entities")
                else None,
                open_period=d.get("open_period"),
                close_date=d.get("close_date"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
