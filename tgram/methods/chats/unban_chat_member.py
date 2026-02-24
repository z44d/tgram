import tgram
from typing import Union


class UnbanChatMember:
    async def unban_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: bool = None,
    ) -> bool:
        """
        Use this method to unban a previously kicked user in a supergroup or channel.
        The user will not return to the group or channel automatically, but will be able to join via link, etc.
        The bot must be an administrator for this to work. By default, this method guarantees that after the call
        the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat
        they will also be removed from the chat. If you don't want this, use the parameter only_if_banned.

        Telegram documentation: https://core.telegram.org/bots/api#unbanchatmember

        :param chat_id: Unique identifier for the target group or username of the target supergroup or channel
            (in the format @username)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param only_if_banned: Do nothing if the user is not banned
        :type only_if_banned: :obj:`bool`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "unbanChatMember",
            chat_id=chat_id,
            user_id=user_id,
            only_if_banned=only_if_banned,
        )
        return result.get("result", {})
