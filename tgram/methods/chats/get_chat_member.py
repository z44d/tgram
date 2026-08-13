import tgram
from tgram.types import (
    ChatMember,
    ChatMemberAdministrator,
    ChatMemberBanned,
    ChatMemberLeft,
    ChatMemberMember,
    ChatMemberOwner,
    ChatMemberRestricted,
)


class GetChatMember:
    async def get_chat_member(
        self: "tgram.TgBot", chat_id: int | str, user_id: int
    ) -> (
        ChatMemberOwner
        | ChatMemberAdministrator
        | ChatMemberMember
        | ChatMemberRestricted
        | ChatMemberBanned
        | ChatMemberLeft
    ):
        result = await self(
            "getChatMember",
            chat_id=chat_id,
            user_id=user_id,
        )
        return ChatMember._parse(me=self, d=result.get("result", {}))
