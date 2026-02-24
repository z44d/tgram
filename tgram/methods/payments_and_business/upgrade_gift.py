import tgram


class UpgradeGift:
    async def upgrade_gift(
        self: "tgram.TgBot",
        business_connection_id: str,
        owned_gift_id: str,
        keep_original_details: bool = None,
        star_count: int = None,
    ) -> bool:
        """
        Upgrades a given regular gift to a unique gift. Requires the can_transfer_and_upgrade_gifts business bot right.
        Additionally requires the can_transfer_stars business bot right if the upgrade is paid. Returns True on success.

        Parameters:
            business_connection_id (str): Unique identifier of the business connection.
            owned_gift_id (str): Unique identifier of the regular gift that should be upgraded to a unique one.
            keep_original_details (bool, optional): Pass True to keep the original gift text, sender and receiver in the upgraded gift.
            star_count (int, optional): The amount of Telegram Stars that will be paid for the upgrade from the business account balance.
        """
        result = await self(
            "upgradeGift",
            business_connection_id=business_connection_id,
            owned_gift_id=owned_gift_id,
            keep_original_details=keep_original_details,
            star_count=star_count,
        )
        return result.get("result", {})
