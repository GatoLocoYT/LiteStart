from pathlib import Path

from PyQt6.QtCore import (
    pyqtSignal,
    Qt,
    QSize
)

from PyQt6.QtGui import QIcon

from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
    QVBoxLayout,
    QLabel
)

from core.pinned_apps_manager import (
    load_pinned_apps
)


class AppButton(QWidget):

    def __init__(self, name, callback):
        super().__init__()

        self.app_name = name

        layout = QVBoxLayout(self)

        layout.setSpacing(4)

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.button = QPushButton()

        self.button.setObjectName(
            "PinnedAppButton"
        )

        icon_path = Path(
            "assets/icons/default.svg"
        )

        self.button.setIcon(
            QIcon(str(icon_path))
        )

        self.button.setIconSize(
            QSize(32, 32)
        )

        self.button.clicked.connect(
            lambda: callback(self.app_name)
        )

        self.label = QLabel(name)

        self.label.setObjectName(
            "AppLabel"
        )

        self.label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            self.button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            self.label
        )


class PinnedApps(QWidget):

    app_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        grid = QGridLayout(self)

        grid.setContentsMargins(
            0,
            8,
            0,
            0
        )

        grid.setHorizontalSpacing(
            32
        )

        grid.setVerticalSpacing(
            18
        )

        pinned_apps = load_pinned_apps()

        for index, app_name in enumerate(
            pinned_apps
        ):

            row = index // 4

            col = index % 4

            app = AppButton(
                app_name,
                self.app_clicked.emit
            )

            grid.addWidget(
                app,
                row,
                col
            )