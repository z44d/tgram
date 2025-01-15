import tgram
from typing import Union


class ApproveChatJoinRequest:
    async def approve_chat_join_request(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> bool:
        """
        Use this method to approve a chat join request.
        The bot must be an administrator in the chat for this to work and must have
        the can_invite_users administrator right. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#approvechatjoinrequest

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "approveChatJoinRequest",
            chat_id=chat_id,
            user_id=user_id,
        )
        return result["result"]
