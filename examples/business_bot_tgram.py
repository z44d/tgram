import logging
from tgram import TgBot, filters
from tgram.types import Message

bot = TgBot("Api_Token_Bot")
logger = logging.basicConfig(level=logging.INFO)

#To listen to any new message from a user only
@bot.on_business_message()
async def business_message(bot: TgBot, message: Message) -> Message:
    chat_id = message.chat.id
    await bot.send_message(business_connection_id=message.business_connection_id, chat_id=chat_id, text="hi i am business bot .")

bot.run_for_updates()
#thank @devzaid
