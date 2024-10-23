import tgram
from .type_ import Type_

from typing import List, Optional
from tgram import utils


class MessageReactionUpdated(Type_):
    """
    This object represents a service message about a change in the list of the current user's reactions to a message.

    Telegram documentation: https://core.telegram.org/bots/api#messagereactionupdated

    :param chat: The chat containing the message the user reacted to
    :type chat: :class:`tgram.types.Chat`

    :param message_id: Unique identifier of the message inside the chat
    :type message_id: :obj:`int`

    :param user: Optional. The user that changed the reaction, if the user isn't anonymous
    :type user: :class:`tgram.types.User`

    :param actor_chat: Optional. The chat on behalf of which the reaction was changed, if the user is anonymous
    :type actor_chat: :class:`tgram.types.Chat`

    :param date: Date of the change in Unix time
    :type date: :obj:`int`

    :param old_reaction: Previous list of reaction types that were set by the user
    :type old_reaction: :obj:`list` of :class:`ReactionType`

    :param new_reaction: New list of reaction types that have been set by the user
    :type new_reaction: :obj:`list` of :class:`ReactionType`

    :return: Instance of the class
    :rtype: :class:`MessageReactionUpdated`
    """

    def __init__(
        self,
        chat: "tgram.types.Chat" = None,
        message_id: "int" = None,
        date: "int" = None,
        old_reaction: List["tgram.types.ReactionType"] = None,
        new_reaction: List["tgram.types.ReactionType"] = None,
        user: "tgram.types.User" = None,
        actor_chat: "tgram.types.Chat" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.chat = chat
        self.message_id = message_id
        self.user = user
        self.actor_chat = actor_chat
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.MessageReactionUpdated"]:
        return (
            MessageReactionUpdated(
                me=me,
                json=d,
                chat=tgram.types.Chat._parse(me=me, d=d.get("chat")),
                message_id=d.get("message_id"),
                date=d.get("date"),
                old_reaction=utils.reaction_type_parse(d.get("old_reaction")),
                new_reaction=utils.reaction_type_parse(d.get("new_reaction")),
                user=tgram.types.User._parse(me=me, d=d.get("user")),
                actor_chat=tgram.types.Chat._parse(me=me, d=d.get("actor_chat")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
