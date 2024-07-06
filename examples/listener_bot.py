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
        data={},
    )


async def answer_name(_, m: Message, data: dict):
    data.update({"name": m.text})
    await m.reply_text("How old are you?")
    return await bot.ask(
        update_type=Handlers.MESSAGE,
        next_step=answer_age,
        cancel=cancel,
        filters=filters.chat(m.chat.id) & filters.text,
        data=data,
    )


async def answer_age(_, m: Message, data: dict):
    return await m.reply_text(f"You are {m.text} y.o, and your name is {data['name']}")


async def cancel(_, m: Message) -> bool:
    if m.text.lower() == "/cancel":
        await m.reply_text("Cancelled.")
        return True
    return False


bot.run_for_updates()
