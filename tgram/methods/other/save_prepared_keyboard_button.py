import tgram

from tgram.types import PreparedKeyboardButton


class SavePreparedKeyboardButton:
    async def save_prepared_keyboard_button(
        self: "tgram.TgBot",
        user_id: int,
        button: "tgram.types.PreparedKeyboardButton",
    ) -> PreparedKeyboardButton:
        """
        Stores a keyboard button that can be sent by a user of a Mini App. Returns a PreparedKeyboardButton object.

        Telegram documentation: https://core.telegram.org/bots/api#savepreparedkeyboardbutton
        """
        result = await self(
            "savePreparedKeyboardButton",
            user_id=user_id,
            button=button,
        )

        return PreparedKeyboardButton._parse(self, result.get("result", {}))
