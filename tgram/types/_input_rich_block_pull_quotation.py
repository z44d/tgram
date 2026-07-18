import tgram
from .type_ import Type_

from typing import Optional


class InputRichBlockPullQuotation(Type_):
    def __init__(
        self,
        type: "str" = "pull_quotation",
        text: "str" = None,
        can_collapse: "bool" = None,
        fallback: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.text = text
        self.can_collapse = can_collapse
        self.fallback = fallback

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InputRichBlockPullQuotation"]:
        return (
            InputRichBlockPullQuotation(
                me=me,
                json=d,
                type=d.get("type"),
                text=d.get("text"),
                can_collapse=d.get("can_collapse"),
                fallback=d.get("fallback"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
