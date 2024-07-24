import tgram
import asyncio
import logging
from typing import Callable

logger = logging.getLogger(__name__)


class ScheduleJob:
    async def schedule_job(
        self: "tgram.TgBot", after: int, func: Callable, **kwargs
    ) -> asyncio.Task:
        if after < 0:
            raise ValueError("You can't do job in the past.")

        async def task():
            logger.warn("New scheduled job started, it will be done after: %s", after)
            await asyncio.sleep(after)
            try:
                if asyncio.iscoroutinefunction(func):
                    await func(**kwargs)
                    logger.info("Job %s is finished", func.__name__)
                else:
                    await self.loop.run_in_executor(
                        self.executor, lambda: func(**kwargs)
                    )
                    logger.info("Job %s is finished", func.__name__)
            except Exception as e:
                logger.exception(e)

        return asyncio.create_task(task())
