import logging

from tgram import TgBot
from tgram.types import (
    InlineQuery,
    ChosenInlineResult,
    CallbackQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from typing import Dict, Tuple

bot = TgBot("API_TOKEN_HERE")
logging.basicConfig(level=logging.INFO)

db: Dict[str, Tuple[str, int, str]] = {}


@bot.on_inline_query()
async def on_inline(b: TgBot, i: InlineQuery) -> bool:
    query = i.query
    results = [
        InlineQueryResultArticle(
            "Write the whisper then the username",
            InputTextMessageContent(
                f"For example: `@{b.me.username} Hi @DevZaid`", parse_mode="markdown"
            ),
        )
    ]

    if not query or "@" not in query:
        return await i.answer(results, cache_time=0)
    else:
        username = query.split("@")[-1].strip().lower()

        return await i.answer(
            [
                InlineQueryResultArticle(
                    f"Send whisper for ( @{username} )",
                    InputTextMessageContent(f"This whisper for ( @{username} )"),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Show whisper 📫", callback_data="uwu")]]
                    ),
                )
            ],
            cache_time=0,
        )


# https://core.telegram.org/bots/inline#collecting-feedback
@bot.on_chosen_inline_result()
async def on_chosen(b: TgBot, c: ChosenInlineResult) -> None:
    db.update(
        {
            c.inline_message_id: (
                c.from_user.id,
                c.query.split("@")[-1].strip().lower(),
                c.query.replace("@" + c.query.split("@")[-1].strip().lower(), ""),
            ),
        }
    )


@bot.on_callback_query()
async def on_callback_query(b: TgBot, c: CallbackQuery) -> bool:
    data = db.get(c.inline_message_id)
    allowed = data[0], data[1]

    if c.from_user.id not in allowed or (
        c.from_user.username and c.from_user.username.lower() not in allowed
    ):
        return await c.answer("This whisper isn't for you", show_alert=True)

    await c.answer(data[-1][:200], show_alert=True)
    if c.from_user.username and c.from_user.username.lower() == allowed[-1]:
        try:
            await b.edit_message_reply_markup(
                inline_message_id=c.inline_message_id,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Show whisper 📭", callback_data="uwu")]]
                ),
            )
        except Exception:
            return


import asyncio

asyncio.run(bot.run())
