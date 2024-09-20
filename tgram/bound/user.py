import tgram

from tgram.utils import Mention, async_property


class UserB:
    @async_property
    async def photo(self: "tgram.types.User") -> "tgram.types.PhotoSize":
        return (await self._me.get_user_profile_photos(self.id, limit=1)).photos[-1][-1]

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
