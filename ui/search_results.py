from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)


class SearchResults(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(6)

        best_match_title = QLabel(
            "Mejor coincidencia"
        )

        best_match_title.setObjectName(
            "SearchCategory"
        )

        layout.addWidget(
            best_match_title
        )

        best_match = QPushButton(
            "Firefox"
        )

        best_match.setObjectName(
            "BestMatch"
        )

        layout.addWidget(
            best_match
        )

        results_title = QLabel(
            "Resultados"
        )

        results_title.setObjectName(
            "SearchCategory"
        )

        layout.addWidget(
            results_title
        )

        fake_results = [
            "Firefox Developer Edition",
            "Firewatch",
            "Firewall",
            "Configuración",
            "Documentos",
            "Imágenes"
        ]

        for result in fake_results:

            button = QPushButton(
                result
            )

            button.setObjectName(
                "SearchResult"
            )

            layout.addWidget(
                button
            )

        layout.addStretch()