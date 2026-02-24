import tgram
from tgram.types import BotCommandScope


class DeleteMyCommands:
    async def delete_my_commands(
        self: "tgram.TgBot", scope: BotCommandScope = None, language_code: str = None
    ) -> bool:
        """
        Use this method to delete the list of the bot's commands for the given scope and user language.
        After deletion, higher level commands will be shown to affected users.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletemycommands

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
            "deleteMyCommands",
            scope=scope,
            language_code=language_code,
        )
        return result.get("result", {})
