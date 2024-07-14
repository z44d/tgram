import logging
from tgram import TgBot

logging.basicConfig(level=logging.DEBUG)

bot = TgBot("API_TOKEN_HERE", parse_mode="Markdown", plugins="./plugins")

bot.run_for_updates()
