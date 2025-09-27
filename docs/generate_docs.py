import json
import os
import requests


def generate_docs():
    with open("tgram_scheme.json", "r") as f:
        scheme = json.load(f)

    os.makedirs("docs", exist_ok=True)

    methods_dir = "docs/methods"
    types_dir = "docs/types"
    filters_dir = "docs/filters"
    os.makedirs(methods_dir, exist_ok=True)
    os.makedirs(types_dir, exist_ok=True)
    os.makedirs(filters_dir, exist_ok=True)

    with open("docs/index.md", "w") as f:
        f.write(
            requests.get(
                "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/README.md"
            ).text
        )

    types_data = scheme.get("types", {})
    methods_data = scheme.get("methods", {})
    filters_data = scheme.get("filters", {})

    def format_type(type_value, context="method"):
        if isinstance(type_value, list):
            return f"List of {' or '.join(format_type(t, context) for t in type_value)}"
        if isinstance(type_value, dict):
            kind = type_value.get("kind")
            if kind == "list":
                return f"List of {format_type(type_value.get('of'), context)}"
            elif kind == "union":
                return " or ".join(
                    format_type(t, context) for t in type_value.get("of")
                )
        if isinstance(type_value, str) and ", " in type_value:
            return " or ".join(type_link(t, context) for t in type_value.split(", "))
        return type_link(type_value, context)

    def type_link(type_name, context="method"):
        if isinstance(type_name, dict):
            return format_type(type_name, context)

        simple_type_name = type_name.split(".")[-1]

        if simple_type_name in types_data:
            if context == "method" or context == "util":
                return f"[{simple_type_name}](../types/{simple_type_name}.md)"
            else:
                return f"[{simple_type_name}]({simple_type_name}.md)"
        return f"`{simple_type_name}`"

    for type_name, type_info in types_data.items():
        with open(os.path.join(types_dir, f"{type_name}.md"), "w") as f:
            f.write(f"#🔮 {type_name}\n\n")
            f.write(f"**{type_info.get('description', '')}**\n\n")
            if type_info.get("properties"):
                f.write("##⚙️ Properties\n\n")
                for prop_name, prop_info in type_info["properties"].items():
                    f.write(
                        f"- **`{prop_name}`** (**{format_type(prop_info['type'], context='type')}** )"
                    )
                    if prop_info.get("description"):
                        f.write(f": **{prop_info['description']}**")
                    f.write("\n")

    # Generate Methods docs
    for method_name, method_info in methods_data.items():
        with open(os.path.join(methods_dir, f"{method_name}.md"), "w") as f:
            f.write(f"#🔧 {method_name}\n\n")
            f.write(f"**{method_info.get('description', '')}**\n\n")

            if method_info.get("parameters"):
                f.write("##⚙️ Parameters\n\n")
                for param_name, param_info in method_info["parameters"].items():
                    f.write(
                        f"- **`{param_name}`** (**{format_type(param_info['type'])}** )"
                    )
                    if not param_info.get("required", True):
                        f.write(" (`optional`)")
                    if param_info.get("description"):
                        f.write(f": **{param_info['description']}**")
                    f.write("\n")

            if method_info.get("returns"):
                f.write(f"\n##📲 Returns\n\n#### {format_type(method_info['returns'])}")

            f.write("\n\n##📀 Examples\n\n")

            required_params = {
                p: info
                for p, info in method_info.get("parameters", {}).items()
                if info.get("required")
            }
            all_params = method_info.get("parameters", {})

            if required_params:
                f.write("-🪫 **Required Parameters**\n\n")
                f.write("```python\n")
                example_str = f"await bot.{method_name}("
                example_params = [f"\n    {p}=your_{p}_here" for p in required_params]
                example_str += ",".join(example_params)
                example_str += "\n)\n```\n"
                f.write(example_str)

            if all_params and len(all_params) > len(required_params):
                f.write("\n-🔋 **All Parameters**\n\n")
                f.write("```python\n")
                example_str = f"await bot.{method_name}("
                example_params = [f"\n    {p}=your_{p}_here" for p in all_params]
                example_str += ",".join(example_params)
                example_str += "\n)\n```\n"
                f.write(example_str)

    # Generate Filters docs
    with open(os.path.join(filters_dir, "index.md"), "w+") as f:
        f.write("#🔮 Filters")
        f.write(
            "\n**Contains custom filters for processing and handling Telegram messages and events.**\n\n"
        )
        f.write("##⚙️ Custom filters")
        f.write("\n- Here is an example for how to create **custom filter**:")
        f.write("\n\n```python\n")
        f.write("from tgram.filters import Filter\nfrom tgram import filters\n\n")
        f.write(
            "only_me = Filter(lambda bot_object, message_object: bool(message_object.from_user.id == my_id))\n\n"
        )
        f.write(
            "@bot.on_message(only_me & filters.private)\n...\n```\n\n##🔥 Ready to use filters:\n"
        )

    for filter_name, filter_info in filters_data.items():
        with open(os.path.join(filters_dir, "index.md"), "a+") as f:
            f.write(f"- `{filter_name}`: ")
            description = filter_info.get("description", "") or "N/A"
            f.write(f"**{description}**\n\n")

    methods_nav_list = []
    for method_name in sorted(methods_data.keys()):
        methods_nav_list.append(f"    - '{method_name}': 'methods/{method_name}.md'")
    methods_nav_str = "\n".join(methods_nav_list)

    types_nav_list = []
    for type_name in sorted(types_data.keys()):
        types_nav_list.append(f"    - '{type_name}': 'types/{type_name}.md'")
    types_nav_str = "\n".join(types_nav_list)

    mkdocs_yml_content = f"""site_name: tgram
theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
plugins:
  - search
nav:
  - Home: index.md
  - Methods:
{methods_nav_str}
  - Types:
{types_nav_str}
  - Filters: filters/index.md
"""

    with open("mkdocs.yml", "w") as f:
        f.write(mkdocs_yml_content)


if __name__ == "__main__":
    generate_docs()
    print("✅ Docs generated")
