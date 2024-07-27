import tgram
from typing import Union
from tgram.types import ChatInviteLink


class RevokeChatInviteLink:
    async def revoke_chat_invite_link(
        self: "tgram.TgBot", chat_id: Union[int, str], invite_link: str
    ) -> ChatInviteLink:
        """
        Use this method to revoke an invite link created by the bot.
        Note: If the primary link is revoked, a new link is automatically generated The bot must be an administrator
        in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#revokechatinvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param invite_link: The invite link to revoke
        :type invite_link: :obj:`str`

        :return: Returns the new invite link as ChatInviteLink object.
        :rtype: :class:`tgram.types.ChatInviteLink`
        """

        result = await self._send_request(
            "revokeChatInviteLink",
            chat_id=chat_id,
            invite_link=invite_link,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])
