import tgram

from typing import Optional


class ChatMemberUpdatedB:
    @property
    def user(self: "tgram.types.ChatMemberUpdated") -> Optional["tgram.types.User"]:
        """
        Get the user who sent the callback query.

        Returns:
            Optional[tgram.types.User]: The user who sent the callback query.
        """
        return self.from_user

    sender_user = user
