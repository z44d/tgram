import tgram

from typing import Optional


class ChatJoinRequestB:
    @property
    def user(self: "tgram.types.ChatJoinRequest") -> Optional["tgram.types.User"]:
        return self.from_user

    sender_user = user
