import os

from core.app_indexer import (
    get_startmenu_apps
)

APPS_CACHE = get_startmenu_apps()


def launch_app(app_name):

    for app in APPS_CACHE:

        if app["name"] == app_name:

            try:

                os.startfile(
                    app["path"]
                )

                return True

            except Exception as e:

                print(
                    f"Error lanzando {app_name}: {e}"
                )

                return False

    print(
        f"No encontrada: {app_name}"
    )

    return False