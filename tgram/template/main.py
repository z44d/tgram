import sys
import asyncio
import logging
import platform

from tgram import TgBot

# from tgram.types import LinkPreviewOptions
from config import TOKEN

logging.basicConfig(level=logging.INFO)
py_version = sys.version_info[:2]
logger = logging.getLogger(__name__)


async def main():
    bot = TgBot(
        TOKEN,
        # parse_mode="Markdown",
        # link_preview_options=LinkPreviewOptions(is_disabled=True),
        plugins="./plugins",
        retry_after=15,
    )

    await bot.run()


def run_in_regular_event_loop():
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(main())


if __name__ == "__main__":
    if platform.system() == "Linux":
        try:
            import uvloop

            if py_version >= (3, 11):
                with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
                    runner.run(main())
            else:
                uvloop.install()
                asyncio.run(main())
        except ModuleNotFoundError:
            logger.warning(
                "You are a Linux user, so it's better to install and use uvloop as ultra-fast event loop, see more: https://github.com/MagicStack/uvloop"
            )
            run_in_regular_event_loop()
    else:
        run_in_regular_event_loop()
