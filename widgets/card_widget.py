from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout
from PySide6.QtCore import Qt

class CardWidget(QWidget):

    def __init__(self,title,value="--",subtitle=""):
        super().__init__()

        self.title = QLabel()
        self.value = QLabel(value)
        self.subtitle = QLabel(subtitle)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.value)
        layout.addStretch()
        layout.addWidget(self.subtitle)