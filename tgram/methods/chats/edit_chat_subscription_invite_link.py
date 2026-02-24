import tgram

from typing import Union
from tgram.types import ChatInviteLink


class EditChatSubscriptionInviteLink:
    async def edit_chat_subscription_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        invite_link: str,
        name: str = None,
    ) -> ChatInviteLink:
        """
        Use this method to edit a subscription invite link created by the bot.
        The bot must have the can_invite_users administrator rights.

        Telegram documentation: https://core.telegram.org/bots/api#editchatsubscriptioninvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param invite_link: The invite link to edit
        :type invite_link: :obj:`str`

        :param name: Invite link name; 0-32 characters
        :type name: :obj:`str`

        :return: Returns the new invite link as ChatInviteLink object.
        :rtype: :class:`tgram.types.ChatInviteLink`
        """

        result = await self(
            "editChatSubscriptionInviteLink",
            chat_id=chat_id,
            invite_link=invite_link,
            name=name,
        )
        return ChatInviteLink._parse(me=self, d=result.get("result", {}))
