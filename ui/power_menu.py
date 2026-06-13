from PyQt6.QtWidgets import (
    QPushButton,
    QMenu
)


class PowerButton(QPushButton):

    def __init__(self):
        super().__init__("⏻")

        self.setObjectName(
            "PowerButton"
        )

        self.setup_menu()

    def setup_menu(self):

        menu = QMenu(self)

        menu.setObjectName(
            "PowerMenu"
        )

        suspend_action = menu.addAction(
            "Suspender"
        )

        restart_action = menu.addAction(
            "Reiniciar"
        )

        shutdown_action = menu.addAction(
            "Apagar"
        )

        logout_action = menu.addAction(
            "Cerrar sesión"
        )

        suspend_action.triggered.connect(
            lambda: print("Presionado Suspender")
        )

        restart_action.triggered.connect(
            lambda: print("Presionado Reiniciar")
        )

        shutdown_action.triggered.connect(
            lambda: print("Presionado Apagar")
        )

        logout_action.triggered.connect(
            lambda: print("Presionado Cerrar sesión")
        )

        self.setMenu(menu)