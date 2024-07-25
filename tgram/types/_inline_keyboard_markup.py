import tgram
from .type_ import Type_

from typing import List, Optional


class InlineKeyboardMarkup(Type_):
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinekeyboardmarkup

    :param keyboard: :obj:`list` of button rows, each represented by an :obj:`list` of
        :class:`tgram.types.InlineKeyboardButton` objects
    :type keyboard: :obj:`list` of :obj:`list` of :class:`tgram.types.InlineKeyboardButton`

    :param row_width: number of :class:`tgram.types.InlineKeyboardButton` objects on each row
    :type row_width: :obj:`int`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineKeyboardMarkup`
    """

    def __init__(
        self,
        inline_keyboard: List[List["tgram.types.InlineKeyboardButton"]] = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.inline_keyboard = inline_keyboard

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InlineKeyboardMarkup"]:
        return (
            InlineKeyboardMarkup(
                me=me,
                json=d,
                inline_keyboard=[
                    [
                        tgram.types.Inlinetgram.types.KeyboardButton._parse(me=me, d=x)
                        for x in i
                    ]
                    for i in d.get("inline_keyboard")
                ]
                if d.get("inline_keyboard")
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
