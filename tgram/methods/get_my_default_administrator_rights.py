import tgram
from tgram.types import ChatAdministratorRights


class GetMyDefaultAdministratorRights:
    async def get_my_default_administrator_rights(
        self: "tgram.TgBot", for_channels: bool = None
    ) -> ChatAdministratorRights:
        """
        Use this method to get the current default administrator rights of the bot.
        Returns ChatAdministratorRights on success.

        Telegram documentation: https://core.telegram.org/bots/api#getmydefaultadministratorrights

        :param for_channels: Pass True to get the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be returned.
        :type for_channels: :obj:`bool`

        :return: Returns ChatAdministratorRights on success.
        :rtype: :class:`tgram.types.ChatAdministratorRights`
        """

        result = await self._send_request(
            "getMyDefaultAdministratorRights",
            for_channels=for_channels,
        )
        return ChatAdministratorRights._parse(me=self, d=result["result"])
