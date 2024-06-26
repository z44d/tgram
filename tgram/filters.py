from typing import Callable, Any


class Filter:
    def __init__(self, filter_: Callable[[Any], bool]) -> None:
        self._filter = filter_

    def __call__(self, arg: Any) -> bool:
        return self._filter(arg)

    def __invert__(self) -> "Filter":
        return Filter(lambda v: not self(v))

    def __and__(self, other: "Filter") -> "Filter":
        return Filter(lambda v: self(v) and other(v))

    def __or__(self, other: "Filter") -> "Filter":
        return Filter(lambda v: self(v) or other(v))


all = Filter(lambda _: True)
threaded = Filter(lambda m: getattr(m, "message_thread_id"))
from_user = Filter(lambda m: getattr(m, "from_user"))
sender_chat = Filter(lambda m: getattr(m, "sender_chat"))
business_connection_id = Filter(lambda m: getattr(m, "business_connection_id"))
forward = Filter(lambda m: getattr(m, "forward_origin"))
topic_message = Filter(lambda m: getattr(m, "is_topic_message"))
automatic_forward = Filter(lambda m: getattr(m, "is_automatic_forward"))
reply = Filter(lambda m: getattr(m, "reply_to_message"))
quote = Filter(lambda m: getattr(m, "quote"))
reply_to_story = Filter(lambda m: getattr(m, "reply_to_story"))
via_bot = Filter(lambda m: getattr(m, "via_bot"))
protected_content = Filter(lambda m: getattr(m, "has_protected_content"))
from_offline = Filter(lambda m: getattr(m, "is_from_offline"))
media_group = Filter(lambda m: getattr(m, "media_group_id"))
text = Filter(lambda m: getattr(m, "text"))
entities = Filter(lambda m: getattr(m, "entities"))
effected_message = Filter(lambda m: getattr(m, "effect_id"))
animation = Filter(lambda m: getattr(m, "animation"))
audio = Filter(lambda m: getattr(m, "audio"))
document = Filter(lambda m: getattr(m, "document"))
photo = Filter(lambda m: getattr(m, "photo"))
sticker = Filter(lambda m: getattr(m, "sticker"))
story = Filter(lambda m: getattr(m, "story"))
video = Filter(lambda m: getattr(m, "video"))
video_note = Filter(lambda m: getattr(m, "video_note"))
voice = Filter(lambda m: getattr(m, "voice"))
caption = Filter(lambda m: getattr(m, "caption"))
media_spoiler = Filter(lambda m: getattr(m, "has_media_spoiler"))
contact = Filter(lambda m: getattr(m, "contact"))
dice = Filter(lambda m: getattr(m, "dice"))
game = Filter(lambda m: getattr(m, "game"))
poll = Filter(lambda m: getattr(m, "poll"))
venue = Filter(lambda m: getattr(m, "venue"))
location = Filter(lambda m: getattr(m, "location"))
new_chat_members = Filter(lambda m: getattr(m, "new_chat_members"))
left_chat_member = Filter(lambda m: getattr(m, "left_chat_member"))
new_chat_title = Filter(lambda m: getattr(m, "new_chat_title"))
new_chat_photo = Filter(lambda m: getattr(m, "new_chat_photo"))
delete_chat_photo = Filter(lambda m: getattr(m, "delete_chat_photo"))
group_chat_created = Filter(lambda m: getattr(m, "group_chat_created"))
supergroup_chat_created = Filter(lambda m: getattr(m, "supergroup_chat_created"))
channel_chat_created = Filter(lambda m: getattr(m, "channel_chat_created"))
message_auto_delete_timer_changed = Filter(
    lambda m: getattr(m, "message_auto_delete_timer_changed")
)
migrate_to_chat_id = Filter(lambda m: getattr(m, "migrate_to_chat_id"))
migrate_from_chat_id = Filter(lambda m: getattr(m, "migrate_from_chat_id"))
pinned_message = Filter(lambda m: getattr(m, "pinned_message"))
invoice = Filter(lambda m: getattr(m, "invoice"))
successful_payment = Filter(lambda m: getattr(m, "successful_payment"))
users_shared = Filter(lambda m: getattr(m, "users_shared"))
chat_shared = Filter(lambda m: getattr(m, "chat_shared"))
connected_website = Filter(lambda m: getattr(m, "connected_website"))
write_access_allowed = Filter(lambda m: getattr(m, "write_access_allowed"))
passport_data = Filter(lambda m: getattr(m, "passport_data"))
proximity_alert_triggered = Filter(lambda m: getattr(m, "proximity_alert_triggered"))
boost_added = Filter(lambda m: getattr(m, "boost_added"))
chat_background_set = Filter(lambda m: getattr(m, "chat_background_set"))
forum_topic_created = Filter(lambda m: getattr(m, "forum_topic_created"))
forum_topic_edited = Filter(lambda m: getattr(m, "forum_topic_edited"))
forum_topic_closed = Filter(lambda m: getattr(m, "forum_topic_closed"))
forum_topic_reopened = Filter(lambda m: getattr(m, "forum_topic_reopened"))
general_forum_topic_hidden = Filter(lambda m: getattr(m, "general_forum_topic_hidden"))
general_forum_topic_unhidden = Filter(
    lambda m: getattr(m, "general_forum_topic_unhidden")
)
giveaway_created = Filter(lambda m: getattr(m, "giveaway_created"))
giveaway = Filter(lambda m: getattr(m, "giveaway"))
giveaway_winners = Filter(lambda m: getattr(m, "giveaway_winners"))
giveaway_completed = Filter(lambda m: getattr(m, "giveaway_completed"))
video_chat_scheduled = Filter(lambda m: getattr(m, "video_chat_scheduled"))
video_chat_started = Filter(lambda m: getattr(m, "video_chat_started"))
video_chat_ended = Filter(lambda m: getattr(m, "video_chat_ended"))
video_chat_participants_invited = Filter(
    lambda m: getattr(m, "video_chat_participants_invited")
)
web_app_data = Filter(lambda m: getattr(m, "web_app_data"))
reply_markup = Filter(lambda m: getattr(m, "reply_markup"))
