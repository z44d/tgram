import tgram
from .type_ import Type_

from typing import Optional


class RichBlockCaption(Type_):
    """
    This object represents a caption for a rich message.

    Telegram Documentation: https://core.telegram.org/bots/api#richblockcaption

    :param text: Rich text
    :type text: :class:`tgram.types.RichText`

    :return: Instance of the class
    :rtype: :class:`tgram.types.RichBlockCaption`
    """

    def __init__(
        self,
        text: "tgram.types.RichText" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.RichBlockCaption"]:
        return (
            RichBlockCaption(
                me=me,
                json=d,
                text=tgram.utils.rich_text_parse(me, d.get("text"))
                if d.get("text")
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
