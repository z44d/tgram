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
</p>

# Tgram [![PyPI](https://img.shields.io/pypi/v/tgram.svg?logo=python&logoColor=%23959DA5&label=pypi&labelColor=%23282f37)](https://pypi.org/project/tgram/) [![Downloads](https://static.pepy.tech/badge/tgram)](https://pepy.tech/project/tgram)

#### Example Usage
```python
import logging
from tgram import TgBot, filters
from tgram.types import Message

bot = TgBot("TOKEN")
logger = logging.basicConfig(level=logging.INFO)

@bot.on_message(filters.text)
async def on_message(bot: TgBot, message: Message) -> Message:
    #Echo
    return await bot.send_message(
        message.chat.id,
        message.text,
        entities=message.entities
    )

bot.run_for_updates()
```

## TODO
- Bound methods for types.
- Smart plugins with auto-load.
- Documentation site.

## Requirements
- Python 3.8 or higher.
- A [Telegram BOT Token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).

## How to install?
Here's how to install the Tgram library. The commands are given below:

``` bash
# With Git
pip install git+https://github.com/2ei/tgram -U

# With PyPi (Recommended)
pip install tgram -U
```

## LICENSE
[MIT](https://github.com/2ei/tgram?tab=MIT-1-ov-file)
