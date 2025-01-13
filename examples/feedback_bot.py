import os
import asyncio

from tgram import TgBot, filters
from tgram.types import Message, ReplyParameters, ReactionTypeEmoji

from typing import Dict

BOT_TOKEN = os.environ.get("BOT_TOKEN", "API_TOKEN_HERE")
OWNER_ID = int(os.environ.get("OWNER_ID", 12345678))

bot = TgBot(BOT_TOKEN, parse_mode="Markdown")
cache: Dict[int, Message] = {}


@bot.on_message(filters.private & ~filters.user(OWNER_ID))
async def function_1(_, m: Message) -> Message:
    if m.text is not None and m.text.lower() == "/start":
        return await m.reply_text(
            (
                "Hello {mention}!\nSend your message and i will forward it to `{owner}`"
            ).format(mention=m.from_user.mention.markdown, owner=OWNER_ID)
        )
    else:
        forwarded_msg = await m.forward(OWNER_ID)
        cache.update({forwarded_msg.id: forwarded_msg})
        return await m.reply_text(
            f"Your message is sent to `{OWNER_ID}`, wait for the response."
        )


@bot.on_message(filters.reply & filters.private & filters.user(OWNER_ID))
async def function_2(_, m: Message) -> Message:
    if m.reply_to_message.id in cache:
        msg_data = cache[m.reply_to_message.id]
        await m.copy(
            msg_data.chat.id,
            m.caption,
            caption_entities=m.caption_entities,
            reply_parameters=ReplyParameters(
                msg_data.id, allow_sending_without_reply=True
            ),
        )
        return await bot.set_message_reaction(
            m.chat.id, m.id, [ReactionTypeEmoji("👍")]
        )


async def main():
    await bot.run_for_updates()


asyncio.run(main())
