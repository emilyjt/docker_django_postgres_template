import os
import secrets
import uuid
from pathlib import Path

RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    """
    Return a securely generated random string.
    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)
    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return "".join(secrets.choice(allowed_chars) for i in range(length))


def get_random_secret_key():
    """
    Return a 50 character random string usable as a SECRET_KEY setting value.
    """
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789!@#$%^*-_+"
    return get_random_string(50, chars)


if __name__ == "__main__":
    # Use like: BASE_DIR / ".env"
    BASE_DIR = Path(__file__).resolve().parent

    domain_name = input("Please enter the domain name this will be deployed to:\n")
    service_name = domain_name.split(".")[0]

    ###########################################################################
    # This section performs the following tasks:
    #     - Renames `.env_example` to `.env`
    #     - Adds the user provided `domain_name` to .env
    #     - Generates a `service_name` from the `domain_name` and adds it to
    #       the .env file as well
    #     - Generates a uuid4 and uses it for the django admin url
    #     - Generates some passwords automatically and adds them to the .env
    ###########################################################################

    try:
        os.rename(BASE_DIR / ".env_example", BASE_DIR / ".env")
    except Exception:
        pass

    with open(BASE_DIR / ".env") as f:
        env_data = f.read()

    new_env = env_data

    new_env = new_env.replace("example.co.uk", domain_name, 1)
    new_env = new_env.replace("templates_django", service_name, 1)
    new_env = new_env.replace("example_url", str(uuid.uuid4()), 1)

    while "example_password" in new_env:
        new_env = new_env.replace("example_password", get_random_secret_key(), 1)

    if env_data != new_env:
        with open(BASE_DIR / ".env", "w") as f:
            f.write(new_env)

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

        if "database" in _root:
            continue

        for _file in _files:
            if "README.md" in _file:
                continue

            if ".env" in _file:
                continue

            if "www.init.py" in _file:
                continue

            try:
                with open(os.path.join(_root, _file)) as open_file:
                    file_data = open_file.read()
            except Exception:
                continue

            new_data = file_data.replace("templates_django", service_name)

            if new_data != file_data:
                with open(os.path.join(_root, _file), "w") as open_file:
                    open_file.write(new_data)

                    files_total += 1

        for _dir in _dirs:
            if "templates_django" in _dir:
                os.rename(
                    os.path.join(_root, _dir),
                    os.path.join(_root, _dir.replace("templates_django", service_name)),
                )

                dirs_total += 1

    print(
        f"{ files_total } files have been updated, and { dirs_total } directories have been renamed."
    )
