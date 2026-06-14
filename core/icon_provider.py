from PyQt6.QtGui import QIcon

import platform

from core.app_indexer import get_startmenu_apps


IS_WINDOWS = (
    platform.system() == "Windows"
)

if IS_WINDOWS:
    import win32com.client


DEFAULT_ICON = QIcon(
    "assets/icons/default.svg"
)

APPS_CACHE = get_startmenu_apps()


def get_app_icon(app_name):

    if not IS_WINDOWS:

        return DEFAULT_ICON

    print("\n====================")
    print(f"Buscando icono para: {app_name}")

    app = next(
        (
            a
            for a in APPS_CACHE
            if a["name"] == app_name
        ),
        None
    )

    if not app:

        print("Aplicación no encontrada en cache")

        return DEFAULT_ICON

    print("Registro encontrado:")
    print(app)

    try:

        shell = win32com.client.Dispatch(
            "WScript.Shell"
        )

        shortcut = shell.CreateShortCut(
            app["path"]
        )

        target = shortcut.Targetpath

        print(
            f"Shortcut: {app['path']}"
        )

        print(
            f"Target: {target}"
        )

        if not target:

            print(
                "Target vacío"
            )

            return DEFAULT_ICON

        icon = QIcon(target)

        print(
            f"QIcon.isNull(): {icon.isNull()}"
        )

        if icon.isNull():

            print(
                "Qt NO pudo extraer icono del exe"
            )

            return DEFAULT_ICON

        print(
            "Icono cargado correctamente"
        )

        return icon

    except Exception as e:

        print(
            "ERROR obteniendo icono:"
        )

        print(e)

        return DEFAULT_ICON