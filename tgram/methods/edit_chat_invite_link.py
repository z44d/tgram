import tgram
from typing import Union
from tgram.types import ChatInviteLink


class EditChatInviteLink:
    async def edit_chat_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """
        Use this method to edit a non-primary invite link created by the bot.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#editchatinvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param name: Invite link name; 0-32 characters
        :type name: :obj:`str`

        :param invite_link: The invite link to edit
        :type invite_link: :obj:`str`

        :param expire_date: Point in time (Unix timestamp) when the link will expire
        :type expire_date: :obj:`int`

        :param member_limit: Maximum number of users that can be members of the chat simultaneously
        :type member_limit: :obj:`int`

        :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified
        :type creates_join_request: :obj:`bool`

        :return: Returns the new invite link as ChatInviteLink object.
        :rtype: :class:`tgram.types.ChatInviteLink`
        """

        result = await self._send_request(
            "editChatInviteLink",
            chat_id=chat_id,
            invite_link=invite_link,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])
