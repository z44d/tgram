import tgram

from typing import Union

class VerifyChat:
    async def verify_chat(
        self: "tgram.TgBot",
        chat_id: Union[str, int],
        custom_description: str = None
    ) -> bool:
        """
        Verifies a chat on behalf of the organization which is represented by the bot. Returns True on success.
        Telegram documentation: https://core.telegram.org/bots/api#verifychat

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type chat_id: :obj:`int` or :obj:`str`

        :param custom_description: UCustom description for the verification; 0-70 characters.
            Must be empty if the organization isn't allowed to provide a custom verification description.
        :type custom_description: :obj:`str`

        :return: True on success
        :rtype: :obj:`bool`
        """

        result = await self(
            "verifyChat",
            chat_id=chat_id,
            custom_description=custom_description
        )
        return result["result"]
