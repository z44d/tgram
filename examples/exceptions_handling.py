import logging

from tgram import TgBot, filters
from tgram.types import Message
from tgram.errors import MessageTextEmpty

bot = TgBot("API_TOKEN_HERE")

logging.basicConfig(level=logging.INFO)


@bot.on_exception()
async def on_e(bot: TgBot, e: Exception, method: str, **kwargs):
    print(e)
    if isinstance(e, MessageTextEmpty):
        kwargs.update({"text": "Hi"})
        r = await bot._send_request(method, **kwargs)

        msg = Message._parse(bot, r["result"])
        print(msg)


@bot.on_message(filters.command("start"))
async def on_c(_, m: Message):
    try:
        # Will raise MessageTextEmpty error, but we'll ignore it and handle it in the decorator.
        await m.reply_text("")
    except Exception:
        pass


bot.run()
