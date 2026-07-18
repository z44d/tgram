import tgram
from .type_ import Type_

from typing import Optional


class Link(Type_):
    """
    This object represents a link.

    Telegram Documentation: https://core.telegram.org/bots/api#link

    :param url: URL
    :type url: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.Link`
    """

    def __init__(
        self,
        url: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.url = url

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.Link"]:
        return (
            Link(me=me, json=d, url=d.get("url"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
