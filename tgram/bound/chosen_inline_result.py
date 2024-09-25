import tgram

from typing import Optional


class ChosenInlineResultB:
    @property
    def user(self: "tgram.types.ChosenInlineResult") -> Optional["tgram.types.User"]:
        return self.from_user

    sender_user = user
