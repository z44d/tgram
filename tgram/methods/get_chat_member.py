import tgram
from typing import Union
from tgram.types import ChatMember
from tgram.types import ChatMemberAdministrator
from tgram.types import ChatMemberBanned
from tgram.types import ChatMemberLeft
from tgram.types import ChatMemberMember
from tgram.types import ChatMemberOwner
from tgram.types import ChatMemberRestricted


class GetChatMember:
    async def get_chat_member(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> Union[
        ChatMemberOwner,
        ChatMemberAdministrator,
        ChatMemberMember,
        ChatMemberRestricted,
        ChatMemberBanned,
        ChatMemberLeft,
    ]:
        result = await self._send_request(
            "getChatMember",
            chat_id=chat_id,
            user_id=user_id,
        )
        return ChatMember._parse(me=self, d=result["result"])
