import tgram


class ConvertGiftToStars:
    async def convert_gift_to_stars(
        self: "tgram.TgBot",
        business_connection_id: str,
        owned_gift_id: str,
    ) -> bool:
        """
        Converts a given regular gift to Telegram Stars. Requires the can_convert_gifts_to_stars business bot right. Returns True on success.

        Parameters:
            business_connection_id (str): Unique identifier of the business connection.
            owned_gift_id (str): Unique identifier of the regular gift that should be converted to Telegram Stars.
        """
        result = await self(
            "convertGiftToStars",
            business_connection_id=business_connection_id,
            owned_gift_id=owned_gift_id,
        )
        return result.get("result", {})
