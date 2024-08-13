> [!NOTE]
> This is a simple webhook example with tgram

## How to set webhook?

```python
from tgram import TgBot, utils

bot = TgBot("API_TOKEN_HERE")

print(
    bot.set_webhook(
        f"https://example.com/{bot.bot_token}/", drop_pending_updates=True,
        allowed_updates=utils.ALL_UPDATES)
)
```