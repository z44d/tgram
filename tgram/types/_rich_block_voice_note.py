from typing import Optional

import tgram

from .type_ import Type_


class RichBlockVoiceNote(Type_):
    """
    This object represents a voice note rich block.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockvoicenote

    :param type: Type of the rich block
    :type type: :obj:`str`

    :param voice: Optional. Voice
    :type voice: :class:`tgram.types.Voice`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockVoiceNote`
    """

    def __init__(
        self,
        type: "str" = "voice_note",
        voice: "tgram.types.Voice" = None,
        me: "tgram.TgBot" = None,
        json: "dict | None" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.voice = voice

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict | None = None, force: bool | None = None
    ) -> Optional["tgram.types.RichBlockVoiceNote"]:
        return (
            RichBlockVoiceNote(
                me=me,
                json=d,
                type=d.get("type"),
                voice=tgram.types.Voice._parse(me=me, d=d.get("voice"))
                if d.get("voice")
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
