#🔮 Filters
**Contains custom filters for processing and handling Telegram messages and events.**

##⚙️ Custom filters
- Here is an example for how to create **custom filter**:

```python
from tgram.filters import Filter
from tgram import filters

only_me = Filter(lambda bot_object, message_object: bool(message_object.from_user.id == my_id))

@bot.on_message(only_me & filters.private)
...
```

##🔥 Ready to use filters:
- `all`: **Matches any update.**

- `animation`: **Message contains an animation; Message.animation is set.**

- `audio`: **Message contains an audio file; Message.audio is set.**

- `automatic_forward`: **Channel post automatically forwarded to the discussion group; Message.is_automatic_forward is True.**

- `boost_added`: **Service message: user boosted the chat; Message.boost_added is set.**

- `business_connection`: **Message comes via a business connection; Message.business_connection_id is set.**

- `caption`: **Message has a caption; Message.caption is set.**

- `channel_chat_created`: **Service message: the channel has been created; Message.channel_chat_created is True.**

- `chat_background_set`: **Service message: chat background set; Message.chat_background_set is set.**

- `chat_shared`: **Service message: a chat was shared with the bot; Message.chat_shared is set.**

- `checklist`: **Message is a checklist; Message.checklist is set.**

- `checklist_tasks_added`: **Service message: tasks were added to a checklist; Message.checklist_tasks_added is set.**

- `checklist_tasks_done`: **Service message: checklist tasks were marked done/undone; Message.checklist_tasks_done is set.**

- `connected_website`: **Message contains a connected website domain; Message.connected_website is set.**

- `contact`: **Message contains a contact; Message.contact is set.**

- `delete_chat_photo`: **Service message: chat photo was deleted; Message.delete_chat_photo is True.**

- `dice`: **Message contains a dice; Message.dice is set.**

- `direct_message`: **Message belongs to a channel direct messages topic; Message.direct_messages_topic is set.**

- `direct_message_price_changed`: **Service message: price for paid messages changed in DM; Message.direct_message_price_changed is set.**

- `document`: **Message contains a general file; Message.document is set.**

- `effected_message`: **Message has an effect applied; Message.effect_id is set.**

- `entitied`: **Message text contains entities; Message.entities is set.**

- `forum_topic_closed`: **Service message: forum topic closed; Message.forum_topic_closed is set.**

- `forum_topic_created`: **Service message: forum topic created; Message.forum_topic_created is set.**

- `forum_topic_edited`: **Service message: forum topic edited; Message.forum_topic_edited is set.**

- `forum_topic_reopened`: **Service message: forum topic reopened; Message.forum_topic_reopened is set.**

- `forward`: **Message is a forwarded message; Message.forward_origin is set.**

- `from_offline`: **Message was sent by an implicit/automated action; Message.is_from_offline is True.**

- `from_user`: **Message has from_user (sent by a user).**

- `game`: **Message contains a game; Message.game is set.**

- `general_forum_topic_hidden`: **Service message: the 'General' forum topic was hidden; Message.general_forum_topic_hidden is set.**

- `general_forum_topic_unhidden`: **Service message: the 'General' forum topic was unhidden; Message.general_forum_topic_unhidden is set.**

- `giveaway`: **Message is a scheduled giveaway; Message.giveaway is set.**

- `giveaway_completed`: **Service message: a giveaway without public winners was completed; Message.giveaway_completed is set.**

- `giveaway_created`: **Service message: a scheduled giveaway was created; Message.giveaway_created is set.**

- `giveaway_winners`: **Service message: a giveaway with public winners was completed; Message.giveaway_winners is set.**

- `group`: **Update is from a group or supergroup chat.**

- `group_chat_created`: **Service message: the group has been created; Message.group_chat_created is True.**

- `invoice`: **Message is an invoice; Message.invoice is set.**

- `left_chat_member`: **Service message: a member left/was removed; Message.left_chat_member is set.**

- `location`: **Message contains a location; Message.location is set.**

- `media`: **Matches messages that contain any media (photo, video, document, etc.).**

- `media_group`: **Message is part of a media group; Message.media_group_id is set.**

- `media_spoiler`: **Message media is covered by a spoiler; Message.has_media_spoiler is True.**

- `message_auto_delete_timer_changed`: **Service message: auto-delete timer settings changed; Message.message_auto_delete_timer_changed is set.**

- `migrate_from_chat_id`: **Service message: supergroup migrated from a group; Message.migrate_from_chat_id is set.**

- `migrate_to_chat_id`: **Service message: group migrated to a supergroup; Message.migrate_to_chat_id is set.**

- `new_chat_members`: **Service message: new chat members joined; Message.new_chat_members is set.**

- `new_chat_photo`: **Service message: chat photo was changed; Message.new_chat_photo is set.**

- `new_chat_title`: **Service message: chat title was changed; Message.new_chat_title is set.**

- `paid_post`: **Message is a paid post; Message.is_paid_post is True.**

- `passport_data`: **Message contains Telegram Passport data; Message.passport_data is set.**

- `photo`: **Message contains a photo; Message.photo is set.**

- `pinned_message`: **Service message: a message was pinned; Message.pinned_message is set.**

- `poll`: **Message contains a native poll; Message.poll is set.**

- `private`: **Update is from a private chat.**

- `protected_content`: **Message has protected content; Message.has_protected_content is True.**

- `proximity_alert_triggered`: **Service message: proximity alert was triggered; Message.proximity_alert_triggered is set.**

- `quote`: **Message quotes part of another message; Message.quote is set.**

- `refunded_payment`: **Service message: payment was refunded; Message.refunded_payment is set.**

- `reply`: **Message is a reply; Message.reply_to_message is set.**

- `reply_markup`: **Message has an inline keyboard attached; Message.reply_markup is set.**

- `reply_to_checklist_task`: **Message replies to a specific checklist task; Message.reply_to_checklist_task_id is set.**

- `sender_chat`: **Message has sender_chat (sent on behalf of a chat).**

- `service`: **Matches service messages (e.g., joins, leaves, edits).**

- `sticker`: **Message contains a sticker; Message.sticker is set.**

- `story`: **Message is a forwarded story; Message.story is set.**

- `story_reply`: **Message is a reply to a story; Message.reply_to_story is set.**

- `successful_payment`: **Service message: payment was successful; Message.successful_payment is set.**

- `suggested_post`: **Message contains suggested post info; Message.suggested_post_info is set.**

- `suggested_post_approval_failed`: **Service message: approval of a suggested post failed; Message.suggested_post_approval_failed is set.**

- `suggested_post_approved`: **Service message: a suggested post was approved; Message.suggested_post_approved is set.**

- `suggested_post_declined`: **Service message: a suggested post was declined; Message.suggested_post_declined is set.**

- `suggested_post_paid`: **Service message: payment for a suggested post was received; Message.suggested_post_paid is set.**

- `suggested_post_refunded`: **Service message: payment for a suggested post was refunded; Message.suggested_post_refunded is set.**

- `supergroup_chat_created`: **Service message: the supergroup has been created; Message.supergroup_chat_created is True.**

- `text`: **Message contains text; Message.text is set.**

- `threaded`: **Message belongs to a thread in a supergroup; Message.message_thread_id is set.**

- `topic_message`: **Message is sent to a forum topic; Message.is_topic_message is True.**

- `users_shared`: **Service message: users were shared with the bot; Message.users_shared is set.**

- `venue`: **Message contains a venue; Message.venue is set.**

- `via_bot`: **Message was sent via a bot; Message.via_bot is set.**

- `video`: **Message contains a video; Message.video is set.**

- `video_chat_ended`: **Service message: video chat ended; Message.video_chat_ended is set.**

- `video_chat_participants_invited`: **Service message: new participants invited to a video chat; Message.video_chat_participants_invited is set.**

- `video_chat_scheduled`: **Service message: video chat scheduled; Message.video_chat_scheduled is set.**

- `video_chat_started`: **Service message: video chat started; Message.video_chat_started is set.**

- `video_note`: **Message contains a video note; Message.video_note is set.**

- `voice`: **Message contains a voice note; Message.voice is set.**

- `web_app_data`: **Service message: data sent by a Web App; Message.web_app_data is set.**

- `write_access_allowed`: **Service message: user allowed the bot to write messages; Message.write_access_allowed is set.**

- `chat`: **Filter messages coming from one or more chats**

- `chat_type`: **Filter updates that match a given chat type.**

- `command`: **Filter commands, i.e.: text messages starting with "/" or any other custom prefix.**

- `parameter`: **Filters command parameters using the specified regular expression pattern.**

- `regex`: **Filter updates that match a given regular expression pattern.**

- `sender`: **Filter messages coming from one or more sender chat**

- `user`: **Filter messages coming from one or more users**

