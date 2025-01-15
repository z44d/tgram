import tgram
from tgram.types import BotDescription


class GetMyDescription:
    async def get_my_description(
        self: "tgram.TgBot", language_code: str = None
    ) -> BotDescription:
        """
        Use this method to get the current bot description for the given user language.
        Returns BotDescription on success.

        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :obj:`str`

        :return: :class:`tgram.types.BotDescription`
        """

        result = await self(
            "getMyDescription",
            language_code=language_code,
        )
        return BotDescription._parse(me=self, d=result["result"])
