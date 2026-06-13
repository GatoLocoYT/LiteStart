import json
from pathlib import Path

PINNED_APPS_FILE = Path(
    "config/pinned_apps.json"
)


def load_pinned_apps():

    if not PINNED_APPS_FILE.exists():

        return []

    with open(
        PINNED_APPS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_pinned_apps(apps):

    with open(
        PINNED_APPS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            apps,
            file,
            indent=4,
            ensure_ascii=False
        )


def pin_app(app_name):

    apps = load_pinned_apps()

    if app_name not in apps:

        apps.append(app_name)

        save_pinned_apps(apps)


def unpin_app(app_name):

    apps = load_pinned_apps()

    if app_name in apps:

        apps.remove(app_name)

        save_pinned_apps(apps)