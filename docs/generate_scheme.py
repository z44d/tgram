import inspect
import json
from typing import (
    get_type_hints,
    Any,
    Dict,
    Union,
    get_origin,
    get_args,
    List,
    ForwardRef,
)

import tgram
import docstring_parser

visited = set()
IGNORE_FIELDS = {"key", "json"}


def clean_type(tp):
    if isinstance(tp, ForwardRef):
        return tp.__forward_arg__

    origin = get_origin(tp)
    args = get_args(tp)

    if origin is Union:
        non_none_args = [a for a in args if a is not type(None)]
        if len(non_none_args) == 1:
            return clean_type(non_none_args[0])
        cleaned = [clean_type(a) for a in non_none_args]
        # If any branch is non-string (e.g., list structure), return a structured union
        if any(not isinstance(c, str) for c in cleaned):
            return {"kind": "union", "of": cleaned}
        return ", ".join(cleaned)

    elif origin in {list, List}:
        if args:
            inner = args[0]
            inner_origin = get_origin(inner)
            if inner_origin is Union:
                return {
                    "kind": "list",
                    "of": {
                        "kind": "union",
                        "of": [clean_type(a) for a in get_args(inner)],
                    },
                }
            return {"kind": "list", "of": clean_type(inner)}
        return {"kind": "list", "of": "Any"}

    elif hasattr(tp, "__name__"):
        return tp.__name__

    elif hasattr(tp, "_name"):
        base = tp._name
        if args:
            return f"{base}[{', '.join(clean_type(a) for a in args)}]"
        return base

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


def extract_filters(module) -> Dict[str, Any]:
    """Return a mapping with two groups: variables and functions.

    variables: top-level instances of Filter
    functions: callables whose return annotation is Filter (e.g., command, regex, chat, user, sender, parameter)
    """
    variables: Dict[str, Any] = {}
    functions: Dict[str, Any] = {}

    FilterClass = getattr(module, "Filter", None)

    for name, obj in inspect.getmembers(module):
        if name.startswith("_") or name.endswith("_"):
            continue

        # Variable filters (instances)
        if FilterClass is not None and isinstance(obj, FilterClass):
            description = inspect.getdoc(obj) or getattr(obj, "__doc__", "") or ""
            variables[name] = {"description": description}
            continue

        # Filter factory functions (return Filter)
        if inspect.isfunction(obj) and obj.__module__.startswith(module.__name__):
            try:
                sig = inspect.signature(obj)
            except Exception:
                continue

            # Determine if it returns a Filter by annotation (best effort)
            ret_ann = sig.return_annotation
            returns_filter = False
            if ret_ann is not inspect.Signature.empty:
                # Compare by name in case of from __future__ annotations
                if isinstance(ret_ann, type):
                    returns_filter = FilterClass is not None and issubclass(
                        ret_ann, FilterClass
                    )
                else:
                    returns_filter = str(ret_ann).endswith("Filter")

            if not returns_filter:
                continue

            doc = parse_docstring(obj)

            functions[name] = {
                "description": doc.short_description or "",
            }

    return {**variables, **functions}


if __name__ == "__main__":
    methods_data, types_data = walk_module(tgram)
    filters_data = extract_filters(tgram.filters)

    output = {"methods": methods_data, "types": types_data, "filters": filters_data}

    with open("tgram_scheme.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=1)

    print("✅ Extracted successfully to tgram_scheme.json")
