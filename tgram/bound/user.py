import tgram

from tgram.utils import Mention, AsyncProperty
from typing import Optional


class UserB:
    @property
    def photo(self: "tgram.types.User") -> Optional["tgram.types.PhotoSize"]:
        async def func():
            r = await self._me.get_user_profile_photos(self.id, limit=1)

            if r.photos:
                return r.photos[-1][-1]

            return None

        return AsyncProperty(func, self._me).__call__()

    @property
    def mention(
        self: "tgram.types.User",
        name: str = None,
    ) -> Mention:
        return Mention(name or self.first_name, self.id)

    @property
    def full_name(self: "tgram.types.User") -> str:
        return (
            self.first_name
            if not self.last_name
            else f"{self.first_name} {self.last_name}"
        )

    @property
    def profile_link(self: "tgram.types.User") -> str:
        return (
            f"tg://user?id={self.id}"
            if not self.username
            else f"https://t.me/{self.username}"
        )
