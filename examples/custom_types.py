import logging

from tgram import TgBot, filters
from tgram.types import Message

bot = TgBot("API_TOKEN_HERE")
logging.basicConfig(level=logging.INFO)


class CustomizedMessage(Message):
    @property
    def hello(self) -> str:
        return f"Hello {self.from_user.full_name} !"


bot.customize(Message, CustomizedMessage)


@bot.on_message(filters.private & filters.command("start"))
async def say_hello(_, m: CustomizedMessage) -> CustomizedMessage:
    return await m.reply_text(m.hello)


bot.run_for_updates()
