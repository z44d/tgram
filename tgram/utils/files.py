import os

from pathlib import Path


def get_file_name(obj):
    name = getattr(obj, "name", None)
    if name and isinstance(name, str) and name[0] != "<" and name[-1] != ">":
        return os.path.basename(name)


def get_file_path(file):
    return Path(file) if isinstance(file, str) and os.path.isfile(file) else file
