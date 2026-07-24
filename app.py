import sys

from PySide6.QtWidgets import QApplication

from core.config_manager import ConfigManager
from ui.main_window import MainWindow
from ui.styles import APP_STYLE


def main():
    app = QApplication(sys.argv)

    app.setStyleSheet(APP_STYLE)

    config = ConfigManager()

    window = MainWindow(config)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()