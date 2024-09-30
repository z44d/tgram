from tgram import TgBot
from tgram.types import CallbackQuery


@TgBot.on_callback_query()
async def on_c(bot: TgBot, query: CallbackQuery) -> bool:
    return await query.answer("Hi.", show_alert=True)
