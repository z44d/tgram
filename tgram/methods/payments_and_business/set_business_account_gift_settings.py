import tgram


class SetBusinessAccountGiftSettings:
    async def set_business_account_gift_settings(
        self: "tgram.TgBot",
        business_connection_id: str,
        show_gift_button: bool,
        accepted_gift_types: "tgram.types.AcceptedGiftTypes",
    ) -> bool:
        """
        Changes the privacy settings pertaining to incoming gifts in a managed business account.
        Requires the can_change_gift_settings business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#setbusinessaccountgiftsettings

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param show_gift_button: Pass True, if a button for sending a gift to the user or by the business account must always be shown in the input field
        :type show_gift_button: :obj:`bool`

        :param accepted_gift_types: Types of gifts accepted by the business account
        :type accepted_gift_types: :obj:`tgram.types.AcceptedGiftTypes`

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """
        result = await self(
            "setBusinessAccountGiftSettings",
            business_connection_id=business_connection_id,
            show_gift_button=show_gift_button,
            accepted_gift_types=accepted_gift_types,
        )
        return result.get("result", {})
