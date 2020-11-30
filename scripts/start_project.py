import os


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
    ]

    translate_table = {ord(char): "" for char in non_url_safe}

    text = text.translate(translate_table)
    text = "_".join(text.split())
    return text.lower()


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    project_name = input("What would you like your project to be called?\n")
    slug = _slugify(project_name)

    # Delete everything reachable from the directory named in "top",
    # assuming there are no symbolic links.
    # CAUTION:  This is dangerous!  For example, if top == '/', it
    # could delete all your disk files.

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

        for _file in _files:
            if "README.md" in _file:
                continue

            with open(os.path.join(_root, _file)) as open_file:
                file_data = open_file.read()

            file_data = file_data.replace("django_template", slug)

            with open(os.path.join(_root, _file), "w") as open_file:
                open_file.write(file_data)

        for _dir in _dirs:
            print(
                f"Renaming: {os.path.join(_root, _dir)} to: {os.path.join(_root, _dir.replace('django_template', slug))}"
            )
            os.rename(
                os.path.join(_root, _dir),
                os.path.join(_root, _dir.replace("django_template", slug)),
            )

    # try:
    #     os.rename(
    #         os.path.join(BASE_DIR, "src", "django_template", "django_template"),
    #         os.path.join(BASE_DIR, "src", "django_template", slug),
    #     )
    #     os.rename(
    #         os.path.join(BASE_DIR, "src", "django_template"),
    #         os.path.join(BASE_DIR, "src", slug),
    #     )
    # except FileNotFoundError:
    #     pass
