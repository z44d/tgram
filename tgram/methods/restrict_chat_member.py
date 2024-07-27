import tgram
from typing import Union
from tgram.types import ChatPermissions


class RestrictChatMember:
    async def restrict_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
        until_date: int = None,
    ) -> bool:
        """
        Use this method to restrict a user in a supergroup.
        The bot must be an administrator in the supergroup for this to work and must have
        the appropriate admin rights. Pass True for all boolean parameters to lift restrictions from a user.

        Telegram documentation: https://core.telegram.org/bots/api#restrictchatmember

        .. warning::
            Individual parameters are deprecated and will be removed, use 'permissions' instead

        :param chat_id: Unique identifier for the target group or username of the target supergroup
            or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param until_date: Date when restrictions will be lifted for the user, unix time.
            If user is restricted for more than 366 days or less than 30 seconds from the current time,
            they are considered to be restricted forever
        :type until_date: :obj:`int`, optional

        :param can_send_messages: deprecated
        :type can_send_messages: :obj:`bool`

        :param can_send_media_messages: deprecated
        :type can_send_media_messages: :obj:`bool`

        :param can_send_polls: deprecated
        :type can_send_polls: :obj:`bool`

        :param can_send_other_messages: deprecated
        :type can_send_other_messages: :obj:`bool`

        :param can_add_web_page_previews: deprecated
        :type can_add_web_page_previews: :obj:`bool`

        :param can_change_info: deprecated
        :type can_change_info: :obj:`bool`

        :param can_invite_users: deprecated
        :type can_invite_users: :obj:`bool`

        :param can_pin_messages: deprecated
        :type can_pin_messages: :obj:`bool`

        :param use_independent_chat_permissions: Pass True if chat permissions are set independently.
            Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,
            can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes
            permissions; the can_send_polls permission will imply the can_send_messages permission.
        :type use_independent_chat_permissions: :obj:`bool`, optional

        :param permissions: Pass ChatPermissions object to set all permissions at once. Use this parameter instead of
            passing all boolean parameters to avoid backward compatibility problems in future.
        :type permissions: :obj:`tgram.types.ChatPermissions`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "restrictChatMember",
            chat_id=chat_id,
            user_id=user_id,
            permissions=permissions,
            use_independent_chat_permissions=use_independent_chat_permissions,
            until_date=until_date,
        )
        return result["result"]
