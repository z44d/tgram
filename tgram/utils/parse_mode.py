import tgram

from typing import Optional


def get_parse_mode(
    bot: Optional["tgram.TgBot"] = None, parse_mode: Optional[str] = None
) -> Optional[str]:
    if parse_mode is not None:
        # Check if parse_mode indicates a disabled state
        if parse_mode.lower() in {"d", "disable", "disabled"}:
            return None
        return parse_mode

    # If no parse_mode is provided, return the bot's default if available
    return bot.parse_mode if bot else None
