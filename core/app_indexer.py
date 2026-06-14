# app_indexer.py
import platform
from pathlib import Path


def get_startmenu_apps():
    apps = []

    locations = [
        Path(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        ),
        Path.home()
        / "AppData"
        / "Roaming"
        / "Microsoft"
        / "Windows"
        / "Start Menu"
        / "Programs"
    ]

    for location in locations:
        if not location.exists():
            continue

        for shortcut in location.rglob("*.lnk"):
            apps.append(
                {
                    "name": shortcut.stem,
                    "path": str(shortcut)
                }
            )

    return apps


def get_installed_apps():
    system = platform.system()

    if system == "Windows":
        return get_startmenu_apps()

    if system == "Linux":
        from core.linux_indexer import get_linux_apps
        return get_linux_apps()

    return []