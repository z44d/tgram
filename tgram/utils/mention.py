import logging

log = logging.getLogger(__name__)

HTML_MENTION = '<a href="tg://user?id={user_id}">{name}</a>'
MARKDOWN_MENTION = "[{name}](tg://user?id={user_id})"


class Mention:
    def __init__(self, name: str, user_id: int) -> None:
        self.name = name
        self.user_id = user_id

    @property
    def markdown(self) -> str:
        return MARKDOWN_MENTION.format(name=self.name, user_id=self.user_id)

    @property
    def html(self) -> str:
        return HTML_MENTION.format(name=self.name, user_id=self.user_id)

    def __str__(self) -> str:
        log.warning("Make sure to use Mention.markdown or Mention.html.")
        return self.name
