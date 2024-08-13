from tgram import TgBot

from tgram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


async def private_handler(bot: TgBot, message: Message) -> Message:
    return await message.reply_text(
        f"Hi, {message.from_user.mention.markdown}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Button", callback_data="any")]]
        ),
    )


async def callback_handler(bot: TgBot, call: CallbackQuery) -> bool:
    return await call.answer("Hi", show_alert=True)
