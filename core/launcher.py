import os
import shlex
import platform
import subprocess

from core.app_indexer import (
    get_installed_apps
)

IS_WINDOWS = (
    platform.system() == "Windows"
)

IS_LINUX = (
    platform.system() == "Linux"
)


def launch_app(app_name):

    apps_cache = get_installed_apps()

    for app in apps_cache:

        if app["name"] != app_name:
            continue

        try:

            if IS_WINDOWS:

                os.startfile(
                    app["path"]
                )

                return True

            elif IS_LINUX:

                command = shlex.split(
                    app["exec"]
                )

                print(
                    f"Lanzando Linux: {command}"
                )

                subprocess.Popen(
                    command
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