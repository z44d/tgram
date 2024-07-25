import tgram

from tgram.utils import String


class UserB:
    @property
    def mention(
        self: "tgram.types.User",
        name: str = None,
    ) -> String:
        return String(name or self.first_name).put(
            [
                tgram.types.MessageEntity(
                    "text_mention", 0, len(name or self.first_name), user=self
                )
            ]
        )

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
