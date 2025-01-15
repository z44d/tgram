import tgram
from typing import Union


class DemoteChatMember:
    async def demote_chat_member(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> bool:
        """
        Use this method to demote a user in a supergroup or a channel. The bot must be an administrator

        Telegram documentation: null

        :param chat_id: Unique identifier for the target chat or username of the target channel (
            in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "promoteChatMember",
            chat_id=chat_id,
            user_id=user_id,
            is_anonymous=False,
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_promote_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_post_stories=False,
            can_edit_stories=False,
            can_delete_stories=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_pin_messages=False,
            can_manage_topics=False,
        )
        return result["result"]
