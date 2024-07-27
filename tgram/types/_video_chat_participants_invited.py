import tgram
from .type_ import Type_

from typing import List, Optional


class VideoChatParticipantsInvited(Type_):
    """
    This object represents a service message about new members invited to a video chat.

    Telegram Documentation: https://core.telegram.org/bots/api#videochatparticipantsinvited

    :param users: New members that were invited to the video chat
    :type users: :obj:`list` of :class:`tgram.types.User`

    :return: Instance of the class
    :rtype: :class:`tgram.types.VideoChatParticipantsInvited`
    """

    def __init__(
        self,
        users: List["tgram.types.User"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.users = users

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.VideoChatParticipantsInvited"]:
        return (
            VideoChatParticipantsInvited(
                me=me,
                json=d,
                users=[tgram.types.User._parse(me=me, d=i) for i in d.get("users")]
                if d.get("users")
                else None,
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
