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

    translate_table = {ord(char): u"" for char in non_url_safe}

    text = text.translate(translate_table)
    text = u"_".join(text.split())
    return text.lower()


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    project_name = input("What would you like your project to be called?\n")
    slug = _slugify(project_name)

    files_to_change = [
        os.path.join(BASE_DIR, "useful_information.txt"),
        os.path.join(BASE_DIR, "pyproject.toml"),
        os.path.join(BASE_DIR, "docker-compose.yml"),
        os.path.join(
            BASE_DIR, "src", "django_template", "django_template", "main", "__init__.py"
        ),
        os.path.join(
            BASE_DIR, "src", "django_template", "django_template", "main", "apps.py"
        ),
        os.path.join(
            BASE_DIR,
            "src",
            "django_template",
            "django_template",
            "account",
            "__init__.py",
        ),
        os.path.join(
            BASE_DIR, "src", "django_template", "django_template", "account", "apps.py"
        ),
        os.path.join(BASE_DIR, "src", "django_template", "config", "urls.py"),
        os.path.join(
            BASE_DIR, "src", "django_template", "config", "settings", "base.py"
        ),
        os.path.join(BASE_DIR, "docker", "development", "Dockerfile"),
        os.path.join(BASE_DIR, "docker", "production", "Dockerfile"),
        os.path.join(BASE_DIR, ".envs", "development", ".postgres"),
        os.path.join(BASE_DIR, ".envs", "production", ".postgres"),
    ]

    for file in files_to_change:
        with open(file) as open_file:
            file_data = open_file.read()

        file_data = file_data.replace("django_template", slug)

        with open(file, "w") as open_file:
            open_file.write(file_data)

    os.rename(
        os.path.join(BASE_DIR, "src", "django_template", "django_template"),
        os.path.join(BASE_DIR, "src", "django_template", slug),
    )
    os.rename(
        os.path.join(BASE_DIR, "src", "django_template"),
        os.path.join(BASE_DIR, "src", slug),
    )
