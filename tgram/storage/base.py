import tgram

from abc import abstractmethod, ABC
from typing import Any, Dict, Union, List, Tuple


class StorageBase(ABC):
    def __init__(self, bot: "tgram.TgBot", type: "str", client) -> None:
        if type == "kvsqlite":
            from kvsqlite import Client

            self.client = client or Client(
                "tgram-" + str(bot.me.id), workers=bot.workers, loop=bot.loop
            )
        elif type == "redis":
            import redis.asyncio as redis

            self.client = client or redis.Redis(decode_responses=True)
        self.bot = bot

    @abstractmethod
    async def set(self, key: str, value: Any) -> bool:
        """
        Set a key, value into database.
        """
        raise NotImplementedError

    @abstractmethod
    async def get(self, key: str) -> Any:
        """
        Get a value from database using a key.
        """
        raise NotImplementedError

    @abstractmethod
    async def add_chat(self, chat: "tgram.types.Chat") -> bool:
        """
        Add Chat json info into database.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_chat(
        self, chat_id: Union[int, str], parse: bool = False
    ) -> Union[dict, "tgram.types.Chat"]:
        """
        Get a Chat object or json info from database.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_chats(self) -> Dict[str, dict]:
        """
        Get all chats from the list.
        """
        raise NotImplementedError

    @abstractmethod
    async def update_chats(self, chats: Dict[str, dict]) -> bool:
        """
        Update Chats List.
        """
        raise NotImplementedError

    @abstractmethod
    async def add_user(self, user: "tgram.types.User") -> bool:
        """
        Add User json info into database.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_user(
        self, user_id: Union[int, str], parse: bool = False
    ) -> Union[dict, "tgram.types.User"]:
        """
        Get a User object or json info from database.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_users(self) -> Dict[str, dict]:
        """
        Get all chats from the list.
        """
        raise NotImplementedError

    @abstractmethod
    async def update_users(self, users: Dict[str, dict]) -> bool:
        """
        Update Users List.
        """
        raise NotImplementedError

    @abstractmethod
    async def mute(self, chat_id: int, user_id: int) -> bool:
        """
        Mute a User or Sender-Chat in Group Chat.
        """
        raise NotImplementedError

    @abstractmethod
    async def unmute(self, chat_id: int, user_id: int) -> bool:
        """
        Un-Mute a User or Sender-Chat in Group Chat.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_mute_list(self) -> List[Tuple[int, int]]:
        """
        Get a List of Muted users/senders-chats.
        """
        raise NotImplementedError

    @abstractmethod
    async def update_mute_list(self, mute_list: List[Tuple[int, int]]) -> bool:
        """
        Update The List of Muted users/senders-chats.
        """
        raise NotImplementedError
