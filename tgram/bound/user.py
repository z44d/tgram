import tgram

from tgram.utils import Mention


class UserB:
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
