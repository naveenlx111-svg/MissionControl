from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton
from widgets.clock_widget import ClockWidget
from PySide6.QtCore import Signal

class HeaderWidget(QWidget):
    settings_clicked = Signal()
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)

        title = QLabel("Mission Control")

        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        title.setFont(font)

        layout.addWidget(title)
        layout.addStretch()
        clock = ClockWidget()
        clock.setStyleSheet("background:red;")
        layout.addWidget(clock)

        self.settings_btn = QPushButton("⚙")
        self.settings_btn.setFixedSize(40, 40)
        self.settings_btn.clicked.connect(self.settings_clicked.emit)
        layout.addWidget(self.settings_btn)