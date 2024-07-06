from .handlers import Handlers

import os

from pathlib import Path

API_URL = "https://api.telegram.org/"
ALL_UPDATES = [
    getattr(Handlers, i)
    for i in filter(lambda x: not x.startswith("_"), Handlers.__dict__)
]


def get_file_name(obj):
    name = getattr(obj, "name", None)
    if name and isinstance(name, str) and name[0] != "<" and name[-1] != ">":
        return os.path.basename(name)


def get_file_path(file):
    return Path(file) if isinstance(file, str) and os.path.isfile(file) else file
