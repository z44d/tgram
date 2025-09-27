
import os
import asyncio

from tgram import TgBot, filters
from tgram.types import Message

from typing import Dict


BOT_TOKEN = os.getenv('TOKEN', '123456789:xxxxxxx') # replace with your bot token
                     
bot = TgBot(
  bot_token=BOT_TOKEN
)


@bot.on_message(filters.all & filters.private)
async def on_message(bot: TgBot, message: Message) -> Message:

    chat_id = message.chat.id
    message_id = message.message_id
  
    await bot.copy_message(
             chat_id=chat_id,
             from_chat_id=chat_id,
             message_id=message_id
    )


async def main():
    await bot.run_for_updates()


asyncio.run(main())
