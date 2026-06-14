from pathlib import Path

from PyQt6.QtCore import pyqtSignal, Qt, QSize
from PyQt6.QtGui import QIcon, QGuiApplication

from core.icon_provider import get_app_icon

from PyQt6.QtGui import QIcon

from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QMenu,
)

from core.pinned_apps_manager import load_pinned_apps, unpin_app


class AppButton(QWidget):

    def __init__(self, name, callback, unpin_callback):
        super().__init__()

        self.app_name = name

        self.unpin_callback = unpin_callback

        layout = QVBoxLayout(self)

        layout.setSpacing(4)

        layout.setContentsMargins(0, 0, 0, 0)

        self.button = QPushButton()

        self.button.setObjectName("PinnedAppButton")

        self.button.setIcon(get_app_icon(name))

        self.button.setIconSize(QSize(32, 32))

        self.button.clicked.connect(lambda: callback(self.app_name))

        self.button.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.button.customContextMenuRequested.connect(self.show_context_menu)

        self.label = QLabel(name)

        self.label.setObjectName("AppLabel")

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.label)

    def show_context_menu(self, position):

        menu = QMenu()

        menu.setStyleSheet("""
            QMenu {
                background-color: #FFFFFF;
                border: 1px solid #E5E5E5;
                padding: 4px;
            }

            QMenu::item {
                padding: 8px 24px;
                color: #1C1C1C;
            }

            QMenu::item:selected {
                background-color: #F2F2F2;
            }
        """)

        open_action = menu.addAction("Abrir")

        menu.addSeparator()

        unpin_action = menu.addAction("Desanclar del inicio")

        copy_action = menu.addAction("Copiar nombre")

        selected_action = menu.exec(self.button.mapToGlobal(position))

        if selected_action == open_action:

            self.button.click()

        elif selected_action == unpin_action:

            unpin_app(self.app_name)

            print(f"Desanclando: {self.app_name}")

            self.unpin_callback()

        elif selected_action == copy_action:

            QGuiApplication.clipboard().setText(self.app_name)

            print(f"Copiando: {self.app_name}")


class PinnedApps(QWidget):

    app_clicked = pyqtSignal(str)

    pinned_changed = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.grid = None

        self.setup_ui()

    def setup_ui(self):

        self.grid = QGridLayout(self)

        self.grid.setContentsMargins(0, 8, 0, 0)

        self.grid.setHorizontalSpacing(32)

        self.grid.setVerticalSpacing(18)

        self.reload_apps()

    def reload_apps(self):

        while self.grid.count():

            item = self.grid.takeAt(0)

            widget = item.widget()

            if widget:

                widget.deleteLater()

        pinned_apps = load_pinned_apps()

        for index, app_name in enumerate(pinned_apps):

            row = index // 4

            col = index % 4

            app = AppButton(app_name, self.app_clicked.emit, self.pinned_changed.emit)

            self.grid.addWidget(app, row, col)
