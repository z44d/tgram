import tgram
from tgram.types import File


class GetFile:
    async def get_file(self: "tgram.TgBot", file_id: str) -> File:
        """
        Use this method to get basic info about a file and prepare it for downloading.
        For the moment, bots can download files of up to 20MB in size.
        On success, a File object is returned.
        It is guaranteed that the link will be valid for at least 1 hour.
        When the link expires, a new one can be requested by calling get_file again.

        Telegram documentation: https://core.telegram.org/bots/api#getfile

        :param file_id: File identifier
        :type file_id: :obj:`str`

        :return: :class:`tgram.types.File`
        """

        result = await self(
            "getFile",
            file_id=file_id,
        )
        return File._parse(me=self, d=result.get("result", {}))
