import logging
import asyncio

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from tgram import TgBot, filters
from tgram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from tgram.utils import custom_emoji

# Enable logging
logging.basicConfig(level=logging.INFO)

# Initialize bot with your token
# Replace "YOUR_BOT_TOKEN" with your actual bot token
bot = TgBot("YOUR_BOT_TOKEN", parse_mode="HTML")

@bot.on_message(filters.command("start"))
async def start(_, message: Message):
    # Example of buttons with different styles
    # Note: Styles 'primary', 'danger', and 'success' might only be visible in specific clients or contexts
    # that support them, or they might map to specific callback data conventions depending on the client.
    # The 'style' parameter is passed to the InlineKeyboardButton constructor.
    keys = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Primary (Blue)", style="primary", callback_data="btn_primary"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Danger (Red)", style="danger", callback_data="btn_danger"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Success (Green)", style="success", callback_data="btn_success"
                )
            ],
        ]
    )
    
    # Using the premium emoji helper
    # logic: custom_emoji("emoji_char", "custom_emoji_id")
    # This generates a <tg-emoji> html tag.
    emo = custom_emoji("〰", "5269705687126009911")
    
    # Respond with the custom emoji and the styled buttons
    await message.reply(
        f"Here are the button styles matches:\n\n{emo} <b>Button Styles</b>",
        reply_markup=keys
    )

@bot.on_callback_query()
async def callback_handler(bot, callback_query):
    await callback_query.answer(f"You clicked: {callback_query.data}")

if __name__ == "__main__":
    asyncio.run(bot.run_for_updates())
