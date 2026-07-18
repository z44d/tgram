import tgram
from tgram.types import BotAccessSettings


class GetManagedBotAccessSettings:
    async def get_managed_bot_access_settings(
        self: "tgram.TgBot",
        user_id: int,
    ) -> BotAccessSettings:
        """
        Use this method to get the access settings of a managed bot.
        Returns a BotAccessSettings object on success.

        Telegram Documentation: https://core.telegram.org/bots/api#getmanagedbotaccesssettings

        :param user_id: User identifier of the managed bot whose access settings will be returned
        :type user_id: :obj:`int`

        :return: BotAccessSettings object on success
        :rtype: :class:`tgram.types.BotAccessSettings`
        """

        result = await self(
            "getManagedBotAccessSettings",
            user_id=user_id,
        )
        return BotAccessSettings._parse(me=self, d=result.get("result", {}))
