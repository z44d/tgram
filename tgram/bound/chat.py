import tgram

from typing import Union


class ChatB:
    async def leave(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
    ) -> bool:
        return await self._me.leave_chat(self.id)
