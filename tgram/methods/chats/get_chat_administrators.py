import tgram
from tgram.types import ChatMember, ChatMemberAdministrator, ChatMemberOwner


class GetChatAdministrators:
    async def get_chat_administrators(
        self: "tgram.TgBot",
        chat_id: int | str,
        return_bots: bool | None = None,
    ) -> list[ChatMemberAdministrator | ChatMemberOwner]:
        result = await self(
            "getChatAdministrators",
            chat_id=chat_id,
            return_bots=return_bots,
        )
        return [ChatMember._parse(me=self, d=i) for i in result.get("result", {})]
