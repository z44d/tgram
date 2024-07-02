<p align="center">
    <a href="https://github.com/2ei/tgram">
        <img src="https://raw.githubusercontent.com/7n2/nothing/main/tgbot-small.png" alt="tgram" width="128">
    </a>
    <br>
    <b>A very friendly BOT API library for python developers.</b>
    </br>
    <a href="https://t.me/tgbot_channel">
        Channel
    </a>
    •
    <a href="https://t.me/tgbot_chat">
        Chat
    </a>
    •
    <a href="https://2ei.github.io/tgram/">
        Documentation
    </a>
</p>

# tgram [![PyPI](https://img.shields.io/pypi/v/tgram.svg?logo=python&logoColor=%23959DA5&label=pypi&labelColor=%23282f37)](https://pypi.org/project/tgram/) [![Downloads](https://static.pepy.tech/badge/tgram)](https://pepy.tech/project/tgram)

#### Example Usage
```python
from tgram import TgBot, filters
from tgram.types import Message

bot = TgBot("TOKEN")

@bot.on_message(filters.text & filters.private)
async def on_message(bot: TgBot, message: Message) -> Message:
    #Echo
    return await message.reply_text(
        message.text,
        entities=message.entities)

bot.run_for_updates()
```

## TODO
- Smart plugins with auto-load.

## Requirements
- Python 3.8 or higher.
- A [Telegram BOT Token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).

## How to install?
Here's how to install the tgram library. The commands are given below:

``` bash
# With Git
pip install git+https://github.com/2ei/tgram -U

# With PyPi (Recommended)
pip install tgram -U
```