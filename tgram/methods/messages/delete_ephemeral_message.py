import tgram
from typing import Union


class DeleteEphemeralMessage:
    async def delete_ephemeral_message(
        self: "tgram.TgBot", chat_id: Union[int, str], message_id: int
    ) -> bool:
        result = await self(
            "deleteEphemeralMessage",
            chat_id=chat_id,
            message_id=message_id,
        )
        return result.get("result", {})
