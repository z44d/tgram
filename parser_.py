class Type_:
    def __str__(self) -> str:
        return self.__parse()

    def __repr__(self) -> str:
        return self.__parse()

    def __parse(self, indent=1) -> str:
        lines = []
        indent_str = " " * indent if indent > 1 else ""

        for key, value in self.__dict__.items():
            if value is not None and not key.startswith("_"):
                if isinstance(value, Type_):
                    lines.append(f"{indent_str}{key}: {value.__parse(indent * 2)}")
                elif isinstance(value, list):
                    if not value:
                        lines.append(f"{indent_str}{key}: []")
                    else:
                        elements = []
                        for item in value:
                            if isinstance(item, Type_):
                                elements.append(item.__parse(indent * 2))
                            ## For InlineKeyboardMarkup, ReplyKeyboardMarkup
                            elif isinstance(item, list):
                                for item_2 in item:
                                    if isinstance(item_2, Type_):
                                        elements.append(
                                            f"\n{' ' * (indent * 2) if indent > 1 else ''}["
                                            + item_2.__parse(indent * 4)
                                            + f"\n{' ' * (indent * 2) if indent > 1 else ''}]"
                                        )
                            else:
                                elements.append(repr(item))
                        elements_str = (
                            "["
                            + ",\n".join([f"{' ' * (indent * 2)}{e}" for e in elements])
                            + f"\n{' ' * indent if indent > 1 else ''}]"
                        )
                        lines.append(f"{indent_str}{key}: {elements_str}")
                elif isinstance(value, dict):
                    if not value:
                        lines.append(f"{indent_str}{key}: {{}}")
                    else:
                        elements = [f"{repr(k)}: {repr(v)}" for k, v in value.items()]
                        elements_str = "{" + ", ".join(elements) + "}"
                        lines.append(f"{indent_str}{key}: {elements_str}")
                else:
                    lines.append(f"{indent_str}{key}: {repr(value)}")

        return (
            ("\n" if indent > 1 else "")
            + f"{indent_str}_: {repr(self.__class__.__name__)}\n"
            + "\n".join(lines)
        )

    @staticmethod
    def list_to_json(l) -> list:
        _ = []
        for i in l:
            if isinstance(i, list):
                _.append(Type_.list_to_json(i))
            elif isinstance(i, Type_):
                _.append(i.to_json())
            else:
                _.append(i)
        return _

    def to_json(self) -> dict:
        d = {}
        for key in filter(
            lambda x: not x.startswith("_") and getattr(self, x), self.__dict__
        ):
            value = getattr(self, key)
            if isinstance(value, list):
                value = Type_.list_to_json(value)
            elif isinstance(value, Type_):
                value = value.to_json()

            d.update({key: value})
        return d
