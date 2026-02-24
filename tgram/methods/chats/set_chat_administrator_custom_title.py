import tgram
from typing import Union


class SetChatAdministratorCustomTitle:
    async def set_chat_administrator_custom_title(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int, custom_title: str
    ) -> bool:
        """
        Use this method to set a custom title for an administrator in a supergroup promoted by the bot.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setchatadministratorcustomtitle

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param custom_title: New custom title for the administrator;
            0-16 characters, emoji are not allowed
        :type custom_title: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setChatAdministratorCustomTitle",
            chat_id=chat_id,
            user_id=user_id,
            custom_title=custom_title,
        )
        return result.get("result", {})
