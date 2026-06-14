from PyQt6.QtCore import (
    pyqtSignal,
    Qt
)

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QMenu
)
from PyQt6.QtGui import QGuiApplication

from core.pinned_apps_manager import (
    pin_app
)


class SearchResults(QWidget):

    result_clicked = pyqtSignal(str)

    pinned_changed = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.current_index = 0

        self.result_buttons = []

        self.setup_ui()

    def setup_ui(self):

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.layout.setSpacing(6)

    def clear_results(self):

        while self.layout.count():

            item = self.layout.takeAt(0)

            widget = item.widget()

            if widget:

                widget.deleteLater()

    def show_context_menu(
        self,
        button,
        position
    ):

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
                border-radius: 4px;
            }
        """)

        open_action = menu.addAction(
            "Abrir"
        )
        menu.addSeparator()
        
        pin_action = menu.addAction(
            "Anclar al inicio"
        )

        copy_action = menu.addAction(
            "Copiar nombre"
        )

        selected_action = menu.exec(
            button.mapToGlobal(position)
        )

        if selected_action == open_action:

            self.result_clicked.emit(
                button.text()
            )

        elif selected_action == pin_action:

            pin_app(
                button.text()
            )

            print(
                f"Anclada: {button.text()}"
            )

            self.pinned_changed.emit()

        elif selected_action == copy_action:
            QGuiApplication.clipboard().setText(
                button.text()
            )

    def create_result_button(
        self,
        text,
        object_name
    ):

        button = QPushButton(text)

        button.setObjectName(
            object_name
        )

        button.clicked.connect(
            lambda: self.result_clicked.emit(text)
        )

        button.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        button.customContextMenuRequested.connect(
            lambda pos,
            btn=button:
            self.show_context_menu(
                btn,
                pos
            )
        )

        return button

    def update_results(self, results):

        self.clear_results()

        self.result_buttons.clear()

        self.current_index = 0

        if not results:

            no_results = QLabel(
                "Sin resultados"
            )

            no_results.setObjectName(
                "SearchCategory"
            )

            self.layout.addWidget(
                no_results
            )

            return

        best_title = QLabel(
            "Mejor coincidencia"
        )

        best_title.setObjectName(
            "SearchCategory"
        )

        self.layout.addWidget(
            best_title
        )

        best_match = self.create_result_button(
            results[0],
            "BestMatch"
        )

        self.result_buttons.append(
            best_match
        )

        self.layout.addWidget(
            best_match
        )

        if len(results) > 1:

            results_title = QLabel(
                "Resultados"
            )

            results_title.setObjectName(
                "SearchCategory"
            )

            self.layout.addWidget(
                results_title
            )

            for result in results[1:]:

                button = self.create_result_button(
                    result,
                    "SearchResult"
                )

                self.result_buttons.append(
                    button
                )

                self.layout.addWidget(
                    button
                )

        self.update_selection()

        self.layout.addStretch()

    def update_selection(self):

        for index, button in enumerate(
            self.result_buttons
        ):

            button.setProperty(
                "selected",
                index == self.current_index
            )

            button.style().unpolish(
                button
            )

            button.style().polish(
                button
            )

            button.update()

    def select_next(self):

        if not self.result_buttons:
            return

        self.current_index = min(
            self.current_index + 1,
            len(self.result_buttons) - 1
        )

        self.update_selection()

    def select_previous(self):

        if not self.result_buttons:
            return

        self.current_index = max(
            self.current_index - 1,
            0
        )

        self.update_selection()

    def activate_current(self):

        if not self.result_buttons:
            return

        self.result_buttons[
            self.current_index
        ].click()