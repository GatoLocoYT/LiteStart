import platform
import subprocess


IS_WINDOWS = (
    platform.system() == "Windows"
)

IS_LINUX = (
    platform.system() == "Linux"
)


def suspend():

    try:

        if IS_LINUX:

            subprocess.Popen(
                ["systemctl", "suspend"]
            )

        elif IS_WINDOWS:

            subprocess.Popen(
                [
                    "rundll32.exe",
                    "powrprof.dll,SetSuspendState",
                    "0,1,0"
                ]
            )

    except Exception as e:

        print(e)


def restart():

    try:

        if IS_LINUX:

            subprocess.Popen(
                ["systemctl", "reboot"]
            )

        elif IS_WINDOWS:

            subprocess.Popen(
                [
                    "shutdown",
                    "/r",
                    "/t",
                    "0"
                ]
            )

    except Exception as e:

        print(e)


def shutdown():

    try:

        if IS_LINUX:

            subprocess.Popen(
                ["systemctl", "poweroff"]
            )

        elif IS_WINDOWS:

            subprocess.Popen(
                [
                    "shutdown",
                    "/s",
                    "/t",
                    "0"
                ]
            )

    except Exception as e:

        print(e)


def logout():

    try:

        if IS_LINUX:

            subprocess.Popen(
                ["gnome-session-quit", "--logout", "--no-prompt"]
            )

        elif IS_WINDOWS:

            subprocess.Popen(
                ["shutdown", "/l"]
            )

    except Exception as e:

        print(e)