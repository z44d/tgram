import tgram
from typing import List
from tgram.types import ShippingOption


class AnswerShippingQuery:
    async def answer_shipping_query(
        self: "tgram.TgBot",
        shipping_query_id: str,
        ok: bool,
        shipping_options: List[ShippingOption] = None,
        error_message: str = None,
    ) -> bool:
        """
        Asks for an answer to a shipping question.

        Telegram documentation: https://core.telegram.org/bots/api#answershippingquery

        :param shipping_query_id: Unique identifier for the query to be answered
        :type shipping_query_id: :obj:`str`

        :param ok: Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
        :type ok: :obj:`bool`

        :param shipping_options: Required if ok is True. A JSON-serialized array of available shipping options.
        :type shipping_options: :obj:`list` of :obj:`ShippingOption`

        :param error_message: Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order
            (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.
        :type error_message: :obj:`str`

        :return: On success, True is returned.
        :rtype: :obj:`bool`
        """

        result = await self(
            "answerShippingQuery",
            shipping_query_id=shipping_query_id,
            ok=ok,
            shipping_options=shipping_options,
            error_message=error_message,
        )
        return result["result"]
