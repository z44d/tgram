def custom_emoji(emoji: str, custom_emoji_id: str) -> str:
    """
    Helper function to generate a premium emoji HTML tag.

    :param emoji: The emoji character.
    :param custom_emoji_id: The custom emoji ID.
    :return: The formatted HTML string.
    """
    return f"<tg-emoji emoji-id='{custom_emoji_id}'>{emoji}</tg-emoji>"
