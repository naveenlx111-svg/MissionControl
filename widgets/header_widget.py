from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QFont

from widgets.clock_widget import ClockWidget


class HeaderWidget(QWidget):

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