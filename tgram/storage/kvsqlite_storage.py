import tgram
from .base import StorageBase

from typing import Any, Dict, List, Tuple, Union


class KvsqliteStorage(StorageBase):
    def __init__(self, bot: "tgram.TgBot", client=None) -> None:
        super().__init__(bot, "kvsqlite", client)

    async def set(self, key: str, value: Any) -> bool:
        return await self.client.set(key, value)

    async def get(self, key: str) -> Any:
        return await self.client.get(key)

    async def add_chat(self, chat: "tgram.types.Chat") -> bool:
        chat_json = chat.json
        chats = await self.get_chats()
        if chat.username:
            chats.update({chat.username.lower(): chat.id})
        chats.update({chat.id: chat_json})
        return await self.update_chats(chats)

    async def get_chat(
        self, chat_id: Union[int, str], parse: bool = False
    ) -> Union[dict, "tgram.types.Chat"]:
        chats = await self.get_chats()

        if chat := chats.get(chat_id.lower() if isinstance(chat_id, str) else chat_id):
            if isinstance(chat, int):
                return await self.get_chat(chat, parse)
            return tgram.types.Chat._parse(self.bot, chat) if parse else chat

        return {}

    async def get_chats(self) -> Dict[str, dict]:
        return await self.client.get("chats") or {}

    async def update_chats(self, chats: Dict[str, dict]) -> bool:
        return await self.client.set("chats", chats)

    async def add_user(self, user: "tgram.types.User") -> bool:
        user_json = user.json
        users = await self.get_users()
        if user.username:
            users.update({user.username.lower(): user.id})
        users.update({user.id: user_json})
        return await self.update_users(users)

    async def get_user(
        self, user_id: Union[int, str], parse: bool = False
    ) -> Union[dict, "tgram.types.User"]:
        users = await self.get_users()

        if user := users.get(user_id.lower() if isinstance(user_id, str) else user_id):
            if isinstance(user, int):
                return await self.get_user(user, parse)
            return tgram.types.User._parse(self.bot, user) if parse else user

        return {}

    async def get_users(self) -> Dict[str, Dict]:
        return await self.client.get("users") or {}

    async def update_users(self, users: Dict[str, dict]) -> bool:
        return await self.client.set("users", users)

    async def mute(self, chat_id: int, user_id: int) -> bool:
        mute_list = await self.get_mute_list()
        packet = (chat_id, user_id)
        if packet in mute_list:
            return False
        mute_list.append(packet)
        return await self.update_mute_list(mute_list)

    async def unmute(self, chat_id: int, user_id: int) -> bool:
        mute_list = await self.get_mute_list()
        packet = (chat_id, user_id)
        if packet not in mute_list:
            return False
        mute_list.remove(packet)
        return await self.update_mute_list(mute_list)

    async def get_mute_list(self) -> List[Tuple[int, int]]:
        return await self.get("mute") or []

    async def update_mute_list(self, mute_list: List[Tuple[int, int]]) -> bool:
        return await self.set("mute", mute_list)
