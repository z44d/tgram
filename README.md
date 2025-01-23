<div align="center"> <a href="https://github.com/z44d/tgram"> <img src="https://github.com/user-attachments/assets/ad99412f-8d69-446c-bedf-5b7663f69727" alt="tgram" width="128"> </a> <h1>tgram</h1> <b>A developer-friendly Telegram Bot API library designed for Python enthusiasts.</b> <br> <a href="https://t.me/tgbot_channel">Channel</a> • <a href="https://z44d.github.io/tgram/">Documentation</a> • <a href="https://github.com/z44d/tgram/tree/main/examples">Examples</a> </div>

<br>

<div align="center"> <a href="https://core.telegram.org/bots/api-changelog#november-17-2024"> <img src="https://img.shields.io/badge/Bot%20API-8.2-blue?logo=telegram" alt="Supported Bot API version"> </a> <a href="https://pypi.org/project/tgram/"> <img src="https://img.shields.io/pypi/v/tgram.svg?logo=python&logoColor=%23959DA5&label=pypi&labelColor=%23282f37" alt="PyPI"> </a> <a href="https://pepy.tech/project/tgram"> <img src="https://static.pepy.tech/badge/tgram" alt="Downloads"> </a> <a href="https://t.me/tgbot_channel"> <img src="https://img.shields.io/badge/Telegram-Channel-blue.svg?logo=telegram" alt="Telegram Channel"> </a> <a href="https://t.me/tgbot_chat"> <img src="https://img.shields.io/badge/Telegram-Group-blue.svg?logo=telegram" alt="Telegram Group"> </a> </div>

## 🚀 Quick Start
Here's a basic example to get started with tgram:
```python
from tgram import TgBot, filters
from tgram.types import Message

bot = TgBot("YOUR_BOT_TOKEN")

@bot.on_message(filters.text & filters.private)
async def on_message(bot: TgBot, message: Message) -> Message:
    # Echo the incoming message
    return await message.reply_text(
        message.text,
        entities=message.entities
    )

bot.run()
```

## 📦 Features
- **Smart Plugins**: Auto-loadable plugins for modular development.
- **Filters for Handlers**: Simplify event handling with filters.
- **Bound Methods**: Access bound methods for different update types easily.

## 📚 Documentation
Full documentation is available [here](https://z44d.github.io/tgram/).

## 🔧 Installation
You can install the tgram library using one of the following methods:
### Via git:
```bash
pip install git+https://github.com/z44d/tgram -U
```
### Via PyPI (Recommended)
```bash
pip install tgram -U
```

## 💡 Requirements
- **Python**: Version 3.8 or higher.
- **Telegram Bot Token**: Obtain one by following [this guide](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).

## 💬 Help & Support
- For general questions and help, join our **[Telegram chat](https://t.me/tgbot_chat)**.
- Follow updates via the **[Telegram Channel](https://t.me/tgbot_channel)**.
