from PyQt6.QtWidgets import (
    QPushButton,
    QMenu
)
from core.power_actions import (
    suspend,
    restart,
    shutdown,
    logout
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
            suspend
        )

        restart_action.triggered.connect(
            restart
        )

        shutdown_action.triggered.connect(
            shutdown
        )

        logout_action.triggered.connect(
            logout
        )

        self.setMenu(menu)