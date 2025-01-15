import tgram
from typing import List
from tgram.types import PassportElementError


class SetPassportDataErrors:
    async def set_passport_data_errors(
        self: "tgram.TgBot", user_id: int, errors: List[PassportElementError]
    ) -> bool:
        result = await self(
            "setPassportDataErrors",
            user_id=user_id,
            errors=errors,
        )
        return result["result"]
