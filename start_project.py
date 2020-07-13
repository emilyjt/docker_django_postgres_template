"""

"""

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
        os.path.join(BASE_DIR, "django_template", "account", "__init__.py"),
        os.path.join(BASE_DIR, "django_template", "account", "apps.py"),
        os.path.join(BASE_DIR, "django_template", "main", "__init__.py"),
        os.path.join(BASE_DIR, "django_template", "main", "apps.py"),
        os.path.join(BASE_DIR, "config", "urls.py"),
        os.path.join(BASE_DIR, "config", "settings", "base.py"),
    ]

    for file in files_to_change:
        with open(file) as open_file:
            if "django_template" in open_file.read():
                print("true")
