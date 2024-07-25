import tgram
import io
from typing import Union
from pathlib import Path
from tgram.errors import APIException


class DownloadFile:
    async def download_file(
        self: "tgram.TgBot", file_id: str, file_path: str = None, in_memory: bool = None
    ) -> Union[Path, io.BytesIO]:
        file = await self.get_file(file_id)
        file_path = file_path or file.file_path.split("/")[1]
        url = self.api_url + f"file/bot{self.bot_token}/{file.file_path}"
        session = await self._get_session()
        async with session.request("GET", url=url) as response:
            if response.status != 200:
                raise APIException("Download file", response)
            result = await response.read()
        if in_memory:
            memory_file = io.BytesIO()
            memory_file.write(result)
            memory_file.seek(0)
            memory_file.name = file_path
            return memory_file
        else:
            with open(Path(file_path), "wb") as f:
                f.write(result)
            return Path(file_path)
