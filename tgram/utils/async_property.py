import tgram
import inspect


class AsyncProperty:
    def __init__(self, f, bot: "tgram.TgBot") -> None:
        self.f = f
        self.bot = bot

    async def __call__(self, *args):
        if inspect.iscoroutinefunction(self.f):
            r = await self.f()
        else:
            r = await self.bot.loop.run_in_executor(self.bot.executor, self.f, *args)

        return r
