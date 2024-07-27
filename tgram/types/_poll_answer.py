import tgram
from .type_ import Type_

from typing import List, Optional


class PollAnswer(Type_):
    """
    This object represents an answer of a user in a non-anonymous poll.

    Telegram Documentation: https://core.telegram.org/bots/api#pollanswer

    :param poll_id: Unique poll identifier
    :type poll_id: :obj:`str`

    :param voter_chat: Optional. The chat that changed the answer to the poll, if the voter is anonymous
    :type voter_chat: :class:`tgram.types.Chat`

    :param user: Optional. The user, who changed the answer to the poll
    :type user: :class:`tgram.types.User`

    :param option_ids: 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted
        their vote.
    :type option_ids: :obj:`list` of :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.PollAnswer`
    """

    def __init__(
        self,
        poll_id: "str" = None,
        option_ids: List["int"] = None,
        voter_chat: "tgram.types.Chat" = None,
        user: "tgram.types.User" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.PollAnswer"]:
        return (
            PollAnswer(
                me=me,
                json=d,
                poll_id=d.get("poll_id"),
                option_ids=d.get("option_ids"),
                voter_chat=tgram.types.Chat._parse(me=me, d=d.get("voter_chat")),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
