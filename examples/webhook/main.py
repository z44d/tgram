import uvicorn

from tgram import TgBot
from tgram.types import Update

from fastapi import FastAPI
from typing import Dict

app = FastAPI(debug=True)
bots: Dict[int, TgBot] = {}


def get_tgbot_object(token: str) -> TgBot:
    bot_id = int(token.split(":")[0])

    if bot_id in bots:
        return bots.get(bot_id)

    bot = TgBot(token, plugins="./plugins")
    bot.load_plugins()
    bots.update({bot_id: bot})

    return bot


@app.post("/{token}/")
async def get_updates(token: str, update: dict):
    if update:
        bot = get_tgbot_object(token)
        await bot._check_update(Update._parse(bot, update))
    else:
        return


uvicorn.run(app, host="0.0.0.0", port=80)
