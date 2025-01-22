import pytest
import os
from tgram import TgBot

BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
CHAT_ID = 5117901887


@pytest.fixture
def bot():
    bot = TgBot(BOT_TOKEN)

    return bot


@pytest.mark.asyncio
async def test_customized_message(bot):
    try:
        await bot.send_message(chat_id=CHAT_ID, text="")
    except Exception as e:
        assert e.__class__.__name__ == "MessageTextEmpty"
