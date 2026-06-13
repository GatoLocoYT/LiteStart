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