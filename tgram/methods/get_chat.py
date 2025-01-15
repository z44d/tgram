import tgram
from typing import Union
from tgram.types import ChatFullInfo


class GetChat:
    async def get_chat(self: "tgram.TgBot", chat_id: Union[int, str]) -> ChatFullInfo:
        """
        Use this method to get up to date information about the chat (current name of the user for one-on-one
        conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.

        Telegram documentation: https://core.telegram.org/bots/api#getchat

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: Chat information
        :rtype: :class:`tgram.types.ChatFullInfo`
        """

        result = await self(
            "getChat",
            chat_id=chat_id,
        )
        return ChatFullInfo._parse(me=self, d=result["result"])
