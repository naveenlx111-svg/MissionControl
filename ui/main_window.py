from PySide6.QtWidgets import (QMainWindow,
                               QWidget,
                               QVBoxLayout,
                               QHBoxLayout,
                               QLabel,
                               )
from PySide6.QtCore import Qt
from widgets.header_widget import HeaderWidget
from widgets.dashboard_widget import DashboardWidget
from ui.dialogs.settings_dialog import SettingsDialog

class MainWindow(QMainWindow):

    def __init__(self,config):
        super().__init__()
        self.config = config
        self.setup_window()
        self.setup_ui()
        self.connect_signals()

    def setup_window(self):
        self.setWindowTitle("Mission Control")
        self.resize(1400, 850)

    def setup_ui(self):
        #central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        #Main Layout
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)
        self.header_layout = QHBoxLayout()
        self.dashboard_layout = QVBoxLayout()
        self.footer_layout = QHBoxLayout()        
        #Temporary Labels
        self.header = HeaderWidget()
        self.dashboard = DashboardWidget(self.config)

        self.header_layout.addWidget(self.header)
        self.dashboard_layout.addWidget(self.dashboard)
        self.footer_layout.addWidget(QLabel("Footer"))

        #Add layouts
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addLayout(self.dashboard_layout)
        self.main_layout.addLayout(self.footer_layout)


    def connect_signals(self):
        self.header.settings_clicked.connect(self.open_settings)
    def open_settings(self):
        dialog = SettingsDialog()

        dialog.settings_saved.connect(self.dashboard.refresh)

        dialog.exec()