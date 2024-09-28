import asyncio
import tgram

from typing import List


async def compose(bots: List["tgram.TgBot"]):
    tasks = [asyncio.create_task(bot.run_for_updates()) for bot in bots]

    return await asyncio.wait(tasks)
