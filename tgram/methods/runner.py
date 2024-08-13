import tgram

from typing import Any, Coroutine, Literal


class Runner:
    async def run(self: "tgram.TgBot", main: Coroutine = None) -> Any:
        """
        Use this method to run a couroutine function or handle new updates.

        :param main: The couroutine function.
        :type main: :obj:`Coroutine`

        :rtype: :obj:`Any`
        """
        if main is None:
            return await self.run_for_updates()
        return self.loop.run_until_complete(main)

    async def stop(self) -> Literal[True]:
        """
        Use this method to stop getting and handling new updates.

        :rtype: :obj:`bool`
        """
        self.is_running = False
        return True
