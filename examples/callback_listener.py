from tgram import TgBot, filters

from tgram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from tgram.handlers import Handlers

bot = TgBot("API_TOKEN_HERE")


@bot.on_message(filters.private & filters.command("start"))
async def on_message(bot: TgBot, m: Message):
    await m.reply_text(
        "Click on the button.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Button", callback_data="data")]]
        ),
    )
    # This is will make it work only one time.
    return await bot.ask(
        update_type=Handlers.CALLBACK_QUERY,
        next_step=answer_callback,
        filters=filters.user(m.from_user.id) & filters.regex("^data$"),
    )


async def answer_callback(_, c: CallbackQuery, __):
    return await c.answer("Hi, how are you?", show_alert=True)


import asyncio

asyncio.run(bot.run())
