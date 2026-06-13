from PyQt6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QApplication,
    QFrame
)

from PyQt6.QtCore import Qt, QTimer

from ui import search_results
from ui.pinned_apps import PinnedApps
from ui.power_menu import PowerButton
from ui.search_bar import SearchBar
from ui.search_results import SearchResults

from core.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)


class StartMenu(QWidget):

    def __init__(self):
        super().__init__()

        self.menu_open = False

        self.setup_ui()
        self.position_window()

    def setup_ui(self):

        self.setWindowTitle("LiteStart")

        self.setFixedSize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Tool
            | Qt.WindowType.WindowStaysOnTopHint
        )

        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # ==================================================
        # CUERPO PRINCIPAL
        # ==================================================

        main_body = QWidget()
        main_body.setObjectName("MainBody")

        body_layout = QVBoxLayout(main_body)

        body_layout.setContentsMargins(
            24,
            24,
            24,
            24
        )

        body_layout.setSpacing(16)

        # ==================================================
        # BARRA SUPERIOR
        # ==================================================

        top_bar = QHBoxLayout()

        top_bar.addStretch()

        close_button = QPushButton("✕")
        close_button.setObjectName("CloseButton")

        close_button.clicked.connect(
            self.close
        )

        top_bar.addWidget(close_button)

        body_layout.addLayout(top_bar)

        # ==================================================
        # BUSCADOR
        # ==================================================

        self.search_bar = SearchBar()

        body_layout.addWidget(
            self.search_bar
        )

        self.search_results = SearchResults()

        self.search_results.hide()

        body_layout.addWidget(
            self.search_results
        )

        self.search_bar.text_changed.connect(
            self.on_search_changed
        )

        # ==================================================
        # APLICACIONES ANCLADAS
        # ==================================================

        self.section_title = QLabel(
            "Aplicaciones ancladas"
        )

        self.section_title.setObjectName(
            "SectionTitle"
        )

        self.pinned_apps = PinnedApps()

        body_layout.addWidget(self.section_title)
        body_layout.addWidget(self.pinned_apps)

        body_layout.addStretch()

        # ==================================================
        # BARRA INFERIOR
        # ==================================================

        bottom_bar = QFrame()

        bottom_bar.setObjectName(
            "BottomBar"
        )

        bottom_bar.setFixedHeight(70)

        bottom_layout = QHBoxLayout(
            bottom_bar
        )

        bottom_layout.setContentsMargins(
            20,
            0,
            20,
            0
        )

        bottom_layout.setSpacing(10)

        user_label = QLabel(
            "Usuario"
        )

        user_label.setObjectName(
            "UserLabel"
        )

        bottom_layout.addWidget(
            user_label
        )

        bottom_layout.addStretch()

        self.power_button = PowerButton()

        bottom_layout.addWidget(
            self.power_button
        )

        # ==================================================
        # ENSAMBLADO FINAL
        # ==================================================

        root_layout.addWidget(
            main_body
        )

        root_layout.addWidget(
            bottom_bar
        )

    # ======================================================
    # EVENTOS
    # ======================================================
    def on_search_changed(self, text):

        searching = len(
            text.strip()
        ) > 0

        self.search_results.setVisible(
            searching
        )

        self.section_title.setVisible(
            not searching
        )

        self.pinned_apps.setVisible(
            not searching
        )

    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Escape:
            self.close()

        super().keyPressEvent(event)

    def focusOutEvent(self, event):

        QTimer.singleShot(
            100,
            self.check_focus
        )

        super().focusOutEvent(event)

    def check_focus(self):

        active_window = QApplication.activeWindow()

        if active_window is None:
            self.close()
            return

        if active_window != self:
            self.close()

    # ======================================================
    # POSICIONAMIENTO
    # ======================================================

    def position_window(self):

        screen = QApplication.primaryScreen()

        geometry = (
            screen.availableGeometry()
        )

        x = 10

        y = (
            geometry.height()
            - self.height()
            - 10
        )

        self.move(x, y)
    