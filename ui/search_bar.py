from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QLineEdit
)


class SearchBar(QWidget):

    text_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(8)

        self.search_icon = QLabel("🔍")

        self.search_input = QLineEdit()

        self.search_input.setPlaceholderText(
            "Buscar aplicaciones, archivos y configuraciones"
        )

        self.search_input.textChanged.connect(
            self.text_changed.emit
        )

        layout.addWidget(
            self.search_icon
        )

        layout.addWidget(
            self.search_input
        )