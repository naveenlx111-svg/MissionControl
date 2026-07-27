from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton
from widgets.clock_widget import ClockWidget
from ui.dialogs.settings_dialogs import SettingsDialog

class HeaderWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def open_settings(self):
        dialog = SettingsDialog()
        dialog.exec()

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
        self.settings_btn.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_btn)