from typing import Optional

import tgram


class ChosenInlineResultB:
    @property
    def user(self: "tgram.types.ChosenInlineResult") -> Optional["tgram.types.User"]:
        return self.from_user

    sender_user = user
