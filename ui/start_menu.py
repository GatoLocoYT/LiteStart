from PyQt6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QApplication,
    QFrame,
    QScrollArea,
)

from PyQt6.QtCore import Qt, QTimer

from core.search_engine import search

from ui.pinned_apps import PinnedApps
from ui.power_menu import PowerButton
from ui.search_bar import SearchBar
from ui.search_results import SearchResults
from core.launcher import (
    launch_app as launch_system_app
)

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

        root_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        root_layout.setSpacing(0)

        # ==================================================
        # CUERPO PRINCIPAL
        # ==================================================

        main_body = QWidget()

        main_body.setObjectName(
            "MainBody"
        )

        body_layout = QVBoxLayout(
            main_body
        )

        body_layout.setContentsMargins(
            24,
            24,
            24,
            24
        )

        body_layout.setSpacing(
            16
        )

        # ==================================================
        # BARRA SUPERIOR
        # ==================================================

        top_bar = QHBoxLayout()

        top_bar.addStretch()

        close_button = QPushButton("✕")

        close_button.setObjectName(
            "CloseButton"
        )

        close_button.clicked.connect(
            self.close
        )

        top_bar.addWidget(
            close_button
        )

        body_layout.addLayout(
            top_bar
        )

        # ==================================================
        # BUSCADOR
        # ==================================================

        self.search_bar = SearchBar()

        body_layout.addWidget(
            self.search_bar
        )

        # ==================================================
        # RESULTADOS
        # ==================================================

        self.search_results = SearchResults()

        self.search_results.hide()

        # ==================================================
        # APPS ANCLADAS
        # ==================================================

        self.section_title = QLabel(
            "Aplicaciones ancladas"
        )

        self.section_title.setObjectName(
            "SectionTitle"
        )

        self.pinned_apps = PinnedApps()

        # ==================================================
        # SCROLL AREA
        # ==================================================

        scroll_area = QScrollArea()

        scroll_area.setWidgetResizable(
            True
        )

        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        scroll_area.setFrameShape(
            QFrame.Shape.NoFrame
        )

        content_widget = QWidget()

        content_widget.setObjectName(
            "ContentWidget"
        )

        content_layout = QVBoxLayout(
            content_widget
        )

        content_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        content_layout.setSpacing(
            12
        )

        content_layout.addWidget(
            self.search_results
        )

        content_layout.addWidget(
            self.section_title
        )

        content_layout.addWidget(
            self.pinned_apps
        )

        content_layout.addStretch()

        scroll_area.setWidget(
            content_widget
        )

        body_layout.addWidget(
            scroll_area
        )

        self.search_bar.text_changed.connect(
            self.on_search_changed
        )

        self.search_results.result_clicked.connect(
            self.on_result_clicked
        )

        self.pinned_apps.app_clicked.connect(
            self.on_pinned_app_clicked
        )

        self.search_results.pinned_changed.connect(
            self.pinned_apps.reload_apps
        )

        self.pinned_apps.pinned_changed.connect(
            self.pinned_apps.reload_apps
        )

        # ==================================================
        # BARRA INFERIOR
        # ==================================================

        bottom_bar = QFrame()

        bottom_bar.setObjectName(
            "BottomBar"
        )

        bottom_bar.setFixedHeight(
            70
        )

        bottom_layout = QHBoxLayout(
            bottom_bar
        )

        bottom_layout.setContentsMargins(
            20,
            0,
            20,
            0
        )

        bottom_layout.setSpacing(
            10
        )

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
    # LANZADOR
    # ======================================================

    def launch_app(self, app_name):
        success = launch_system_app(
            app_name
        )

        if success:
            self.close()
        

    def on_pinned_app_clicked(self, app_name):

        self.launch_app(
            app_name
        )

    def on_result_clicked(self, result_name):

        self.launch_app(
            result_name
        )

    # ======================================================
    # BÚSQUEDA
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

        if searching:

            results = search(
                text
            )

            self.search_results.update_results(
                results
            )

    # ======================================================
    # EVENTOS
    # ======================================================

    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Escape:

            self.close()
        
        if event.key() == Qt.Key.Key_Down:

            self.search_results.select_next()
            return

        if event.key() == Qt.Key.Key_Up:

            self.search_results.select_previous()
            return

        if event.key() == Qt.Key.Key_Return:

            self.search_results.activate_current()
            return

        if event.key() == Qt.Key.Key_Enter:

            self.search_results.activate_current()
            return

        super().keyPressEvent(
            event
        )

    def focusOutEvent(self, event):

        QTimer.singleShot(
            100,
            self.check_focus
        )

        super().focusOutEvent(
            event
        )

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

        geometry = screen.availableGeometry()

        x = geometry.x() + 10

        y = (
            geometry.y()
            + geometry.height()
            - self.height()
            - 10
        )

        self.move(
            x,
            y
        )