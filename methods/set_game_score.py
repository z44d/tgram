import tgram
from typing import Union
from tgram.types import Message


class SetGameScore:
    async def set_game_score(
        self: "tgram.TgBot",
        user_id: int,
        score: int,
        force: bool = None,
        disable_edit_message: bool = None,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "setGameScore",
            user_id=user_id,
            score=score,
            force=force,
            disable_edit_message=disable_edit_message,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )
