import base64
import struct

from typing import List, TypedDict
from io import BytesIO

from tgram import utils


def b64_decode(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def rle_decode(s: bytes) -> bytes:
    r: List[int] = []
    z: bool = False

    for b in s:
        if not b:
            z = True
            continue

        if z:
            r.extend((0,) * b)
            z = False
        else:
            r.append(b)

    return bytes(r)


FILE_TYPES = {
    0: "Thumbnail",
    1: "ChatPhoto",
    2: "Photo",
    3: "Voice",
    4: "Video",
    5: "Document",
    8: "Sticker",
    9: "Audio",
    10: "Animation",
    13: "VideoNote",
    17: "Document",
}

SUPPORTED_FILE_TYPES_TO_SEND = (2, 3, 4, 5, 8, 9, 10, 13, 17)

WEB_LOCATION_FLAG = 1 << 24
FILE_REFERENCE_FLAG = 1 << 25


class DecodedFileId(TypedDict):
    file_type_int: int
    file_type: str
    dc_id: int
    file_id: str


def decode_file_id(file_id: str) -> DecodedFileId:
    decoded = rle_decode(b64_decode(file_id))
    major = decoded[-1]

    if major < 4:
        buffer = BytesIO(decoded[:-1])
    else:
        buffer = BytesIO(decoded[:-2])

    file_type_int, dc_id = struct.unpack("<ii", buffer.read(8))

    file_type_int &= ~WEB_LOCATION_FLAG
    file_type_int &= ~FILE_REFERENCE_FLAG

    try:
        file_type = FILE_TYPES[file_type_int]
    except ValueError:
        raise ValueError(f"Unknown file_type {file_type} of file_id {file_id}")

    return utils.Json(
        {
            "file_type_int": file_type_int,
            "file_type": file_type,
            "dc_id": dc_id,
            "file_id": file_id,
        }
    )
