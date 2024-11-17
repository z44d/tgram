import tgram

from tgram.types import PreparedInlineMessage, InlineQueryResult


class SavePreparedInlineMessage:
    async def save_prepared_inline_message(
        self: "tgram.TgBot",
        user_id: int,
        result: InlineQueryResult,
        allow_user_chats: bool = None,
        allow_bot_chats: bool = None,
        allow_group_chats: bool = None,
        allow_channel_chats: bool = None,
    ) -> PreparedInlineMessage:
        """
        Stores a message that can be sent by a user of a Mini App. Returns a PreparedInlineMessage object.

        Telegram documentation: https://core.telegram.org/bots/api#savepreparedinlinemessage
        """
        result = await self._send_request(
            "savePreparedInlineMessage",
            user_id=user_id,
            result=result,
            allow_user_chats=allow_user_chats,
            allow_bot_chats=allow_bot_chats,
            allow_group_chats=allow_group_chats,
            allow_channel_chats=allow_channel_chats,
        )

        return PreparedInlineMessage._parse(self, result["result"])
