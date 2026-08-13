from typing import Optional

import tgram


def get_parse_mode(
    bot: Optional["tgram.TgBot"] = None, parse_mode: str | None = None
) -> str | None:
    parse_mode = parse_mode or (bot.parse_mode if bot else None)

    if parse_mode and parse_mode.lower() in {"d", "disable", "disabled"}:
        return None
    return parse_mode
