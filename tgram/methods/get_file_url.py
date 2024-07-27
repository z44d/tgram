import tgram


class GetFileUrl:
    async def get_file_url(self: "tgram.TgBot", file_id: str) -> str:
        """
        Get a valid URL for downloading a file.

        :param file_id: File identifier to get download URL for.
        :type file_id: :obj:`str`

        :return: URL for downloading the file.
        :rtype: :obj:`str`
        """
        file = await self.get_file(file_id)
        return self.api_url + f"file/bot{self.bot_token}/{file.file_path}"
