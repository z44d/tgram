import tgram
from typing import Union
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message


class EditMessageLiveLocation:
    async def edit_message_live_location(
        self: "tgram.TgBot",
        latitude: float,
        longitude: float,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        live_period: int = None,
        horizontal_accuracy: float = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        result = await self._send_request(
            "editMessageLiveLocation",
            latitude=latitude,
            longitude=longitude,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            live_period=live_period,
            horizontal_accuracy=horizontal_accuracy,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )
