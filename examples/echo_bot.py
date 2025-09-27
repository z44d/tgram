from tgram import TgBot, filters
from tgram.types import Message

bot = TgBot("YOUR_BOT_TOKEN")


@bot.on_message(filters.private)
async def on_message(bot: TgBot, message: Message) -> Message:
    # Echo the incoming message
    if message.text:
        return await message.reply_text(message.text.markdown, parse_mode="Markdown")
    else:
        return await message.copy(message.chat.id)


bot.run()
