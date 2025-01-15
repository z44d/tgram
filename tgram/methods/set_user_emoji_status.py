import tgram


class SetUserEmojiStatus:
    async def set_user_emoji_status(
        self: "tgram.Tgbot",
        user_id: int,
        emoji_status_custom_emoji_id: str = None,
        emoji_status_expiration_date: int = None,
    ) -> bool:
        """
        Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method requestEmojiStatusAccess. Returns True on success.

        Telegram documentation: https://core.telegram.org/bots/api#setuseremojistatus

        :param user_id: OUnique identifier of the target user.
        :type user_id: :obj:`int`

        :param emoji_status_custom_emoji_id: Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status.
        :type emoji_status_custom_emoji_id: :obj:`str`

        :param emoji_status_expiration_date: Expiration date of the emoji status, if any.
        :type emoji_status_expiration_date: :obj:`int`

        :return: True on success.
        """
        result = await self(
            "setUserEmojiStatus",
            user_id=user_id,
            emoji_status_custom_emoji_id=emoji_status_custom_emoji_id,
            emoji_status_expiration_date=emoji_status_expiration_date,
        )
        return result["result"]
