from tgram import utils


class ChatNotFound(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class GroupChatMigrated(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class InvalidFileId(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class MessageUneditable(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class MessageNotModified(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class MessageTextEmpty(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class UserNotFound(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class WrongParameter(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class TerminatedByOtherLongPollOrWebhook(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class BotWasBlocked(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class UnableSendToBots(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class BotWasKicked(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class UserDeactivated(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class FloodWait(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])
        self.value: int = args[1].get("parameters", {}).get("retry_after", 0)


class Unauthorized(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


class WebhookIsActive(Exception):
    def __init__(self, *args) -> None:
        super().__init__(args[0])


exceptions = {
    "chat not found": (
        ChatNotFound,
        "The chat is unknown to the bot, Double check the provided chat_id.",
    ),
    "group chat was migrated to a supergroup chat": (
        GroupChatMigrated,
        "Occurs when a group chat has been converted/migrated to a supergroup, Check the provided chat_id and make sure the new Super Group ID is passed.",
    ),
    "invalid file id": (
        InvalidFileId,
        "The file id you are trying to retrieve doesn't exist.",
    ),
    "message can't be edited": (
        MessageUneditable,
        "The message text cannot be edited, Check is message belong to chat or is message exist in chat.",
    ),
    "message is not modified": (
        MessageNotModified,
        "The current and new message text and reply markups are the same, Actually chanange the text or reply markup of the message to be edited.",
    ),
    "message text is empty": (
        MessageTextEmpty,
        "The message text is empty or not provided, Provide a valid message text.",
    ),
    "user not found": (UserNotFound, "user_id is incorrect"),
    "wrong parameter action in request": (
        WrongParameter,
        "Occurs when the action property value is invalid, Provide a valid value to the action property as specified in the documentation.",
    ),
    "terminated by other long poll or webhook": (
        "TerminatedByOtherLongPollOrWebhook",
        "You have already set up a webhook and are trying to get the updates via getUpdates.",
    ),
    "bot was blocked by the user": (BotWasBlocked, "The user have blocked the bot."),
    "bot can't send messages to bots": (
        UnableSendToBots,
        "You tried to send a message to another bot. This is not possible.",
    ),
    "bot was kicked from the group chat": (
        BotWasKicked,
        "Bot was kicked from the provided chat.",
    ),
    "user is deactivated": (
        UserDeactivated,
        "You're trying to perform an action on a user account that has been deactivated or deleted.",
    ),
    "Too Many Requests": (
        FloodWait,
        "You are hitting the API limit, more information here https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this",
    ),
    "Unauthorized": (
        Unauthorized,
        "Bot token is incorrect, Correct your bot token and try again.",
    ),
    "can't use getUpdates method while webhook is active; use deleteWebhook to delete the webhook first": (
        WebhookIsActive,
        "You are trying to use getUpdates while a webhook is active, Use deleteWebhook to delete the webhook first.",
    ),
}


class APIException(Exception):
    def __init__(
        self, message: str, error_code: int, description: str, parameters: dict = None
    ) -> None:
        super().__init__(message)
        self.error_code = error_code
        self.description = description
        self.parameters = parameters

    @staticmethod
    def _from_json(json: dict):
        for i in exceptions:
            if i in json["description"]:
                e = exceptions.get(i)
                return e[0](e[1], json)

        return APIException(
            message=f"You got {json['error_code']} error: {json['description']}",
            error_code=json.get("error_code"),
            description=json.get("description"),
            parameters=utils.Json(json.get("parameters", {})),
        )


class StopPropagation(Exception):
    pass
