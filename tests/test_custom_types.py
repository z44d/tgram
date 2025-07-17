import pytest
import os
from tgram import TgBot
from tgram.types import Message

BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
CHAT_ID = 5117901887


class CustomizedMessage(Message):
    @property
    def check(self):
        return "Check Passed!"


@pytest.fixture
def bot():
    bot = TgBot(BOT_TOKEN)
    bot.customize(Message, CustomizedMessage)

    return bot


@pytest.mark.asyncio
async def test_customized_message(bot):
    response = await bot.send_message(chat_id=CHAT_ID, text="Cheaking..")
    assert response.__class__.__name__ == "CustomizedMessage"
    assert response.check == "Check Passed!"
