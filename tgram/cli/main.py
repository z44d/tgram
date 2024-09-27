import os
import argparse
import requests
import re
import json

from tgram import TgBot


methods = [
    *["_send_request"],
    *[i for i in filter(lambda x: not x.startswith("_"), dir(TgBot))],
]


def camel_to_snake(name):
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
    return snake


def generate():
    TEMPLATE = {
        ".env": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/cli/template/.env",
        ".gitignore": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/cli/template/.gitignore",
        "README.md": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/cli/template/generate.md",
        "config.py": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/cli/template/config.py",
        "main.py": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/cli/template/main.py",
        "requirements.txt": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/cli/template/requirements.txt",
    }

    print("Generating ready-template..")

    for i in TEMPLATE:
        with open(i, "w+", encoding="utf-8") as f:
            f.write(requests.get(TEMPLATE.get(i)).text)

            print(f"File [ {i} ] has been generated.")

    if not os.path.isdir("plugins"):
        os.mkdir("plugins")

    with open("plugins/start.py", "w+", encoding="utf-8") as f:
        f.write(
            requests.get(
                "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/cli/template/plugins/start.py"
            ).text
        )

        print("Plugins folder has been generated.")

    print("\033[92m" + "GENERATED SUCCESSFULLY")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--template", required=False, action="store_true")
    parser.add_argument(
        "--token", type=str, required=False, help="Your Telegram bot token"
    )
    parser.add_argument(
        "--method",
        type=str,
        required=False,
        help="Telegram API method (e.g., sendMessage)",
    )
    parser.add_argument("args", nargs="*", default=[])

    args = parser.parse_args()

    if args.template:
        return generate()

    elif not args.token and not args.method:
        print(
            "You have to use tgram [-t] to generate a ready-to-use template, otherwise you have to use [--token] & [--method] \n"
            + "For Example: [tgram --token TOKEN --method sendMessage chat_id hi]"
        )

    else:
        token, method, args = (
            args.token,
            camel_to_snake(args.method.replace("send_request", "_send_request")),
            json.loads(args.args[0]) if len(args.args) == 1 else tuple(args.args),
        )
        try:
            bot = TgBot(token)

            if method not in methods:
                print("Wrong method [{}]".format(method))

            func = getattr(bot, method)

            if isinstance(args, dict):
                r = func(**args)
            else:
                r = func(*args)

            print(r)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
