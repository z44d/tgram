from tgram import utils


class APIException(Exception):
    def __init__(
        self, message: str, error_code: int, description: str, parameters: dict = None
    ) -> None:
        super().__init__(message)
        self.error_code = error_code
        self.description = description
        self.parameters = parameters

    @staticmethod
    def _from_json(json: dict) -> "APIException":
        return APIException(
            message=f"You got {json['error_code']} error: {json['description']}",
            error_code=json.get("error_code"),
            description=json.get("description"),
            parameters=utils.Json(json.get("parameters", {})),
        )


class StopPropagation(Exception):
    pass
