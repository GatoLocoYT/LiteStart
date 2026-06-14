import sys

from PyQt6.QtWidgets import QApplication

from ui.start_menu import StartMenu

from core.paths import (
    STYLES_DIR
)


def load_styles(app):

    with open(
        STYLES_DIR / "theme.qss",
        "r",
        encoding="utf-8"
    ) as file:

        app.setStyleSheet(
            file.read()
        )


def main():

    app = QApplication(
        sys.argv
    )

    load_styles(app)

    menu = StartMenu()

    menu.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()