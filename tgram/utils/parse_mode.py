import tgram

from typing import Optional


def get_parse_mode(
    bot: Optional["tgram.TgBot"] = None, parse_mode: Optional[str] = None
) -> Optional[str]:
    return (
        None
        if parse_mode.lower() in ("d", "disable", "disabled")
        else (parse_mode if parse_mode is not None else bot.parse_mode if bot else None)
    )
