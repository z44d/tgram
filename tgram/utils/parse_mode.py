import tgram

from typing import Optional


def get_parse_mode(
    bot: Optional["tgram.TgBot"] = None, parse_mode: Optional[str] = None
) -> Optional[str]:
    if parse_mode and parse_mode.lower() in ('d', 'disable', 'disabled'):
        return None
    else:
        return parse_mode or (bot.parse_mode if bot else None)
