import json

# Mapping from Telegram API types to Python types
TYPE_MAPPING = {
    "integer": "int",
    "string": "str",
    "array": "List",
    "boolean": "bool",
    "float": "float",
    "reference": "Any",  # Assuming references are of any type
    "object": "dict",  # Assuming objects are of dictionary type
    "enum": "Any",  # Assuming enums are of any type
}


def convert_camel_to_snake(camel_case_string):
    result = [camel_case_string[0].lower()]
    for char in camel_case_string[1:]:
        if char.isupper():
            result.append("_")
            result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)


def convert_type(api_type_info):
    api_type = api_type_info.get("type", "bool")
    if api_type == "reference":
        reference = api_type_info.get("reference", "bool")
        return reference  # Return the reference type as-is
    elif api_type == "array":
        inner_type = api_type_info.get("array", {}).get("type", "Any")
        if inner_type == "reference":
            d = {
                "type": inner_type,
                "reference": api_type_info.get("array").get("reference"),
            }
        else:
            d = {"type": inner_type}
        return f"List[{convert_type(d)}]"
    elif api_type == "any_of":
        # print(api_type_info)
        any_of = api_type_info.get("any_of")
        if any_of is None:
            return "bool"
        _ = []
        for i in any_of:
            _.append(convert_type(i))
        return f"Union[{','.join(_)}]"
    else:
        return TYPE_MAPPING.get(api_type, "bool")


def generate_methods_file(json_data):
    methods_code = ""

    for method_data in json_data.get("methods", []):
        method_name = method_data.get("name", "")
        snake_method_name = convert_camel_to_snake(method_name)
        method_description = method_data.get(
            "documentation_link", "No description provided"
        )
        arguments = method_data.get("arguments", [])
        return_type_info = method_data.get("return_type", {})
        return_type = convert_type(return_type_info)

        methods_code += f"    def {snake_method_name}(self"

        required_args = []
        optional_args = []

        for arg in arguments:
            arg_name = arg["name"]
            arg_type_info = arg["type_info"]
            arg_type = convert_type(arg_type_info)
            if arg["required"]:
                required_args.append((arg_name, arg_type))
            else:
                optional_args.append((arg_name, arg_type))

        # Add required arguments first
        for arg_name, arg_type in required_args:
            methods_code += f", {arg_name}: {arg_type}"

        # Then add optional arguments
        for arg_name, arg_type in optional_args:
            methods_code += f", {arg_name}: {arg_type} = None"

        methods_code += f") -> {return_type}:\n"
        methods_code += f'        """{method_description}"""\n'
        methods_code += f"        ...\n\n"

    return methods_code


# def generate_types_file(json_data):
#     types_code = ""

#     for object_data in json_data.get("objects", []):
#         object_name = object_data.get("name", "")
#         object_description = object_data.get("description", "No description provided")
#         properties = object_data.get("properties", [])

#         types_code += f"class {object_name}:\n"
#         types_code += f'    """{object_description}"""\n'

#         for prop in properties:
#             prop_name = prop["name"]
#             prop_description = prop["description"]
#             prop_type_info = prop["type_info"]
#             prop_type = convert_type(prop_type_info)

#             types_code += f"    {prop_name}: {prop_type}  # {prop_description}\n"
#         if not properties:
#             types_code += "    pass"

#         types_code += "\n"

#     return types_code


if __name__ == "__main__":
    json_file = "method.json"

    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    methods_code = generate_methods_file(json_data)
    # types_code = generate_types_file(json_data)

    with open("methods.py", "w", encoding="utf-8") as f:
        f.write("from typing import Optional, List, Any\n")
        f.write("from types_ import *\n\n")  # Import all types from types.py
        f.write("class TelegramBotMethods:\n")
        f.write(methods_code)

    import os

    os.system("ruff format")

    # with open("types.py", "w", encoding="utf-8") as f:
    #     f.write(types_code)

    print("Python file 'methods.py' have been generated.")
