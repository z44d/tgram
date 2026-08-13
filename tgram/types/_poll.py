from typing import Optional

import tgram
from tgram.utils import String

from .type_ import Type_


class Poll(Type_):
    """
    This object contains information about a poll.

    Telegram Documentation: https://core.telegram.org/bots/api#poll

    :param id: Unique poll identifier
    :type id: :obj:`str`

    :param question: Poll question, 1-300 characters
    :type question: :class:`tgram.utils.String`

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

    :param correct_option_ids: Optional. 0-based identifiers of the correct answer options. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    :type correct_option_ids: :obj:`list` of :obj:`int`

    :param explanation: Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    :type explanation: :class:`tgram.utils.String`

    :param explanation_entities: Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    :type explanation_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param open_period: Optional. Amount of time in seconds the poll will be active after creation
    :type open_period: :obj:`int`

    :param close_date: Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    :type close_date: :obj:`int`

    :param question_entities: Optional. Special entities that appear in the question. Currently, only custom emoji entities are allowed in poll questions
    :type question_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param allows_revoting: Optional. True, if the poll allows revoting.
    :type allows_revoting: :obj:`bool`

    :param description: Optional. Poll description, 0-512 characters.
    :type description: :class:`tgram.utils.String`

    :param description_entities: Optional. Special entities that appear in the description. Currently, only custom emoji entities are allowed in poll descriptions.
    :type description_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

    :param media: Optional. Media in the poll
    :type media: :class:`tgram.types.PollMedia`

    :param explanation_media: Optional. Media in the quiz explanation
    :type explanation_media: :class:`tgram.types.PollMedia`

    :param members_only: Optional. True, if only members of the chat can vote in the poll
    :type members_only: :obj:`bool`

    :param country_codes: Optional. List of country codes, for polls that are only available in certain countries
    :type country_codes: :obj:`list` of :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Poll`
    """

    def __init__(
        self,
        id: "str | None" = None,
        question: "String" = None,
        options: list["tgram.types.PollOption"] | None = None,
        total_voter_count: "int | None" = None,
        is_closed: "bool | None" = None,
        is_anonymous: "bool | None" = None,
        type: "str | None" = None,
        allows_multiple_answers: "bool | None" = None,
        question_entities: list["tgram.types.MessageEntity"] | None = None,
        correct_option_ids: list["int"] | None = None,
        explanation: "String" = None,
        explanation_entities: list["tgram.types.MessageEntity"] | None = None,
        open_period: "int | None" = None,
        close_date: "int | None" = None,
        allows_revoting: "bool | None" = None,
        description: "String" = None,
        description_entities: list["tgram.types.MessageEntity"] | None = None,
        media: "tgram.types.PollMedia" = None,
        explanation_media: "tgram.types.PollMedia" = None,
        members_only: "bool | None" = None,
        country_codes: list["str"] | None = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.id = id
        self.question = String(question).put(question_entities)
        self.question_entities = question_entities
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_ids = correct_option_ids
        self.explanation = (
            String(explanation).put(explanation_entities) if explanation else None
        )
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date
        self.allows_revoting = allows_revoting
        self.description = (
            String(description).put(description_entities) if description else None
        )
        self.description_entities = description_entities
        self.media = media
        self.explanation_media = explanation_media
        self.members_only = members_only
        self.country_codes = country_codes

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
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
                correct_option_ids=d.get("correct_option_ids"),
                explanation=d.get("explanation"),
                explanation_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("explanation_entities")
                ]
                if d.get("explanation_entities")
                else None,
                open_period=d.get("open_period"),
                close_date=d.get("close_date"),
                allows_revoting=d.get("allows_revoting"),
                description=d.get("description"),
                description_entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("description_entities")
                ]
                if d.get("description_entities")
                else None,
                media=tgram.types.PollMedia._parse(me=me, d=d.get("media")),
                explanation_media=tgram.types.PollMedia._parse(
                    me=me, d=d.get("explanation_media")
                ),
                members_only=d.get("members_only"),
                country_codes=d.get("country_codes"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
