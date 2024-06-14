import requests, json
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from typing import List, Optional, Any

methods = json.loads(open("method.json", "r").read())["methods"]

names = [i["name"] for i in methods]


# Function to convert type names from Telegram API to Python type hints
def convert_type(tg_type: str) -> str:
    type_mapping = {
        "Integer": "int",
        "String": "str",
        "Boolean": "bool",
        "Float": "float",
        "True": "bool",
    }
    if tg_type in type_mapping:
        return type_mapping[tg_type]
    if tg_type.startswith("Array of "):
        converted = f"{convert_type(tg_type[9:])}"
        tt = (
            f'"{converted}"'
            if not "List[" in converted and not "Union[" in converted
            else converted
        )
        return f"List[{tt}]"
    elif tg_type.count(" or "):
        tt = []
        for i in filter(lambda x: x != "or", tg_type.split()):
            if i in type_mapping:
                t = type_mapping[i]
            else:
                t = i
            tt.append(t)
        return "Union[{}]".format(" ,".join([f'"{i}"' for i in tt]))
    return tg_type.replace(" or ", ", ")


# Function to scrape the Telegram Bot API documentation
def scrape_telegram_api():
    url = "https://core.telegram.org/bots/api"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Try finding a section containing types by inspecting larger sections of the page
    divs = soup.find_all("div")

    for i, div in enumerate(divs):
        div_text = div.get_text(strip=True)
        if "Available types" in div_text:
            print(f"Found potential 'Available types' div at index {i}.\n")
            break
    else:
        print("Could not find the 'Available types' section.")
        return []

    # Assuming we found the correct div, let's try to extract the type definitions from it
    type_headers = div.find_all("h4")
    if not type_headers:
        print("Could not find any type headers.")
        return []

    type_definitions = []
    for header in type_headers:
        type_name = header.text.strip()
        type_description = header.find_next_sibling("p").text.strip()
        fields = []

        table = header.find_next_sibling("table")
        if table:
            rows = table.find_all("tr")[1:]  # skip header row
            for row in rows:
                columns = row.find_all("td")
                if len(columns) < 3:
                    print(f"Skipping row with insufficient columns: {row}")
                    continue
                field_name = columns[0].text.strip()
                field_type = columns[1].text.strip()
                field_optional = "Optional" if "Optional" in columns[2].text else ""
                fields.append((field_name, field_type, field_optional))

        type_definitions.append((type_name, type_description, fields))

    return type_definitions


def generate_dataclasses(type_definitions):
    dataclasses_code = ""
    for type_name, type_description, fields in type_definitions:
        if type_name.count(" ") or type_name in names:
            continue
        dataclasses_code += f"class {type_name}(Type_):\n"
        dataclasses_code += f"    def __init__(self"
        init_fields = []
        optional_fields = []

        for field_name, field_type, field_optional in fields:
            python_type = convert_type(field_type)
            field_name = (
                field_name.replace("from", "from_user")
                if field_name == "from"
                else field_name
            )
            if field_optional:
                tt = (
                    f'"{python_type}"'
                    if not python_type.startswith("List[")
                    and not python_type.startswith("Union[")
                    else python_type
                )
                python_type = f"{tt}"
                # init_fields.append((field_name, python_type, field_optional))
                optional_fields.append((field_name, python_type, field_optional))
            else:
                tt = (
                    f'"{python_type}"'
                    if not python_type.startswith("List[")
                    and not python_type.startswith("Union[")
                    else python_type
                )
                init_fields.append((field_name, tt, field_optional))

        for i in optional_fields:
            init_fields.append(i)

        for field_name, python_type, opt in init_fields:
            field_name = (
                field_name.replace("from", "from_user")
                if field_name == "from"
                else field_name
            )
            dataclasses_code += f", {field_name}: {python_type}" + (
                " = None" if opt else ""
            )
        dataclasses_code += "):\n"

        for field_name, field_type, field_optional in fields:
            field_name = (
                field_name.replace("from", "from_user")
                if field_name == "from"
                else field_name
            )
            python_type = convert_type(field_type)
            if field_optional:
                dataclasses_code += f"        self.{field_name} = {field_name}\n"
            else:
                dataclasses_code += f"        self.{field_name} = {field_name}\n"

        dataclasses_code += "\n"
    return dataclasses_code


# Main script
if __name__ == "__main__":
    type_definitions = scrape_telegram_api()
    if not type_definitions:
        print("No type definitions were scraped.")
    else:
        dataclasses_code = generate_dataclasses(type_definitions)
        with open("types_.py", "w+") as f:
            f.write("from typing import List, Optional, Union\n\n")
            f.write(open("./parser_.py", "r").read())
            f.write(dataclasses_code)
        import os

        os.system("ruff format types_.py")
        print("Python dataclass definitions have been written to types_.py")
