import tgram
from typing import List
from tgram.types import BotCommand
from tgram.types import BotCommandScope


class GetMyCommands:
    async def get_my_commands(
        self: "tgram.TgBot", scope: BotCommandScope = None, language_code: str = None
    ) -> List[BotCommand]:
        """
        Use this method to get the current list of the bot's commands.
        Returns List of BotCommand on success.

        Telegram documentation: https://core.telegram.org/bots/api#getmycommands

        :param scope: The scope of users for which the commands are relevant.
            Defaults to BotCommandScopeDefault.
        :type scope: :class:`tgram.types.BotCommandScope`

        :param language_code: A two-letter ISO 639-1 language code. If empty,
            commands will be applied to all users from the given scope,
            for whose language there are no dedicated commands
        :type language_code: :obj:`str`

        :return: List of BotCommand on success.
        :rtype: :obj:`list` of :class:`tgram.types.BotCommand`
        """

        result = await self(
            "getMyCommands",
            scope=scope,
            language_code=language_code,
        )
        return [BotCommand._parse(me=self, d=i) for i in result["result"]]
