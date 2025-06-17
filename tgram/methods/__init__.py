from .stickers.add_sticker_to_set import AddStickerToSet
from .other.answer_callback_query import AnswerCallbackQuery
from .other.answer_inline_query import AnswerInlineQuery
from .other.answer_pre_checkout_query import AnswerPreCheckoutQuery
from .other.answer_shipping_query import AnswerShippingQuery
from .other.answer_web_app_query import AnswerWebAppQuery
from .chats.approve_chat_join_request import ApproveChatJoinRequest
from .messages.ask import Ask
from .chats.ban_chat_member import BanChatMember
from .chats.ban_chat_sender_chat import BanChatSenderChat
from .bot.close import Close
from .forums.close_forum_topic import CloseForumTopic
from .forums.close_general_forum_topic import CloseGeneralForumTopic
from .messages.copy_message import CopyMessage
from .messages.copy_messages import CopyMessages
from .chats.create_chat_invite_link import CreateChatInviteLink
from .chats.create_chat_subscription_invite_link import CreateChatSubscriptionInviteLink
from .forums.create_forum_topic import CreateForumTopic
from .other.create_invoice_link import CreateInvoiceLink
from .stickers.create_new_sticker_set import CreateNewStickerSet
from .chats.decline_chat_join_request import DeclineChatJoinRequest
from .chats.delete_chat_photo import DeleteChatPhoto
from .chats.delete_chat_sticker_set import DeleteChatStickerSet
from .forums.delete_forum_topic import DeleteForumTopic
from .messages.delete_message import DeleteMessage
from .messages.delete_messages import DeleteMessages
from .bot.delete_my_commands import DeleteMyCommands
from .stickers.delete_sticker_from_set import DeleteStickerFromSet
from .stickers.delete_sticker_set import DeleteStickerSet
from .bot.delete_webhook import DeleteWebhook
from .chats.demote_chat_member import DemoteChatMember
from .files.download_file import DownloadFile
from .chats.edit_chat_invite_link import EditChatInviteLink
from .chats.edit_chat_subscription_invite_link import EditChatSubscriptionInviteLink
from .forums.edit_forum_topic import EditForumTopic
from .forums.edit_general_forum_topic import EditGeneralForumTopic
from .messages.edit_message_caption import EditMessageCaption
from .messages.edit_message_live_location import EditMessageLiveLocation
from .messages.edit_message_media import EditMessageMedia
from .messages.edit_message_reply_markup import EditMessageReplyMarkup
from .messages.edit_message_text import EditMessageText
from .payments_and_business.edit_user_star_subscription import EditUserStarSubscription
from .chats.export_chat_invite_link import ExportChatInviteLink
from .messages.forward_message import ForwardMessage
from .messages.forward_messages import ForwardMessages
from .bot.get_available_gifts import GetAvailableGifts
from .payments_and_business.get_business_connection import GetBusinessConnection
from .chats.get_chat import GetChat
from .chats.get_chat_administrators import GetChatAdministrators
from .chats.get_chat_member import GetChatMember
from .chats.get_chat_member_count import GetChatMemberCount
from .chats.get_chat_menu_button import GetChatMenuButton
from .chats.get_custom_emoji_stickers import GetCustomEmojiStickers
from .files.get_file import GetFile
from .files.get_file_url import GetFileUrl
from .forums.get_forum_topic_icon_stickers import GetForumTopicIconStickers
from .other.get_game_high_scores import GetGameHighScores
from .bot.get_me import GetMe
from .bot.get_my_commands import GetMyCommands
from .bot.get_my_default_administrator_rights import GetMyDefaultAdministratorRights
from .bot.get_my_description import GetMyDescription
from .bot.get_my_name import GetMyName
from .bot.get_my_short_description import GetMyShortDescription
from .payments_and_business.get_star_transactions import GetStarTransactions
from .stickers.get_sticker_set import GetStickerSet
from .bot.get_updates import GetUpdates
from .chats.get_user_chat_boosts import GetUserChatBoosts
from .chats.get_user_profile_photos import GetUserProfilePhotos
from .bot.get_webhook_info import GetWebhookInfo
from .forums.hide_general_forum_topic import HideGeneralForumTopic
from .chats.leave_chat import LeaveChat
from .bot.log_out import LogOut
from .chats.pin_chat_message import PinChatMessage
from .chats.promote_chat_member import PromoteChatMember
from .payments_and_business.refund_star_payment import RefundStarPayment
from .forums.reopen_forum_topic import ReopenForumTopic
from .forums.reopen_general_forum_topic import ReopenGeneralForumTopic
from .stickers.replace_sticker_in_set import ReplaceStickerInSet
from .chats.restrict_chat_member import RestrictChatMember
from .chats.revoke_chat_invite_link import RevokeChatInviteLink
from .messages.send_animation import SendAnimation
from .messages.send_audio import SendAudio
from .messages.send_chat_action import SendChatAction
from .messages.send_contact import SendContact
from .messages.send_dice import SendDice
from .messages.send_document import SendDocument
from .messages.send_game import SendGame
from .messages.send_gift import SendGift
from .messages.send_invoice import SendInvoice
from .messages.send_location import SendLocation
from .messages.send_media_from_file_id import SendMediaFromFileId
from .messages.send_media_group import SendMediaGroup
from .messages.send_message import SendMessage
from .messages.send_paid_media import SendPaidMedia
from .messages.send_photo import SendPhoto
from .messages.send_poll import SendPoll
from .messages.send_sticker import SendSticker
from .messages.send_venue import SendVenue
from .messages.send_video import SendVideo
from .messages.send_video_note import SendVideoNote
from .messages.send_voice import SendVoice
from .chats.set_chat_administrator_custom_title import SetChatAdministratorCustomTitle
from .chats.set_chat_description import SetChatDescription
from .chats.set_chat_menu_button import SetChatMenuButton
from .chats.set_chat_permissions import SetChatPermissions
from .chats.set_chat_photo import SetChatPhoto
from .chats.set_chat_sticker_set import SetChatStickerSet
from .chats.set_chat_title import SetChatTitle
from .stickers.set_custom_emoji_sticker_set_thumbnail import (
    SetCustomEmojiStickerSetThumbnail,
)
from .other.set_game_score import SetGameScore
from .messages.set_message_reaction import SetMessageReaction
from .bot.set_my_commands import SetMyCommands
from .bot.set_my_default_administrator_rights import SetMyDefaultAdministratorRights
from .bot.set_my_description import SetMyDescription
from .bot.set_my_name import SetMyName
from .bot.set_my_short_description import SetMyShortDescription
from .other.set_passport_data_errors import SetPassportDataErrors
from .stickers.set_sticker_emoji_list import SetStickerEmojiList
from .stickers.set_sticker_keywords import SetStickerKeywords
from .stickers.set_sticker_mask_position import SetStickerMaskPosition
from .stickers.set_sticker_position_in_set import SetStickerPositionInSet
from .stickers.set_sticker_set_thumbnail import SetStickerSetThumbnail
from .stickers.set_sticker_set_title import SetStickerSetTitle
from .other.set_user_emoji_status import SetUserEmojiStatus
from .bot.set_webhook import SetWebhook
from .messages.stop_message_live_location import StopMessageLiveLocation
from .messages.stop_poll import StopPoll
from .other.save_prepared_inline_message import SavePreparedInlineMessage
from .chats.unban_chat_member import UnbanChatMember
from .chats.unban_chat_sender_chat import UnbanChatSenderChat
from .forums.unhide_general_forum_topic import UnhideGeneralForumTopic
from .chats.unpin_all_chat_messages import UnpinAllChatMessages
from .forums.unpin_all_forum_topic_messages import UnpinAllForumTopicMessages
from .forums.unpin_all_general_forum_topic_messages import (
    UnpinAllGeneralForumTopicMessages,
)
from .chats.unpin_chat_message import UnpinChatMessage
from .chats.unrestrict_chat_member import UnRestrictChatMember
from .stickers.upload_sticker_file import UploadStickerFile

from .bot.runner import Runner

from .chats.verify_chat import VerifyChat
from .chats.verify_user import VerifyUser
from .chats.remove_chat_verification import RemoveChatVerification
from .chats.remove_user_verification import RemoveUserVerification

from .payments_and_business.read_business_message import ReadBusinessMessage
from .payments_and_business.delete_business_messages import DeleteBusinessMessages
from .payments_and_business.set_business_account_name import SetBusinessAccountName
from .payments_and_business.set_business_account_username import (
    SetBusinessAccountUsername,
)
from .payments_and_business.set_business_account_bio import SetBusinessAccountBio
from .payments_and_business.set_business_account_profile_photo import (
    SetBusinessAccountProfilePhoto,
)
from .payments_and_business.remove_business_account_profile_photo import (
    RemoveBusinessAccountProfilePhoto,
)
from .payments_and_business.set_business_account_gift_settings import (
    SetBusinessAccountGiftSettings,
)
from .payments_and_business.get_business_account_star_balance import (
    GetBusinessAccountStarBalance,
)
from .payments_and_business.transfer_business_account_stars import (
    TransferBusinessAccountStars,
)
from .payments_and_business.get_business_account_gifts import GetBusinessAccountGifts


class TelegramBotMethods(
    AddStickerToSet,
    AnswerCallbackQuery,
    AnswerInlineQuery,
    AnswerPreCheckoutQuery,
    AnswerShippingQuery,
    AnswerWebAppQuery,
    ApproveChatJoinRequest,
    Ask,
    BanChatMember,
    BanChatSenderChat,
    Close,
    CloseForumTopic,
    CloseGeneralForumTopic,
    CopyMessage,
    CopyMessages,
    CreateChatInviteLink,
    CreateChatSubscriptionInviteLink,
    CreateForumTopic,
    CreateInvoiceLink,
    CreateNewStickerSet,
    DeclineChatJoinRequest,
    DeleteChatPhoto,
    DeleteChatStickerSet,
    DeleteForumTopic,
    DeleteMessage,
    DeleteMessages,
    DeleteBusinessMessages,
    DeleteMyCommands,
    DeleteStickerFromSet,
    DeleteStickerSet,
    DeleteWebhook,
    DemoteChatMember,
    DownloadFile,
    EditChatInviteLink,
    EditChatSubscriptionInviteLink,
    EditForumTopic,
    EditGeneralForumTopic,
    EditMessageCaption,
    EditMessageLiveLocation,
    EditMessageMedia,
    EditMessageReplyMarkup,
    EditMessageText,
    EditUserStarSubscription,
    ExportChatInviteLink,
    ForwardMessage,
    ForwardMessages,
    GetAvailableGifts,
    GetBusinessConnection,
    GetChat,
    GetChatAdministrators,
    GetChatMember,
    GetChatMemberCount,
    GetChatMenuButton,
    GetCustomEmojiStickers,
    GetFile,
    GetFileUrl,
    GetForumTopicIconStickers,
    GetGameHighScores,
    GetMe,
    GetMyCommands,
    GetMyDefaultAdministratorRights,
    GetMyDescription,
    GetMyName,
    GetMyShortDescription,
    GetStarTransactions,
    GetStickerSet,
    GetUpdates,
    GetUserChatBoosts,
    GetUserProfilePhotos,
    GetWebhookInfo,
    GetBusinessAccountGifts,
    GetBusinessAccountStarBalance,
    HideGeneralForumTopic,
    LeaveChat,
    LogOut,
    PinChatMessage,
    PromoteChatMember,
    RefundStarPayment,
    ReopenForumTopic,
    ReopenGeneralForumTopic,
    ReplaceStickerInSet,
    RestrictChatMember,
    RevokeChatInviteLink,
    ReadBusinessMessage,
    SendAnimation,
    SendAudio,
    SendChatAction,
    SendContact,
    SendDice,
    SendDocument,
    SendGame,
    SendGift,
    SendInvoice,
    SendLocation,
    SendMediaFromFileId,
    SendMediaGroup,
    SendMessage,
    SendPaidMedia,
    SendPhoto,
    SendPoll,
    SendSticker,
    SendVenue,
    SendVideo,
    SendVideoNote,
    SendVoice,
    SetChatAdministratorCustomTitle,
    SetChatDescription,
    SetChatMenuButton,
    SetChatPermissions,
    SetChatPhoto,
    SetChatStickerSet,
    SetChatTitle,
    SetCustomEmojiStickerSetThumbnail,
    SetGameScore,
    SetMessageReaction,
    SetMyCommands,
    SetMyDefaultAdministratorRights,
    SetMyDescription,
    SetMyName,
    SetMyShortDescription,
    SetPassportDataErrors,
    SetStickerEmojiList,
    SetStickerKeywords,
    SetStickerMaskPosition,
    SetStickerPositionInSet,
    SetStickerSetThumbnail,
    SetStickerSetTitle,
    SetUserEmojiStatus,
    SetWebhook,
    SetBusinessAccountName,
    SetBusinessAccountUsername,
    SetBusinessAccountBio,
    SetBusinessAccountProfilePhoto,
    SetBusinessAccountGiftSettings,
    StopMessageLiveLocation,
    StopPoll,
    SavePreparedInlineMessage,
    UnbanChatMember,
    UnbanChatSenderChat,
    UnhideGeneralForumTopic,
    UnpinAllChatMessages,
    UnpinAllForumTopicMessages,
    UnpinAllGeneralForumTopicMessages,
    UnpinChatMessage,
    UnRestrictChatMember,
    UploadStickerFile,
    Runner,
    VerifyChat,
    VerifyUser,
    RemoveUserVerification,
    RemoveChatVerification,
    RemoveBusinessAccountProfilePhoto,
    TransferBusinessAccountStars,
):
    pass
