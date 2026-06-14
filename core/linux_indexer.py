from pathlib import Path
import configparser


DESKTOP_DIRS = [
    Path("/usr/share/applications"),
    Path.home() / ".local/share/applications",
    Path("/var/lib/snapd/desktop/applications"),
]


def clean_exec_command(exec_cmd):
    # Los .desktop suelen traer placeholders tipo %U, %u, %F, %f, %i, %c, %k
    parts_to_remove = [
        "%U", "%u", "%F", "%f", "%i", "%c", "%k"
    ]

    for part in parts_to_remove:
        exec_cmd = exec_cmd.replace(part, "")

    return exec_cmd.strip()


def should_skip(entry):
    if entry.get("Type", "") != "Application":
        return True

    if entry.get("NoDisplay", "").lower() == "true":
        return True

    if entry.get("Hidden", "").lower() == "true":
        return True

    if not entry.get("Name", ""):
        return True

    if not entry.get("Exec", ""):
        return True

    return False


def get_linux_apps():
    apps = []

    for directory in DESKTOP_DIRS:
        if not directory.exists():
            continue

        for desktop_file in directory.glob("*.desktop"):
            try:
                config = configparser.ConfigParser(
                    interpolation=None,
                    strict=False
                )

                config.read(
                    desktop_file,
                    encoding="utf-8"
                )

                if "Desktop Entry" not in config:
                    continue

                entry = config["Desktop Entry"]

                if should_skip(entry):
                    continue

                name = entry.get("Name", "").strip()
                exec_cmd = clean_exec_command(
                    entry.get("Exec", "")
                )
                icon = entry.get("Icon", "").strip()

                apps.append(
                    {
                        "name": name,
                        "path": exec_cmd,
                        "exec": exec_cmd,
                        "icon": icon,
                        "desktop_file": str(desktop_file),
                    }
                )

            except Exception as error:
                print(
                    f"Error leyendo {desktop_file}: {error}"
                )

    apps.sort(
        key=lambda app: app["name"].lower()
    )

    return apps