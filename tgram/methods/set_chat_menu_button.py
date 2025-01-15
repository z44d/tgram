import tgram
from tgram.types import MenuButton


class SetChatMenuButton:
    async def set_chat_menu_button(
        self: "tgram.TgBot", chat_id: int = None, menu_button: MenuButton = None
    ) -> bool:
        """
        Use this method to change the bot's menu button in a private chat,
        or the default menu button.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setchatmenubutton

        :param chat_id: Unique identifier for the target private chat.
            If not specified, default bot's menu button will be changed.
        :type chat_id: :obj:`int` or :obj:`str`

        :param menu_button: A JSON-serialized object for the new bot's menu button. Defaults to MenuButtonDefault
        :type menu_button: :class:`tgram.types.MenuButton`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setChatMenuButton",
            chat_id=chat_id,
            menu_button=menu_button,
        )
        return result["result"]
