import pytest
import os
from tgram import TgBot, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
CHAT_ID = 5117901887


@pytest.fixture
def bot():
    bot = TgBot(BOT_TOKEN)

    return bot


@pytest.mark.asyncio
async def test_customized_message(bot):
    response = await bot.send_message(chat_id=CHAT_ID, text="Cheaking..")
    assert await filters.text(bot, response) is True

    ## Trying again with media message and text filter..
    response = await bot.send_photo(
        chat_id=CHAT_ID, photo="https://avatars.githubusercontent.com/u/162994967?v=4"
    )
    assert await filters.text(bot, response) is False
