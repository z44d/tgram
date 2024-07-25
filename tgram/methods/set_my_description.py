import tgram


class SetMyDescription:
    async def set_my_description(
        self: "tgram.TgBot", description: str = None, language_code: str = None
    ) -> bool:
        """
        Use this method to change the bot's description, which is shown in
        the chat with the bot if the chat is empty.
        Returns True on success.

        :param description: New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.
        :type description: :obj:`str`

        :param language_code: A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for
            whose language there is no dedicated description.
        :type language_code: :obj:`str`

        :return: True on success.
        """

        result = await self._send_request(
            "setMyDescription",
            description=description,
            language_code=language_code,
        )
        return result["result"]
