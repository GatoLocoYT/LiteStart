from pathlib import Path

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
    QVBoxLayout,
    QLabel
)


class AppButton(QWidget):

    def __init__(self, name, icon_name):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setSpacing(4)
        layout.setContentsMargins(0, 0, 0, 0)

        self.button = QPushButton()
        self.button.setObjectName("PinnedAppButton")

        icon_path = Path(f"assets/icons/{icon_name}.svg")

        if not icon_path.exists():
            icon_path = Path("assets/icons/default.svg")

        self.button.setIcon(QIcon(str(icon_path)))
        self.button.setIconSize(QSize(32, 32))

        self.label = QLabel(name)
        self.label.setObjectName("AppLabel")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)


class PinnedApps(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        grid = QGridLayout(self)
        grid.setContentsMargins(0, 8, 0, 0)
        grid.setHorizontalSpacing(32)
        grid.setVerticalSpacing(18)

        apps = [
            {"name": "Firefox", "icon": "firefox"},
            {"name": "VSCode", "icon": "vscode"},
            {"name": "Steam", "icon": "steam"},
            {"name": "Discord", "icon": "discord"},
            {"name": "VLC", "icon": "vlc"},
            {"name": "Files", "icon": "files"},
            {"name": "OBS", "icon": "obs"},
            {"name": "Terminal", "icon": "terminal"},
        ]

        for index, app_data in enumerate(apps):
            row = index // 4
            col = index % 4

            app = AppButton(
                app_data["name"],
                app_data["icon"]
            )

            grid.addWidget(app, row, col)