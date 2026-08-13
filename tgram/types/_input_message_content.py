from typing import Optional

import tgram

from .type_ import Type_


class InputMessageContent(Type_):
    def __init__(
        self,
        message_text: "str | None" = None,
        parse_mode: "str | None" = None,
        entities: list["tgram.types.MessageEntity"] | None = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview_options = link_preview_options

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.InputMessageContent"]:
        return (
            InputMessageContent(
                me=me,
                json=d,
                message_text=d.get("message_text"),
                parse_mode=d.get("parse_mode"),
                entities=[
                    tgram.types.MessageEntity._parse(me=me, d=i)
                    for i in d.get("entities")
                ]
                if d.get("entities")
                else None,
                link_preview_options=tgram.types.LinkPreviewOptions._parse(
                    me=me, d=d.get("link_preview_options")
                ),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
