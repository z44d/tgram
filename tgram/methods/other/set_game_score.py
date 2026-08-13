import tgram
from tgram.types import Message


class SetGameScore:
    async def set_game_score(
        self: "tgram.TgBot",
        user_id: int,
        score: int,
        force: bool | None = None,
        disable_edit_message: bool | None = None,
        chat_id: int | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
    ) -> Message | bool:
        result = await self(
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
            Message._parse(me=self, d=result.get("result", {}))
            if isinstance(result.get("result", {}), dict)
            else result.get("result", {})
        )
