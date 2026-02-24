import tgram
from typing import Union


class ExportChatInviteLink:
    async def export_chat_invite_link(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> str:
        """
        Use this method to export an invite link to a supergroup or a channel. The bot must be an administrator
        in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#exportchatinvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: exported invite link as String on success.
        :rtype: :obj:`str`
        """

        result = await self(
            "exportChatInviteLink",
            chat_id=chat_id,
        )
        return result.get("result", {})
