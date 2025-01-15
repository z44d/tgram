import tgram
from tgram.types import MenuButton


class GetChatMenuButton:
    async def get_chat_menu_button(
        self: "tgram.TgBot", chat_id: int = None
    ) -> MenuButton:
        """
        Use this method to get the current value of the bot's menu button
        in a private chat, or the default menu button.
        Returns MenuButton on success.

        Telegram Documentation: https://core.telegram.org/bots/api#getchatmenubutton

        :param chat_id: Unique identifier for the target private chat.
            If not specified, default bot's menu button will be returned.
        :type chat_id: :obj:`int` or :obj:`str`

        :return: types.MenuButton
        :rtype: :class:`tgram.types.MenuButton`
        """

        result = await self(
            "getChatMenuButton",
            chat_id=chat_id,
        )
        return MenuButton._parse(me=self, d=result["result"])
