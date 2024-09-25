import tgram

from typing import Optional


class ChatMemberUpdatedB:
    @property
    def user(self: "tgram.types.ChatMemberUpdated") -> Optional["tgram.types.User"]:
        return self.from_user

    sender_user = user
