import tgram

from typing import Optional


class ShippingQueryB:
    @property
    def user(self: "tgram.types.ShippingQuery") -> Optional["tgram.types.User"]:
        return self.from_user

    sender_user = user
