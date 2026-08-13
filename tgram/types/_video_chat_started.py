from typing import Optional

import tgram

from .type_ import Type_


class VideoChatStarted(Type_):
    """
    This object represents a service message about a video chat started in the chat. Currently holds no information.
    """

    def __init__(
        self,
        duration: "int | None" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.duration = duration

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.VideoChatStarted"]:
        return (
            VideoChatStarted(me=me, json=d, duration=d.get("duration"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
