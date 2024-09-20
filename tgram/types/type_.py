import tgram
import logging
from json import dumps
from tgram.utils import Json


logger = logging.getLogger(__name__)


class Type_:
    def __init__(self, me: "tgram.TgBot" = None, json: dict = None) -> None:
        BOUNDED_TYPES = (
            tgram.types.User,
            tgram.types.CallbackQuery,
            tgram.types.Message,
            tgram.types.Chat,
            tgram.types.ChatFullInfo,
            tgram.types.InlineQuery,
            tgram.types.PreCheckoutQuery,
        )
        self._me = (
            me
            if any((isinstance(self, BOUNDED_TYPES), me is not None and me.storage))
            else None
        )
        self._json = json

    @property
    def json(self) -> dict:
        return Json(self._json or {})

    @staticmethod
    def default(obj: "Type_" = None):
        if not isinstance(obj, Type_):
            return repr(obj)
        return {
            "_": obj.__class__.__name__,
            **{
                attr: getattr(obj, attr)
                for attr in filter(
                    lambda x: not x.startswith("_") and getattr(obj, x) is not None,
                    obj.__dict__,
                )
            },
        }

    def __str__(self) -> str:
        return dumps(self, indent=2, default=Type_.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return "tgram.types.{}({})".format(
            self.__class__.__name__,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in filter(lambda x: not x.startswith("_"), self.__dict__)
                if getattr(self, attr) is not None
            ),
        )

    @staticmethod
    def _custom_parse(a: "Type_" = None, b: type = None) -> type:
        if b is None:
            return a
        obj = b()
        obj._me = a._me
        obj._json = a._json
        try:
            for attr in filter(lambda x: not x.startswith("_"), dir(a)):
                if hasattr(type(a), attr) and (
                    callable(getattr(type(a), attr))
                    or isinstance(getattr(type(a), attr), property)
                ):
                    setattr(type(obj), attr, getattr(type(a), attr))
                else:
                    setattr(obj, attr, getattr(a, attr))
            return obj
        except Exception as e:
            logger.warn(
                "You got an error (%s) (The original type returned) when the bot trying to give you custom type, make sure you are doing it in right way, see the example here %s",
                str(e),
                "https://github.com/z44d/tgram/blob/main/examples/custom_types.py",
            )
            return a
