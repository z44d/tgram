import tgram
from typing import Union
from tgram.types import ChatInviteLink


class CreateChatSubscriptionInviteLink:
    async def create_chat_subscription_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        subscription_period: int,
        subscription_price: int,
        name: str = None,
    ) -> ChatInviteLink:
        """
        Use this method to create a subscription invite link for a channel chat.
        The bot must have the can_invite_users administrator rights.
        The link can be edited using the method editChatSubscriptionInviteLink or revoked using the method revokeChatInviteLink.

        Telegram documentation: https://core.telegram.org/bots/api#createchatsubscriptioninvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param subscription_period: The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days).
        :type subscription_period: :obj:`int`

        :param subscription_price: The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-2500
        :type subscription_price: :obj:`int`

        :param name: Invite link name; 0-32 characters
        :type name: :obj:`str`

        :return: Returns the new invite link as ChatInviteLink object.
        :rtype: :class:`tgram.types.ChatInviteLink`
        """

        result = await self._send_request(
            "sreateChatSubscriptionInviteLink",
            chat_id=chat_id,
            subscription_period=subscription_period,
            subscription_price=subscription_price,
            name=name,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])
