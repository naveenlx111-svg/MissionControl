from PySide6.QtWidgets import QLabel, QVBoxLayout, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class CardWidget(QFrame):
    def __init__(self, title, value="--", subtitle=""):
        super().__init__()

        self.setup_ui(title, value, subtitle)

    def setup_ui(self, title, value, subtitle):
        # ---------- Card ----------
        self.setObjectName("Card")
        self.setMinimumHeight(180)

        # ---------- Labels ----------
        self.title = QLabel(title)
        self.value = QLabel(str(value))
        self.subtitle = QLabel(subtitle)

        self.title.setObjectName("CardTitle")
        self.value.setObjectName("CardValue")
        self.subtitle.setObjectName("CardSubtitle")

        # ---------- Alignment ----------
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ---------- Fonts ----------
        title_font = QFont()
        title_font.setPointSize(11)
        title_font.setBold(True)

        value_font = QFont()
        value_font.setPointSize(32)
        value_font.setBold(True)

        subtitle_font = QFont()
        subtitle_font.setPointSize(10)

        self.title.setFont(title_font)
        self.value.setFont(value_font)
        self.subtitle.setFont(subtitle_font)

        # ---------- Layout ----------
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.value)
        layout.addStretch()
        layout.addWidget(self.subtitle)

    # ---------- Public API ----------

    def set_title(self, title):
        self.title.setText(title)

    def set_value(self, value):
        self.value.setText(str(value))

    def set_subtitle(self, subtitle):
        self.subtitle.setText(subtitle)