import tgram
from .type_ import Type_

from typing import List, Optional


class UsersShared(Type_):
    """
    This object contains information about the users whose identifiers were shared with the bot
    using a KeyboardButtonRequestUsers button.

    Telegram documentation: https://core.telegram.org/bots/api#usersshared

    :param request_id: Identifier of the request
    :type request_id: :obj:`int`

    :param users: Information about users shared with the bot
    :type users: :obj:`list` of :obj:`types.SharedUser`

    :return: Instance of the class
    :rtype: :class:`UsersShared`
    """

    def __init__(
        self,
        request_id: "int" = None,
        users: List["tgram.types.SharedUser"] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_id = request_id
        self.users = users

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.UsersShared"]:
        return (
            UsersShared(
                me=me,
                json=d,
                request_id=d.get("request_id"),
                users=[
                    tgram.types.Sharedtgram.types.User._parse(me=me, d=i)
                    for i in d.get("users")
                ]
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
