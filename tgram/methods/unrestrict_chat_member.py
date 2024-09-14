import tgram
from typing import Union
from tgram.types import ChatPermissions


class UnRestrictChatMember:
    async def unrestrict_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        use_independent_chat_permissions: bool = None,
    ) -> bool:
        """
        Use this method to unrestrict a user in a supergroup.
        The bot must be an administrator in the supergroup for this to work and must have
        the appropriate admin rights.
        Telegram documentation: https://core.telegram.org/bots/api#restrictchatmember

        :param chat_id: Unique identifier for the target group or username of the target supergroup
            or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param use_independent_chat_permissions: Pass True if chat permissions are set independently.
            Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,
            can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes
            permissions; the can_send_polls permission will imply the can_send_messages permission.
        :type use_independent_chat_permissions: :obj:`bool`, optional

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "restrictChatMember",
            chat_id=chat_id,
            user_id=user_id,
            permissions=ChatPermissions(
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
            ),
            use_independent_chat_permissions=use_independent_chat_permissions,
        )
        return result["result"]
