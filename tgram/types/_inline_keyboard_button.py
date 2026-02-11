import tgram
from .type_ import Type_

from typing import Optional


class InlineKeyboardButton(Type_):
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    Telegram Documentation: https://core.telegram.org/bots/api#inlinekeyboardbutton

    :param text: Label text on the button
    :type text: :obj:`str`

    :param url: Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be
        used to mention a user by their ID without using a username, if this is allowed by their privacy settings.
    :type url: :obj:`str`

    :param callback_data: Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    :type callback_data: :obj:`str`

    :param web_app: Optional. Description of the Web App that will be launched when the user presses the button. The Web
        App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only
        in private chats between a user and the bot.
    :type web_app: :class:`tgram.types.WebAppInfo`

    :param login_url: Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for
        the Telegram Login Widget.
    :type login_url: :class:`tgram.types.LoginUrl`

    :param switch_inline_query: Optional. If set, pressing the button will prompt the user to select one of their chats,
        open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which
        case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline
        mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions - in
        this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    :type switch_inline_query: :obj:`str`

    :param switch_inline_query_current_chat: Optional. If set, pressing the button will insert the bot's username
        and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username
        will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting
        something from multiple options.
    :type switch_inline_query_current_chat: :obj:`str`

    :param switch_inline_query_chosen_chat: Optional. If set, pressing the button will prompt the user to select one of their chats of the
        specified type, open that chat and insert the bot's username and the specified inline query in the input field
    :type switch_inline_query_chosen_chat: :class:`tgram.types.SwitchInlineQueryChosenChat`

    :param copy_text: Optional. Description of the button that copies the specified text to the clipboard.
    :type copy_text: :class:`tgram.types.CopyTextButton`

    :param callback_game: Optional. Description of the game that will be launched when the user presses the
        button. NOTE: This type of button must always be the first button in the first row.
    :type callback_game: :class:`tgram.types.CallbackGame`

    :param pay: Optional. Specify True, to send a Pay button. NOTE: This type of button must always be the first button in
        the first row and can only be used in invoice messages.
    :type pay: :obj:`bool`

    :param icon_custom_emoji_id: Optional. Unique identifier of the custom emoji shown before the text of the button
    :type icon_custom_emoji_id: :obj:`str`

    :param style: Optional. Style of the button. Must be one of “danger”, “success”, or “primary”
    :type style: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.InlineKeyboardButton`
    """

    def __init__(
        self,
        text: "str" = None,
        callback_data: "str" = None,
        url: "str" = None,
        web_app: "tgram.types.WebAppInfo" = None,
        login_url: "tgram.types.LoginUrl" = None,
        switch_inline_query: "str" = None,
        switch_inline_query_current_chat: "str" = None,
        switch_inline_query_chosen_chat: "tgram.types.SwitchInlineQueryChosenChat" = None,
        copy_text: "tgram.types.CopyTextButton" = None,
        callback_game: "tgram.types.CallbackGame" = None,
        pay: "bool" = None,
        icon_custom_emoji_id: "str" = None,
        style: "str" = None,
        user_id: "int" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.text = text
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.copy_text = copy_text
        self.callback_game = callback_game
        self.pay = pay
        self.icon_custom_emoji_id = icon_custom_emoji_id
        self.style = style

        self.url = url or (f"tg://user?id={user_id}" if user_id is not None else None)

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.InlineKeyboardButton"]:
        return (
            InlineKeyboardButton(
                me=me,
                json=d,
                text=d.get("text"),
                url=d.get("url"),
                callback_data=d.get("callback_data"),
                web_app=tgram.types.WebAppInfo._parse(me=me, d=d.get("web_app")),
                login_url=tgram.types.LoginUrl._parse(me=me, d=d.get("login_url")),
                switch_inline_query=d.get("switch_inline_query"),
                switch_inline_query_current_chat=d.get(
                    "switch_inline_query_current_chat"
                ),
                switch_inline_query_chosen_chat=tgram.types.SwitchInlineQueryChosenChat._parse(
                    me=me, d=d.get("switch_inline_query_chosen_chat")
                ),
                copy_text=tgram.types.CopyTextButton._parse(
                    me=me, d=d.get("copy_text")
                ),
                callback_game=tgram.types.CallbackGame._parse(
                    me=me, d=d.get("callback_game")
                ),
                pay=d.get("pay"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
                style=d.get("style"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
