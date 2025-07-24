import inspect
import json
from typing import get_type_hints, Any, Dict

import tgram
import docstring_parser

visited = set()
IGNORE_FIELDS = {"key", "json"}


def clean_type(tp):
    if hasattr(tp, "__name__"):
        return tp.__name__
    if hasattr(tp, "_name"):
        base = tp._name
        args = getattr(tp, "__args__", [])
        return f"{base}[{', '.join(clean_type(a) for a in args)}]"
    return str(tp)


def parse_docstring(obj):
    doc = inspect.getdoc(obj) or ""
    return docstring_parser.parse(doc)


def extract_method_info(cls) -> Dict[str, Any]:
    methods = {}

    for name, func in inspect.getmembers(cls, inspect.isfunction):
        if name.startswith("_"):
            continue

        try:
            sig = inspect.signature(func)
            doc = parse_docstring(func)
        except Exception:
            continue

        parameters = {}
        doc_params = {p.arg_name: p.description for p in doc.params}

        for pname, param in sig.parameters.items():
            if pname in {"self", "cls"}:
                continue
            hint = (
                clean_type(param.annotation)
                if param.annotation != inspect.Parameter.empty
                else "Any"
            )
            required = param.default == inspect.Parameter.empty
            description = doc_params.get(pname, "")
            parameters[pname] = {
                "type": hint,
                "required": required,
                "description": description,
            }

        return_type = (
            clean_type(sig.return_annotation)
            if sig.return_annotation != inspect.Signature.empty
            else "Any"
        )

        methods[name] = {
            "description": doc.short_description or "",
            "parameters": parameters,
            "returns": return_type,
            "path": f"{cls.__module__}.{cls.__name__}.{name}",
        }

    return methods


def extract_type_info(cls) -> Dict[str, Any]:
    doc = parse_docstring(cls)
    props = {}

    hints = get_type_hints(cls)
    doc_fields = {p.arg_name: p.description for p in doc.params}

    for attr, hint in hints.items():
        if attr in IGNORE_FIELDS:
            continue
        props[attr] = {
            "type": clean_type(hint),
            "description": doc_fields.get(attr, ""),
        }

    # fallback to __init__ signature if no hints
    if not props:
        try:
            init_sig = inspect.signature(cls.__init__)
            for pname, param in init_sig.parameters.items():
                if pname in {"self", "cls", "me"} or pname in IGNORE_FIELDS:
                    continue
                hint = (
                    clean_type(param.annotation)
                    if param.annotation != inspect.Parameter.empty
                    else "Any"
                )
                description = doc_fields.get(pname, "")
                props[pname] = {
                    "type": hint.split(".")[-1] if "." in hint else hint,
                    "description": description,
                }
        except Exception:
            pass

    return {"description": doc.short_description or "", "properties": props}


def walk_module(module, depth=0):
    if module.__name__ in visited or depth > 6:
        return {}, {}
    visited.add(module.__name__)

    methods, types = {}, {}

    for name, obj in inspect.getmembers(module):
        if name.startswith("_") or name.endswith("_"):
            continue

        print(name)

        if inspect.isclass(obj) and obj.__module__.startswith("tgram"):
            if "methods" in obj.__module__:
                method_info = extract_method_info(obj)
                if method_info:
                    methods.update(method_info)
            elif "types" in obj.__module__:
                types[obj.__name__] = extract_type_info(obj)

        elif inspect.ismodule(obj) and obj.__name__.startswith("tgram"):
            sub_methods, sub_types = walk_module(obj, depth + 1)
            methods.update(sub_methods)
            types.update(sub_types)

    return methods, types


if __name__ == "__main__":
    methods_data, types_data = walk_module(tgram)

    output = {"methods": methods_data, "types": types_data}

    with open("tgram_schema.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("✅ Extracted successfully to tgram_schema.json")
