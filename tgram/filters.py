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
business_connection = Filter(
    lambda _, m: bool(getattr(m, "business_connection_id", False))
)
forward = Filter(lambda _, m: bool(getattr(m, "forward_origin", False)))
topic_message = Filter(lambda _, m: bool(getattr(m, "is_topic_message", False)))
automatic_forward = Filter(lambda _, m: bool(getattr(m, "is_automatic_forward", False)))
reply = Filter(lambda _, m: bool(getattr(m, "reply_to_message", False)))
quote = Filter(lambda _, m: bool(getattr(m, "quote", False)))
story_reply = Filter(lambda _, m: bool(getattr(m, "reply_to_story", False)))
via_bot = Filter(lambda _, m: bool(getattr(m, "via_bot", False)))
protected_content = Filter(
    lambda _, m: bool(getattr(m, "has_protected_content", False))
)
from_offline = Filter(lambda _, m: bool(getattr(m, "is_from_offline", False)))
media_group = Filter(lambda _, m: bool(getattr(m, "media_group_id", False)))
text = Filter(lambda _, m: bool(getattr(m, "text", False)))
entitied = Filter(lambda _, m: bool(getattr(m, "entities", False)))
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

reply_to_checklist_task = Filter(
    lambda _, m: isinstance(m, tgram.types.Message) and m.reply_to_checklist_task_id
)
direct_message = Filter(
    lambda _, m: isinstance(m, tgram.types.Message) and m.direct_messages_topic
)
paid_post = Filter(lambda _, m: isinstance(m, tgram.types.Message) and m.is_paid_post)
suggested_post = Filter(
    lambda _, m: isinstance(m, tgram.types.Message) and m.suggested_post_info
)
suggested_post_declined = Filter(
    lambda _, m: isinstance(m, tgram.types.Message) and m.suggested_post_declined
)
suggested_post_approved = Filter(
    lambda _, m: isinstance(m, tgram.types.Message) and m.suggested_post_approved
)
suggested_post_approval_failed = Filter(
    lambda _, m: isinstance(m, tgram.types.Message) and m.suggested_post_approval_failed
)
suggested_post_paid = Filter(
    lambda _, m: isinstance(m, tgram.types.Message) and m.suggested_post_paid
)
suggested_post_refunded = Filter(
    lambda _, m: isinstance(m, tgram.types.Message) and m.suggested_post_refunded
)

#
# Add __doc__ attributor for docs generation
#
all.__doc__ = "Matches any update."
threaded.__doc__ = (
    "Message belongs to a thread in a supergroup; Message.message_thread_id is set."
)
from_user.__doc__ = "Message has from_user (sent by a user)."
sender_chat.__doc__ = "Message has sender_chat (sent on behalf of a chat)."
business_connection.__doc__ = (
    "Message comes via a business connection; Message.business_connection_id is set."
)
forward.__doc__ = "Message is a forwarded message; Message.forward_origin is set."
topic_message.__doc__ = (
    "Message is sent to a forum topic; Message.is_topic_message is True."
)
automatic_forward.__doc__ = "Channel post automatically forwarded to the discussion group; Message.is_automatic_forward is True."
reply.__doc__ = "Message is a reply; Message.reply_to_message is set."
quote.__doc__ = "Message quotes part of another message; Message.quote is set."
story_reply.__doc__ = "Message is a reply to a story; Message.reply_to_story is set."
via_bot.__doc__ = "Message was sent via a bot; Message.via_bot is set."
protected_content.__doc__ = (
    "Message has protected content; Message.has_protected_content is True."
)
from_offline.__doc__ = (
    "Message was sent by an implicit/automated action; Message.is_from_offline is True."
)
media_group.__doc__ = "Message is part of a media group; Message.media_group_id is set."
text.__doc__ = "Message contains text; Message.text is set."
entitied.__doc__ = "Message text contains entities; Message.entities is set."
effected_message.__doc__ = "Message has an effect applied; Message.effect_id is set."
animation.__doc__ = "Message contains an animation; Message.animation is set."
audio.__doc__ = "Message contains an audio file; Message.audio is set."
document.__doc__ = "Message contains a general file; Message.document is set."
photo.__doc__ = "Message contains a photo; Message.photo is set."
sticker.__doc__ = "Message contains a sticker; Message.sticker is set."
story.__doc__ = "Message is a forwarded story; Message.story is set."
video.__doc__ = "Message contains a video; Message.video is set."
video_note.__doc__ = "Message contains a video note; Message.video_note is set."
voice.__doc__ = "Message contains a voice note; Message.voice is set."
caption.__doc__ = "Message has a caption; Message.caption is set."
media_spoiler.__doc__ = (
    "Message media is covered by a spoiler; Message.has_media_spoiler is True."
)
checklist.__doc__ = "Message is a checklist; Message.checklist is set."
contact.__doc__ = "Message contains a contact; Message.contact is set."
dice.__doc__ = "Message contains a dice; Message.dice is set."
game.__doc__ = "Message contains a game; Message.game is set."
poll.__doc__ = "Message contains a native poll; Message.poll is set."
venue.__doc__ = "Message contains a venue; Message.venue is set."
location.__doc__ = "Message contains a location; Message.location is set."
new_chat_members.__doc__ = (
    "Service message: new chat members joined; Message.new_chat_members is set."
)
left_chat_member.__doc__ = (
    "Service message: a member left/was removed; Message.left_chat_member is set."
)
new_chat_title.__doc__ = (
    "Service message: chat title was changed; Message.new_chat_title is set."
)
new_chat_photo.__doc__ = (
    "Service message: chat photo was changed; Message.new_chat_photo is set."
)
delete_chat_photo.__doc__ = (
    "Service message: chat photo was deleted; Message.delete_chat_photo is True."
)
group_chat_created.__doc__ = (
    "Service message: the group has been created; Message.group_chat_created is True."
)
supergroup_chat_created.__doc__ = "Service message: the supergroup has been created; Message.supergroup_chat_created is True."
channel_chat_created.__doc__ = "Service message: the channel has been created; Message.channel_chat_created is True."
message_auto_delete_timer_changed.__doc__ = "Service message: auto-delete timer settings changed; Message.message_auto_delete_timer_changed is set."
migrate_to_chat_id.__doc__ = "Service message: group migrated to a supergroup; Message.migrate_to_chat_id is set."
migrate_from_chat_id.__doc__ = "Service message: supergroup migrated from a group; Message.migrate_from_chat_id is set."
pinned_message.__doc__ = (
    "Service message: a message was pinned; Message.pinned_message is set."
)
invoice.__doc__ = "Message is an invoice; Message.invoice is set."
successful_payment.__doc__ = (
    "Service message: payment was successful; Message.successful_payment is set."
)
refunded_payment.__doc__ = (
    "Service message: payment was refunded; Message.refunded_payment is set."
)
users_shared.__doc__ = (
    "Service message: users were shared with the bot; Message.users_shared is set."
)
chat_shared.__doc__ = (
    "Service message: a chat was shared with the bot; Message.chat_shared is set."
)
connected_website.__doc__ = (
    "Message contains a connected website domain; Message.connected_website is set."
)
write_access_allowed.__doc__ = "Service message: user allowed the bot to write messages; Message.write_access_allowed is set."
passport_data.__doc__ = (
    "Message contains Telegram Passport data; Message.passport_data is set."
)
proximity_alert_triggered.__doc__ = "Service message: proximity alert was triggered; Message.proximity_alert_triggered is set."
boost_added.__doc__ = (
    "Service message: user boosted the chat; Message.boost_added is set."
)
chat_background_set.__doc__ = (
    "Service message: chat background set; Message.chat_background_set is set."
)
checklist_tasks_done.__doc__ = "Service message: checklist tasks were marked done/undone; Message.checklist_tasks_done is set."
checklist_tasks_added.__doc__ = "Service message: tasks were added to a checklist; Message.checklist_tasks_added is set."
direct_message_price_changed.__doc__ = "Service message: price for paid messages changed in DM; Message.direct_message_price_changed is set."
forum_topic_created.__doc__ = (
    "Service message: forum topic created; Message.forum_topic_created is set."
)
forum_topic_edited.__doc__ = (
    "Service message: forum topic edited; Message.forum_topic_edited is set."
)
forum_topic_closed.__doc__ = (
    "Service message: forum topic closed; Message.forum_topic_closed is set."
)
forum_topic_reopened.__doc__ = (
    "Service message: forum topic reopened; Message.forum_topic_reopened is set."
)
general_forum_topic_hidden.__doc__ = "Service message: the 'General' forum topic was hidden; Message.general_forum_topic_hidden is set."
general_forum_topic_unhidden.__doc__ = "Service message: the 'General' forum topic was unhidden; Message.general_forum_topic_unhidden is set."
giveaway_created.__doc__ = "Service message: a scheduled giveaway was created; Message.giveaway_created is set."
giveaway.__doc__ = "Message is a scheduled giveaway; Message.giveaway is set."
giveaway_winners.__doc__ = "Service message: a giveaway with public winners was completed; Message.giveaway_winners is set."
giveaway_completed.__doc__ = "Service message: a giveaway without public winners was completed; Message.giveaway_completed is set."
video_chat_scheduled.__doc__ = (
    "Service message: video chat scheduled; Message.video_chat_scheduled is set."
)
video_chat_started.__doc__ = (
    "Service message: video chat started; Message.video_chat_started is set."
)
video_chat_ended.__doc__ = (
    "Service message: video chat ended; Message.video_chat_ended is set."
)
video_chat_participants_invited.__doc__ = "Service message: new participants invited to a video chat; Message.video_chat_participants_invited is set."
web_app_data.__doc__ = (
    "Service message: data sent by a Web App; Message.web_app_data is set."
)
reply_markup.__doc__ = (
    "Message has an inline keyboard attached; Message.reply_markup is set."
)
service.__doc__ = "Matches service messages (e.g., joins, leaves, edits)."
media.__doc__ = (
    "Matches messages that contain any media (photo, video, document, etc.)."
)
reply_to_checklist_task.__doc__ = "Message replies to a specific checklist task; Message.reply_to_checklist_task_id is set."
direct_message.__doc__ = "Message belongs to a channel direct messages topic; Message.direct_messages_topic is set."
paid_post.__doc__ = "Message is a paid post; Message.is_paid_post is True."
suggested_post.__doc__ = (
    "Message contains suggested post info; Message.suggested_post_info is set."
)
suggested_post_declined.__doc__ = "Service message: a suggested post was declined; Message.suggested_post_declined is set."
suggested_post_approved.__doc__ = "Service message: a suggested post was approved; Message.suggested_post_approved is set."
suggested_post_approval_failed.__doc__ = "Service message: approval of a suggested post failed; Message.suggested_post_approval_failed is set."
suggested_post_paid.__doc__ = "Service message: payment for a suggested post was received; Message.suggested_post_paid is set."
suggested_post_refunded.__doc__ = "Service message: payment for a suggested post was refunded; Message.suggested_post_refunded is set."


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

private.__doc__ = "Update is from a private chat."
group.__doc__ = "Update is from a group or supergroup chat."


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
