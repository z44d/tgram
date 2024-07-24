import tgram
from typing import Union
from tgram.types import ForceReply
from tgram.types import InlineKeyboardMarkup
from tgram.types import Message
from tgram.types import ReplyKeyboardMarkup
from tgram.types import ReplyKeyboardRemove
from tgram.types import ReplyParameters


class SendLocation:
    async def send_location(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        business_connection_id: str = None,
        message_thread_id: int = None,
        horizontal_accuracy: float = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        Telegram documentation: https://core.telegram.org/bots/api#sendlocation

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param latitude: Latitude of the location
        :type latitude: :obj:`float`

        :param longitude: Longitude of the location
        :type longitude: :obj:`float`

        :param live_period: Period in seconds during which the location will be updated (see Live Locations, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
        :type live_period: :obj:`int`

        :param reply_to_message_id: Deprecated - Use reply_parameters instead. If the message is a reply, ID of the original message
        :type reply_to_message_id: :obj:`int`

        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard
            or to force a reply from the user.
        :type reply_markup: :class:`tgram.types.InlineKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardMarkup` or :class:`tgram.types.ReplyKeyboardRemove`
            or :class:`tgram.types.ForceReply`

        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type disable_notification: :obj:`bool`

        :param timeout: Timeout in seconds for the request.
        :type timeout: :obj:`int`

        :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
        :type horizontal_accuracy: :obj:`float`

        :param heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        :type heading: :obj:`int`

        :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        :type proximity_alert_radius: :obj:`int`

        :param allow_sending_without_reply: Deprecated - Use reply_parameters instead. Pass True, if the message should be sent even if the specified replied-to message is not found
        :type allow_sending_without_reply: :obj:`bool`

        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :type protect_content: :obj:`bool`

        :param message_thread_id: Identifier of a message thread, in which the message will be sent
        :type message_thread_id: :obj:`int`

        :param reply_parameters: Reply parameters.
        :type reply_parameters: :class:`tgram.types.ReplyParameters`

        :param business_connection_id: Identifier of a business connection, in which the message will be sent
        :type business_connection_id: :obj:`str`

        :param message_effect_id: Unique identifier of the message effect
        :type message_effect_id: :obj:`str`

        :return: On success, the sent Message is returned.
        :rtype: :class:`tgram.types.Message`
        """

        result = await self._send_request(
            "sendLocation",
            chat_id=chat_id,
            latitude=latitude,
            longitude=longitude,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])
