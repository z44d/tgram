import asyncio
import logging
from tgram import TgBot, filters
from tgram.types import Message

bot = TgBot("1234567890:ABCD_EFG-.....", fetch_outgoing_messages=True)
logging.basicConfig(level=logging.INFO)


@bot.edited_outgoing_message()
async def on_eoutgoing(_, m: Message):
    print(m.id, m.text)
    await asyncio.sleep(10)
    await m.delete()


@bot.outgoing_message()
async def on_outgoing(_, m: Message):
    print(m.id, m.text)
    await asyncio.sleep(10)
    await m.edit_text("Bye!, I'll delete this message after 10 seconds.")


@bot.on_message(filters.command("start") & filters.private)
async def pr(_, m: Message):
    return await m.reply("Hi!, I'll say good bye after 10 seconds.")


import asyncio

asyncio.run(bot.run())
