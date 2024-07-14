from tgram import TgBot, filters
from tgram.types import CallbackQuery


@TgBot.on_callback_query(filters.regex("^fine$"))
def callback(bot: TgBot, query: CallbackQuery) -> bool:
    return query.answer("Good to know!", show_alert=True)
