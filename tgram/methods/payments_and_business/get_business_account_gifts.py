import tgram
from tgram.types import OwnedGifts


class GetBusinessAccountGifts:
    async def get_business_account_gifts(
        self: "tgram.TgBot",
        business_connection_id: str,
        exclude_unsaved: bool = None,
        exclude_saved: bool = None,
        exclude_unlimited: bool = None,
        exclude_limited_upgradable: bool = None,
        exclude_limited_non_upgradable: bool = None,
        exclude_unique: bool = None,
        exclude_from_blockchain: bool = None,
        sort_by_price: bool = None,
        offset: str = "",
        limit: int = 100,
    ) -> OwnedGifts:
        """
        Use this method to get the gifts received and owned by a managed business account.
        Requires the can_view_gifts_and_stars business bot right.
        Returns an OwnedGifts object on success.

        Telegram documentation: https://core.telegram.org/bots/api#getbusinessaccountgifts

        :param business_connection_id: Unique identifier of the business connection
        :type business_connection_id: :obj:`str`
        :param exclude_unsaved: Exclude gifts that aren't saved to the account's profile page
        :type exclude_unsaved: :obj:`bool`, optional
        :param exclude_saved: Exclude gifts that are saved to the account's profile page
        :type exclude_saved: :obj:`bool`, optional
        :param exclude_unlimited: Exclude gifts that can be purchased an unlimited number of times
        :type exclude_unlimited: :obj:`bool`, optional
        :param exclude_limited_upgradable: Exclude limited gifts that can be upgraded to unique
        :type exclude_limited_upgradable: :obj:`bool`, optional
        :param exclude_limited_non_upgradable: Exclude limited gifts that cannot be upgraded to unique
        :type exclude_limited_non_upgradable: :obj:`bool`, optional
        :param exclude_unique: Exclude unique gifts
        :type exclude_unique: :obj:`bool`, optional
        :param exclude_from_blockchain: Exclude gifts that were assigned from the TON blockchain
        :type exclude_from_blockchain: :obj:`bool`, optional
        :param sort_by_price: Sort results by gift price instead of send date
        :type sort_by_price: :obj:`bool`, optional
        :param offset: Offset of the first entry to return; use empty string for first chunk
        :type offset: :obj:`str`, optional
        :param limit: Maximum number of gifts to return; 1-100, defaults to 100
        :type limit: :obj:`int`, optional

        :return: Returns an OwnedGifts object on success.
        :rtype: :class:`tgram.types.OwnedGifts`
        """
        result = await self(
            "getBusinessAccountGifts",
            business_connection_id=business_connection_id,
            exclude_unsaved=exclude_unsaved,
            exclude_saved=exclude_saved,
            exclude_unlimited=exclude_unlimited,
            exclude_limited_upgradable=exclude_limited_upgradable,
            exclude_limited_non_upgradable=exclude_limited_non_upgradable,
            exclude_unique=exclude_unique,
            exclude_from_blockchain=exclude_from_blockchain,
            sort_by_price=sort_by_price,
            offset=offset,
            limit=limit,
        )
        return OwnedGifts._parse(me=self, d=result.get("result", {}))
