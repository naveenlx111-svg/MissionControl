from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QHBoxLayout

from widgets.base_widget import BaseWidget


class ClockWidget(BaseWidget):

    def create_widgets(self):
        self.clock_label = QLabel()

        self.clock_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.clock_label.setFont(font)

    def create_layout(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.clock_label)

    def connect_signals(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

    def refresh(self):
        self.clock_label.setText(
            datetime.now().strftime("%I:%M:%S %p")
        )