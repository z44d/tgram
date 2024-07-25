import tgram
from .type_ import Type_

from typing import Optional


class LoginUrl(Type_):
    """
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:

    Telegram Documentation: https://core.telegram.org/bots/api#loginurl

    :param url: An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed.
        If the user refuses to provide authorization data, the original URL without information about the user will be
        opened. The data added is the same as described in Receiving authorization data. NOTE: You must always check the hash
        of the received data to verify the authentication and the integrity of the data as described in Checking
        authorization.
    :type url: :obj:`str`

    :param forward_text: Optional. New text of the button in forwarded messages.
    :type forward_text: :obj:`str`

    :param bot_username: Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for
        more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the
        domain linked with the bot. See Linking your domain to the bot for more details.
    :type bot_username: :obj:`str`

    :param request_write_access: Optional. Pass True to request the permission for your bot to send messages to the
        user.
    :type request_write_access: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.LoginUrl`
    """

    def __init__(
        self,
        url: "str" = None,
        forward_text: "str" = None,
        bot_username: "str" = None,
        request_write_access: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.LoginUrl"]:
        return (
            LoginUrl(
                me=me,
                json=d,
                url=d.get("url"),
                forward_text=d.get("forward_text"),
                bot_username=d.get("bot_username"),
                request_write_access=d.get("request_write_access"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
