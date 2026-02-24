import tgram
from typing import List
from tgram.types import GameHighScore


class GetGameHighScores:
    async def get_game_high_scores(
        self: "tgram.TgBot",
        user_id: int,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> List[GameHighScore]:
        """
        Use this method to get data for high score tables. Will return the score of the specified user and several of
        their neighbors in a game. On success, returns an Array of GameHighScore objects.

        This method will currently return scores for the target user, plus two of their closest neighbors on each side.
        Will also return the top three users if the user and their neighbors are not among them.
        Please note that this behavior is subject to change.

        Telegram documentation: https://core.telegram.org/bots/api#getgamehighscores

        :param user_id: User identifier
        :type user_id: :obj:`int`

        :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Required if inline_message_id is not specified. Identifier of the sent message
        :type message_id: :obj:`int`

        :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
        :type inline_message_id: :obj:`str`

        :return: On success, returns an Array of GameHighScore objects.
        :rtype: List[types.GameHighScore]
        """

        result = await self(
            "getGameHighScores",
            user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )
        return [GameHighScore._parse(me=self, d=i) for i in result.get("result", {})]
