import tgram

from typing import Union


class ChatB:
    async def leave(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
    ) -> bool:
        return await self._me.leave_chat(self.id)

    async def ban_member(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None,
    ) -> bool:
        return await self._me.ban_chat_member(
            self.id,
            user_id=user_id,
            until_date=until_date,
            revoke_messages=revoke_messages,
        )

    async def unban_member(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
        user_id: int,
        only_if_banned: bool = None,
    ) -> bool:
        return await self._me.unban_chat_member(
            self.id,
            user_id=user_id,
            only_if_banned=only_if_banned,
        )

    async def ban_sender_chat(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"], sender_chat_id: int
    ) -> bool:
        return await self._me.ban_chat_sender_chat(
            self.id, sender_chat_id=sender_chat_id
        )

    async def unban_sender_chat(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"], sender_chat_id: int
    ) -> bool:
        return await self._me.unban_chat_sender_chat(
            self.id, sender_chat_id=sender_chat_id
        )

    async def restrict_member(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
        user_id: int,
        permissions: "tgram.types.ChatPermissions",
        use_independent_chat_permissions: bool = None,
        until_date: int = None,
    ) -> bool:
        return await self._me.restrict_chat_member(
            self.id,
            user_id=user_id,
            permissions=permissions,
            use_independent_chat_permissions=use_independent_chat_permissions,
            until_date=until_date,
        )

    async def unrestrict_member(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
        user_id: int,
        use_independent_chat_permissions: bool = None,
    ) -> bool:
        return await self._me.unrestrict_chat_member(
            self.id,
            user_id=user_id,
            use_independent_chat_permissions=use_independent_chat_permissions,
        )
