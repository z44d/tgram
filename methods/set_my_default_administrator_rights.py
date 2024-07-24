import tgram
from tgram.types import ChatAdministratorRights


class SetMyDefaultAdministratorRights:
    async def set_my_default_administrator_rights(
        self: "tgram.TgBot",
        rights: ChatAdministratorRights = None,
        for_channels: bool = None,
    ) -> bool:
        """
        Use this method to change the default administrator rights requested by the bot
        when it's added as an administrator to groups or channels.
        These rights will be suggested to users, but they are are free to modify
        the list before adding the bot.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setmydefaultadministratorrights

        :param rights: A JSON-serialized object describing new default administrator rights. If not specified,
            the default administrator rights will be cleared.
        :type rights: :class:`tgram.types.ChatAdministratorRights`

        :param for_channels: Pass True to change the default administrator rights of the bot in channels.
            Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.
        :type for_channels: :obj:`bool`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setMyDefaultAdministratorRights",
            rights=rights,
            for_channels=for_channels,
        )
        return result["result"]
