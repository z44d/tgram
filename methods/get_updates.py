import tgram
from typing import List
from tgram.types import Update


class GetUpdates:
    async def get_updates(
        self: "tgram.TgBot",
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: List[str] = None,
    ) -> List[Update]:
        """
        Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

        Telegram documentation: https://core.telegram.org/bots/api#getupdates


        :param offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates.
            By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset
            higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue.
            All previous updates will forgotten.
        :type offset: :obj:`int`, optional

        :param limit: Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :type limit: :obj:`int`, optional

        :param timeout: Request connection timeout
        :type timeout: :obj:`int`, optional

        :param allowed_updates: Array of string. List the types of updates you want your bot to receive.
        :type allowed_updates: :obj:`list`, optional

        :param request_timeout: Timeout in seconds for request.
        :type request_timeout: :obj:`int`, optional

        :return: An Array of Update objects is returned.
        :rtype: :obj:`list` of :class:`tgram.types.Update`
        """

        result = await self._send_request(
            "getUpdates",
            offset=offset,
            limit=limit,
            timeout=timeout,
            allowed_updates=allowed_updates,
        )
        return [Update._parse(me=self, d=i) for i in result["result"]]
