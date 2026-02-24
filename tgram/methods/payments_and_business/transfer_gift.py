import tgram


class TransferGift:
    async def transfer_gift(
        self: "tgram.TgBot",
        business_connection_id: str,
        owned_gift_id: str,
        new_owner_chat_id: int,
        star_count: int = None,
    ) -> bool:
        """
        Transfers an owned unique gift to another user. Requires the can_transfer_and_upgrade_gifts business bot right.
        Requires can_transfer_stars business bot right if the transfer is paid. Returns True on success.

        Parameters:
            business_connection_id (str): Unique identifier of the business connection.
            owned_gift_id (str): Unique identifier of the regular gift that should be transferred.
            new_owner_chat_id (int): Unique identifier of the chat which will own the gift. The chat must be active in the last 24 hours.
            star_count (int, optional): The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the can_transfer_stars business bot right is required.
        """
        result = await self(
            "transferGift",
            business_connection_id=business_connection_id,
            owned_gift_id=owned_gift_id,
            new_owner_chat_id=new_owner_chat_id,
            star_count=star_count,
        )
        return result.get("result", {})
