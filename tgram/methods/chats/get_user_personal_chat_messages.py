import tgram
from tgram.types import Message


class GetUserPersonalChatMessages:
    async def get_user_personal_chat_messages(
        self: "tgram.TgBot",
        user_id: int,
    ) -> list[Message]:
        """
        Use this method to get messages from the personal chat of a user.
        On success, a list of Messages is returned.

        Telegram Documentation: https://core.telegram.org/bots/api#getuserpersonalchatmessages

        :param user_id: User identifier
        :type user_id: :obj:`int`

        :return: List of Messages on success
        :rtype: :obj:`list` of :class:`tgram.types.Message`
        """

        result = await self(
            "getUserPersonalChatMessages",
            user_id=user_id,
        )
        return [Message._parse(me=self, d=i) for i in result.get("result", [])]
