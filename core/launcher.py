import os
import platform
import subprocess

from core.app_indexer import (
    get_installed_apps
)

APPS_CACHE = get_installed_apps()

IS_WINDOWS = (
    platform.system() == "Windows"
)

IS_LINUX = (
    platform.system() == "Linux"
)


def launch_app(app_name):

    for app in APPS_CACHE:

        if app["name"] != app_name:
            continue

        try:

            if IS_WINDOWS:

                os.startfile(
                    app["path"]
                )

                return True

            elif IS_LINUX:

                subprocess.Popen(
                    app["exec"].split()
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