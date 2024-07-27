import tgram
from tgram.types import BotShortDescription


class GetMyShortDescription:
    async def get_my_short_description(
        self: "tgram.TgBot", language_code: str = None
    ) -> BotShortDescription:
        """
        Use this method to get the current bot short description for the given user language.
        Returns BotShortDescription on success.

        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :obj:`str`

        :return: :class:`tgram.types.BotShortDescription`
        """

        result = await self._send_request(
            "getMyShortDescription",
            language_code=language_code,
        )
        return BotShortDescription._parse(me=self, d=result["result"])
