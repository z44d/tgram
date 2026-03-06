import tgram
from typing import Union


class SetChatMemberTag:
    async def set_chat_member_tag(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        tag: str,
    ) -> bool:
        """
        Use this method to set a custom profile tag for a chat member.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setchatmembertag

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param tag: New profile tag for the user. May be an empty string to remove the tag.
        :type tag: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self(
            "setChatMemberTag",
            chat_id=chat_id,
            user_id=user_id,
            tag=tag,
        )
        return result.get("result", {})
