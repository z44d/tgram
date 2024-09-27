from pathlib import Path as _Path
from typing import Union as _Union, Literal as _Literal
from io import BytesIO as _BytesIo

from ._animation import Animation
from ._audio import Audio
from ._background_fill import BackgroundFill
from ._background_fill_freeform_gradient import BackgroundFillFreeformGradient
from ._background_fill_gradient import BackgroundFillGradient
from ._background_fill_solid import BackgroundFillSolid
from ._background_type import BackgroundType
from ._background_type_chat_theme import BackgroundTypeChatTheme
from ._background_type_fill import BackgroundTypeFill
from ._background_type_pattern import BackgroundTypePattern
from ._background_type_wallpaper import BackgroundTypeWallpaper
from ._birthdate import Birthdate
from ._bot_command import BotCommand
from ._bot_command_scope import BotCommandScope
from ._bot_command_scope_all_chat_administrators import (
    BotCommandScopeAllChatAdministrators,
)
from ._bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats
from ._bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
from ._bot_command_scope_chat import BotCommandScopeChat
from ._bot_command_scope_chat_administrators import BotCommandScopeChatAdministrators
from ._bot_command_scope_chat_member import BotCommandScopeChatMember
from ._bot_command_scope_default import BotCommandScopeDefault
from ._bot_description import BotDescription
from ._bot_name import BotName
from ._bot_short_description import BotShortDescription
from ._business_connection import BusinessConnection
from ._business_intro import BusinessIntro
from ._business_location import BusinessLocation
from ._business_messages_deleted import BusinessMessagesDeleted
from ._business_opening_hours import BusinessOpeningHours
from ._business_opening_hours_interval import BusinessOpeningHoursInterval
from ._callback_game import CallbackGame
from ._callback_query import CallbackQuery
from ._chat import Chat
from ._chat_administrator_rights import ChatAdministratorRights
from ._chat_background import ChatBackground
from ._chat_boost import ChatBoost
from ._chat_boost_added import ChatBoostAdded
from ._chat_boost_removed import ChatBoostRemoved
from ._chat_boost_source import ChatBoostSource
from ._chat_boost_source_gift_code import ChatBoostSourceGiftCode
from ._chat_boost_source_giveaway import ChatBoostSourceGiveaway
from ._chat_boost_source_premium import ChatBoostSourcePremium
from ._chat_boost_updated import ChatBoostUpdated
from ._chat_full_info import ChatFullInfo
from ._chat_invite_link import ChatInviteLink
from ._chat_join_request import ChatJoinRequest
from ._chat_location import ChatLocation
from ._chat_member import ChatMember
from ._chat_member_administrator import ChatMemberAdministrator
from ._chat_member_banned import ChatMemberBanned
from ._chat_member_left import ChatMemberLeft
from ._chat_member_member import ChatMemberMember
from ._chat_member_owner import ChatMemberOwner
from ._chat_member_restricted import ChatMemberRestricted
from ._chat_member_updated import ChatMemberUpdated
from ._chat_permissions import ChatPermissions
from ._chat_photo import ChatPhoto
from ._chat_shared import ChatShared
from ._chosen_inline_result import ChosenInlineResult
from ._contact import Contact
from ._dice import Dice
from ._document import Document
from ._encrypted_credentials import EncryptedCredentials
from ._encrypted_passport_element import EncryptedPassportElement
from ._external_reply_info import ExternalReplyInfo
from ._file import File
from ._force_reply import ForceReply
from ._forum_topic import ForumTopic
from ._forum_topic_closed import ForumTopicClosed
from ._forum_topic_created import ForumTopicCreated
from ._forum_topic_edited import ForumTopicEdited
from ._forum_topic_reopened import ForumTopicReopened
from ._game import Game
from ._game_high_score import GameHighScore
from ._general_forum_topic_hidden import GeneralForumTopicHidden
from ._general_forum_topic_unhidden import GeneralForumTopicUnhidden
from ._giveaway import Giveaway
from ._giveaway_completed import GiveawayCompleted
from ._giveaway_created import GiveawayCreated
from ._giveaway_winners import GiveawayWinners
from ._inaccessible_message import InaccessibleMessage
from ._inline_keyboard_button import InlineKeyboardButton
from ._inline_keyboard_markup import InlineKeyboardMarkup
from ._inline_query import InlineQuery
from ._inline_query_result_article import InlineQueryResultArticle
from ._inline_query_result_audio import InlineQueryResultAudio
from ._inline_query_result_cached_audio import InlineQueryResultCachedAudio
from ._inline_query_result_cached_document import InlineQueryResultCachedDocument
from ._inline_query_result_cached_gif import InlineQueryResultCachedGif
from ._inline_query_result_cached_mpeg4_gif import InlineQueryResultCachedMpeg4Gif
from ._inline_query_result_cached_photo import InlineQueryResultCachedPhoto
from ._inline_query_result_cached_sticker import InlineQueryResultCachedSticker
from ._inline_query_result_cached_video import InlineQueryResultCachedVideo
from ._inline_query_result_cached_voice import InlineQueryResultCachedVoice
from ._inline_query_result_contact import InlineQueryResultContact
from ._inline_query_result_document import InlineQueryResultDocument
from ._inline_query_result_game import InlineQueryResultGame
from ._inline_query_result_gif import InlineQueryResultGif
from ._inline_query_result_location import InlineQueryResultLocation
from ._inline_query_result_mpeg4_gif import InlineQueryResultMpeg4Gif
from ._inline_query_result_photo import InlineQueryResultPhoto
from ._inline_query_result_venue import InlineQueryResultVenue
from ._inline_query_result_video import InlineQueryResultVideo
from ._inline_query_result_voice import InlineQueryResultVoice
from ._inline_query_results_button import InlineQueryResultsButton
from ._input_contact_message_content import InputContactMessageContent
from ._input_invoice_message_content import InputInvoiceMessageContent
from ._input_location_message_content import InputLocationMessageContent
from ._input_media_animation import InputMediaAnimation
from ._input_media_audio import InputMediaAudio
from ._input_media_document import InputMediaDocument
from ._input_media_photo import InputMediaPhoto
from ._input_media_video import InputMediaVideo
from ._input_message_content import InputMessageContent
from ._input_paid_media_photo import InputPaidMediaPhoto
from ._input_paid_media_video import InputPaidMediaVideo
from ._input_poll_option import InputPollOption
from ._input_sticker import InputSticker
from ._input_text_message_content import InputTextMessageContent
from ._input_venue_message_content import InputVenueMessageContent
from ._invoice import Invoice
from ._keyboard_button import KeyboardButton
from ._keyboard_button_poll_type import KeyboardButtonPollType
from ._keyboard_button_request_chat import KeyboardButtonRequestChat
from ._keyboard_button_request_users import KeyboardButtonRequestUsers
from ._labeled_price import LabeledPrice
from ._link_preview_options import LinkPreviewOptions
from ._listener import Listener
from ._location import Location
from ._login_url import LoginUrl
from ._mask_position import MaskPosition
from ._menu_button import MenuButton
from ._menu_button_commands import MenuButtonCommands
from ._menu_button_default import MenuButtonDefault
from ._menu_button_web_app import MenuButtonWebApp
from ._message import Message
from ._message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
from ._message_entity import MessageEntity
from ._message_id import MessageId
from ._message_origin_channel import MessageOriginChannel
from ._message_origin_chat import MessageOriginChat
from ._message_origin_hidden_user import MessageOriginHiddenUser
from ._message_origin_user import MessageOriginUser
from ._message_reaction_count_updated import MessageReactionCountUpdated
from ._message_reaction_updated import MessageReactionUpdated
from ._order_info import OrderInfo
from ._paid_media_info import PaidMediaInfo
from ._paid_media_photo import PaidMediaPhoto
from ._paid_media_preview import PaidMediaPreview
from ._paid_media_purchased import PaidMediaPurchased
from ._paid_media_video import PaidMediaVideo
from ._passport_data import PassportData
from ._passport_element_error import PassportElementError
from ._passport_element_error_data_field import PassportElementErrorDataField
from ._passport_element_error_file import PassportElementErrorFile
from ._passport_element_error_files import PassportElementErrorFiles
from ._passport_element_error_front_side import PassportElementErrorFrontSide
from ._passport_element_error_reverse_side import PassportElementErrorReverseSide
from ._passport_element_error_selfie import PassportElementErrorSelfie
from ._passport_element_error_translation_file import (
    PassportElementErrorTranslationFile,
)
from ._passport_element_error_translation_files import (
    PassportElementErrorTranslationFiles,
)
from ._passport_element_error_unspecified import PassportElementErrorUnspecified
from ._passport_file import PassportFile
from ._photo_size import PhotoSize
from ._poll import Poll
from ._poll_answer import PollAnswer
from ._poll_option import PollOption
from ._pre_checkout_query import PreCheckoutQuery
from ._proximity_alert_triggered import ProximityAlertTriggered
from ._reaction_count import ReactionCount
from ._reaction_type_custom_emoji import ReactionTypeCustomEmoji
from ._reaction_type_emoji import ReactionTypeEmoji
from ._reaction_type_paid import ReactionTypePaid
from ._refunded_payment import RefundedPayment
from ._reply_keyboard_markup import ReplyKeyboardMarkup
from ._reply_keyboard_remove import ReplyKeyboardRemove
from ._reply_parameters import ReplyParameters
from ._response_parameters import ResponseParameters
from ._revenue_withdrawal_state_failed import RevenueWithdrawalStateFailed
from ._revenue_withdrawal_state_pending import RevenueWithdrawalStatePending
from ._revenue_withdrawal_state_succeeded import RevenueWithdrawalStateSucceeded
from ._sent_web_app_message import SentWebAppMessage
from ._shared_user import SharedUser
from ._shipping_address import ShippingAddress
from ._shipping_option import ShippingOption
from ._shipping_query import ShippingQuery
from ._star_transaction import StarTransaction
from ._star_transactions import StarTransactions
from ._sticker import Sticker
from ._sticker_set import StickerSet
from ._story import Story
from ._successful_payment import SuccessfulPayment
from ._switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat
from ._text_quote import TextQuote
from ._transaction_partner_fragment import TransactionPartnerFragment
from ._transaction_partner_other import TransactionPartnerOther
from ._transaction_partner_telegram_ads import TransactionPartnerTelegramAds
from ._transaction_partner_user import TransactionPartnerUser
from ._update import Update
from ._user import User
from ._user_chat_boosts import UserChatBoosts
from ._user_profile_photos import UserProfilePhotos
from ._users_shared import UsersShared
from ._venue import Venue
from ._video import Video
from ._video_chat_ended import VideoChatEnded
from ._video_chat_participants_invited import VideoChatParticipantsInvited
from ._video_chat_scheduled import VideoChatScheduled
from ._video_chat_started import VideoChatStarted
from ._video_note import VideoNote
from ._voice import Voice
from ._web_app_data import WebAppData
from ._web_app_info import WebAppInfo
from ._webhook_info import WebhookInfo
from ._write_access_allowed import WriteAccessAllowed

InlineQueryResult = _Union[
    "InlineQueryResultCachedAudio",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultArticle",
    "InlineQueryResultAudio",
    "InlineQueryResultContact",
    "InlineQueryResultGame",
    "InlineQueryResultDocument",
    "InlineQueryResultGif",
    "InlineQueryResultLocation",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultPhoto",
    "InlineQueryResultVenue",
    "InlineQueryResultVideo",
    "InlineQueryResultVoice",
]

InputFile = _Union["bytes", "_Path", "str", "_BytesIo"]

InputMedia = _Union[
    "InputMediaAudio", "InputMediaDocument", "InputMediaPhoto", "InputMediaVideo"
]

InputPaidMedia = _Union["InputPaidMediaPhoto", "InputPaidMediaVideo"]

MaybeInaccessibleMessage = _Union["InaccessibleMessage", "Message"]

MessageOrigin = _Union[
    "MessageOriginUser",
    "MessageOriginHiddenUser",
    "MessageOriginChat",
    "MessageOriginChannel",
]

PaidMedia = _Union["PaidMediaPreview", "PaidMediaPhoto", "PaidMediaVideo"]

ReactionType = _Union[
    "ReactionTypeCustomEmoji", "ReactionTypeEmoji", "ReactionTypePaid"
]

RevenueWithdrawalState = _Union[
    "RevenueWithdrawalStatePending",
    "RevenueWithdrawalStateSucceeded",
    "RevenueWithdrawalStateFailed",
]

TransactionPartner = _Union[
    "TransactionPartnerFragment",
    "TransactionPartnerUser",
    "TransactionPartnerOther",
    "TransactionPartnerTelegramAds",
]

ParseMode = _Literal["Markdown", "MarkdownV2", "HTML"]

__all__ = [
    "Animation",
    "Audio",
    "BackgroundFill",
    "BackgroundFillFreeformGradient",
    "BackgroundFillGradient",
    "BackgroundFillSolid",
    "BackgroundType",
    "BackgroundTypeChatTheme",
    "BackgroundTypeFill",
    "BackgroundTypePattern",
    "BackgroundTypeWallpaper",
    "Birthdate",
    "BotCommand",
    "BotCommandScope",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "BotCommandScopeDefault",
    "BotDescription",
    "BotName",
    "BotShortDescription",
    "BusinessConnection",
    "BusinessIntro",
    "BusinessLocation",
    "BusinessMessagesDeleted",
    "BusinessOpeningHours",
    "BusinessOpeningHoursInterval",
    "CallbackGame",
    "CallbackQuery",
    "Chat",
    "ChatAdministratorRights",
    "ChatBackground",
    "ChatBoost",
    "ChatBoostAdded",
    "ChatBoostRemoved",
    "ChatBoostSource",
    "ChatBoostSourceGiftCode",
    "ChatBoostSourceGiveaway",
    "ChatBoostSourcePremium",
    "ChatBoostUpdated",
    "ChatFullInfo",
    "ChatInviteLink",
    "ChatJoinRequest",
    "ChatLocation",
    "ChatMember",
    "ChatMemberAdministrator",
    "ChatMemberBanned",
    "ChatMemberLeft",
    "ChatMemberMember",
    "ChatMemberOwner",
    "ChatMemberRestricted",
    "ChatMemberUpdated",
    "ChatPermissions",
    "ChatPhoto",
    "ChatShared",
    "ChosenInlineResult",
    "Contact",
    "Dice",
    "Document",
    "EncryptedCredentials",
    "EncryptedPassportElement",
    "ExternalReplyInfo",
    "File",
    "ForceReply",
    "ForumTopic",
    "ForumTopicClosed",
    "ForumTopicCreated",
    "ForumTopicEdited",
    "ForumTopicReopened",
    "Game",
    "GameHighScore",
    "GeneralForumTopicHidden",
    "GeneralForumTopicUnhidden",
    "Giveaway",
    "GiveawayCompleted",
    "GiveawayCreated",
    "GiveawayWinners",
    "InaccessibleMessage",
    "InlineKeyboardButton",
    "InlineKeyboardMarkup",
    "InlineQuery",
    "InlineQueryResult",
    "InlineQueryResultArticle",
    "InlineQueryResultAudio",
    "InlineQueryResultCachedAudio",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultContact",
    "InlineQueryResultDocument",
    "InlineQueryResultGame",
    "InlineQueryResultGif",
    "InlineQueryResultLocation",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultPhoto",
    "InlineQueryResultVenue",
    "InlineQueryResultVideo",
    "InlineQueryResultVoice",
    "InlineQueryResultsButton",
    "InputContactMessageContent",
    "InputFile",
    "InputInvoiceMessageContent",
    "InputLocationMessageContent",
    "InputMedia",
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputMediaPhoto",
    "InputMediaVideo",
    "InputMessageContent",
    "InputPaidMedia",
    "InputPaidMediaPhoto",
    "InputPaidMediaVideo",
    "InputPollOption",
    "InputSticker",
    "InputTextMessageContent",
    "InputVenueMessageContent",
    "Invoice",
    "KeyboardButton",
    "KeyboardButtonPollType",
    "KeyboardButtonRequestChat",
    "KeyboardButtonRequestUsers",
    "LabeledPrice",
    "LinkPreviewOptions",
    "Listener",
    "Location",
    "LoginUrl",
    "MaskPosition",
    "MaybeInaccessibleMessage",
    "MenuButton",
    "MenuButtonCommands",
    "MenuButtonDefault",
    "MenuButtonWebApp",
    "Message",
    "MessageAutoDeleteTimerChanged",
    "MessageEntity",
    "MessageId",
    "MessageOrigin",
    "MessageOriginChannel",
    "MessageOriginChat",
    "MessageOriginHiddenUser",
    "MessageOriginUser",
    "MessageReactionCountUpdated",
    "MessageReactionUpdated",
    "OrderInfo",
    "PaidMedia",
    "PaidMediaInfo",
    "PaidMediaPhoto",
    "PaidMediaPreview",
    "PaidMediaPurchased",
    "PaidMediaVideo",
    "PassportData",
    "PassportElementError",
    "PassportElementErrorDataField",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
    "PassportFile",
    "PhotoSize",
    "Poll",
    "PollAnswer",
    "PollOption",
    "PreCheckoutQuery",
    "ProximityAlertTriggered",
    "ReactionCount",
    "ReactionType",
    "ReactionTypeCustomEmoji",
    "ReactionTypeEmoji",
    "RefundedPayment",
    "ReplyKeyboardMarkup",
    "ReplyKeyboardRemove",
    "ReplyParameters",
    "ResponseParameters",
    "RevenueWithdrawalState",
    "RevenueWithdrawalStateFailed",
    "RevenueWithdrawalStatePending",
    "RevenueWithdrawalStateSucceeded",
    "SentWebAppMessage",
    "SharedUser",
    "ShippingAddress",
    "ShippingOption",
    "ShippingQuery",
    "StarTransaction",
    "StarTransactions",
    "Sticker",
    "StickerSet",
    "Story",
    "SuccessfulPayment",
    "SwitchInlineQueryChosenChat",
    "TextQuote",
    "TransactionPartner",
    "TransactionPartnerFragment",
    "TransactionPartnerOther",
    "TransactionPartnerTelegramAds",
    "TransactionPartnerUser",
    "Update",
    "User",
    "UserChatBoosts",
    "UserProfilePhotos",
    "UsersShared",
    "Venue",
    "Video",
    "VideoChatEnded",
    "VideoChatParticipantsInvited",
    "VideoChatScheduled",
    "VideoChatStarted",
    "VideoNote",
    "Voice",
    "WebAppData",
    "WebAppInfo",
    "WebhookInfo",
    "WriteAccessAllowed",
]
