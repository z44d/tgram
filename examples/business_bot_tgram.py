import logging
from tgram import TgBot
from tgram.types import Message

bot = TgBot("Api_Token_Bot")
logger = logging.basicConfig(level=logging.INFO)


@bot.on_business_message()
async def business_message(_, message: Message) -> Message:
    await message.reply_text("Hi, I'm business bot.")


bot.run_for_updates()
# thank @devzaid
