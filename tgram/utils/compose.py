import asyncio

import tgram


async def compose(bots: list["tgram.TgBot"]):
    return await asyncio.gather(*[bot.run() for bot in bots])
