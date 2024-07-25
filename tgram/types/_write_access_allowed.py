import tgram
from .type_ import Type_

from typing import Optional


class WriteAccessAllowed(Type_):
    """
    This object represents a service message about a user allowing a bot to write
    messages after adding it to the attachment menu, launching a Web App from a link,
    or accepting an explicit request from a Web App sent by the method requestWriteAccess.

    Telegram documentation: https://core.telegram.org/bots/api#writeaccessallowed

    :param from_request: Optional. True, if the access was granted after the user accepted an
        explicit request from a Web App sent by the method requestWriteAccess
    :type from_request: :obj:`bool`

    :param web_app_name: Optional. Name of the Web App which was launched from a link
    :type web_app_name: :obj:`str`

    :param from_attachment_menu: Optional. True, if the access was granted when the bot was added to the attachment or side menu
    :type from_attachment_menu: :obj:`bool`
    """

    def __init__(
        self,
        from_request: "bool" = None,
        web_app_name: "str" = None,
        from_attachment_menu: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.WriteAccessAllowed"]:
        return (
            WriteAccessAllowed(
                me=me,
                json=d,
                from_request=d.get("from_request"),
                web_app_name=d.get("web_app_name"),
                from_attachment_menu=d.get("from_attachment_menu"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
