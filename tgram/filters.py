from typing import Callable, Any, Union, List, Pattern, Coroutine
import tgram
import re
import inspect
import asyncio


class Filter:
    def __init__(self, filter_: Union[Callable, Coroutine]) -> None:
        self._filter = filter_

    async def __call__(self, bot: "tgram.TgBot", update: Any) -> bool:
        if inspect.iscoroutinefunction(self._filter):
            result = await self._filter(bot, update)
        else:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, self._filter, bot, update)
        return bool(result)

    def __invert__(self) -> "Filter":
        async def func(*args):
            return not await self(*args)

        return Filter(func)

    def __and__(self, other: "Filter") -> "Filter":
        async def func(*args):
            return await self(*args) and await other(*args)

        return Filter(func)

    def __or__(self, other: "Filter") -> "Filter":
        async def func(*args):
            return await self(*args) or await other(*args)

        return Filter(func)


all = Filter(lambda _, __: True)
threaded = Filter(lambda _, m: bool(getattr(m, "message_thread_id", False)))
from_user = Filter(lambda _, m: bool(getattr(m, "from_user", False)))
sender_chat = Filter(lambda _, m: bool(getattr(m, "sender_chat", False)))
business_connection_id = Filter(
    lambda _, m: bool(getattr(m, "business_connection_id", False))
)
forward = Filter(lambda _, m: bool(getattr(m, "forward_origin", False)))
topic_message = Filter(lambda _, m: bool(getattr(m, "is_topic_message", False)))
automatic_forward = Filter(lambda _, m: bool(getattr(m, "is_automatic_forward", False)))
reply = Filter(lambda _, m: bool(getattr(m, "reply_to_message", False)))
quote = Filter(lambda _, m: bool(getattr(m, "quote", False)))
reply_to_story = Filter(lambda _, m: bool(getattr(m, "reply_to_story", False)))
via_bot = Filter(lambda _, m: bool(getattr(m, "via_bot", False)))
protected_content = Filter(
    lambda _, m: bool(getattr(m, "has_protected_content", False))
)
from_offline = Filter(lambda _, m: bool(getattr(m, "is_from_offline", False)))
media_group = Filter(lambda _, m: bool(getattr(m, "media_group_id", False)))
text = Filter(lambda _, m: bool(getattr(m, "text", False)))
entities = Filter(lambda _, m: bool(getattr(m, "entities", False)))
effected_message = Filter(lambda _, m: bool(getattr(m, "effect_id", False)))
animation = Filter(lambda _, m: bool(getattr(m, "animation", False)))
audio = Filter(lambda _, m: bool(getattr(m, "audio", False)))
document = Filter(lambda _, m: bool(getattr(m, "document", False)))
photo = Filter(lambda _, m: bool(getattr(m, "photo", False)))
sticker = Filter(lambda _, m: bool(getattr(m, "sticker", False)))
story = Filter(lambda _, m: bool(getattr(m, "story", False)))
video = Filter(lambda _, m: bool(getattr(m, "video", False)))
video_note = Filter(lambda _, m: bool(getattr(m, "video_note", False)))
voice = Filter(lambda _, m: bool(getattr(m, "voice", False)))
caption = Filter(lambda _, m: bool(getattr(m, "caption", False)))
media_spoiler = Filter(lambda _, m: bool(getattr(m, "has_media_spoiler", False)))
checklist = Filter(lambda _, m: bool(getattr(m, "checklist", False)))
contact = Filter(lambda _, m: bool(getattr(m, "contact", False)))
dice = Filter(lambda _, m: bool(getattr(m, "dice", False)))
game = Filter(lambda _, m: bool(getattr(m, "game", False)))
poll = Filter(lambda _, m: bool(getattr(m, "poll", False)))
venue = Filter(lambda _, m: bool(getattr(m, "venue", False)))
location = Filter(lambda _, m: bool(getattr(m, "location", False)))
new_chat_members = Filter(lambda _, m: bool(getattr(m, "new_chat_members", False)))
left_chat_member = Filter(lambda _, m: bool(getattr(m, "left_chat_member", False)))
new_chat_title = Filter(lambda _, m: bool(getattr(m, "new_chat_title", False)))
new_chat_photo = Filter(lambda _, m: bool(getattr(m, "new_chat_photo", False)))
delete_chat_photo = Filter(lambda _, m: bool(getattr(m, "delete_chat_photo", False)))
group_chat_created = Filter(lambda _, m: bool(getattr(m, "group_chat_created", False)))
supergroup_chat_created = Filter(
    lambda _, m: bool(getattr(m, "supergroup_chat_created", False))
)
channel_chat_created = Filter(
    lambda _, m: bool(getattr(m, "channel_chat_created", False))
)
message_auto_delete_timer_changed = Filter(
    lambda _, m: bool(getattr(m, "message_auto_delete_timer_changed", False))
)
migrate_to_chat_id = Filter(lambda _, m: bool(getattr(m, "migrate_to_chat_id", False)))
migrate_from_chat_id = Filter(
    lambda _, m: bool(getattr(m, "migrate_from_chat_id", False))
)
pinned_message = Filter(lambda _, m: bool(getattr(m, "pinned_message", False)))
invoice = Filter(lambda _, m: bool(getattr(m, "invoice", False)))
successful_payment = Filter(lambda _, m: bool(getattr(m, "successful_payment", False)))
refunded_payment = Filter(lambda _, m: bool(getattr(m, "refunded_payment", False)))
users_shared = Filter(lambda _, m: bool(getattr(m, "users_shared", False)))
chat_shared = Filter(lambda _, m: bool(getattr(m, "chat_shared", False)))
connected_website = Filter(lambda _, m: bool(getattr(m, "connected_website", False)))
write_access_allowed = Filter(
    lambda _, m: bool(getattr(m, "write_access_allowed", False))
)
passport_data = Filter(lambda _, m: bool(getattr(m, "passport_data", False)))
proximity_alert_triggered = Filter(
    lambda _, m: bool(getattr(m, "proximity_alert_triggered", False))
)
boost_added = Filter(lambda _, m: bool(getattr(m, "boost_added", False)))
chat_background_set = Filter(
    lambda _, m: bool(getattr(m, "chat_background_set", False))
)
checklist_tasks_done = Filter(
    lambda _, m: bool(getattr(m, "checklist_tasks_done", False))
)
checklist_tasks_added = Filter(
    lambda _, m: bool(getattr(m, "checklist_tasks_added", False))
)
direct_message_price_changed = Filter(
    lambda _, m: bool(getattr(m, "direct_message_price_changed", False))
)
forum_topic_created = Filter(
    lambda _, m: bool(getattr(m, "forum_topic_created", False))
)
forum_topic_edited = Filter(lambda _, m: bool(getattr(m, "forum_topic_edited", False)))
forum_topic_closed = Filter(lambda _, m: bool(getattr(m, "forum_topic_closed", False)))
forum_topic_reopened = Filter(
    lambda _, m: bool(getattr(m, "forum_topic_reopened", False))
)
general_forum_topic_hidden = Filter(
    lambda _, m: bool(getattr(m, "general_forum_topic_hidden", False))
)
general_forum_topic_unhidden = Filter(
    lambda _, m: bool(getattr(m, "general_forum_topic_unhidden", False))
)
giveaway_created = Filter(lambda _, m: bool(getattr(m, "giveaway_created", False)))
giveaway = Filter(lambda _, m: bool(getattr(m, "giveaway", False)))
giveaway_winners = Filter(lambda _, m: bool(getattr(m, "giveaway_winners", False)))
giveaway_completed = Filter(lambda _, m: bool(getattr(m, "giveaway_completed", False)))
video_chat_scheduled = Filter(
    lambda _, m: bool(getattr(m, "video_chat_scheduled", False))
)
video_chat_started = Filter(lambda _, m: bool(getattr(m, "video_chat_started", False)))
video_chat_ended = Filter(lambda _, m: bool(getattr(m, "video_chat_ended", False)))
video_chat_participants_invited = Filter(
    lambda _, m: bool(getattr(m, "video_chat_participants_invited", False))
)
web_app_data = Filter(lambda _, m: bool(getattr(m, "web_app_data", False)))
reply_markup = Filter(lambda _, m: bool(getattr(m, "reply_markup", False)))

service = Filter(lambda _, m: isinstance(m, tgram.types.Message) and m.service)
media = Filter(lambda _, m: isinstance(m, tgram.types.Message) and m.media)


def sender(ids: Union[str, int, List[Union[str, int]]]) -> Filter:
    """Filter messages coming from one or more sender chat"""
    ids = (
        {ids.lower() if isinstance(ids, str) else ids}
        if not isinstance(ids, list)
        else {i.lower() if isinstance(i, str) else i for i in ids}
    )
    return Filter(
        lambda _, m: getattr(m, "sender_chat")
        and (
            m.sender_chat.id in ids
            or (m.sender_chat.username and m.sender_chat.username.lower() in ids)
        )
    )


def user(ids: Union[str, int, List[Union[str, int]]]) -> Filter:
    """Filter messages coming from one or more users"""
    ids = (
        {ids.lower() if isinstance(ids, str) else ids}
        if not isinstance(ids, list)
        else {i.lower() if isinstance(i, str) else i for i in ids}
    )
    return Filter(
        lambda _, m: getattr(m, "from_user")
        and (
            m.from_user.id in ids
            or (m.from_user.username and m.from_user.username.lower() in ids)
        )
    )


def chat(ids: Union[str, int, List[Union[str, int]]]) -> Filter:
    """Filter messages coming from one or more chats"""
    ids = (
        {ids.lower() if isinstance(ids, str) else ids}
        if not isinstance(ids, list)
        else {i.lower() if isinstance(i, str) else i for i in ids}
    )
    return Filter(
        lambda _, m: getattr(m, "chat")
        and (m.chat.id in ids or (m.chat.username and m.chat.username.lower() in ids))
    )


def regex(pattern: Union[str, Pattern], flags: int = 0) -> Filter:
    """Filter updates that match a given regular expression pattern."""
    compiler = pattern if isinstance(pattern, Pattern) else re.compile(pattern, flags)

    async def regex_filter(_, m):
        if not isinstance(
            m,
            (
                tgram.types.Message,
                tgram.types.CallbackQuery,
                tgram.types.InlineQuery,
                tgram.types.PreCheckoutQuery,
            ),
        ):
            raise ValueError(f"Regex filter doesn't work with {m.__class__.__name__}")

        value = (
            (m.text or m.caption)
            if isinstance(m, tgram.types.Message)
            else m.data
            if isinstance(m, tgram.types.CallbackQuery)
            else m.query
            if isinstance(m, tgram.types.InlineQuery)
            else m.invoice_payload
            if isinstance(m, tgram.types.PreCheckoutQuery)
            else None
        )

        if value is None:
            return False

        m.matches = list(compiler.finditer(value)) or None
        return bool(m.matches)

    return Filter(regex_filter)


def chat_type(types: Union[list, str]) -> Filter:
    """Filter updates that match a given chat type."""
    types = (
        {types.lower()} if not isinstance(types, list) else {i.lower() for i in types}
    )

    async def chat_filter(_, m):
        if isinstance(m, tgram.types.CallbackQuery) and m.message and m.message.chat:
            chat_type = m.message.chat.type
        elif isinstance(m, tgram.types.InlineQuery):
            chat_type = m.chat_type
        elif getattr(m, "chat"):  # Most of other updates types have chat attribute.
            chat_type = m.chat.type
        else:
            raise ValueError(
                f"Chat type filter doesn't work with {m.__class__.__name__}"
            )

        return bool(chat_type in types)

    return Filter(chat_filter)


private = chat_type("private")
group = chat_type(["group", "supergroup"])


def command(
    commands: Union[str, List[str]],
    prefixes: Union[str, List[str]] = "/",
    case_sensitive: bool = False,
) -> Filter:
    """Filter commands, i.e.: text messages starting with "/" or any other custom prefix."""
    commands = commands if isinstance(commands, list) else [commands]
    commands = {c if case_sensitive else c.lower() for c in commands}

    prefixes = [] if prefixes is None else prefixes
    prefixes = prefixes if isinstance(prefixes, list) else [prefixes]
    prefixes = set(prefixes) if prefixes else {""}
    command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

    async def filter_func(b: "tgram.TgBot", m: "tgram.types.Message"):
        text = m.text or m.caption
        username = b.me.username

        if text is None:
            return False

        for prefix in prefixes:
            if not text.startswith(prefix):
                continue

            without_prefix = text[len(prefix) :]

            for cmd in commands:
                if not re.match(
                    rf"^(?:{cmd}(?:@?{username})?)(?:\s|$)",
                    without_prefix,
                    flags=re.IGNORECASE if not case_sensitive else 0,
                ):
                    continue

                without_command = re.sub(
                    rf"{cmd}(?:@?{username})?\s?",
                    "",
                    without_prefix,
                    count=1,
                    flags=re.IGNORECASE if not case_sensitive else 0,
                )
                m.command = [cmd] + [
                    re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                    for m in command_re.finditer(without_command)
                ]
                return True

        return False

    return Filter(filter_func)


def parameter(pattern: Union[str, Pattern]) -> Filter:
    """
    Filters command parameters using the specified regular expression pattern.

    This filter extracts parameters from commands (e.g., `/start ref_123`) by matching them against the provided regex pattern.
    Useful for handling commands with dynamic arguments.

    Args:
        pattern (Union[str, Pattern]): The regular expression pattern to match command parameters.
        flags (int, optional): Regex flags to modify matching behavior. Defaults to 0.

    Returns:
        Filter: A filter object that matches command parameters based on the given pattern.
    """

    async def parameter_func(b: "tgram.TgBot", m: "tgram.types.Message") -> bool:
        if not m.text:
            return False

        param = m.parameter

        if not param:
            return False

        return bool(re.match(pattern, param))

    return Filter(parameter_func)
