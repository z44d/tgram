import logging

from tgram import TgBot, filters
from tgram.types import (
    KeyboardButtonRequestChat,
    KeyboardButtonRequestUsers,
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

bot = TgBot("API_TOKEN_HERE", parse_mode="Markdown")

logging.basicConfig(level=logging.INFO)


@bot.on_message(filters.regex("^/start$") & filters.private)
async def on_start_message(_, m: Message) -> Message:
    return await m.reply_text(
        f"Hi, {m.from_user.mention.markdown}",
        reply_markup=ReplyKeyboardMarkup(
            [
                [
                    KeyboardButton(
                        "Channel",
                        request_chat=KeyboardButtonRequestChat(chat_is_channel=True),
                    ),
                    KeyboardButton(
                        "Group",
                        request_chat=KeyboardButtonRequestChat(chat_is_channel=False),
                    ),
                ],
                [
                    KeyboardButton(
                        "User",
                        request_users=KeyboardButtonRequestUsers(user_is_bot=False),
                    ),
                    KeyboardButton(
                        "Bot",
                        request_users=KeyboardButtonRequestUsers(user_is_bot=True),
                    ),
                ],
            ],
            resize_keyboard=True,
            input_field_placeholder="Choose chat type",
        ),
    )


@bot.on_message(filters.chat_shared | filters.users_shared)
async def get_id(_, m: Message) -> Message:
    if m.chat_shared:
        text = f"Chat ID: `{m.chat_shared.chat_id}`"
    else:
        text = (
            "Users ID: `"
            + " ".join([str(i.user_id) for i in m.users_shared.users])
            + "`"
        )

    return await m.reply_text(text)


import asyncio

asyncio.run(bot.run())
