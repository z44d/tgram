from argparse import ArgumentParser, Namespace


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="This script is only to generate ready-template :)"
    )

    parser.add_argument("-t", "--template", required=True, action="store_true")

    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.template:
        TEMPLATE = {
            ".env": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/template/.env",
            ".gitignore": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/template/.gitignore",
            "README.md": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/template/generate.md",
            "config.py": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/template/config.py",
            "main.py": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/template/main.py",
            "requirements.txt": "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/template/requirements.txt",
        }

        import requests

        print("Generating ready-template..")

        for i in TEMPLATE:
            with open(i, "w+", encoding="utf-8") as f:
                f.write(requests.get(TEMPLATE.get(i)).text)

                print(f"File [ {i} ] has been generated.")

        import os

        if not os.path.isdir("plugins"):
            os.mkdir("plugins")

        with open("plugins/start.py", "w+", encoding="utf-8") as f:
            f.write(
                requests.get(
                    "https://raw.githubusercontent.com/z44d/tgram/refs/heads/main/tgram/template/plugins/start.py"
                ).text
            )

            print("Plugins folder has been generated.")

        print("\033[92m" + "GENERATED SUCCESSFULLY")

if __name__ == "__main__":
    main()