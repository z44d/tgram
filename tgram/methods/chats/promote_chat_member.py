import tgram
from typing import Union


class PromoteChatMember:
    async def promote_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: bool = None,
        can_manage_chat: bool = None,
        can_delete_messages: bool = None,
        can_manage_video_chats: bool = None,
        can_restrict_members: bool = None,
        can_promote_members: bool = None,
        can_change_info: bool = None,
        can_invite_users: bool = None,
        can_post_stories: bool = None,
        can_edit_stories: bool = None,
        can_delete_stories: bool = None,
        can_post_messages: bool = None,
        can_edit_messages: bool = None,
        can_pin_messages: bool = None,
        can_manage_topics: bool = None,
    ) -> bool:
        """
        Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator
        in the chat for this to work and must have the appropriate admin rights.
        Pass False for all boolean parameters to demote a user.

        Telegram documentation: https://core.telegram.org/bots/api#promotechatmember

        :param chat_id: Unique identifier for the target chat or username of the target channel (
            in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param can_change_info: Pass True, if the administrator can change chat title, photo and other settings
        :type can_change_info: :obj:`bool`

        :param can_post_messages: Pass True, if the administrator can create channel posts, channels only
        :type can_post_messages: :obj:`bool`

        :param can_edit_messages: Pass True, if the administrator can edit messages of other users, channels only
        :type can_edit_messages: :obj:`bool`

        :param can_delete_messages: Pass True, if the administrator can delete messages of other users
        :type can_delete_messages: :obj:`bool`

        :param can_invite_users: Pass True, if the administrator can invite new users to the chat
        :type can_invite_users: :obj:`bool`

        :param can_restrict_members: Pass True, if the administrator can restrict, ban or unban chat members
        :type can_restrict_members: :obj:`bool`

        :param can_pin_messages: Pass True, if the administrator can pin messages, supergroups only
        :type can_pin_messages: :obj:`bool`

        :param can_promote_members: Pass True, if the administrator can add new administrators with a subset
            of his own privileges or demote administrators that he has promoted, directly or indirectly
            (promoted by administrators that were appointed by him)
        :type can_promote_members: :obj:`bool`

        :param is_anonymous: Pass True, if the administrator's presence in the chat is hidden
        :type is_anonymous: :obj:`bool`

        :param can_manage_chat: Pass True, if the administrator can access the chat event log, chat statistics,
            message statistics in channels, see channel members,
            see anonymous administrators in supergroups and ignore slow mode.
            Implied by any other administrator privilege
        :type can_manage_chat: :obj:`bool`

        :param can_manage_video_chats: Pass True, if the administrator can manage voice chats
            For now, bots can use this privilege only for passing to other administrators.
        :type can_manage_video_chats: :obj:`bool`

        :param can_manage_voice_chats: Deprecated, use can_manage_video_chats.
        :type can_manage_voice_chats: :obj:`bool`

        :param can_manage_topics: Pass True if the user is allowed to create, rename, close,
            and reopen forum topics, supergroups only
        :type can_manage_topics: :obj:`bool`

        :param can_post_stories: Pass True if the administrator can create the channel's stories
        :type can_post_stories: :obj:`bool`

        :param can_edit_stories: Pass True if the administrator can edit the channel's stories
        :type can_edit_stories: :obj:`bool`

        :param can_delete_stories: Pass True if the administrator can delete the channel's stories
        :type can_delete_stories: :obj:`bool`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "promoteChatMember",
            chat_id=chat_id,
            user_id=user_id,
            is_anonymous=is_anonymous,
            can_manage_chat=can_manage_chat,
            can_delete_messages=can_delete_messages,
            can_manage_video_chats=can_manage_video_chats,
            can_restrict_members=can_restrict_members,
            can_promote_members=can_promote_members,
            can_change_info=can_change_info,
            can_invite_users=can_invite_users,
            can_post_stories=can_post_stories,
            can_edit_stories=can_edit_stories,
            can_delete_stories=can_delete_stories,
            can_post_messages=can_post_messages,
            can_edit_messages=can_edit_messages,
            can_pin_messages=can_pin_messages,
            can_manage_topics=can_manage_topics,
        )
        return result.get("result", {})
