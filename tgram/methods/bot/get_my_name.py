import tgram
from tgram.types import BotName


class GetMyName:
    async def get_my_name(self: "tgram.TgBot", language_code: str = None) -> BotName:
        """
        Use this method to get the current bot name for the given user language.
        Returns BotName on success.

        Telegram documentation: https://core.telegram.org/bots/api#getmyname

        :param language_code: Optional. A two-letter ISO 639-1 language code or an empty string
        :type language_code: :obj:`str`

        :return: :class:`tgram.types.BotName`
        """

        result = await self(
            "getMyName",
            language_code=language_code,
        )
        return BotName._parse(me=self, d=result.get("result", {}))
