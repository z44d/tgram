import tgram


class SetMyName:
    async def set_my_name(
        self: "tgram.TgBot", name: str = None, language_code: str = None
    ) -> bool:
        """
        Use this method to change the bot's name. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setmyname

        :param name: Optional. New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language.
        :type name: :obj:`str`

        :param language_code: Optional. A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose
            language there is no dedicated name.
        :type language_code: :obj:`str`

        :return: True on success.
        """

        result = await self(
            "setMyName",
            name=name,
            language_code=language_code,
        )
        return result["result"]
