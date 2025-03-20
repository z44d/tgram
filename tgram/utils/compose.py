import asyncio
import tgram

from typing import List


async def compose(bots: List["tgram.TgBot"]):
    return await asyncio.gather(*[bot.run() for bot in bots])
