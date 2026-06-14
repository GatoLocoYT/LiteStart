from PyQt6.QtGui import QIcon

import platform

from core.app_indexer import (
    get_installed_apps
)

IS_WINDOWS = (
    platform.system() == "Windows"
)

IS_LINUX = (
    platform.system() == "Linux"
)

if IS_WINDOWS:
    import win32com.client


DEFAULT_ICON = QIcon(
    "assets/icons/default.svg"
)


def get_app_icon(app_name):

    apps_cache = get_installed_apps()

    app = next(
        (
            a
            for a in apps_cache
            if a["name"] == app_name
        ),
        None
    )

    if not app:

        return DEFAULT_ICON

    # ==================================================
    # LINUX
    # ==================================================

    if IS_LINUX:

        icon_name = app.get(
            "icon",
            ""
        )

        if icon_name:

            icon = QIcon.fromTheme(
                icon_name
            )

            if not icon.isNull():

                print(
                    f"Icono Linux encontrado: {icon_name}"
                )

                return icon

        return DEFAULT_ICON

    # ==================================================
    # WINDOWS
    # ==================================================

    try:

        shell = win32com.client.Dispatch(
            "WScript.Shell"
        )

        shortcut = shell.CreateShortCut(
            app["path"]
        )

        target = shortcut.Targetpath

        if not target:

            return DEFAULT_ICON

        icon = QIcon(target)

        if icon.isNull():

            return DEFAULT_ICON

        return icon

    except Exception:

        return DEFAULT_ICON