import tgram
from typing import Union


class BanChatMember:
    async def ban_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None,
    ) -> bool:
        """
        Use this method to ban a user in a group, a supergroup or a channel.
        In the case of supergroups and channels, the user will not be able to return to the chat on their
        own using invite links, etc., unless unbanned first.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#banchatmember

        :param chat_id: Unique identifier for the target group or username of the target supergroup
            or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param until_date: Date when the user will be unbanned, unix time. If user is banned for more than 366 days or
               less than 30 seconds from the current time they are considered to be banned forever
        :type until_date: :obj:`int`

        :param revoke_messages: Bool: Pass True to delete all messages from the chat for the user that is being removed.
            If False, the user will be able to see messages in the group that were sent before the user was removed.
            Always True for supergroups and channels.
        :type revoke_messages: :obj:`bool`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "banChatMember",
            chat_id=chat_id,
            user_id=user_id,
            until_date=until_date,
            revoke_messages=revoke_messages,
        )
        return result["result"]
