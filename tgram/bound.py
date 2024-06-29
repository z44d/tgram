import tgram

from typing import Union, List


class MessageB:
    async def reply_text(
        self: "tgram.types.Message",
        text: str,
        parse_mode: str = None,
        entities: List["tgram.types.MessageEntity"] = None,
        link_preview_options: "tgram.types.LinkPreviewOptions" = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_markup: Union[
            "tgram.types.InlineKeyboardMarkup",
            "tgram.types.ReplyKeyboardMarkup",
            "tgram.types.ReplyKeyboardRemove",
            "tgram.types.ForceReply",
        ] = None,
    ) -> "tgram.types.Message":
        return await self._me.send_message(
            chat_id=self.chat.id,
            text=text,
            business_connection_id=self.business_connection_id,
            message_thread_id=self.message_thread_id,
            parse_mode=parse_mode if parse_mode is not None else self._me.parse_mode,
            entities=entities,
            link_preview_options=link_preview_options or self._me.link_preview_options,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self._me.protect_content,
            message_effect_id=message_effect_id,
            reply_markup=reply_markup,
            reply_parameters=tgram.types.ReplyParameters(self.message_id),
        )

    @property
    def id(self: "tgram.types.Message") -> int:
        return self.message_id
