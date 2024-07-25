import tgram
from .type_ import Type_

from typing import List, Optional


class ReplyKeyboardMarkup(Type_):
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    .. code-block:: python3
        :caption: Example on creating ReplyKeyboardMarkup object

        from tgram.types import ReplyKeyboardMarkup, KeyboardButton

        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton('Text'))
        # or:
        markup.add('Text')

        # display this markup:
        bot.send_message(chat_id, 'Text', reply_markup=markup)

    Telegram Documentation: https://core.telegram.org/bots/api#replykeyboardmarkup

    :param keyboard: :obj:`list` of button rows, each represented by an :obj:`list` of
        :class:`tgram.types.KeyboardButton` objects
    :type keyboard: :obj:`list` of :obj:`list` of :class:`tgram.types.KeyboardButton`

    :param resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make
        the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is
        always of the same height as the app's standard keyboard.
    :type resize_keyboard: :obj:`bool`

    :param one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard
        will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can
        press a special button in the input field to see the custom keyboard again. Defaults to false.
    :type one_time_keyboard: :obj:`bool`

    :param input_field_placeholder: Optional. The placeholder to be shown in the input field when the keyboard is
        active; 1-64 characters
    :type input_field_placeholder: :obj:`str`

    :param selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets:
        1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message
        in the same chat and forum topic, sender of the original message. Example: A user requests to change the bot's
        language, bot replies to the request with a keyboard to select the new language. Other users in the group don't
        see the keyboard.
    :type selective: :obj:`bool`

    :param is_persistent: Optional. Use this parameter if you want to show the keyboard to specific users only.
        Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a
        reply (has reply_to_message_id), sender of the original message.

        Example: A user requests to change the bot's language, bot replies to the request with a keyboard to
        select the new language. Other users in the group don't see the keyboard.

    :return: Instance of the class
    :rtype: :class:`tgram.types.ReplyKeyboardMarkup`
    """

    def __init__(
        self,
        keyboard: List[List["tgram.types.KeyboardButton"]] = None,
        is_persistent: "bool" = None,
        resize_keyboard: "bool" = None,
        one_time_keyboard: "bool" = None,
        input_field_placeholder: "str" = None,
        selective: "bool" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ReplyKeyboardMarkup"]:
        return (
            ReplyKeyboardMarkup(
                me=me,
                json=d,
                keyboard=[
                    [tgram.types.KeyboardButton._parse(me=me, d=x) for x in i]
                    for i in d.get("keyboard")
                ]
                if d.get("keyboard")
                else None,
                is_persistent=d.get("is_persistent"),
                resize_keyboard=d.get("resize_keyboard"),
                one_time_keyboard=d.get("one_time_keyboard"),
                input_field_placeholder=d.get("input_field_placeholder"),
                selective=d.get("selective"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
