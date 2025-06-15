import tgram


class RemoveBusinessAccountProfilePhoto:
    async def remove_business_account_profile_photo(
        self: "tgram.TgBot",
        business_connection_id: str,
        is_public: bool = None,
    ) -> bool:
        """
        Removes the current profile photo of a managed business account.
        Requires the can_edit_profile_photo business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#removebusinessaccountprofilephoto

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param is_public: Pass True to remove the public photo, which is visible even if the main photo is hidden by the business account's privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo.
        :type is_public: :obj:`bool`, optional

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """
        result = await self(
            "removeBusinessAccountProfilePhoto",
            business_connection_id=business_connection_id,
            is_public=is_public,
        )
        return result["result"]
