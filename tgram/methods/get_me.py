import tgram
from tgram.types import User


class GetMe:
    async def get_me(self: "tgram.TgBot") -> User:
        """
        Returns basic information about the bot in form of a User object.

        Telegram documentation: https://core.telegram.org/bots/api#getme
        """

        result = await self(
            "getMe",
        )
        return User._parse(me=self, d=result["result"])
