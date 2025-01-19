import tgram

from typing import Union, List
from tgram.utils import Mention


class ChatB:
    async def leave(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
    ) -> bool:
        """
        Leave the chat.

        Returns:
            bool: True if the bot successfully left the chat, False otherwise.
        """
        return await self._me.leave_chat(self.id)

    async def ban_member(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None,
    ) -> bool:
        """
        Ban a member from the chat.

        Args:
            user_id (int): The ID of the user to ban.
            until_date (int, optional): Date when the user will be unbanned, unix time.
            revoke_messages (bool, optional): Pass True to delete all messages from the chat for the user that is being removed.

        Returns:
            bool: True if the user was successfully banned, False otherwise.
        """
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
        """
        Unban a previously banned member from the chat.

        Args:
            user_id (int): The ID of the user to unban.
            only_if_banned (bool, optional): Do nothing if the user is not banned.

        Returns:
            bool: True if the user was successfully unbanned, False otherwise.
        """
        return await self._me.unban_chat_member(
            self.id,
            user_id=user_id,
            only_if_banned=only_if_banned,
        )

    async def ban_sender_chat(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"], sender_chat_id: int
    ) -> bool:
        """
        Ban a channel chat in a supergroup or a channel.

        Args:
            sender_chat_id (int): The ID of the sender chat to ban.

        Returns:
            bool: True if the sender chat was successfully banned, False otherwise.
        """
        return await self._me.ban_chat_sender_chat(
            self.id, sender_chat_id=sender_chat_id
        )

    async def unban_sender_chat(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"], sender_chat_id: int
    ) -> bool:
        """
        Unban a previously banned channel chat in a supergroup or a channel.

        Args:
            sender_chat_id (int): The ID of the sender chat to unban.

        Returns:
            bool: True if the sender chat was successfully unbanned, False otherwise.
        """
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
        """
        Restrict a member in the chat.

        Args:
            user_id (int): The ID of the user to restrict.
            permissions (tgram.types.ChatPermissions): New user permissions.
            use_independent_chat_permissions (bool, optional): Pass True if chat permissions are set independently.
            until_date (int, optional): Date when restrictions will be lifted for the user, unix time.

        Returns:
            bool: True if the user was successfully restricted, False otherwise.
        """
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
        """
        Unrestrict a previously restricted member in the chat.

        Args:
            user_id (int): The ID of the user to unrestrict.
            use_independent_chat_permissions (bool, optional): Pass True if chat permissions are set independently.

        Returns:
            bool: True if the user was successfully unrestricted, False otherwise.
        """
        return await self._me.unrestrict_chat_member(
            self.id,
            user_id=user_id,
            use_independent_chat_permissions=use_independent_chat_permissions,
        )

    async def mute(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"], user_id: int
    ) -> bool:
        """
        Mute a member in the chat.

        Args:
            user_id (int): The ID of the user to mute.

        Returns:
            bool: True if the user was successfully muted, False otherwise.
        """
        if self._me.storage is None:
            raise ValueError("Please enable storage option in TgBot class.")

        return await self._me.storage.mute(self.id, user_id)

    async def unmute(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"], user_id: int
    ) -> bool:
        """
        Unmute a previously muted member in the chat.

        Args:
            user_id (int): The ID of the user to unmute.

        Returns:
            bool: True if the user was successfully unmuted, False otherwise.
        """
        if self._me.storage is None:
            raise ValueError("Please enable storage option in TgBot class.")

        return await self._me.storage.unmute(self.id, user_id)

    async def get_muted_members(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
    ) -> List[int]:
        """
        Get a list of muted members in the chat.

        Returns:
            List[int]: A list of user IDs who are muted in the chat.
        """
        if self._me.storage is None:
            raise ValueError("Please enable storage option in TgBot class.")

        mute_list = await self._me.storage.get_mute_list()

        return [user_id for chat_id, user_id in mute_list if chat_id is self.id]

    @property
    def mention(
        self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"],
        name: str = None,
    ) -> Mention:
        """
        Get a mention object for the chat.

        Args:
            name (str, optional): The name to use for the mention. Defaults to the chat's first name.

        Returns:
            Mention: A mention object for the chat.
        """
        if self.type != "private":
            raise ValueError(
                "You can't mention groups or channels, the chat instance must be user."
            )

        return Mention(name or self.first_name, self.id)

    @property
    def full_name(self: Union["tgram.types.Chat", "tgram.types.ChatFullInfo"]) -> str:
        """
        Get the full name of the chat.

        Returns:
            str: The full name of the chat.
        """
        if self.type != "private":
            raise ValueError(
                "You can't get full name of groups or channels, the chat instance must be user."
            )

        return (
            self.first_name
            if not self.last_name
            else f"{self.first_name} {self.last_name}"
        )
