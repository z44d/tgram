import tgram
from .type_ import Type_

from typing import Optional


class CallbackGame(Type_):
    def __init__(
        self,
        user_id: "int" = None,
        score: "int" = None,
        force: "bool" = None,
        disable_edit_message: "bool" = None,
        chat_id: "int" = None,
        message_id: "int" = None,
        inline_message_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.user_id = user_id
        self.score = score
        self.force = force
        self.disable_edit_message = disable_edit_message
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.CallbackGame"]:
        return (
            CallbackGame(
                me=me,
                json=d,
                user_id=d.get("user_id"),
                score=d.get("score"),
                force=d.get("force"),
                disable_edit_message=d.get("disable_edit_message"),
                chat_id=d.get("chat_id"),
                message_id=d.get("message_id"),
                inline_message_id=d.get("inline_message_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
