import tgram
from tgram.types import BotCommand, BotCommandScope


class SetMyCommands:
    async def set_my_commands(
        self: "tgram.TgBot",
        commands: list[BotCommand],
        scope: BotCommandScope = None,
        language_code: str | None = None,
    ) -> bool:
        """
        Use this method to change the list of the bot's commands.

        Telegram documentation: https://core.telegram.org/bots/api#setmycommands

        :param commands: List of BotCommand. At most 100 commands can be specified.
        :type commands: :obj:`list` of :class:`tgram.types.BotCommand`

        :param scope: The scope of users for which the commands are relevant.
            Defaults to BotCommandScopeDefault.
        :type scope: :class:`tgram.types.BotCommandScope`

        :param language_code: A two-letter ISO 639-1 language code. If empty,
            commands will be applied to all users from the given scope,
            for whose language there are no dedicated commands
        :type language_code: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setMyCommands",
            commands=commands,
            scope=scope,
            language_code=language_code,
        )
        return result.get("result", {})
