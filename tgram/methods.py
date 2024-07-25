# This is auto generated file, if you found any issue, please report me here: https://github.com/2ei/tgram/issues/new
import io
import asyncio
import logging

from typing import Callable, List, Union
import tgram
from tgram.types import (
    Update,
    WebhookInfo,
    User,
    Message,
    MessageEntity,
    LinkPreviewOptions,
    ReplyParameters,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    MessageId,
    InputPollOption,
    ReactionType,
    UserProfilePhotos,
    File,
    ChatPermissions,
    ChatInviteLink,
    ChatFullInfo,
    ChatMember,
    ChatMemberOwner,
    ChatMemberAdministrator,
    ChatMemberBanned,
    ChatMemberLeft,
    ChatMemberRestricted,
    ChatMemberMember,
    Sticker,
    ForumTopic,
    UserChatBoosts,
    BusinessConnection,
    BotCommand,
    BotCommandScope,
    BotName,
    BotDescription,
    BotShortDescription,
    MenuButton,
    ChatAdministratorRights,
    InputMedia,
    Poll,
    StickerSet,
    InputSticker,
    MaskPosition,
    InlineQueryResult,
    InlineQueryResultsButton,
    SentWebAppMessage,
    LabeledPrice,
    ShippingOption,
    StarTransactions,
    PassportElementError,
    GameHighScore,
    InputPaidMedia,
    Listener,
)

from .errors import APIException
from .utils import get_file_path

from pathlib import Path

logger = logging.getLogger(__name__)


class TelegramBotMethods:
    async def get_updates(
        self: "tgram.TgBot",
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: List[str] = None,
    ) -> List[Update]:
        """
        Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

        Telegram documentation: https://core.telegram.org/bots/api#getupdates


        :param offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates.
            By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset
            higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue.
            All previous updates will forgotten.
        :type offset: :obj:`int`, optional

        :param limit: Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :type limit: :obj:`int`, optional

        :param timeout: Request connection timeout
        :type timeout: :obj:`int`, optional

        :param allowed_updates: Array of string. List the types of updates you want your bot to receive.
        :type allowed_updates: :obj:`list`, optional

        :param request_timeout: Timeout in seconds for request.
        :type request_timeout: :obj:`int`, optional

        :return: An Array of Update objects is returned.
        :rtype: :obj:`list` of :class:`tgram.types.Update`
        """

        result = await self._send_request(
            "getUpdates",
            offset=offset,
            limit=limit,
            timeout=timeout,
            allowed_updates=allowed_updates,
        )
        return [Update._parse(me=self, d=i) for i in result["result"]]

    async def set_webhook(
        self: "tgram.TgBot",
        url: str,
        certificate: Union[Path, bytes, str] = None,
        ip_address: str = None,
        max_connections: int = None,
        allowed_updates: List[str] = None,
        drop_pending_updates: bool = None,
        secret_token: str = None,
    ) -> bool:
        """
        Use this method to specify a URL and receive incoming updates via an outgoing webhook.
        Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL,
        containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after
        a reasonable amount of attempts. Returns True on success.

        If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token.
        If specified, the request will contain a header “X-Telegram-Bot-Api-Secret-Token” with the secret token as content.

        Telegram Documentation: https://core.telegram.org/bots/api#setwebhook

        :param url: HTTPS URL to send updates to. Use an empty string to remove webhook integration, defaults to None
        :type url: :obj:`str`, optional

        :param certificate: Upload your public key certificate so that the root certificate in use can be checked, defaults to None
        :type certificate: :class:`str`, optional

        :param max_connections: The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100.
            Defaults to 40. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput,
            defaults to None
        :type max_connections: :obj:`int`, optional

        :param allowed_updates: A JSON-serialized list of the update types you want your bot to receive. For example,
            specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See Update
            for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default).
            If not specified, the previous setting will be used.

            Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received
            for a short period of time. Defaults to None

        :type allowed_updates: :obj:`list`, optional

        :param ip_address: The fixed IP address which will be used to send webhook requests instead of the IP address
            resolved through DNS, defaults to None
        :type ip_address: :obj:`str`, optional

        :param drop_pending_updates: Pass True to drop all pending updates, defaults to None
        :type drop_pending_updates: :obj:`bool`, optional

        :param timeout: Timeout of a request, defaults to None
        :type timeout: :obj:`int`, optional

        :param secret_token: A secret token to be sent in a header “X-Telegram-Bot-Api-Secret-Token” in every webhook request, 1-256 characters.
            Only characters A-Z, a-z, 0-9, _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you. Defaults to None
        :type secret_token: :obj:`str`, optional

        :return: True on success.
        :rtype: :obj:`bool` if the request was successful.
        """

        result = await self._send_request(
            "setWebhook",
            url=url,
            certificate=certificate,
            ip_address=ip_address,
            max_connections=max_connections,
            allowed_updates=allowed_updates,
            drop_pending_updates=drop_pending_updates,
            secret_token=secret_token,
        )
        return result["result"]

    async def delete_webhook(
        self: "tgram.TgBot", drop_pending_updates: bool = None
    ) -> bool:
        """
        Use this method to remove webhook integration if you decide to switch back to getUpdates.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletewebhook

        :param drop_pending_updates: Pass True to drop all pending updates, defaults to None
        :type drop_pending_updates: :obj: `bool`, optional

        :param timeout: Request connection timeout, defaults to None
        :type timeout: :obj:`int`, optional

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteWebhook",
            drop_pending_updates=drop_pending_updates,
        )
        return result["result"]

    async def get_webhook_info(self: "tgram.TgBot") -> WebhookInfo:
        """
        Use this method to get current webhook status. Requires no parameters.
        On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.

        Telegram documentation: https://core.telegram.org/bots/api#getwebhookinfo

        :param timeout: Request connection timeout
        :type timeout: :obj:`int`, optional

        :return: On success, returns a WebhookInfo object.
        :rtype: :class:`tgram.types.WebhookInfo`
        """

        result = await self._send_request(
            "getWebhookInfo",
        )
        return WebhookInfo._parse(me=self, d=result["result"])

    async def get_me(self: "tgram.TgBot") -> User:
        """
        Returns basic information about the bot in form of a User object.

        Telegram documentation: https://core.telegram.org/bots/api#getme
        """

        result = await self._send_request(
            "getMe",
        )
        return User._parse(me=self, d=result["result"])

    async def log_out(self: "tgram.TgBot") -> bool:
        """
        Use this method to log out from the cloud Bot API server before launching the bot locally.
        You MUST log out the bot before running it locally, otherwise there is no guarantee
        that the bot will receive updates.
        After a successful call, you can immediately log in on a local server,
        but will not be able to log in back to the cloud Bot API server for 10 minutes.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#logout

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "logOut",
        )
        return result["result"]

    async def close(self: "tgram.TgBot") -> bool:
        """
        Use this method to close the bot instance before moving it from one local server to another.
        You need to delete the webhook before calling this method to ensure that the bot isn't launched again
        after server restart.
        The method will return error 429 in the first 10 minutes after the bot is launched.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#close

        :return: :obj:`bool`
        """

        result = await self._send_request(
            "close",
        )
        return result["result"]

    async def send_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        text: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send text messages.

        Warning: Do not send more than about 4096 characters each message, otherwise you'll risk an HTTP 414 error.
        If you must send more than 4096 characters,
        use the `split_string` or `smart_split` function in util.py.

        Telegram documentation: https://core.telegram.org/bots/api#sendmessage

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param text: Text of the message to be sent
        :type text: :obj:`str`

        :param parse_mode: Mode for parsing entities in the message text.
        :type parse_mode: :obj:`str`

        :param entities: List of special entities that appear in message text, which can be specified instead of parse_mode
        :type entities: Array of :class:`tgram.types.MessageEntity`

        :param disable_web_page_preview: Deprecated - Use link_preview_options instead.
        :type disable_web_page_preview: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: If True, the message content will be hidden for all users except for the target user
        :type protect_content: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param link_preview_options: Options for previewing links.
        :type link_preview_options: :class:`tgram.types.LinkPreviewOptions`

        :param business_connection_id: Unique identifier for the target business connection
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendMessage",
            chat_id=chat_id,
            text=text,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            parse_mode=parse_mode or self.parse_mode,
            entities=entities,
            link_preview_options=link_preview_options or self.link_preview_options,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def forward_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> Message:
        """
        Use this method to forward messages of any kind.

        Telegram documentation: https://core.telegram.org/bots/api#forwardmessage

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound
        :type disable_notification: :obj:`bool`

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :type from_chat_id: :obj:`int` or :obj:`str`

        :param message_id: Message identifier in the chat specified in from_chat_id
        :type message_id: :obj:`int`

        :param protect_content: Protects the contents of the forwarded message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :type message_thread_id: :obj:`int`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "forwardMessage",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
        )
        return Message._parse(me=self, d=result["result"])

    async def forward_messages(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> List[MessageId]:
        """
        Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded,
        they are skipped. Service messages and messages with protected content can't be forwarded.
        Album grouping is kept for forwarded messages. On success, an array of MessageId of the sent messages is returned.

        Telegram documentation: https://core.telegram.org/bots/api#forwardmessages

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :type from_chat_id: :obj:`int` or :obj:`str`

        :param message_ids: Message identifiers in the chat specified in from_chat_id
        :type message_ids: :obj:`list`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound
        :type disable_notification: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the messages will be sent
        :type message_thread_id: :obj:`int`

        :param protect_content: Protects the contents of the forwarded message from forwarding and saving
        :type protect_content: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.MessageID`
        """

        result = await self._send_request(
            "forwardMessages",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_ids=message_ids,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
        )
        return [MessageId._parse(me=self, d=i) for i in result["result"]]

    async def copy_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> MessageId:
        """
        Use this method to copy messages of any kind.

        Telegram documentation: https://core.telegram.org/bots/api#copymessage

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :type from_chat_id: :obj:`int` or :obj:`str`
        :param message_id: Message identifier in the chat specified in from_chat_id
        :type message_id: :obj:`int`

        :param caption: New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept
        :type caption: :obj:`str`

        :param parse_mode: Mode for parsing entities in the new caption.
        :type parse_mode: :obj:`str`

        :param caption_entities: A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode
        :type caption_entities: Array of :class:`tgram.types.MessageEntity`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param show_caption_above_media: Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages.
        :type show_caption_above_media: :obj:`bool`

        :return: On success, the MessageId of the sent message is returned.
        :rtype: :class:`tgram.types.MessageID`
        """

        result = await self._send_request(
            "copyMessage",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return MessageId._parse(me=self, d=result["result"])

    async def copy_messages(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        remove_caption: bool = None,
    ) -> List[MessageId]:
        """
        Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped.
        Service messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied
        only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessages, but
        the copied messages don't have a link to the original message. Album grouping is kept for copied messages.
        On success, an array of MessageId of the sent messages is returned.

        Telegram documentation: https://core.telegram.org/bots/api#copymessages

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :type from_chat_id: :obj:`int` or :obj:`str`

        :param message_ids: Message identifiers in the chat specified in from_chat_id
        :type message_ids: :obj:`list` of :obj:`int`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound
        :type disable_notification: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the messages will be sent
        :type message_thread_id: :obj:`int`

        :param protect_content: Protects the contents of the forwarded message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param remove_caption: Pass True to copy the messages without their captions
        :type remove_caption: :obj:`bool`

        :return: On success, an array of MessageId of the sent messages is returned.
        :rtype: :obj:`list` of :class:`tgram.types.MessageID`
        """

        result = await self._send_request(
            "copyMessages",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_ids=message_ids,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            remove_caption=remove_caption,
        )
        return [MessageId._parse(me=self, d=i) for i in result["result"]]

    async def send_photo(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        photo: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send photos. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendphoto

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended),
            pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data.
            The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20.
        :type photo: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption: Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param parse_mode: Mode for parsing entities in the photo caption.
        :type parse_mode: :obj:`str`

        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions
            to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param has_spoiler: Pass True, if the photo should be sent as a spoiler
        :type has_spoiler: :obj:`bool`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Unique identifier for the target business connection
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :param show_caption_above_media: Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages.
        :type show_caption_above_media: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendPhoto",
            chat_id=chat_id,
            photo=get_file_path(photo),
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_audio(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        audio: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        performer: str = None,
        title: str = None,
        thumbnail: Union[Path, bytes, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player.
        Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size,
        this limit may be changed in the future.

        For sending voice messages, use the send_voice method instead.

        Telegram documentation: https://core.telegram.org/bots/api#sendaudio

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param audio: Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended),
            pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data.
            Audio must be in the .MP3 or .M4A format.
        :type audio: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption: Audio caption, 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param duration: Duration of the audio in seconds
        :type duration: :obj:`int`

        :param performer: Performer
        :type performer: :obj:`str`

        :param title: Track name
        :type title: :obj:`str`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup:
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.
        :type parse_mode: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
            The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,
            so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>
        :type thumbnail: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param thumb: Deprecated. Use thumbnail instead
        :type thumb: :obj:`str` or :class:`tgram.types.InputFile`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Unique identifier for the target business connection
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendAudio",
            chat_id=chat_id,
            audio=get_file_path(audio),
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            performer=performer,
            title=title,
            thumbnail=get_file_path(thumbnail),
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_document(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        document: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        thumbnail: Union[Path, bytes, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        disable_content_type_detection: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send general files.

        Telegram documentation: https://core.telegram.org/bots/api#senddocument

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param document: (document) File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a
            String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data
        :type document: :obj:`str` or :class:`tgram.types.InputFile`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param caption: Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param parse_mode: Mode for parsing entities in the document caption
        :type parse_mode: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param thumbnail: InputFile or String : Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>
        :type thumbnail: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param visible_file_name: allows to define file name that will be visible in the Telegram instead of original file name
        :type visible_file_name: :obj:`str`

        :param disable_content_type_detection: Disables automatic server-side content type detection for files uploaded using multipart/form-data
        :type disable_content_type_detection: :obj:`bool`

        :param data: function typo miss compatibility: do not use it
        :type data: :obj:`str`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param thumb: Deprecated. Use thumbnail instead
        :type thumb: :obj:`str` or :class:`tgram.types.InputFile`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Unique identifier for the target business connection
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendDocument",
            chat_id=chat_id,
            document=get_file_path(document),
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            thumbnail=get_file_path(thumbnail),
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            disable_content_type_detection=disable_content_type_detection,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_video(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        video: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[Path, bytes, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        supports_streaming: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document).

        Telegram documentation: https://core.telegram.org/bots/api#sendvideo

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param video: Video to send. You can either pass a file_id as String to resend a video that is already on the Telegram servers, or upload a new video file using multipart/form-data.
        :type video: :obj:`str` or :class:`tgram.types.InputFile`

        :param duration: Duration of sent video in seconds
        :type duration: :obj:`int`

        :param width: Video width
        :type width: :obj:`int`

        :param height: Video height
        :type height: :obj:`int`

        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.
        :type thumbnail: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption: Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param parse_mode: Mode for parsing entities in the video caption
        :type parse_mode: :obj:`str`

        :param caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param supports_streaming: Pass True, if the uploaded video is suitable for streaming
        :type supports_streaming: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param data: function typo miss compatibility: do not use it
        :type data: :obj:`str`

        :param message_thread_id: Identifier of a message thread, in which the video will be sent
        :type message_thread_id: :obj:`int`

        :param has_spoiler: Pass True, if the video should be sent as a spoiler
        :type has_spoiler: :obj:`bool`

        :param thumb: Deprecated. Use thumbnail instead
        :type thumb: :obj:`str` or :class:`tgram.types.InputFile`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :param show_caption_above_media: Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages.
        :type show_caption_above_media: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendVideo",
            chat_id=chat_id,
            video=get_file_path(video),
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=get_file_path(thumbnail),
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            supports_streaming=supports_streaming,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_animation(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        animation: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[Path, bytes, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound).
        On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Telegram documentation: https://core.telegram.org/bots/api#sendanimation

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param animation: Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended),
            pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data.
        :type animation: :obj:`str` or :class:`tgram.types.InputFile`

        :param duration: Duration of sent animation in seconds
        :type duration: :obj:`int`

        :param width: Animation width
        :type width: :obj:`int`

        :param height: Animation height
        :type height: :obj:`int`

        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
            The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,
            so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.
        :type thumbnail: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption: Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param parse_mode: Mode for parsing entities in the animation caption
        :type parse_mode: :obj:`str`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param caption_entities: List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the video will be sent
        :type message_thread_id: :obj:`int`

        :param has_spoiler: Pass True, if the animation should be sent as a spoiler
        :type has_spoiler: :obj:`bool`

        :param thumb: Deprecated. Use thumbnail instead
        :type thumb: :obj:`str` or :class:`tgram.types.InputFile`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :param show_caption_above_media: Pass True, if the caption must be shown above the message media. Supported only for animation, photo and video messages.
        :type show_caption_above_media: :obj:`bool`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendAnimation",
            chat_id=chat_id,
            animation=get_file_path(animation),
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=get_file_path(thumbnail),
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_voice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        voice: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Telegram documentation: https://core.telegram.org/bots/api#sendvoice

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param voice: Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended),
            pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        :type voice: :obj:`str` or :class:`tgram.types.InputFile`

        :param caption: Voice message caption, 0-1024 characters after entities parsing
        :type caption: :obj:`str`

        :param duration: Duration of the voice message in seconds
        :type duration: :obj:`int`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions
            to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.
        :type parse_mode: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
        :type caption_entities: :obj:`list` of :class:`tgram.types.MessageEntity`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Unique identifier for the target business connection
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        """

        result = await self._send_request(
            "sendVoice",
            chat_id=chat_id,
            voice=get_file_path(voice),
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_video_note(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        video_note: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        length: int = None,
        thumbnail: Union[Path, bytes, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long.
        Use this method to send video messages. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendvideonote

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param data: Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended)
            or upload a new video using multipart/form-data. Sending video notes by a URL is currently unsupported
        :type data: :obj:`str` or :class:`tgram.types.InputFile`

        :param duration: Duration of sent video in seconds
        :type duration: :obj:`int`

        :param length: Video width and height, i.e. diameter of the video message
        :type length: :obj:`int`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side.
            The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.
            Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file,
            so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.
        :type thumbnail: :obj:`str` or :class:`tgram.types.InputFile`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the video note will be sent
        :type message_thread_id: :obj:`int`

        :param thumb: Deprecated. Use thumbnail instead
        :type thumb: :obj:`str` or :class:`tgram.types.InputFile`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendVideoNote",
            chat_id=chat_id,
            video_note=get_file_path(video_note),
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            length=length,
            thumbnail=get_file_path(thumbnail),
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_paid_media(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        star_count: int,
        media: List[InputPaidMedia],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        result = await self._send_request(
            "sendPaidMedia",
            chat_id=chat_id,
            star_count=star_count,
            media=media,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_media_group(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        media: List[InputMedia],
        business_connection_id: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
    ) -> List[Message]:
        """
        Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files
        can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendmediagroup

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param media: A JSON-serialized array describing messages to be sent, must include 2-10 items
        :type media: :obj:`list` of :obj:`tgram.types.InputMedia`

        :param disable_notification: Sends the messages silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the messages will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, an array of Messages that were sent is returned.
        :rtype: List[types.Message]
        """

        result = await self._send_request(
            "sendMediaGroup",
            chat_id=chat_id,
            media=media,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
        )
        return [Message._parse(me=self, d=i) for i in result["result"]]

    async def send_location(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        business_connection_id: str = None,
        message_thread_id: int = None,
        horizontal_accuracy: float = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendlocation

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param latitude: Latitude of the location
        :type latitude: :obj:`float`

        :param longitude: Longitude of the location
        :type longitude: :obj:`float`

        :param live_period: Period in seconds during which the location will be updated (see Live Locations, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
        :type live_period: :obj:`int`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
        :type horizontal_accuracy: :obj:`float`

        :param heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        :type heading: :obj:`int`

        :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        :type proximity_alert_radius: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendLocation",
            chat_id=chat_id,
            latitude=latitude,
            longitude=longitude,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_venue(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        foursquare_id: str = None,
        foursquare_type: str = None,
        google_place_id: str = None,
        google_place_type: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendvenue

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` or :obj:`str`

        :param latitude: Latitude of the venue
        :type latitude: :obj:`float`

        :param longitude: Longitude of the venue
        :type longitude: :obj:`float`

        :param title: Name of the venue
        :type title: :obj:`str`

        :param address: Address of the venue
        :type address: :obj:`str`

        :param foursquare_id: Foursquare identifier of the venue
        :type foursquare_id: :obj:`str`

        :param foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”,
            “arts_entertainment/aquarium” or “food/icecream”.)
        :type foursquare_type: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard,
            custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if one of the specified
            replied-to messages is not found.
        :type allow_sending_without_reply: :obj:`bool`

        :param google_place_id: Google Places identifier of the venue
        :type google_place_id: :obj:`str`

        :param google_place_type: Google Places type of the venue.
        :type google_place_type: :obj:`str`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: The thread to which the message will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendVenue",
            chat_id=chat_id,
            latitude=latitude,
            longitude=longitude,
            title=title,
            address=address,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            foursquare_id=foursquare_id,
            foursquare_type=foursquare_type,
            google_place_id=google_place_id,
            google_place_type=google_place_type,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_contact(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        last_name: str = None,
        vcard: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendcontact

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` or :obj:`str`

        :param phone_number: Contact's phone number
        :type phone_number: :obj:`str`

        :param first_name: Contact's first name
        :type first_name: :obj:`str`

        :param last_name: Contact's last name
        :type last_name: :obj:`str`

        :param vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes
        :type vcard: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard,
            custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if one of the specified
            replied-to messages is not found.
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: The thread to which the message will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendContact",
            chat_id=chat_id,
            phone_number=phone_number,
            first_name=first_name,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            last_name=last_name,
            vcard=vcard,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_poll(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        question: str,
        options: List[InputPollOption],
        business_connection_id: str = None,
        message_thread_id: int = None,
        question_parse_mode: str = None,
        question_entities: List[MessageEntity] = None,
        is_anonymous: bool = None,
        type: str = None,
        allows_multiple_answers: bool = None,
        correct_option_id: int = None,
        explanation: str = None,
        explanation_parse_mode: str = None,
        explanation_entities: List[MessageEntity] = None,
        open_period: int = None,
        close_date: int = None,
        is_closed: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send a native poll.
        On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendpoll

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` | :obj:`str`

        :param question: Poll question, 1-300 characters
        :type question: :obj:`str`

        :param options: A JSON-serialized list of 2-10 answer options
        :type options: :obj:`list` of :obj:`InputPollOption`

        :param is_anonymous: True, if the poll needs to be anonymous, defaults to True
        :type is_anonymous: :obj:`bool`

        :param type: Poll type, “quiz” or “regular”, defaults to “regular”
        :type type: :obj:`str`

        :param allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
        :type allows_multiple_answers: :obj:`bool`

        :param correct_option_id: 0-based identifier of the correct answer option. Available only for polls in quiz mode,
            defaults to None
        :type correct_option_id: :obj:`int`

        :param explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll,
            0-200 characters with at most 2 line feeds after entities parsing
        :type explanation: :obj:`str`

        :param explanation_parse_mode: Mode for parsing entities in the explanation. See formatting options for more details.
        :type explanation_parse_mode: :obj:`str`

        :param open_period: Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
        :type open_period: :obj:`int`

        :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed.
        :type close_date: :obj:`int` | :obj:`datetime`

        :param is_closed: Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.
        :type is_closed: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the poll allows multiple options to be voted simultaneously.
        :type allow_sending_without_reply: :obj:`bool`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard,
            instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`InlineKeyboardMarkup` | :obj:`ReplyKeyboardMarkup` | :obj:`ReplyKeyboardRemove` | :obj:`ForceReply`

        :param timeout: Timeout in seconds for waiting for a response from the user.
        :type timeout: :obj:`int`

        :param explanation_entities: A JSON-serialized list of special entities that appear in the explanation,
            which can be specified instead of parse_mode
        :type explanation_entities: :obj:`list` of :obj:`MessageEntity`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: The identifier of a message thread, in which the poll will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of the business connection to send the message through
        :type business_connection_id: :obj:`str`

        :param question_parse_mode: Mode for parsing entities in the question. See formatting options for more details. Currently, only custom emoji entities are allowed
        :type question_parse_mode: :obj:`str`

        :param question_entities: A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of question_parse_mode
        :type question_entities: :obj:`list` of :obj:`MessageEntity`

        :param message_effect_id: Identifier of the message effect to apply to the sent message
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :obj:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendPoll",
            chat_id=chat_id,
            question=question,
            options=options,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            question_parse_mode=question_parse_mode,
            question_entities=question_entities,
            is_anonymous=is_anonymous,
            type=type,
            allows_multiple_answers=allows_multiple_answers,
            correct_option_id=correct_option_id,
            explanation=explanation,
            explanation_parse_mode=explanation_parse_mode,
            explanation_entities=explanation_entities,
            open_period=open_period,
            close_date=close_date,
            is_closed=is_closed,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_dice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#senddice

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param emoji: Emoji on which the dice throw animation is based. Currently, must be one of “🎲”, “🎯”, “🏀”, “⚽”, “🎳”, or “🎰”.
            Dice can have values 1-6 for “🎲”, “🎯” and “🎳”, values 1-5 for “🏀” and “⚽”, and values 1-64 for “🎰”. Defaults to “🎲”
        :type emoji: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions
            to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding
        :type protect_content: :obj:`bool`

        :param message_thread_id: The identifier of a message thread, unique within the chat to which the message with the thread identifier belongs
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Unique identifier for the target business connection
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendDice",
            chat_id=chat_id,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            emoji=emoji,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_chat_action(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        action: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
    ) -> bool:
        """
        Use this method when you need to tell the user that something is happening on the bot's side.
        The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).
        Returns True on success.

        Example: The ImageBot needs some time to process a request and upload the image. Instead of sending a text message along the lines of
        “Retrieving image, please wait…”, the bot may use sendChatAction with action = upload_photo. The user will see a “sending photo” status for the bot.

        Telegram documentation: https://core.telegram.org/bots/api#sendchataction

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` or :obj:`str`

        :param action: Type of action to broadcast. Choose one, depending on what the user is about
            to receive: typing for text messages, upload_photo for photos, record_video or upload_video
            for videos, record_voice or upload_voice for voice notes, upload_document for general files,
            choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes.
        :type action: :obj:`str`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param message_thread_id: The thread to which the message will be sent(supergroups only)
        :type message_thread_id: :obj:`int`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "sendChatAction",
            chat_id=chat_id,
            action=action,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def set_message_reaction(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        reaction: List[ReactionType] = None,
        is_big: bool = None,
    ) -> bool:
        """
        Use this method to change the chosen reactions on a message.
        Service messages can't be reacted to. Automatically forwarded messages from a channel to its discussion group have the same
        available reactions as messages in the channel. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setmessagereaction

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Identifier of the message to set reaction to
        :type message_id: :obj:`int`

        :param reaction: New list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message.
            A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators.
        :type reaction: :obj:`list` of :class:`tgram.types.ReactionType`

        :param is_big: Pass True to set the reaction with a big animation
        :type is_big: :obj:`bool`

        :return: :obj:`bool`
        """

        result = await self._send_request(
            "setMessageReaction",
            chat_id=chat_id,
            message_id=message_id,
            reaction=reaction,
            is_big=is_big,
        )
        return result["result"]

    async def get_user_profile_photos(
        self: "tgram.TgBot", user_id: int, offset: int = None, limit: int = None
    ) -> UserProfilePhotos:
        """
        Use this method to get a list of profile pictures for a user.
        Returns a :class:`tgram.types.UserProfilePhotos` object.

        Telegram documentation: https://core.telegram.org/bots/api#getuserprofilephotos

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param offset: Sequential number of the first photo to be returned. By default, all photos are returned.
        :type offset: :obj:`int`

        :param limit: Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :type limit: :obj:`int`

        :return: `UserProfilePhotos <https://core.telegram.org/bots/api#userprofilephotos>`_
        :rtype: :class:`tgram.types.UserProfilePhotos`

        """

        result = await self._send_request(
            "getUserProfilePhotos",
            user_id=user_id,
            offset=offset,
            limit=limit,
        )
        return UserProfilePhotos._parse(me=self, d=result["result"])

    async def get_file(self: "tgram.TgBot", file_id: str) -> File:
        """
        Use this method to get basic info about a file and prepare it for downloading.
        For the moment, bots can download files of up to 20MB in size.
        On success, a File object is returned.
        It is guaranteed that the link will be valid for at least 1 hour.
        When the link expires, a new one can be requested by calling get_file again.

        Telegram documentation: https://core.telegram.org/bots/api#getfile

        :param file_id: File identifier
        :type file_id: :obj:`str`

        :return: :class:`tgram.types.File`
        """

        result = await self._send_request(
            "getFile",
            file_id=file_id,
        )
        return File._parse(me=self, d=result["result"])

    async def download_file(
        self: "tgram.TgBot", file_id: str, file_path: str = None, in_memory: bool = None
    ) -> Union[Path, io.BytesIO]:
        file = await self.get_file(file_id)
        file_path = file_path or file.file_path.split("/")[1]
        url = self.api_url + f"file/bot{self.bot_token}/{file.file_path}"
        session = await self._get_session()
        async with session.request("GET", url=url) as response:
            if response.status != 200:
                raise APIException("Download file", response)
            result = await response.read()
        if in_memory:
            memory_file = io.BytesIO()
            memory_file.write(result)
            memory_file.seek(0)
            memory_file.name = file_path
            return memory_file
        else:
            with open(Path(file_path), "wb") as f:
                f.write(result)
            return Path(file_path)

    async def get_file_url(self: "tgram.TgBot", file_id: str) -> str:
        """
        Get a valid URL for downloading a file.

        :param file_id: File identifier to get download URL for.
        :type file_id: :obj:`str`

        :return: URL for downloading the file.
        :rtype: :obj:`str`
        """
        file = await self.get_file(file_id)
        return self.api_url + f"file/bot{self.bot_token}/{file.file_path}"

    async def ban_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None,
    ) -> bool:
        """
        Use this method to ban a user in a group, a supergroup or a channel.
        In the case of supergroups and channels, the user will not be able to return to the chat on their
        own using invite links, etc., unless unbanned first.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#banchatmember

        :param chat_id: Unique identifier for the target group or username of the target supergroup
            or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param until_date: Date when the user will be unbanned, unix time. If user is banned for more than 366 days or
               less than 30 seconds from the current time they are considered to be banned forever
        :type until_date: :obj:`int`

        :param revoke_messages: Bool: Pass True to delete all messages from the chat for the user that is being removed.
            If False, the user will be able to see messages in the group that were sent before the user was removed.
            Always True for supergroups and channels.
        :type revoke_messages: :obj:`bool`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "banChatMember",
            chat_id=chat_id,
            user_id=user_id,
            until_date=until_date,
            revoke_messages=revoke_messages,
        )
        return result["result"]

    async def unban_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: bool = None,
    ) -> bool:
        """
        Use this method to unban a previously kicked user in a supergroup or channel.
        The user will not return to the group or channel automatically, but will be able to join via link, etc.
        The bot must be an administrator for this to work. By default, this method guarantees that after the call
        the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat
        they will also be removed from the chat. If you don't want this, use the parameter only_if_banned.

        Telegram documentation: https://core.telegram.org/bots/api#unbanchatmember

        :param chat_id: Unique identifier for the target group or username of the target supergroup or channel
            (in the format @username)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param only_if_banned: Do nothing if the user is not banned
        :type only_if_banned: :obj:`bool`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "unbanChatMember",
            chat_id=chat_id,
            user_id=user_id,
            only_if_banned=only_if_banned,
        )
        return result["result"]

    async def restrict_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
        until_date: int = None,
    ) -> bool:
        """
        Use this method to restrict a user in a supergroup.
        The bot must be an administrator in the supergroup for this to work and must have
        the appropriate admin rights. Pass True for all boolean parameters to lift restrictions from a user.

        Telegram documentation: https://core.telegram.org/bots/api#restrictchatmember

        .. warning::
            Individual parameters are deprecated and will be removed, use 'permissions' instead

        :param chat_id: Unique identifier for the target group or username of the target supergroup
            or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param until_date: Date when restrictions will be lifted for the user, unix time.
            If user is restricted for more than 366 days or less than 30 seconds from the current time,
            they are considered to be restricted forever
        :type until_date: :obj:`int`, optional

        :param can_send_messages: deprecated
        :type can_send_messages: :obj:`bool`

        :param can_send_media_messages: deprecated
        :type can_send_media_messages: :obj:`bool`

        :param can_send_polls: deprecated
        :type can_send_polls: :obj:`bool`

        :param can_send_other_messages: deprecated
        :type can_send_other_messages: :obj:`bool`

        :param can_add_web_page_previews: deprecated
        :type can_add_web_page_previews: :obj:`bool`

        :param can_change_info: deprecated
        :type can_change_info: :obj:`bool`

        :param can_invite_users: deprecated
        :type can_invite_users: :obj:`bool`

        :param can_pin_messages: deprecated
        :type can_pin_messages: :obj:`bool`

        :param use_independent_chat_permissions: Pass True if chat permissions are set independently.
            Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,
            can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes
            permissions; the can_send_polls permission will imply the can_send_messages permission.
        :type use_independent_chat_permissions: :obj:`bool`, optional

        :param permissions: Pass ChatPermissions object to set all permissions at once. Use this parameter instead of
            passing all boolean parameters to avoid backward compatibility problems in future.
        :type permissions: :obj:`tgram.types.ChatPermissions`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "restrictChatMember",
            chat_id=chat_id,
            user_id=user_id,
            permissions=permissions,
            use_independent_chat_permissions=use_independent_chat_permissions,
            until_date=until_date,
        )
        return result["result"]

    async def promote_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: bool = None,
        can_manage_chat: bool = None,
        can_delete_messages: bool = None,
        can_manage_video_chats: bool = None,
        can_restrict_members: bool = None,
        can_promote_members: bool = None,
        can_change_info: bool = None,
        can_invite_users: bool = None,
        can_post_stories: bool = None,
        can_edit_stories: bool = None,
        can_delete_stories: bool = None,
        can_post_messages: bool = None,
        can_edit_messages: bool = None,
        can_pin_messages: bool = None,
        can_manage_topics: bool = None,
    ) -> bool:
        """
        Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator
        in the chat for this to work and must have the appropriate admin rights.
        Pass False for all boolean parameters to demote a user.

        Telegram documentation: https://core.telegram.org/bots/api#promotechatmember

        :param chat_id: Unique identifier for the target chat or username of the target channel (
            in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param can_change_info: Pass True, if the administrator can change chat title, photo and other settings
        :type can_change_info: :obj:`bool`

        :param can_post_messages: Pass True, if the administrator can create channel posts, channels only
        :type can_post_messages: :obj:`bool`

        :param can_edit_messages: Pass True, if the administrator can edit messages of other users, channels only
        :type can_edit_messages: :obj:`bool`

        :param can_delete_messages: Pass True, if the administrator can delete messages of other users
        :type can_delete_messages: :obj:`bool`

        :param can_invite_users: Pass True, if the administrator can invite new users to the chat
        :type can_invite_users: :obj:`bool`

        :param can_restrict_members: Pass True, if the administrator can restrict, ban or unban chat members
        :type can_restrict_members: :obj:`bool`

        :param can_pin_messages: Pass True, if the administrator can pin messages, supergroups only
        :type can_pin_messages: :obj:`bool`

        :param can_promote_members: Pass True, if the administrator can add new administrators with a subset
            of his own privileges or demote administrators that he has promoted, directly or indirectly
            (promoted by administrators that were appointed by him)
        :type can_promote_members: :obj:`bool`

        :param is_anonymous: Pass True, if the administrator's presence in the chat is hidden
        :type is_anonymous: :obj:`bool`

        :param can_manage_chat: Pass True, if the administrator can access the chat event log, chat statistics,
            message statistics in channels, see channel members,
            see anonymous administrators in supergroups and ignore slow mode.
            Implied by any other administrator privilege
        :type can_manage_chat: :obj:`bool`

        :param can_manage_video_chats: Pass True, if the administrator can manage voice chats
            For now, bots can use this privilege only for passing to other administrators.
        :type can_manage_video_chats: :obj:`bool`

        :param can_manage_voice_chats: Deprecated, use can_manage_video_chats.
        :type can_manage_voice_chats: :obj:`bool`

        :param can_manage_topics: Pass True if the user is allowed to create, rename, close,
            and reopen forum topics, supergroups only
        :type can_manage_topics: :obj:`bool`

        :param can_post_stories: Pass True if the administrator can create the channel's stories
        :type can_post_stories: :obj:`bool`

        :param can_edit_stories: Pass True if the administrator can edit the channel's stories
        :type can_edit_stories: :obj:`bool`

        :param can_delete_stories: Pass True if the administrator can delete the channel's stories
        :type can_delete_stories: :obj:`bool`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "promoteChatMember",
            chat_id=chat_id,
            user_id=user_id,
            is_anonymous=is_anonymous,
            can_manage_chat=can_manage_chat,
            can_delete_messages=can_delete_messages,
            can_manage_video_chats=can_manage_video_chats,
            can_restrict_members=can_restrict_members,
            can_promote_members=can_promote_members,
            can_change_info=can_change_info,
            can_invite_users=can_invite_users,
            can_post_stories=can_post_stories,
            can_edit_stories=can_edit_stories,
            can_delete_stories=can_delete_stories,
            can_post_messages=can_post_messages,
            can_edit_messages=can_edit_messages,
            can_pin_messages=can_pin_messages,
            can_manage_topics=can_manage_topics,
        )
        return result["result"]

    async def set_chat_administrator_custom_title(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int, custom_title: str
    ) -> bool:
        """
        Use this method to set a custom title for an administrator in a supergroup promoted by the bot.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setchatadministratorcustomtitle

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param custom_title: New custom title for the administrator;
            0-16 characters, emoji are not allowed
        :type custom_title: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setChatAdministratorCustomTitle",
            chat_id=chat_id,
            user_id=user_id,
            custom_title=custom_title,
        )
        return result["result"]

    async def ban_chat_sender_chat(
        self: "tgram.TgBot", chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """
        Use this method to ban a channel chat in a supergroup or a channel.
        The owner of the chat will not be able to send messages and join live
        streams on behalf of the chat, unless it is unbanned first.
        The bot must be an administrator in the supergroup or channel
        for this to work and must have the appropriate administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#banchatsenderchat

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param sender_chat_id: Unique identifier of the target sender chat
        :type sender_chat_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "banChatSenderChat",
            chat_id=chat_id,
            sender_chat_id=sender_chat_id,
        )
        return result["result"]

    async def unban_chat_sender_chat(
        self: "tgram.TgBot", chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """
        Use this method to unban a previously banned channel chat in a supergroup or channel.
        The bot must be an administrator for this to work and must have the appropriate
        administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unbanchatsenderchat

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param sender_chat_id: Unique identifier of the target sender chat.
        :type sender_chat_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "unbanChatSenderChat",
            chat_id=chat_id,
            sender_chat_id=sender_chat_id,
        )
        return result["result"]

    async def set_chat_permissions(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
    ) -> bool:
        """
        Use this method to set default chat permissions for all members.
        The bot must be an administrator in the group or a supergroup for this to work
        and must have the can_restrict_members admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#setchatpermissions

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param permissions: New default chat permissions
        :type permissions: :class:`tgram.types..ChatPermissions`

        :param use_independent_chat_permissions: Pass True if chat permissions are set independently. Otherwise,
            the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages,
            can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and
            can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.
        :type use_independent_chat_permissions: :obj:`bool`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setChatPermissions",
            chat_id=chat_id,
            permissions=permissions,
            use_independent_chat_permissions=use_independent_chat_permissions,
        )
        return result["result"]

    async def export_chat_invite_link(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> str:
        """
        Use this method to export an invite link to a supergroup or a channel. The bot must be an administrator
        in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#exportchatinvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: exported invite link as String on success.
        :rtype: :obj:`str`
        """

        result = await self._send_request(
            "exportChatInviteLink",
            chat_id=chat_id,
        )
        return result["result"]

    async def create_chat_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """
        Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights.
        The link can be revoked using the method revokeChatInviteLink.
        Returns the new invite link as ChatInviteLink object.

        Telegram documentation: https://core.telegram.org/bots/api#createchatinvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param name: Invite link name; 0-32 characters
        :type name: :obj:`str`

        :param expire_date: Point in time (Unix timestamp) when the link will expire
        :type expire_date: :obj:`int`

        :param member_limit: Maximum number of users that can be members of the chat simultaneously
        :type member_limit: :obj:`int`

        :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified
        :type creates_join_request: :obj:`bool`

        :return: Returns the new invite link as ChatInviteLink object.
        :rtype: :class:`tgram.types.ChatInviteLink`
        """

        result = await self._send_request(
            "createChatInviteLink",
            chat_id=chat_id,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])

    async def edit_chat_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """
        Use this method to edit a non-primary invite link created by the bot.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#editchatinvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param name: Invite link name; 0-32 characters
        :type name: :obj:`str`

        :param invite_link: The invite link to edit
        :type invite_link: :obj:`str`

        :param expire_date: Point in time (Unix timestamp) when the link will expire
        :type expire_date: :obj:`int`

        :param member_limit: Maximum number of users that can be members of the chat simultaneously
        :type member_limit: :obj:`int`

        :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified
        :type creates_join_request: :obj:`bool`

        :return: Returns the new invite link as ChatInviteLink object.
        :rtype: :class:`tgram.types.ChatInviteLink`
        """

        result = await self._send_request(
            "editChatInviteLink",
            chat_id=chat_id,
            invite_link=invite_link,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])

    async def revoke_chat_invite_link(
        self: "tgram.TgBot", chat_id: Union[int, str], invite_link: str
    ) -> ChatInviteLink:
        """
        Use this method to revoke an invite link created by the bot.
        Note: If the primary link is revoked, a new link is automatically generated The bot must be an administrator
        in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#revokechatinvitelink

        :param chat_id: Id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param invite_link: The invite link to revoke
        :type invite_link: :obj:`str`

        :return: Returns the new invite link as ChatInviteLink object.
        :rtype: :class:`tgram.types.ChatInviteLink`
        """

        result = await self._send_request(
            "revokeChatInviteLink",
            chat_id=chat_id,
            invite_link=invite_link,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])

    async def approve_chat_join_request(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> bool:
        """
        Use this method to approve a chat join request.
        The bot must be an administrator in the chat for this to work and must have
        the can_invite_users administrator right. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#approvechatjoinrequest

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "approveChatJoinRequest",
            chat_id=chat_id,
            user_id=user_id,
        )
        return result["result"]

    async def decline_chat_join_request(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> bool:
        """
        Use this method to decline a chat join request.
        The bot must be an administrator in the chat for this to work and must have
        the can_invite_users administrator right. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#declinechatjoinrequest

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "declineChatJoinRequest",
            chat_id=chat_id,
            user_id=user_id,
        )
        return result["result"]

    async def set_chat_photo(
        self: "tgram.TgBot", chat_id: Union[int, str], photo: Union[Path, bytes, str]
    ) -> bool:
        """
        Use this method to set a new profile photo for the chat. Photos can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.
        Note: In regular groups (non-supergroups), this method will only work if the ‘All Members Are Admins’
        setting is off in the target group.

        Telegram documentation: https://core.telegram.org/bots/api#setchatphoto

        :param chat_id: Int or Str: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param photo: InputFile: New chat photo, uploaded using multipart/form-data
        :type photo: :obj:`typing.Union[file_like, str]`
        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setChatPhoto",
            chat_id=chat_id,
            photo=photo,
        )
        return result["result"]

    async def delete_chat_photo(self: "tgram.TgBot", chat_id: Union[int, str]) -> bool:
        """
        Use this method to delete a chat photo. Photos can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.
        Note: In regular groups (non-supergroups), this method will only work if the ‘All Members Are Admins’ setting is off in the target group.

        Telegram documentation: https://core.telegram.org/bots/api#deletechatphoto

        :param chat_id: Int or Str: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteChatPhoto",
            chat_id=chat_id,
        )
        return result["result"]

    async def set_chat_title(
        self: "tgram.TgBot", chat_id: Union[int, str], title: str
    ) -> bool:
        """
        Use this method to change the title of a chat. Titles can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.
        Note: In regular groups (non-supergroups), this method will only work if the ‘All Members Are Admins’
        setting is off in the target group.

        Telegram documentation: https://core.telegram.org/bots/api#setchattitle

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param title: New chat title, 1-255 characters
        :type title: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setChatTitle",
            chat_id=chat_id,
            title=title,
        )
        return result["result"]

    async def set_chat_description(
        self: "tgram.TgBot", chat_id: Union[int, str], description: str = None
    ) -> bool:
        """
        Use this method to change the description of a supergroup or a channel.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

        Telegram documentation: https://core.telegram.org/bots/api#setchatdescription

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param description: Str: New chat description, 0-255 characters
        :type description: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setChatDescription",
            chat_id=chat_id,
            description=description,
        )
        return result["result"]

    async def pin_chat_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: bool = None,
    ) -> bool:
        """
        Use this method to pin a message in a supergroup.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#pinchatmessage

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Identifier of a message to pin
        :type message_id: :obj:`int`

        :param disable_notification: Pass True, if it is not necessary to send a notification
            to all group members about the new pinned message
        :type disable_notification: :obj:`bool`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "pinChatMessage",
            chat_id=chat_id,
            message_id=message_id,
            disable_notification=disable_notification,
        )
        return result["result"]

    async def unpin_chat_message(
        self: "tgram.TgBot", chat_id: Union[int, str], message_id: int = None
    ) -> bool:
        """
        Use this method to unpin specific pinned message in a supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unpinchatmessage

        :param chat_id: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Int: Identifier of a message to unpin
        :type message_id: :obj:`int`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "unpinChatMessage",
            chat_id=chat_id,
            message_id=message_id,
        )
        return result["result"]

    async def unpin_all_chat_messages(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to unpin a all pinned messages in a supergroup chat.
        The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unpinallchatmessages

        :param chat_id: Int or Str: Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "unpinAllChatMessages",
            chat_id=chat_id,
        )
        return result["result"]

    async def leave_chat(self: "tgram.TgBot", chat_id: Union[int, str]) -> bool:
        """
        Use this method for your bot to leave a group, supergroup or channel. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#leavechat

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: :obj:`bool`
        """

        result = await self._send_request(
            "leaveChat",
            chat_id=chat_id,
        )
        return result["result"]

    async def get_chat(self: "tgram.TgBot", chat_id: Union[int, str]) -> ChatFullInfo:
        """
        Use this method to get up to date information about the chat (current name of the user for one-on-one
        conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.

        Telegram documentation: https://core.telegram.org/bots/api#getchat

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: Chat information
        :rtype: :class:`tgram.types.ChatFullInfo`
        """

        result = await self._send_request(
            "getChat",
            chat_id=chat_id,
        )
        return ChatFullInfo._parse(me=self, d=result["result"])

    async def get_chat_administrators(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> List[Union[ChatMemberAdministrator, ChatMemberOwner]]:
        result = await self._send_request(
            "getChatAdministrators",
            chat_id=chat_id,
        )
        return [ChatMember._parse(me=self, d=i) for i in result["result"]]

    async def get_chat_member_count(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> int:
        """
        Use this method to get the number of members in a chat.

        Telegram documentation: https://core.telegram.org/bots/api#getchatmembercount

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: Number of members in the chat.
        :rtype: :obj:`int`
        """

        result = await self._send_request(
            "getChatMemberCount",
            chat_id=chat_id,
        )
        return result["result"]

    async def get_chat_member(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> Union[
        ChatMemberOwner,
        ChatMemberAdministrator,
        ChatMemberMember,
        ChatMemberRestricted,
        ChatMemberBanned,
        ChatMemberLeft,
    ]:
        result = await self._send_request(
            "getChatMember",
            chat_id=chat_id,
            user_id=user_id,
        )
        return ChatMember._parse(me=self, d=result["result"])

    async def set_chat_sticker_set(
        self: "tgram.TgBot", chat_id: Union[int, str], sticker_set_name: str
    ) -> bool:
        """
        Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat
        for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned
        in getChat requests to check if the bot can use this method. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setchatstickerset

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param sticker_set_name: Name of the sticker set to be set as the group sticker set
        :type sticker_set_name: :obj:`str`

        :return: StickerSet object
        :rtype: :class:`tgram.types.StickerSet`
        """

        result = await self._send_request(
            "setChatStickerSet",
            chat_id=chat_id,
            sticker_set_name=sticker_set_name,
        )
        return result["result"]

    async def delete_chat_sticker_set(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat
        for this to work and must have the appropriate admin rights. Use the field can_set_sticker_set
        optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletechatstickerset

        :param chat_id:	Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteChatStickerSet",
            chat_id=chat_id,
        )
        return result["result"]

    async def get_forum_topic_icon_stickers(self: "tgram.TgBot") -> List[Sticker]:
        """
        Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user.
        Requires no parameters. Returns an Array of Sticker objects.

        Telegram documentation: https://core.telegram.org/bots/api#getforumtopiciconstickers

        :return: On success, a list of StickerSet objects is returned.
        :rtype: List[:class:`tgram.types.StickerSet`]
        """

        result = await self._send_request(
            "getForumTopicIconStickers",
        )
        return [Sticker._parse(me=self, d=i) for i in result["result"]]

    async def create_forum_topic(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        name: str,
        icon_color: int = None,
        icon_custom_emoji_id: str = None,
    ) -> ForumTopic:
        """
        Use this method to create a topic in a forum supergroup chat. The bot must be an administrator
        in the chat for this to work and must have the can_manage_topics administrator rights.
        Returns information about the created topic as a ForumTopic object.

        Telegram documentation: https://core.telegram.org/bots/api#createforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param name: Name of the topic, 1-128 characters
        :type name: :obj:`str`

        :param icon_color: Color of the topic icon in RGB format. Currently, must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F
        :type icon_color: :obj:`int`

        :param icon_custom_emoji_id: Custom emoji for the topic icon. Must be an emoji of type “tgs” and must be exactly 1 character long
        :type icon_custom_emoji_id: :obj:`str`

        :return: On success, information about the created topic is returned as a ForumTopic object.
        :rtype: :class:`tgram.types.ForumTopic`
        """

        result = await self._send_request(
            "createForumTopic",
            chat_id=chat_id,
            name=name,
            icon_color=icon_color,
            icon_custom_emoji_id=icon_custom_emoji_id,
        )
        return ForumTopic._parse(me=self, d=result["result"])

    async def edit_forum_topic(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_thread_id: int,
        name: str = None,
        icon_custom_emoji_id: str = None,
    ) -> bool:
        """
        Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an
        administrator in the chat for this to work and must have can_manage_topics administrator rights,
        unless it is the creator of the topic. Returns True on success.

        Telegram Documentation: https://core.telegram.org/bots/api#editforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_thread_id: Identifier of the topic to edit
        :type message_thread_id: :obj:`int`

        :param name: Optional, New name of the topic, 1-128 characters. If not specififed or empty,
            the current name of the topic will be kept
        :type name: :obj:`str`

        :param icon_custom_emoji_id: Optional, New unique identifier of the custom emoji shown as the topic icon.
            Use getForumTopicIconStickers to get all allowed custom emoji identifiers. Pass an empty string to remove the
            icon. If not specified, the current icon will be kept
        :type icon_custom_emoji_id: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "editForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
            name=name,
            icon_custom_emoji_id=icon_custom_emoji_id,
        )
        return result["result"]

    async def close_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """
        Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator
        in the chat for this to work and must have the can_manage_topics administrator rights, unless it is
        the creator of the topic. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#closeforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_thread_id: Identifier of the topic to close
        :type message_thread_id: :obj:`int`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "closeForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def reopen_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """
        Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat
        for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#reopenforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_thread_id: Identifier of the topic to reopen
        :type message_thread_id: :obj:`int`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "reopenForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def delete_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """
        Use this method to delete a topic in a forum supergroup chat. The bot must be an administrator in the chat for this
        to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True
        on success.

        Telegram documentation: https://core.telegram.org/bots/api#deleteforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_thread_id: Identifier of the topic to delete
        :type message_thread_id: :obj:`int`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def unpin_all_forum_topic_messages(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the
        chat for this to work and must have the can_pin_messages administrator right in the supergroup.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unpinallforumtopicmessages

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_thread_id: Identifier of the topic
        :type message_thread_id: :obj:`int`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "unpinAllForumTopicMessages",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def edit_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], name: str
    ) -> bool:
        """
        Use this method to edit the name of the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#editgeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param name: New topic name, 1-128 characters
        :type name: :obj:`str`
        """

        result = await self._send_request(
            "editGeneralForumTopic",
            chat_id=chat_id,
            name=name,
        )
        return result["result"]

    async def close_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to close the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#closegeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`
        """

        result = await self._send_request(
            "closeGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]

    async def reopen_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to reopen the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#reopengeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`
        """

        result = await self._send_request(
            "reopenGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]

    async def hide_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to hide the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#hidegeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`
        """

        result = await self._send_request(
            "hideGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]

    async def unhide_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to unhide the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unhidegeneralforumtopic

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`
        """

        result = await self._send_request(
            "unhideGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]

    async def unpin_all_general_forum_topic_messages(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a General forum topic.
        The bot must be an administrator in the chat for this to work and must have the
        can_pin_messages administrator right in the supergroup.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#unpinAllGeneralForumTopicMessages

        :param chat_id: Unique identifier for the target chat or username of chat
        :type chat_id: :obj:`int` | :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "unpinAllGeneralForumTopicMessages",
            chat_id=chat_id,
        )
        return result["result"]

    async def answer_callback_query(
        self: "tgram.TgBot",
        callback_query_id: str,
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> bool:
        """
        Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to
        the user as a notification at the top of the chat screen or as an alert.

        Telegram documentation: https://core.telegram.org/bots/api#answercallbackquery

        :param callback_query_id: Unique identifier for the query to be answered
        :type callback_query_id: :obj:`int`

        :param text: Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
        :type text: :obj:`str`

        :param show_alert: If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
        :type show_alert: :obj:`bool`

        :param url: URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your
            game - note that this will only work if the query comes from a callback_game button.
        :type url: :obj:`str`

        :param cache_time: The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching
            starting in version 3.14. Defaults to 0.

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "answerCallbackQuery",
            callback_query_id=callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )
        return result["result"]

    async def get_user_chat_boosts(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> UserChatBoosts:
        """
        Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object.

        Telegram documentation: https://core.telegram.org/bots/api#getuserchatboosts

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` | :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :return: On success, a UserChatBoosts object is returned.
        :rtype: :class:`tgram.types.UserChatBoosts`
        """

        result = await self._send_request(
            "getUserChatBoosts",
            chat_id=chat_id,
            user_id=user_id,
        )
        return UserChatBoosts._parse(me=self, d=result["result"])

    async def get_business_connection(
        self: "tgram.TgBot", business_connection_id: str
    ) -> BusinessConnection:
        """
        Use this method to get information about the connection of the bot with a business account.
        Returns a BusinessConnection object on success.

        Telegram documentation: https://core.telegram.org/bots/api#getbusinessconnection

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :return: Returns a BusinessConnection object on success.
        :rtype: :class:`tgram.types.BusinessConnection`
        """

        result = await self._send_request(
            "getBusinessConnection",
            business_connection_id=business_connection_id,
        )
        return BusinessConnection._parse(me=self, d=result["result"])

    async def set_my_commands(
        self: "tgram.TgBot",
        commands: List[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None,
    ) -> bool:
        """
        Use this method to change the list of the bot's commands.

        Telegram documentation: https://core.telegram.org/bots/api#setmycommands

        :param commands: List of BotCommand. At most 100 commands can be specified.
        :type commands: :obj:`list` of :class:`tgram.types.BotCommand`

        :param scope: The scope of users for which the commands are relevant.
            Defaults to BotCommandScopeDefault.
        :type scope: :class:`tgram.types.BotCommandScope`

        :param language_code: A two-letter ISO 639-1 language code. If empty,
            commands will be applied to all users from the given scope,
            for whose language there are no dedicated commands
        :type language_code: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setMyCommands",
            commands=commands,
            scope=scope,
            language_code=language_code,
        )
        return result["result"]

    async def delete_my_commands(
        self: "tgram.TgBot", scope: BotCommandScope = None, language_code: str = None
    ) -> bool:
        """
        Use this method to delete the list of the bot's commands for the given scope and user language.
        After deletion, higher level commands will be shown to affected users.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletemycommands

        :param scope: The scope of users for which the commands are relevant.
            Defaults to BotCommandScopeDefault.
        :type scope: :class:`tgram.types.BotCommandScope`

        :param language_code: A two-letter ISO 639-1 language code. If empty,
            commands will be applied to all users from the given scope,
            for whose language there are no dedicated commands
        :type language_code: :obj:`str`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteMyCommands",
            scope=scope,
            language_code=language_code,
        )
        return result["result"]

    async def get_my_commands(
        self: "tgram.TgBot", scope: BotCommandScope = None, language_code: str = None
    ) -> List[BotCommand]:
        """
        Use this method to get the current list of the bot's commands.
        Returns List of BotCommand on success.

        Telegram documentation: https://core.telegram.org/bots/api#getmycommands

        :param scope: The scope of users for which the commands are relevant.
            Defaults to BotCommandScopeDefault.
        :type scope: :class:`tgram.types.BotCommandScope`

        :param language_code: A two-letter ISO 639-1 language code. If empty,
            commands will be applied to all users from the given scope,
            for whose language there are no dedicated commands
        :type language_code: :obj:`str`

        :return: List of BotCommand on success.
        :rtype: :obj:`list` of :class:`tgram.types.BotCommand`
        """

        result = await self._send_request(
            "getMyCommands",
            scope=scope,
            language_code=language_code,
        )
        return [BotCommand._parse(me=self, d=i) for i in result["result"]]

    async def set_my_name(
        self: "tgram.TgBot", name: str = None, language_code: str = None
    ) -> bool:
        """
        Use this method to change the bot's name. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setmyname

        :param name: Optional. New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language.
        :type name: :obj:`str`

        :param language_code: Optional. A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose
            language there is no dedicated name.
        :type language_code: :obj:`str`

        :return: True on success.
        """

        result = await self._send_request(
            "setMyName",
            name=name,
            language_code=language_code,
        )
        return result["result"]

    async def get_my_name(self: "tgram.TgBot", language_code: str = None) -> BotName:
        """
        Use this method to get the current bot name for the given user language.
        Returns BotName on success.

        Telegram documentation: https://core.telegram.org/bots/api#getmyname

        :param language_code: Optional. A two-letter ISO 639-1 language code or an empty string
        :type language_code: :obj:`str`

        :return: :class:`tgram.types.BotName`
        """

        result = await self._send_request(
            "getMyName",
            language_code=language_code,
        )
        return BotName._parse(me=self, d=result["result"])

    async def set_my_description(
        self: "tgram.TgBot", description: str = None, language_code: str = None
    ) -> bool:
        """
        Use this method to change the bot's description, which is shown in
        the chat with the bot if the chat is empty.
        Returns True on success.

        :param description: New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.
        :type description: :obj:`str`

        :param language_code: A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for
            whose language there is no dedicated description.
        :type language_code: :obj:`str`

        :return: True on success.
        """

        result = await self._send_request(
            "setMyDescription",
            description=description,
            language_code=language_code,
        )
        return result["result"]

    async def get_my_description(
        self: "tgram.TgBot", language_code: str = None
    ) -> BotDescription:
        """
        Use this method to get the current bot description for the given user language.
        Returns BotDescription on success.

        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :obj:`str`

        :return: :class:`tgram.types.BotDescription`
        """

        result = await self._send_request(
            "getMyDescription",
            language_code=language_code,
        )
        return BotDescription._parse(me=self, d=result["result"])

    async def set_my_short_description(
        self: "tgram.TgBot", short_description: str = None, language_code: str = None
    ) -> bool:
        """
        Use this method to change the bot's short description, which is shown on the bot's profile page and
        is sent together with the link when users share the bot.
        Returns True on success.

        :param short_description: New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language.
        :type short_description: :obj:`str`

        :param language_code: A two-letter ISO 639-1 language code.
            If empty, the short description will be applied to all users for whose language there is no dedicated short description.
        :type language_code: :obj:`str`

        :return: True on success.
        """

        result = await self._send_request(
            "setMyShortDescription",
            short_description=short_description,
            language_code=language_code,
        )
        return result["result"]

    async def get_my_short_description(
        self: "tgram.TgBot", language_code: str = None
    ) -> BotShortDescription:
        """
        Use this method to get the current bot short description for the given user language.
        Returns BotShortDescription on success.

        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :obj:`str`

        :return: :class:`tgram.types.BotShortDescription`
        """

        result = await self._send_request(
            "getMyShortDescription",
            language_code=language_code,
        )
        return BotShortDescription._parse(me=self, d=result["result"])

    async def set_chat_menu_button(
        self: "tgram.TgBot", chat_id: int = None, menu_button: MenuButton = None
    ) -> bool:
        """
        Use this method to change the bot's menu button in a private chat,
        or the default menu button.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setchatmenubutton

        :param chat_id: Unique identifier for the target private chat.
            If not specified, default bot's menu button will be changed.
        :type chat_id: :obj:`int` or :obj:`str`

        :param menu_button: A JSON-serialized object for the new bot's menu button. Defaults to MenuButtonDefault
        :type menu_button: :class:`tgram.types.MenuButton`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setChatMenuButton",
            chat_id=chat_id,
            menu_button=menu_button,
        )
        return result["result"]

    async def get_chat_menu_button(
        self: "tgram.TgBot", chat_id: int = None
    ) -> MenuButton:
        """
        Use this method to get the current value of the bot's menu button
        in a private chat, or the default menu button.
        Returns MenuButton on success.

        Telegram Documentation: https://core.telegram.org/bots/api#getchatmenubutton

        :param chat_id: Unique identifier for the target private chat.
            If not specified, default bot's menu button will be returned.
        :type chat_id: :obj:`int` or :obj:`str`

        :return: types.MenuButton
        :rtype: :class:`tgram.types.MenuButton`
        """

        result = await self._send_request(
            "getChatMenuButton",
            chat_id=chat_id,
        )
        return MenuButton._parse(me=self, d=result["result"])

    async def set_my_default_administrator_rights(
        self: "tgram.TgBot",
        rights: ChatAdministratorRights = None,
        for_channels: bool = None,
    ) -> bool:
        """
        Use this method to change the default administrator rights requested by the bot
        when it's added as an administrator to groups or channels.
        These rights will be suggested to users, but they are are free to modify
        the list before adding the bot.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setmydefaultadministratorrights

        :param rights: A JSON-serialized object describing new default administrator rights. If not specified,
            the default administrator rights will be cleared.
        :type rights: :class:`tgram.types.ChatAdministratorRights`

        :param for_channels: Pass True to change the default administrator rights of the bot in channels.
            Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.
        :type for_channels: :obj:`bool`

        :return: True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setMyDefaultAdministratorRights",
            rights=rights,
            for_channels=for_channels,
        )
        return result["result"]

    async def get_my_default_administrator_rights(
        self: "tgram.TgBot", for_channels: bool = None
    ) -> ChatAdministratorRights:
        """
        Use this method to get the current default administrator rights of the bot.
        Returns ChatAdministratorRights on success.

        Telegram documentation: https://core.telegram.org/bots/api#getmydefaultadministratorrights

        :param for_channels: Pass True to get the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be returned.
        :type for_channels: :obj:`bool`

        :return: Returns ChatAdministratorRights on success.
        :rtype: :class:`tgram.types.ChatAdministratorRights`
        """

        result = await self._send_request(
            "getMyDefaultAdministratorRights",
            for_channels=for_channels,
        )
        return ChatAdministratorRights._parse(me=self, d=result["result"])

    async def edit_message_text(
        self: "tgram.TgBot",
        text: str,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageText",
            text=text,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            parse_mode=parse_mode or self.parse_mode,
            entities=entities,
            link_preview_options=link_preview_options or self.link_preview_options,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def edit_message_caption(
        self: "tgram.TgBot",
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageCaption",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def edit_message_media(
        self: "tgram.TgBot",
        media: InputMedia,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageMedia",
            media=media,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def edit_message_live_location(
        self: "tgram.TgBot",
        latitude: float,
        longitude: float,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        live_period: int = None,
        horizontal_accuracy: float = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageLiveLocation",
            latitude=latitude,
            longitude=longitude,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            live_period=live_period,
            horizontal_accuracy=horizontal_accuracy,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def stop_message_live_location(
        self: "tgram.TgBot",
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "stopMessageLiveLocation",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def edit_message_reply_markup(
        self: "tgram.TgBot",
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageReplyMarkup",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def stop_poll(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        business_connection_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Poll:
        """
        Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.

        Telegram documentation: https://core.telegram.org/bots/api#stoppoll

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :type chat_id: :obj:`int` | :obj:`str`

        :param message_id: Identifier of the original message with the poll
        :type message_id: :obj:`int`

        :param reply_markup: A JSON-serialized object for a new message markup.
        :type reply_markup: :obj:`InlineKeyboardMarkup`

        :param business_connection_id: Identifier of the business connection to send the message through
        :type business_connection_id: :obj:`str`

        :return: On success, the stopped Poll is returned.
        :rtype: :obj:`tgram.types.Poll`
        """

        result = await self._send_request(
            "stopPoll",
            chat_id=chat_id,
            message_id=message_id,
            business_connection_id=business_connection_id,
            reply_markup=reply_markup,
        )
        return Poll._parse(me=self, d=result["result"])

    async def delete_message(
        self: "tgram.TgBot", chat_id: Union[int, str], message_id: int
    ) -> bool:
        """
        Use this method to delete a message, including service messages, with the following limitations:
        - A message can only be deleted if it was sent less than 48 hours ago.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted can_post_messages permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletemessage

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Identifier of the message to delete
        :type message_id: :obj:`int`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteMessage",
            chat_id=chat_id,
            message_id=message_id,
        )
        return result["result"]

    async def delete_messages(
        self: "tgram.TgBot", chat_id: Union[int, str], message_ids: List[int]
    ) -> bool:
        """
        Use this method to delete multiple messages simultaneously.
        If some of the specified messages can't be found, they are skipped. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletemessages

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_ids: Identifiers of the messages to be deleted
        :type message_ids: :obj:`list` of :obj:`int`

        :return: Returns True on success.

        """

        result = await self._send_request(
            "deleteMessages",
            chat_id=chat_id,
            message_ids=message_ids,
        )
        return result["result"]

    async def send_sticker(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        sticker: Union[Path, bytes, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers.
        On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendsticker

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param sticker: Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL
            as a String for Telegram to get a .webp file from the Internet, or upload a new one using multipart/form-data.
        :type sticker: :obj:`str` or :class:`tgram.types.InputFile`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param disable_notification: to disable the notification
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param data: function typo miss compatibility: do not use it
        :type data: :obj:`str`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param emoji: Emoji associated with the sticker; only for just uploaded stickers
        :type emoji: :obj:`str`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Unique identifier for the target business connection
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier for the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendSticker",
            chat_id=chat_id,
            sticker=sticker,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            emoji=emoji,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def get_sticker_set(self: "tgram.TgBot", name: str) -> StickerSet:
        """
        Use this method to get a sticker set. On success, a StickerSet object is returned.

        Telegram documentation: https://core.telegram.org/bots/api#getstickerset

        :param name: Sticker set name
        :type name: :obj:`str`

        :return: On success, a StickerSet object is returned.
        :rtype: :class:`tgram.types.StickerSet`
        """

        result = await self._send_request(
            "getStickerSet",
            name=name,
        )
        return StickerSet._parse(me=self, d=result["result"])

    async def get_custom_emoji_stickers(
        self: "tgram.TgBot", custom_emoji_ids: List[str]
    ) -> List[Sticker]:
        """
        Use this method to get information about custom emoji stickers by their identifiers.
        Returns an Array of Sticker objects.

        :param custom_emoji_ids: List of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.
        :type custom_emoji_ids: :obj:`list` of :obj:`str`

        :return: Returns an Array of Sticker objects.
        :rtype: :obj:`list` of :class:`tgram.types.Sticker`
        """

        result = await self._send_request(
            "getCustomEmojiStickers",
            custom_emoji_ids=custom_emoji_ids,
        )
        return [Sticker._parse(me=self, d=i) for i in result["result"]]

    async def upload_sticker_file(
        self: "tgram.TgBot",
        user_id: int,
        sticker: Union[Path, bytes, str],
        sticker_format: str,
    ) -> File:
        """
        Use this method to upload a .png file with a sticker for later use in createNewStickerSet and addStickerToSet
        methods (can be used multiple times). Returns the uploaded File on success.

        Telegram documentation: https://core.telegram.org/bots/api#uploadstickerfile

        :param user_id: User identifier of sticker set owner
        :type user_id: :obj:`int`

        :param png_sticker: DEPRECATED: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px,
            and either width or height must be exactly 512px.
        :type png_sticker: :obj:`filelike object`

        :param sticker: A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format.
            See https://core.telegram.org/stickers for technical requirements. More information on Sending Files »
        :type sticker: :class:`tgram.types.InputFile`

        :param sticker_format: One of "static", "animated", "video".
        :type sticker_format: :obj:`str`

        :return: On success, the sent file is returned.
        :rtype: :class:`tgram.types.File`
        """

        result = await self._send_request(
            "uploadStickerFile",
            user_id=user_id,
            sticker=sticker,
            sticker_format=sticker_format,
        )
        return File._parse(me=self, d=result["result"])

    async def create_new_sticker_set(
        self: "tgram.TgBot",
        user_id: int,
        name: str,
        title: str,
        stickers: List[InputSticker],
        sticker_type: str = None,
        needs_repainting: bool = None,
    ) -> bool:
        """
        Use this method to create new sticker set owned by a user.
        The bot will be able to edit the created sticker set.
        Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#createnewstickerset

        .. note::
            Fields *_sticker are deprecated, pass a list of stickers to stickers parameter instead.

        :param user_id: User identifier of created sticker set owner
        :type user_id: :obj:`int`

        :param name: Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only English letters,
            digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>".
            <bot_username> is case insensitive. 1-64 characters.
        :type name: :obj:`str`

        :param title: Sticker set title, 1-64 characters
        :type title: :obj:`str`

        :param emojis: One or more emoji corresponding to the sticker
        :type emojis: :obj:`str`

        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width
            or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL
            as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        :type png_sticker: :obj:`str`

        :param tgs_sticker: TGS animation with the sticker, uploaded using multipart/form-data.
        :type tgs_sticker: :obj:`str`

        :param webm_sticker: WebM animation with the sticker, uploaded using multipart/form-data.
        :type webm_sticker: :obj:`str`

        :param contains_masks: Pass True, if a set of mask stickers should be created. Deprecated since Bot API 6.2,
            use sticker_type instead.
        :type contains_masks: :obj:`bool`

        :param sticker_type: Type of stickers in the set, pass “regular”, “mask”, or “custom_emoji”. By default, a regular sticker set is created.
        :type sticker_type: :obj:`str`

        :param mask_position: A JSON-serialized object for position where the mask should be placed on faces
        :type mask_position: :class:`tgram.types.MaskPosition`

        :param needs_repainting: Pass True if stickers in the sticker set must be repainted to the color of text when used in messages,
            the accent color if used as emoji status, white on chat photos, or another appropriate color based on context;
            for custom emoji sticker sets only
        :type needs_repainting: :obj:`bool`

        :param stickers: List of stickers to be added to the set
        :type stickers: :obj:`list` of :class:`tgram.types.InputSticker`

        :param sticker_format: deprecated
        :type sticker_format: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "createNewStickerSet",
            user_id=user_id,
            name=name,
            title=title,
            stickers=stickers,
            sticker_type=sticker_type,
            needs_repainting=needs_repainting,
        )
        return result["result"]

    async def add_sticker_to_set(
        self: "tgram.TgBot", user_id: int, name: str, sticker: InputSticker
    ) -> bool:
        """
        Use this method to add a new sticker to a set created by the bot.
        The format of the added sticker must match the format of the other stickers in the set.
        Emoji sticker sets can have up to 200 stickers. Animated and video sticker sets can have up to 50 stickers.
        Static sticker sets can have up to 120 stickers.
        Returns True on success.

        .. note::
            **_sticker, mask_position, emojis parameters are deprecated, use stickers instead

        Telegram documentation: https://core.telegram.org/bots/api#addstickertoset

        :param user_id: User identifier of created sticker set owner
        :type user_id: :obj:`int`

        :param name: Sticker set name
        :type name: :obj:`str`

        :param emojis: One or more emoji corresponding to the sticker
        :type emojis: :obj:`str`

        :param png_sticker: PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either
            width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers,
            pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        :type png_sticker: :obj:`str` or :obj:`filelike object`

        :param tgs_sticker: TGS animation with the sticker, uploaded using multipart/form-data.
        :type tgs_sticker: :obj:`str` or :obj:`filelike object`

        :param webm_sticker: WebM animation with the sticker, uploaded using multipart/form-data.
        :type webm_sticker: :obj:`str` or :obj:`filelike object`

        :param mask_position: A JSON-serialized object for position where the mask should be placed on faces
        :type mask_position: :class:`tgram.types.MaskPosition`

        :param sticker: A JSON-serialized object for sticker to be added to the sticker set
        :type sticker: :class:`tgram.types.InputSticker`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "addStickerToSet",
            user_id=user_id,
            name=name,
            sticker=sticker,
        )
        return result["result"]

    async def set_sticker_position_in_set(
        self: "tgram.TgBot", sticker: str, position: int
    ) -> bool:
        """
        Use this method to move a sticker in a set created by the bot to a specific position . Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setstickerpositioninset

        :param sticker: File identifier of the sticker
        :type sticker: :obj:`str`

        :param position: New sticker position in the set, zero-based
        :type position: :obj:`int`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setStickerPositionInSet",
            sticker=sticker,
            position=position,
        )
        return result["result"]

    async def delete_sticker_from_set(self: "tgram.TgBot", sticker: str) -> bool:
        """
        Use this method to delete a sticker from a set created by the bot. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#deletestickerfromset

        :param sticker: File identifier of the sticker
        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteStickerFromSet",
            sticker=sticker,
        )
        return result["result"]

    async def replace_sticker_in_set(
        self: "tgram.TgBot",
        user_id: int,
        name: str,
        old_sticker: str,
        sticker: InputSticker,
    ) -> bool:
        """
        Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling deleteStickerFromSet, then addStickerToSet,
            then setStickerPositionInSet. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#replaceStickerInSet

        :param user_id: User identifier of the sticker set owner
        :type user_id: :obj:`int`

        :param name: Sticker set name
        :type name: :obj:`str`

        :param old_sticker: File identifier of the replaced sticker
        :type old_sticker: :obj:`str`

        :param sticker: A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.
        :type sticker: :class:`tgram.types.InputSticker`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "replaceStickerInSet",
            user_id=user_id,
            name=name,
            old_sticker=old_sticker,
            sticker=sticker,
        )
        return result["result"]

    async def set_sticker_emoji_list(
        self: "tgram.TgBot", sticker: str, emoji_list: List[str]
    ) -> bool:
        """
        Use this method to set the emoji list of a sticker set.
        Returns True on success.

        :param name: Sticker set name
        :type name: :obj:`str`

        :param emoji_list: List of emojis
        :type emoji_list: :obj:`list` of :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setStickerEmojiList",
            sticker=sticker,
            emoji_list=emoji_list,
        )
        return result["result"]

    async def set_sticker_keywords(
        self: "tgram.TgBot", sticker: str, keywords: List[str] = None
    ) -> bool:
        """
        Use this method to change search keywords assigned to a regular or custom emoji sticker.
        The sticker must belong to a sticker set created by the bot.
        Returns True on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`

        :param keywords: A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters
        :type keywords: :obj:`list` of :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setStickerKeywords",
            sticker=sticker,
            keywords=keywords,
        )
        return result["result"]

    async def set_sticker_mask_position(
        self: "tgram.TgBot", sticker: str, mask_position: MaskPosition = None
    ) -> bool:
        """
        Use this method to change the mask position of a mask sticker.
        The sticker must belong to a sticker set that was created by the bot.
        Returns True on success.

        :param sticker: File identifier of the sticker.
        :type sticker: :obj:`str`

        :param mask_position: A JSON-serialized object for position where the mask should be placed on faces.
        :type mask_position: :class:`tgram.types.MaskPosition`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setStickerMaskPosition",
            sticker=sticker,
            mask_position=mask_position,
        )
        return result["result"]

    async def set_sticker_set_title(self: "tgram.TgBot", name: str, title: str) -> bool:
        """
        Use this method to set the title of a created sticker set.
        Returns True on success.

        :param name: Sticker set name
        :type name: :obj:`str`

        :param title: New sticker set title
        :type title: :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setStickerSetTitle",
            name=name,
            title=title,
        )
        return result["result"]

    async def set_sticker_set_thumbnail(
        self: "tgram.TgBot",
        name: str,
        user_id: int,
        format: str,
        thumbnail: Union[Path, bytes, str] = None,
    ) -> bool:
        """
        Use this method to set the thumbnail of a sticker set.
        Animated thumbnails can be set for animated sticker sets only. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setstickersetthumbnail

        :param name: Sticker set name
        :type name: :obj:`str`

        :param user_id: User identifier
        :type user_id: :obj:`int`

        :param thumbnail: A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a .TGS animation
            with a thumbnail up to 32 kilobytes in size (see https://core.telegram.org/stickers#animated-sticker-requirements for animated sticker technical requirements),
            or a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-sticker-requirements for video sticker technical
            requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from
            the Internet, or upload a new one using multipart/form-data. More information on Sending Files ». Animated and video sticker set thumbnails can't be uploaded via
            HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.
        :type thumbnail: :obj:`filelike object`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setStickerSetThumbnail",
            name=name,
            user_id=user_id,
            format=format,
            thumbnail=get_file_path(thumbnail),
        )
        return result["result"]

    async def set_custom_emoji_sticker_set_thumbnail(
        self: "tgram.TgBot", name: str, custom_emoji_id: str = None
    ) -> bool:
        """
        Use this method to set the thumbnail of a custom emoji sticker set.
        Returns True on success.

        :param name: Sticker set name
        :type name: :obj:`str`

        :param custom_emoji_id: Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.
        :type custom_emoji_id: :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "setCustomEmojiStickerSetThumbnail",
            name=name,
            custom_emoji_id=custom_emoji_id,
        )
        return result["result"]

    async def delete_sticker_set(self: "tgram.TgBot", name: str) -> bool:
        """
        Use this method to delete a sticker set. Returns True on success.

        :param name: Sticker set name
        :type name: :obj:`str`

        :return: Returns True on success.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "deleteStickerSet",
            name=name,
        )
        return result["result"]

    async def answer_inline_query(
        self: "tgram.TgBot",
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        button: InlineQueryResultsButton = None,
    ) -> bool:
        """
        Use this method to send answers to an inline query. On success, True is returned.
        No more than 50 results per query are allowed.

        Telegram documentation: https://core.telegram.org/bots/api#answerinlinequery

        :param inline_query_id: Unique identifier for the answered query
        :type inline_query_id: :obj:`str`

        :param results: Array of results for the inline query
        :type results: :obj:`list` of :obj:`tgram.types.InlineQueryResult`

        :param cache_time: The maximum amount of time in seconds that the result of the inline query
            may be cached on the server.
        :type cache_time: :obj:`int`

        :param is_personal: Pass True, if results may be cached on the server side only for
            the user that sent the query.
        :type is_personal: :obj:`bool`

        :param next_offset: Pass the offset that a client should send in the next query with the same text
            to receive more results.
        :type next_offset: :obj:`str`

        :param switch_pm_parameter: Deep-linking parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters,
            only A-Z, a-z, 0-9, _ and - are allowed.
            Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly.
            To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a
            private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline
            button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.
        :type switch_pm_parameter: :obj:`str`

        :param switch_pm_text: Parameter for the start message sent to the bot when user presses the switch button
        :type switch_pm_text: :obj:`str`

        :param button: A JSON-serialized object describing a button to be shown above inline query results
        :type button: :obj:`tgram.types.InlineQueryResultsButton`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "answerInlineQuery",
            inline_query_id=inline_query_id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            button=button,
        )
        return result["result"]

    async def answer_web_app_query(
        self: "tgram.TgBot", web_app_query_id: str, result: InlineQueryResult
    ) -> SentWebAppMessage:
        """
        Use this method to set the result of an interaction with a Web App and
        send a corresponding message on behalf of the user to the chat from which
        the query originated.
        On success, a SentWebAppMessage object is returned.

        Telegram Documentation: https://core.telegram.org/bots/api#answerwebappquery

        :param web_app_query_id: Unique identifier for the query to be answered
        :type web_app_query_id: :obj:`str`

        :param result: A JSON-serialized object describing the message to be sent
        :type result: :class:`tgram.types.InlineQueryResultBase`

        :return: On success, a SentWebAppMessage object is returned.
        :rtype: :class:`tgram.types.SentWebAppMessage`
        """

        result = await self._send_request(
            "answerWebAppQuery",
            web_app_query_id=web_app_query_id,
            result=result,
        )
        return SentWebAppMessage._parse(me=self, d=result["result"])

    async def send_invoice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        message_thread_id: int = None,
        provider_token: str = None,
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        start_parameter: str = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        """
        Sends invoice.

        Telegram documentation: https://core.telegram.org/bots/api#sendinvoice

        :param chat_id: Unique identifier for the target private chat
        :type chat_id: :obj:`int` or :obj:`str`

        :param title: Product name, 1-32 characters
        :type title: :obj:`str`

        :param description: Product description, 1-255 characters
        :type description: :obj:`str`

        :param invoice_payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
            use for your internal processes.
        :type invoice_payload: :obj:`str`

        :param provider_token: Payments provider token, obtained via @Botfather; Pass None to omit the parameter
            to use "XTR" currency
        :type provider_token: :obj:`str`

        :param currency: Three-letter ISO 4217 currency code,
            see https://core.telegram.org/bots/payments#supported-currencies
        :type currency: :obj:`str`

        :param prices: Price breakdown, a list of components
            (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
        :type prices: List[:obj:`tgram.types.LabeledPrice`]

        :param start_parameter: Unique deep-linking parameter that can be used to generate this invoice
            when used as a start parameter
        :type start_parameter: :obj:`str`

        :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods
            or a marketing image for a service. People like it better when they see what they are paying for.
        :type photo_url: :obj:`str`

        :param photo_size: Photo size in bytes
        :type photo_size: :obj:`int`

        :param photo_width: Photo width
        :type photo_width: :obj:`int`

        :param photo_height: Photo height
        :type photo_height: :obj:`int`

        :param need_name: Pass True, if you require the user's full name to complete the order
        :type need_name: :obj:`bool`

        :param need_phone_number: Pass True, if you require the user's phone number to complete the order
        :type need_phone_number: :obj:`bool`

        :param need_email: Pass True, if you require the user's email to complete the order
        :type need_email: :obj:`bool`

        :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
        :type need_shipping_address: :obj:`bool`

        :param is_flexible: Pass True, if the final price depends on the shipping method
        :type is_flexible: :obj:`bool`

        :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
        :type send_phone_number_to_provider: :obj:`bool`

        :param send_email_to_provider: Pass True, if user's email address should be sent to provider
        :type send_email_to_provider: :obj:`bool`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: A JSON-serialized object for an inline keyboard. If empty,
            one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button
        :type reply_markup: :obj:`str`

        :param provider_data: A JSON-serialized data about the invoice, which will be shared with the payment provider.
            A detailed description of required fields should be provided by the payment provider.
        :type provider_data: :obj:`str`

        :param timeout: Timeout of a request, defaults to None
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param max_tip_amount: The maximum accepted amount for tips in the smallest units of the currency
        :type max_tip_amount: :obj:`int`

        :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the smallest
            units of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip
            amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
        :type suggested_tip_amounts: :obj:`list` of :obj:`int`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: The identifier of a message thread, in which the invoice message will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param message_effect_id: The identifier of a message effect to be applied to the message
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :obj:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendInvoice",
            chat_id=chat_id,
            title=title,
            description=description,
            payload=payload,
            currency=currency,
            prices=prices,
            message_thread_id=message_thread_id,
            provider_token=provider_token,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            start_parameter=start_parameter,
            provider_data=provider_data,
            photo_url=photo_url,
            photo_size=photo_size,
            photo_width=photo_width,
            photo_height=photo_height,
            need_name=need_name,
            need_phone_number=need_phone_number,
            need_email=need_email,
            need_shipping_address=need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider,
            is_flexible=is_flexible,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def create_invoice_link(
        self: "tgram.TgBot",
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        provider_token: str = None,
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
    ) -> str:
        """
        Use this method to create a link for an invoice.
        Returns the created invoice link as String on success.

        Telegram documentation:
        https://core.telegram.org/bots/api#createinvoicelink

        :param title: Product name, 1-32 characters
        :type title: :obj:`str`

        :param description: Product description, 1-255 characters
        :type description: :obj:`str`

        :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
            use for your internal processes.
        :type payload: :obj:`str`

        :param provider_token: Payments provider token, obtained via @Botfather; Pass None to omit the parameter
            to use "XTR" currency
        :type provider_token: :obj:`str`

        :param currency: Three-letter ISO 4217 currency code,
            see https://core.telegram.org/bots/payments#supported-currencies
        :type currency: :obj:`str`

        :param prices: Price breakdown, a list of components
            (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
        :type prices: :obj:`list` of :obj:`tgram.types.LabeledPrice`

        :param max_tip_amount: The maximum accepted amount for tips in the smallest units of the currency
        :type max_tip_amount: :obj:`int`

        :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the smallest
            units of the currency.  At most 4 suggested tip amounts can be specified. The suggested tip
            amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
        :type suggested_tip_amounts: :obj:`list` of :obj:`int`

        :param provider_data: A JSON-serialized data about the invoice, which will be shared with the payment provider.
            A detailed description of required fields should be provided by the payment provider.
        :type provider_data: :obj:`str`

        :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods
            or a photo of the invoice. People like it better when they see a photo of what they are paying for.
        :type photo_url: :obj:`str`

        :param photo_size: Photo size in bytes
        :type photo_size: :obj:`int`

        :param photo_width: Photo width
        :type photo_width: :obj:`int`

        :param photo_height: Photo height
        :type photo_height: :obj:`int`

        :param need_name: Pass True, if you require the user's full name to complete the order
        :type need_name: :obj:`bool`

        :param need_phone_number: Pass True, if you require the user's phone number to complete the order
        :type need_phone_number: :obj:`bool`

        :param need_email: Pass True, if you require the user's email to complete the order
        :type need_email: :obj:`bool`

        :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
        :type need_shipping_address: :obj:`bool`

        :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
        :type send_phone_number_to_provider: :obj:`bool`

        :param send_email_to_provider: Pass True, if user's email address should be sent to provider
        :type send_email_to_provider: :obj:`bool`

        :param is_flexible: Pass True, if the final price depends on the shipping method
        :type is_flexible: :obj:`bool`

        :return: Created invoice link as String on success.
        :rtype: :obj:`str`
        """

        result = await self._send_request(
            "createInvoiceLink",
            title=title,
            description=description,
            payload=payload,
            currency=currency,
            prices=prices,
            provider_token=provider_token,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            provider_data=provider_data,
            photo_url=photo_url,
            photo_size=photo_size,
            photo_width=photo_width,
            photo_height=photo_height,
            need_name=need_name,
            need_phone_number=need_phone_number,
            need_email=need_email,
            need_shipping_address=need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider,
            is_flexible=is_flexible,
        )
        return result["result"]

    async def answer_shipping_query(
        self: "tgram.TgBot",
        shipping_query_id: str,
        ok: bool,
        shipping_options: List[ShippingOption] = None,
        error_message: str = None,
    ) -> bool:
        """
        Asks for an answer to a shipping question.

        Telegram documentation: https://core.telegram.org/bots/api#answershippingquery

        :param shipping_query_id: Unique identifier for the query to be answered
        :type shipping_query_id: :obj:`str`

        :param ok: Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
        :type ok: :obj:`bool`

        :param shipping_options: Required if ok is True. A JSON-serialized array of available shipping options.
        :type shipping_options: :obj:`list` of :obj:`ShippingOption`

        :param error_message: Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order
            (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.
        :type error_message: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "answerShippingQuery",
            shipping_query_id=shipping_query_id,
            ok=ok,
            shipping_options=shipping_options,
            error_message=error_message,
        )
        return result["result"]

    async def answer_pre_checkout_query(
        self: "tgram.TgBot",
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str = None,
    ) -> bool:
        """
        Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the
        field pre_checkout_query. Use this method to respond to such pre-checkout queries.
        On success, True is returned.

        .. note::
            The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

        Telegram documentation: https://core.telegram.org/bots/api#answerprecheckoutquery

        :param pre_checkout_query_id: Unique identifier for the query to be answered
        :type pre_checkout_query_id: :obj:`int`

        :param ok: Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.
        :type ok: :obj:`bool`

        :param error_message: Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout
            (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different
            color or garment!"). Telegram will display this message to the user.
        :type error_message: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "answerPreCheckoutQuery",
            pre_checkout_query_id=pre_checkout_query_id,
            ok=ok,
            error_message=error_message,
        )
        return result["result"]

    async def get_star_transactions(
        self: "tgram.TgBot", offset: int = None, limit: int = None
    ) -> StarTransactions:
        """
        Returns the bot's Telegram Star transactions in chronological order.

        Telegram documentation: https://core.telegram.org/bots/api#getstartransactions

        :param offset: Number of transactions to skip in the response
        :type offset: :obj:`int`

        :param limit: The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :type limit: :obj:`int`

        :return: On success, returns a StarTransactions object.
        :rtype: :obj:`tgram.types.StarTransactions`
        """

        result = await self._send_request(
            "getStarTransactions",
            offset=offset,
            limit=limit,
        )
        return StarTransactions._parse(me=self, d=result["result"])

    async def refund_star_payment(
        self: "tgram.TgBot", user_id: int, telegram_payment_charge_id: str
    ) -> bool:
        """
        Refunds a successful payment in Telegram Stars. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#refundstarpayment

        :param user_id: Identifier of the user whose payment will be refunded
        :type user_id: :obj:`int`

        :param telegram_payment_charge_id: Telegram payment identifier
        :type telegram_payment_charge_id: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self._send_request(
            "refundStarPayment",
            user_id=user_id,
            telegram_payment_charge_id=telegram_payment_charge_id,
        )
        return result["result"]

    async def set_passport_data_errors(
        self: "tgram.TgBot", user_id: int, errors: List[PassportElementError]
    ) -> bool:
        result = await self._send_request(
            "setPassportDataErrors",
            user_id=user_id,
            errors=errors,
        )
        return result["result"]

    async def send_game(
        self: "tgram.TgBot",
        chat_id: int,
        game_short_name: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        """
        Used to send the game.

        Telegram documentation: https://core.telegram.org/bots/api#sendgame

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param game_short_name: Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather.
        :type game_short_name: :obj:`str`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type reply_markup: :obj:`InlineKeyboardMarkup` or :obj:`ReplyKeyboardMarkup` or :obj:`ReplyKeyboardRemove` or :obj:`ForceReply`

        :param timeout: Timeout in seconds for waiting for a response from the bot.
        :type timeout: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if one of the specified replied-to messages is not found.
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Pass True, if content of the message needs to be protected from being viewed by the bot.
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of the thread to which the message will be sent.
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of the business connection.
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Identifier of the message effect.
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :obj:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendGame",
            chat_id=chat_id,
            game_short_name=game_short_name,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def set_game_score(
        self: "tgram.TgBot",
        user_id: int,
        score: int,
        force: bool = None,
        disable_edit_message: bool = None,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "setGameScore",
            user_id=user_id,
            score=score,
            force=force,
            disable_edit_message=disable_edit_message,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def get_game_high_scores(
        self: "tgram.TgBot",
        user_id: int,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> List[GameHighScore]:
        """
        Use this method to get data for high score tables. Will return the score of the specified user and several of
        their neighbors in a game. On success, returns an Array of GameHighScore objects.

        This method will currently return scores for the target user, plus two of their closest neighbors on each side.
        Will also return the top three users if the user and their neighbors are not among them.
        Please note that this behavior is subject to change.

        Telegram documentation: https://core.telegram.org/bots/api#getgamehighscores

        :param user_id: User identifier
        :type user_id: :obj:`int`

        :param chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param message_id: Required if inline_message_id is not specified. Identifier of the sent message
        :type message_id: :obj:`int`

        :param inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
        :type inline_message_id: :obj:`str`

        :return: On success, returns an Array of GameHighScore objects.
        :rtype: List[types.GameHighScore]
        """

        result = await self._send_request(
            "getGameHighScores",
            user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )
        return [GameHighScore._parse(me=self, d=i) for i in result["result"]]

    async def schedule_job(
        self: "tgram.TgBot", after: int, func: Callable, **kwargs
    ) -> asyncio.Task:
        if after < 0:
            raise ValueError("You can't do job in the past.")

        async def task():
            logger.warn("New scheduled job started, it will be done after: %s", after)
            await asyncio.sleep(after)
            try:
                if asyncio.iscoroutinefunction(func):
                    await func(**kwargs)
                    logger.info("Job %s is finished", func.__name__)
                else:
                    await self.loop.run_in_executor(
                        self.executor, lambda: func(**kwargs)
                    )
                    logger.info("Job %s is finished", func.__name__)
            except Exception as e:
                logger.exception(e)

        return asyncio.create_task(task())

    async def ask(
        self: "tgram.TgBot",
        update_type: str,
        next_step: Callable,
        data: dict = None,
        cancel: Callable = None,
        filters: "tgram.filters.Filter" = None,
    ) -> None:
        return self._listen_handlers.append(
            Listener(
                update_type=update_type,
                next_step=next_step,
                data=data if data is not None else {},
                cancel=cancel,
                filters=filters or tgram.filters.all,
            )
        )

    async def send_media_from_file_id(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        file_id: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        file = await self.get_file(file_id)
        file_type = file.file_path.split("/")[0][:-1].title()

        result = await self._send_request(
            f"send{file_type}",
            **{
                "chat_id": chat_id,
                file_type.lower(): file_id,
                "business_connection_id": business_connection_id,
                "message_thread_id": message_thread_id,
                "caption": caption,
                "parse_mode": parse_mode or self.parse_mode,
                "caption_entities": caption_entities,
                "show_caption_above_media": show_caption_above_media,
                "disable_notification": disable_notification,
                "protect_content": protect_content
                if protect_content is not None
                else self.protect_content,
                "message_effect_id": message_effect_id,
                "reply_parameters": reply_parameters,
                "reply_markup": reply_markup,
            },
        )

        return Message._parse(me=self, d=result["result"])
