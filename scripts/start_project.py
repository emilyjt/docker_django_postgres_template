import os
import string
import secrets


def _slugify(text):
    non_url_safe = [
        '"',
        "#",
        "$",
        "%",
        "&",
        "+",
        ",",
        "/",
        ":",
        ";",
        "=",
        "?",
        "@",
        "[",
        "\\",
        "]",
        "^",
        "`",
        "{",
        "|",
        "}",
        "~",
        "'",
        ".",
    ]

    translate_table = {ord(char): "" for char in non_url_safe}

    text = text.translate(translate_table)
    text = "_".join(text.split())
    return text.lower()


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    project_name = input("What would you like your project to be called?\n")
    slug = _slugify(project_name)

    ##########
    # Generate the .env secrets
    ##########
    alphabet = string.ascii_letters + string.digits

    secrets_total = 0

    for _root, _dirs, _files in os.walk(os.path.join(BASE_DIR, ".envs"), topdown=False):
        for _file in _files:
            with open(os.path.join(_root, _file)) as open_file:
                file_data = open_file.read()

            new_data = file_data

            while "template_default_secret" in new_data:
                password = "".join(secrets.choice(alphabet) for i in range(48))
                new_data = new_data.replace("template_default_secret", password, 1)

            if new_data != file_data:
                with open(os.path.join(_root, _file), "w") as open_file:
                    open_file.write(new_data)

                    secrets_total += 1

    print(f"{ secrets_total } secrets have been generated in the /.envs folder.")

    ##########
    # Rename files and folders
    ##########
    files_total = 0
    dirs_total = 0

    for _root, _dirs, _files in os.walk(BASE_DIR, topdown=False):
        if ".git" in _root:
            continue

        if ".venv" in _root:
            continue

        if ".vscode" in _root:
            continue

        if "__pycache__" in _root:
            continue

        if "scripts" in _root:
            continue

        if ".egg-info" in _root:
            continue

        if "node_modules" in _root:
            continue

        for _file in _files:
            if "README.md" in _file:
                continue

            if ".env_example" in _file:
                try:
                    os.rename(os.path.join(_root, _file), os.path.join(_root, ".env"))
                except Exception:
                    pass
                continue

            try:
                with open(os.path.join(_root, _file)) as open_file:
                    file_data = open_file.read()
            except Exception:
                continue

            new_data = file_data.replace("django_template", slug)

            if new_data != file_data:
                with open(os.path.join(_root, _file), "w") as open_file:
                    open_file.write(new_data)

                    files_total += 1

        for _dir in _dirs:
            if "django_template" in _dir:
                os.rename(
                    os.path.join(_root, _dir),
                    os.path.join(_root, _dir.replace("django_template", slug)),
                )

                dirs_total += 1

    print(
        f"{ files_total } files have been updated, and { dirs_total } directories have been renamed."
    )
