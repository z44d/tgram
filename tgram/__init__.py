from .methods import Methods
from .decorators import Decorators

from . import types

__all__ = ["types", "TgBot"]


class TgBot(Methods, Decorators):
    pass  # TODO
