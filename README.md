<div align="center">
    <a href="https://github.com/2ei/tgram">
        <img src="https://github.com/user-attachments/assets/ad99412f-8d69-446c-bedf-5b7663f69727" alt="tgram" width="128">
    </a>
    <h1>tgram</h1>
    <b>Very friendly BOT API library for Python developers.</b>
    </br>
    <a href="https://t.me/tgbot_channel">
        Channel
    </a>
    •
    <a href="https://2ei.github.io/tgram/">
        Documentation
    </a>
    •
    <a href="https://github.com/2ei/tgram/tree/main/examples">
        Examples
    </a>
</div>

<br>

<div align="center">
  <a href="https://core.telegram.org/bots/api-changelog">
    <img src="https://img.shields.io/badge/Bot%20API-7.7-blue?logo=telegram" alt="Supported Bot API version">
  </a>
  <a href="https://pypi.org/project/tgram/">
    <img src="https://img.shields.io/pypi/v/tgram.svg?logo=python&logoColor=%23959DA5&label=pypi&labelColor=%23282f37" alt="PyPI">
  </a>
  <a href="https://pepy.tech/project/tgram">
    <img src="https://static.pepy.tech/badge/tgram" alt="Downloads">
  </a>

  <a href="https://t.me/tgbot_channel">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue.svg?logo=telegram" alt="Telegram Channel">
  </a>
  <a href="https://t.me/tgbot_chat">
    <img src="https://img.shields.io/badge/Telegram-Group-blue.svg?logo=telegram" alt="Telegram Group">
  </a>
  <a href="https://github.com/2ei/tgram/actions/workflows/ruff.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/2ei/tgram/ruff.yml?style=flat&label=Ruff" alt="Ruff Action Workflow Status">
  </a>
  <a href="https://github.com/2ei/tgram/actions/workflows/build-docs.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/2ei/tgram/build-docs.yml?style=flat&label=Docs" alt="Docs Action Workflow Status">
  </a>
  <a href="https://github.com/2ei/tgram/actions/workflows/release.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/2ei/tgram/release.yml?style=flat&label=Release" alt="Release Action Workflow Status">
  </a>
</div>

## Example Usage
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

## Features
- Smart plugins with auto-load.
- Filters for handlers.
- Bound methods for update types.

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

## Help & Support

- Join our [Telegram chat](https://t.me/tgbot_chat).
