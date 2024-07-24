import tgram
from typing import Union
from tgram.types import ChatPermissions


class SetChatPermissions:
    async def set_chat_permissions(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
    ) -> bool:
        """
        Use this method to set default chat permissions for all members.
        The bot must be an administrator in the group or a supergroup for this to work
        and must have the can_restrict_members admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#setchatpermissions

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param permissions: New default chat permissions
        :type permissions: :class:`tgram.types..ChatPermissions`

        :param use_independent_chat_permissions: Pass True if chat permissions are set independently. Otherwise,
            the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,
            can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and
            can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.
        :type use_independent_chat_permissions: :obj:`bool`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setChatPermissions",
            chat_id=chat_id,
            permissions=permissions,
            use_independent_chat_permissions=use_independent_chat_permissions,
        )
        return result["result"]
