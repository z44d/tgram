import tgram


class SetManagedBotAccessSettings:
    async def set_managed_bot_access_settings(
        self: "tgram.TgBot",
        user_id: int,
        is_access_restricted: bool,
        added_user_ids: list[int] | None = None,
    ) -> bool:
        """
        Use this method to change the access settings of a managed bot.
        Returns True on success.

        Telegram Documentation: https://core.telegram.org/bots/api#setmanagedbotaccesssettings

        :param user_id: User identifier of the managed bot whose access settings will be changed
        :type user_id: :obj:`int`

        :param is_access_restricted: Pass True, if only selected users can access the bot. The bot's owner can always access it.
        :type is_access_restricted: :obj:`bool`

        :param added_user_ids: A list of up to 10 identifiers of users who will have access to the bot in addition to its owner.
            Ignored if is_access_restricted is false.
        :type added_user_ids: :obj:`list` of :obj:`int`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "setManagedBotAccessSettings",
            user_id=user_id,
            is_access_restricted=is_access_restricted,
            added_user_ids=added_user_ids,
        )
        return result.get("result", {})
