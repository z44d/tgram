import logging
from tgram import types, TgBot, methods, filters

bot = TgBot("API_TOKEN_HERE")
me = bot.get_me()

logging.basicConfig(level=logging.INFO)

docs_url = "https://z44d.github.io/tgram/"
all_types = [
    i for i in filter(lambda x: not x.startswith("_") and not x.islower(), dir(types))
]
all_methods = [
    i for i in filter(lambda x: not x.startswith("_"), dir(methods.TelegramBotMethods))
]


@bot.on_message(filters.Filter(lambda m: m.chat.type == "private") & filters.text)
async def on_message(_, m: types.Message):
    return await bot.send_message(
        m.chat.id,
        (
            "Hi, {mention}, welcome to tgram docs bot.\n\n"
            "This bot is only working in inline mode, write the bot username with your query to search in docs, "
            "for example: `@{username} send_photo`"
        ).format(
            mention=m.from_user.mention.markdown,
            username=me.username,
        ),
        reply_parameters=types.ReplyParameters(m.message_id),
        parse_mode="Markdown",
    )


@bot.on_inline_query()
async def on_inline(_, inline_query: types.InlineQuery):
    query = inline_query.query.replace(" ", "")

    if not query:
        return await bot.answer_inline_query(
            inline_query.id,
            [
                types.InlineQueryResultArticle(
                    title="Write to search in docs..",
                    input_message_content=types.InputTextMessageContent(
                        f"Write anything to search, example: <code>@{me.username} send_photo</code>",
                        parse_mode="html",
                    ),
                    reply_markup=types.InlineKeyboardMarkup(
                        [[types.InlineKeyboardButton("Docs", docs_url)]]
                    ),
                    url=docs_url,
                )
            ],
        )
    else:
        results, offset = [], int(inline_query.offset or 0)
        methods_redirect, method_description = (
            docs_url + "tgram.html#tgram.methods.TelegramBotMethods.{0}",
            "{0}",
        )
        types_redirect, types_description = (
            docs_url + "tgram.html#tgram.types.{0}",
            "A Bot API type class",
        )

        for i in all_methods:
            if query.lower() in i.lower():
                results.append(
                    types.InlineQueryResultArticle(
                        f"tgram.TgBot.{i}()",
                        description="tgram.TgBot method",
                        input_message_content=types.InputTextMessageContent(
                            ("[{}]({}) - tgram.TgBot method\n\n{}").format(
                                i,
                                methods_redirect.format(i),
                                method_description.format(
                                    getattr(methods.TelegramBotMethods, i).__doc__
                                ),
                            ),
                            parse_mode="Markdown",
                            link_preview_options=types.LinkPreviewOptions(
                                is_disabled=True
                            ),
                        ),
                        thumbnail_url="https://cdn-icons-png.flaticon.com/512/1743/1743948.png",
                    )
                )

        for i in all_types:
            if query.lower() in i.lower():
                results.append(
                    types.InlineQueryResultArticle(
                        f"tgram.types.{i}",
                        description=types_description,
                        input_message_content=types.InputTextMessageContent(
                            ("[{}]({}) - {}\n\n{}").format(
                                i,
                                types_redirect.format(i),
                                types_description,
                                "https://core.telegram.org/bots/api/#" + i.lower(),
                            ),
                            parse_mode="Markdown",
                            link_preview_options=types.LinkPreviewOptions(
                                is_disabled=True
                            ),
                        ),
                        thumbnail_url="https://cdn-icons-png.flaticon.com/512/9031/9031996.png",
                    )
                )

        return await bot.answer_inline_query(
            inline_query_id=inline_query.id,
            results=results,
            cache_time=10,
            next_offset=str(offset + 10) if len(results) > 10 else None,
        )


bot.run_for_updates()
