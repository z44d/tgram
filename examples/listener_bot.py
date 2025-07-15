import logging

from tgram import TgBot, filters, types, handlers, errors

logging.basicConfig(level=logging.INFO)
bot = TgBot("API_TOKEN_HERE")


@bot.on_message(filters.command("start") & filters.private)
async def on_pv_msg(bot: TgBot, m: types.Message):
    await m.reply(
        "Send your name",
        reply_markup=types.ReplyKeyboardMarkup([["/cancel"]], resize_keyboard=True),
    )

    try:
        # Will return Message type, CallbackQuery type, any update type or type Update if the update in bot.allowed_udates and update_type is null
        ask_for_name = await bot.ask(
            m.chat.id,
            handlers.Handlers.MESSAGE,
            cancel=lambda _, mm: bool(mm.text.lower() == "/cancel"),
            filters=filters.text,
        )

        return await ask_for_name.reply("Your name is " + ask_for_name.text)
    except errors.CanceledListener as c:
        # CanceledListener.update is Message type, CallbackQuery type, any update type or type Update if the update in bot.allowed_udates and update_type is null
        return await c.update.reply(
            "Canceled.", reply_markup=types.ReplyKeyboardRemove(selective=True)
        )


if __name__ == "__main__":
    bot.run()