import tgram
from .type_ import Type_

from typing import Optional


class BusinessIntro(Type_):
    """
    This object represents a business intro.

    Telegram documentation: https://core.telegram.org/bots/api#businessintro

    :param title: Optional. Title text of the business intro
    :type title: :obj:`str`

    :param message: Optional. Message text of the business intro
    :type message: :obj:`str`

    :param sticker: Optional. Sticker of the business intro
    :type sticker: :class:`Sticker`

    :return: Instance of the class
    :rtype: :class:`BusinessIntro`
    """

    def __init__(
        self,
        title: "str" = None,
        message: "str" = None,
        sticker: "tgram.types.Sticker" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.title = title
        self.message = message
        self.sticker = sticker

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BusinessIntro"]:
        return (
            BusinessIntro(
                me=me,
                json=d,
                title=d.get("title"),
                message=d.get("message"),
                sticker=tgram.types.Sticker._parse(me=me, d=d.get("sticker")),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
