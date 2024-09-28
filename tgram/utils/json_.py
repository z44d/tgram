from json import dumps


class Json(dict):
    def __str__(self) -> str:
        return dumps(
            self,
            ensure_ascii=False,
            indent=2,
            default=lambda obj: repr(obj) if not isinstance(obj, dict) else obj,
        )
