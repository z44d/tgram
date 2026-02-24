import tgram
from typing import Union
from tgram.types import UserChatBoosts


class GetUserChatBoosts:
    async def get_user_chat_boosts(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> UserChatBoosts:
        """
        Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object.

        Telegram documentation: https://core.telegram.org/bots/api#getuserchatboosts

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` | :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :return: On success, a UserChatBoosts object is returned.
        :rtype: :class:`tgram.types.UserChatBoosts`
        """

        result = await self(
            "getUserChatBoosts",
            chat_id=chat_id,
            user_id=user_id,
        )
        return UserChatBoosts._parse(me=self, d=result.get("result", {}))
