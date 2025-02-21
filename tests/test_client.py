import pytest
import os
from tgram import TgBot
from tgram.types import Message

BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
CHAT_ID = 5117901887
ALLOWED_UPDATES = ["message"]
PARSE_MODE = "HTML"


@pytest.fixture
def bot():
    return TgBot(BOT_TOKEN, allowed_updates=ALLOWED_UPDATES, parse_mode=PARSE_MODE)


@pytest.mark.asyncio
async def test_bot_initialization(bot):
    assert bot.bot_token == BOT_TOKEN
    assert bot.allowed_updates == ALLOWED_UPDATES
    assert bot.parse_mode == PARSE_MODE


@pytest.mark.asyncio
async def test_bot_send_message(bot):
    message = Message(text="Hello, world!")
    response = await bot.send_message(chat_id=CHAT_ID, text=message.text)
    assert response.text == message.text
