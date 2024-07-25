import tgram
import random
from .type_ import Type_

from typing import Optional


class KeyboardButtonRequestUsers(Type_):
    """
    This object defines the criteria used to request a suitable user.
    The identifier of the selected user will be shared with the bot when the corresponding button is pressed.

    Telegram documentation: https://core.telegram.org/bots/api#keyboardbuttonrequestusers

    :param request_id: Signed 32-bit identifier of the request, which will be received back in the UsersShared object.
        Must be unique within the message
    :type request_id: :obj:`int`

    :param user_is_bot: Optional. Pass True to request a bot, pass False to request a regular user.
        If not specified, no additional restrictions are applied.
    :type user_is_bot: :obj:`bool`

    :param user_is_premium: Optional. Pass True to request a premium user, pass False to request a non-premium user.
        If not specified, no additional restrictions are applied.
    :type user_is_premium: :obj:`bool`

    :param max_quantity: Optional. The maximum number of users to be selected; 1-10. Defaults to 1.
    :type max_quantity: :obj:`int`

    :param request_name: Optional. Request name
    :type request_name: :obj:`bool`

    :param request_username: Optional. Request username
    :type request_username: :obj:`bool`

    :param request_photo: Optional. Request photo
    :type request_photo: :obj:`bool`

    :return: Instance of the class
    :rtype: :class:`tgram.types.KeyboardButtonRequestUsers`
    """

    def __init__(
        self,
        user_is_bot: "bool" = None,
        user_is_premium: "bool" = None,
        max_quantity: "int" = None,
        request_name: "bool" = None,
        request_username: "bool" = None,
        request_photo: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.request_id = random.randint(10000, 99999)
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity
        self.request_name = request_name
        self.request_username = request_username
        self.request_photo = request_photo

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.KeyboardButtonRequestUsers"]:
        return (
            KeyboardButtonRequestUsers(
                me=me,
                json=d,
                user_is_bot=d.get("user_is_bot"),
                user_is_premium=d.get("user_is_premium"),
                max_quantity=d.get("max_quantity"),
                request_name=d.get("request_name"),
                request_username=d.get("request_username"),
                request_photo=d.get("request_photo"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
