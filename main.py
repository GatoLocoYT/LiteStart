import sys

from PyQt6.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMenu
)

from PyQt6.QtGui import (
    QIcon,
    QAction
)

from ui.start_menu import StartMenu

from core.paths import (
    STYLES_DIR,
    ASSETS_DIR
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

    menu.show_menu()


    print(
        "Tray disponible:",
        QSystemTrayIcon.isSystemTrayAvailable()
    )

    tray = QSystemTrayIcon()

    tray.setIcon(
        QIcon(
            str(
                ASSETS_DIR
                / "icons"
                / "icon.svg"
            )
        )
    )

    tray.setToolTip(
        "LiteStart"
    )

    tray_menu = QMenu()

    show_action = QAction(
        "Mostrar LiteStart",
        tray
    )

    exit_action = QAction(
        "Salir",
        tray
    )

    tray_menu.addAction(
        show_action
    )

    tray_menu.addSeparator()

    tray_menu.addAction(
        exit_action
    )

    tray.setContextMenu(
        tray_menu
    )

    show_action.triggered.connect(
        menu.show_menu
    )

    exit_action.triggered.connect(
        app.quit
    )

    def on_tray_activated(reason):

        if (
            reason
            ==
            QSystemTrayIcon.ActivationReason.Trigger
        ):

            if menu.isVisible():

                menu.hide_menu()

            else:

                menu.show_menu()

    tray.activated.connect(
        on_tray_activated
    )

    tray.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()