from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Mission Control")
        self.resize(1400,850)
        