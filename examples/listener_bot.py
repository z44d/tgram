from tgram import TgBot, filters

from tgram.types import Message
from tgram.handlers import Handlers

bot = TgBot("API_TOKEN_HERE")


@bot.on_message(filters.private & filters.command("start"))
async def on_message(bot: TgBot, m: Message):
    await m.reply_text("What is your name?\nSend /cancel to cancel it.")
    return await bot.ask(
        update_type=Handlers.MESSAGE,
        next_step=answer_name,
        cancel=cancel,
        filters=filters.chat(m.chat.id) & filters.text,
    )


async def answer_name(_, m: Message):
    await m.reply_text(f"Your Name is: {m.text}\nHow old are you?")
    return await bot.ask(
        update_type=Handlers.MESSAGE,
        next_step=answer_age,
        cancel=cancel,
        filters=filters.chat(m.chat.id) & filters.text,
    )


async def answer_age(_, m: Message):
    return await m.reply_text(f"You are {m.text} y.o")


async def cancel(_, m: Message) -> bool:
    if m.text.lower() == "/cancel":
        await m.reply_text("Cancelled.")
        return True
    return False


bot.run_for_updates()
