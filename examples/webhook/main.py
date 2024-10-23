import uvicorn
import asyncio
import os
import logging

from tgram import TgBot
from tgram.types import Update
from tgram.storage.utils import check_update
from tgram.errors import MutedError

from fastapi import FastAPI
from typing import Dict, Tuple, Optional

logger = logging.getLogger(__name__)

app = FastAPI(debug=True)
bots: Dict[int, TgBot] = {}
queue = asyncio.Queue()


def get_tgbot_object(token: str) -> TgBot:
    """Fetch or create a TgBot object based on the token."""
    bot_id = int(token.split(":")[0])

    if bot_id in bots:
        return bots[bot_id]

    bot = TgBot(token, plugins="./plugins")
    bot.load_plugins()
    bots[bot_id] = bot

    return bot


@app.post("/{token}/")
async def get_updates(token: str, update: dict) -> None:
    """Receive updates via webhook and queue them for processing."""
    if update:
        bot = get_tgbot_object(token)
        parsed_update = Update._parse(bot, update)
        queue.put_nowait((bot, parsed_update))


async def handle_update(bot: TgBot, update: Update) -> None:
    """Handle a single update with error handling."""
    try:
        await check_update(update)
        await bot._check_update(update)
    except MutedError:
        # Silently skip muted errors
        pass
    except Exception as e:
        logger.exception("Error handling update: %s", e)


async def updates_worker(lock: asyncio.Lock) -> None:
    """Worker task to process updates from the queue."""
    while True:
        packet: Optional[Tuple[TgBot, Update]] = await queue.get()
        if packet is None:
            break

        bot, update = packet
        async with lock:
            if isinstance(update, Update):
                await handle_update(bot, update)
            elif isinstance(update, dict):
                try:
                    await bot._process_exception(
                        update["e"], update["m"], **update["kwargs"]
                    )
                except Exception as e:
                    logger.exception("Error processing exception: %s", e)


async def start_workers(worker_count: int) -> None:
    """Start multiple worker tasks to handle incoming updates."""
    for _ in range(worker_count):
        asyncio.create_task(updates_worker(asyncio.Lock()))

    logger.warning("Started %s workers to handle new updates.", worker_count)


async def main() -> None:
    """Main entry point to start the application and workers."""
    worker_count = min(32, (os.cpu_count() or 0) + 4) * 2
    await start_workers(worker_count)

    uvicorn.run(
        app=app,
        host=os.getenv("WEBHOOK_HOST", "0.0.0.0"),
        port=int(os.getenv("WEBHOOK_PORT", 80)),
    )


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(main())
