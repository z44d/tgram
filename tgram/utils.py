from .handlers import Handlers

API_URL = "https://api.telegram.org/"
ALL_UPDATES = [
    getattr(Handlers, i)
    for i in filter(lambda x: not x.startswith("_"), Handlers.__dict__)
]
