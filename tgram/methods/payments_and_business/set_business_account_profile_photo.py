import tgram

from typing import Union
from tgram.utils import convert_input_media


class SetBusinessAccountProfilePhoto:
    async def set_business_account_profile_photo(
        self: "tgram.TgBot",
        business_connection_id: str,
        photo: Union[
            "tgram.types.InputProfilePhotoStatic",
            "tgram.types.InputProfilePhotoAnimated",
        ],
        is_public: bool = None,
    ) -> bool:
        """
        Changes the profile photo of a managed business account.
        Requires the can_edit_profile_photo business bot right.

        Telegram documentation: https://core.telegram.org/bots/api#setbusinessaccountprofilephoto

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`

        :param photo: The new profile photo to set
        :type photo: :class:`tgram.types.InputProfilePhotoStatic` or :class:`tgram.types.InputProfilePhotoAnimated`

        :param is_public: Pass True to set the public photo, which will be visible even if the main photo is hidden by the business account's privacy settings. An account can have only one public photo.
        :type is_public: :obj:`bool`, optional

        :return: On success, returns True.
        :rtype: :obj:`bool`
        """
        converted, file = convert_input_media([photo])
        result = await self(
            "setBusinessAccountProfilePhoto",
            business_connection_id=business_connection_id,
            photo=converted[0],
            is_public=is_public,
            **file,
        )
        return result["result"]
