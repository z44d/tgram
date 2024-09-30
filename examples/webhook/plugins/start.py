from tgram import TgBot, filters

from tgram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@TgBot.on_message(filters.command("start"))
async def on_start(bot: TgBot, message: Message) -> Message:
    return await message.reply_text(
        "Hi from Tgram",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Buttonn", callback_data="yay")]]
        ),
    )
