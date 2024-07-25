from tgram import TgBot, filters

from tgram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@TgBot.on_message(filters.command("start") & filters.private)
async def on_start_message(bot: TgBot, m: Message) -> Message:
    return await m.reply_text(
        f"Hi {m.from_user.mention.markdown}!, How are you today?",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("I'm fine", callback_data="fine")]]
        ),
    )
