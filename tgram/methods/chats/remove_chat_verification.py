import tgram

from typing import Union


class RemoveChatVerification:
    async def remove_chat_verification(
        self: "tgram.TgBot",
        chat_id: Union[str, int],
    ) -> bool:
        """
        Removes verification from a chat that is currently verified on behalf of the organization represented by the bot. Returns True on success.
        Telegram documentation: https://core.telegram.org/bots/api#removechatverification

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "removeChatVerification",
            chat_id=chat_id,
        )
        return result.get("result", {})
