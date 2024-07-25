import tgram
from .type_ import Type_

from typing import Optional


class LinkPreviewOptions(Type_):
    """
    Describes the options used for link preview generation.

    Telegram documentation: https://core.telegram.org/bots/api#linkpreviewoptions

    :param is_disabled: Optional. True, if the link preview is disabled
    :type is_disabled: :obj:`bool`

    :param url: Optional. URL to use for the link preview. If empty, then the first URL found in the message text will be used
    :type url: :obj:`str`

    :param prefer_small_media: Optional. True, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
    :type prefer_small_media: :obj:`bool`

    :param prefer_large_media: Optional. True, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
    :type prefer_large_media: :obj:`bool`

    :param show_above_text: Optional. True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text
    :type show_above_text: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`LinkPreviewOptions`
    """

    def __init__(
        self,
        is_disabled: "bool" = None,
        url: "str" = None,
        prefer_small_media: "bool" = None,
        prefer_large_media: "bool" = None,
        show_above_text: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.LinkPreviewOptions"]:
        return (
            LinkPreviewOptions(
                me=me,
                json=d,
                is_disabled=d.get("is_disabled"),
                url=d.get("url"),
                prefer_small_media=d.get("prefer_small_media"),
                prefer_large_media=d.get("prefer_large_media"),
                show_above_text=d.get("show_above_text"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
