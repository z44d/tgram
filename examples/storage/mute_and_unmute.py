import asyncio
import logging

from tgram import TgBot, filters
from tgram.types import Message

# Initialize the bot with the given API token and storage engine.
bot = TgBot(
    "API_TOKEN_HERE",
    storage_engine="kvsqlite",  # You can switch to Redis if preferred.
)
logging.basicConfig(level=logging.INFO)


async def unmute_after(chat_id: int, user_id: int, delay: int) -> bool:
    """
    Unmutes a user after a given delay.
    """
    await asyncio.sleep(delay)
    return await bot.storage.unmute(chat_id, user_id)


@bot.on_message(filters.command("mute"))
async def mute_command(_, message: Message) -> Message:
    user_id = (message.from_user or message.sender_chat).id
    chat_id = message.chat.id

    # Mute the user for 15 seconds, preventing message processing and auto-deleting messages.
    await bot.storage.mute(
        chat_id, user_id
    )  # Alternatively, you can use message.chat.mute()

    # Schedule the user to be unmuted after 15 seconds.
    asyncio.create_task(unmute_after(chat_id, user_id, 15))

    return await message.reply("You are muted for 15 seconds.")


# Start the bot's event loop and polling.
bot.run()
