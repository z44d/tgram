from tgram import TgBot, filters
from tgram.types import Message


@TgBot.on_message(filters.command("start") & filters.private)
async def on_start_command(bot: TgBot, m: Message) -> Message:
    await m.react("❤️")
    return await m.reply_text(
        "Hi from [Tgram](https://github.com/z44d/tgram)", parse_mode="markdown"
    )
