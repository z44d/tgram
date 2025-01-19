import tgram

from typing import Optional


class ChatJoinRequestB:
    @property
    def user(self: "tgram.types.ChatJoinRequest") -> Optional["tgram.types.User"]:
        """
        Get the user who sent the callback query.

        Returns:
            Optional[tgram.types.User]: The user who sent the callback query.
        """
        return self.from_user

    sender_user = user
