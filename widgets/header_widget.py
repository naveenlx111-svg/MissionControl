from PySide6.QtWidgets import QWidget,QLabel,QHBoxLayout
from PySide6.QtCore import Qt,QTimer
from datetime import datetime

class HeaderWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.start_timer()
    
    def setup_ui(self):
        layout = QHBoxLayout(self)

        self.title = QLabel("Mission Control")
        self.time = QLabel()

        self.title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.time.setAlignment(Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.time)

    def start_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.update_time()
        self.timer.start(1000)

    def update_time(self):
        now = datetime.now()
        self.time.setText(now.strftime("%d %b %Y   %H:%M:%S"))