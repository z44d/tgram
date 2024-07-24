import tgram


class UserB:
    @property
    def mention(
        self: "tgram.types.User",
        name: str = None,
        parse_mode: str = "Markdown",
    ) -> str:
        return (
            "[{name}](tg://user?id={id})"
            if (self._me.parse_mode or parse_mode).lower() != "html"
            else '<a href="tg://user?id={id}">{name}</a>'
        ).format(name=name or self.first_name, id=self.id)

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
