import tgram
from .type_ import Type_

from typing import Optional


class CopyTextButton(Type_):
    """
    This object represents an inline keyboard button that copies specified text to the clipboard.

    Telegram documentation: https://core.telegram.org/bots/api#copytextbutton

    :param text: The text to be copied to the clipboard; 1-256 characters
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`CopyTextButton`
    """

    def __init__(
        self,
        text: "str",
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.CopyTextButton"]:
        return (
            CopyTextButton(me=me, json=d, text=d.get("text"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
