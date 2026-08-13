
import tgram
from tgram.types import SentWebAppMessage, WebAppInfo


class SendChatJoinRequestWebApp:
    async def send_chat_join_request_web_app(
        self: "tgram.TgBot",
        chat_id: int | str,
        user_id: int,
        query_id: str,
        web_app_info: WebAppInfo,
    ) -> SentWebAppMessage:
        """
        Use this method to send a message from a chat join request web app.

        Telegram documentation: https://core.telegram.org/bots/api#sendchatjoinrequestwebapp

        :param chat_id: Unique identifier for the target chat or username of the target supergroup
            (in the format @supergroupusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param user_id: Unique identifier of the target user
        :type user_id: :obj:`int`

        :param query_id: Unique identifier of the query to be answered
        :type query_id: :obj:`str`

        :param web_app_info: Web App information
        :type web_app_info: :class:`tgram.types.WebAppInfo`

        :return: On success, a SentWebAppMessage object is returned.
        :rtype: :class:`tgram.types.SentWebAppMessage`
        """

        result = await self(
            "sendChatJoinRequestWebApp",
            chat_id=chat_id,
            user_id=user_id,
            query_id=query_id,
            web_app_info=web_app_info,
        )
        return SentWebAppMessage._parse(me=self, d=result.get("result", {}))
