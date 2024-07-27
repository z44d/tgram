import tgram
from typing import List
from typing import Union
from tgram.types import ChatMember
from tgram.types import ChatMemberAdministrator
from tgram.types import ChatMemberOwner


class GetChatAdministrators:
    async def get_chat_administrators(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> List[Union[ChatMemberAdministrator, ChatMemberOwner]]:
        result = await self._send_request(
            "getChatAdministrators",
            chat_id=chat_id,
        )
        return [ChatMember._parse(me=self, d=i) for i in result["result"]]
