import tgram
from typing import List
from typing import Union
from tgram.types import ReactionType


class SetMessageReaction:
    async def set_message_reaction(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        reaction: List[ReactionType] = None,
        is_big: bool = None,
    ) -> bool:
        """
        Use this method to change the chosen reactions on a message.
        Service messages can't be reacted to. Automatically forwarded messages from a channel to its discussion group have the same
        available reactions as messages in the channel. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setmessagereaction

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Identifier of the message to set reaction to
        :type message_id: :obj:`int`

        :param reaction: New list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message.
            A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators.
        :type reaction: :obj:`list` of :class:`tgram.types.ReactionType`

        :param is_big: Pass True to set the reaction with a big animation
        :type is_big: :obj:`bool`

        :return: :obj:`bool`
        """

        result = await self(
            "setMessageReaction",
            chat_id=chat_id,
            message_id=message_id,
            reaction=reaction,
            is_big=is_big,
        )
        return result.get("result", {})
