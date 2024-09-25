import tgram

from typing import Optional


class PaidMediaPurchasedB:
    @property
    def user(self: "tgram.types.PaidMediaPurchased") -> Optional["tgram.types.User"]:
        return self.from_user

    sender_user = user
