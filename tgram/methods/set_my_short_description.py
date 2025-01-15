import tgram


class SetMyShortDescription:
    async def set_my_short_description(
        self: "tgram.TgBot", short_description: str = None, language_code: str = None
    ) -> bool:
        """
        Use this method to change the bot's short description, which is shown on the bot's profile page and
        is sent together with the link when users share the bot.
        Returns True on success.

        :param short_description: New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language.
        :type short_description: :obj:`str`

        :param language_code: A two-letter ISO 639-1 language code.
            If empty, the short description will be applied to all users for whose language there is no dedicated short description.
        :type language_code: :obj:`str`

        :return: True on success.
        """

        result = await self(
            "setMyShortDescription",
            short_description=short_description,
            language_code=language_code,
        )
        return result["result"]
