from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QProgressBar, QVBoxLayout

from widgets.card_widget import CardWidget


class ProgressWidget(CardWidget):

    def __init__(self, config):
        self.config = config
        super().__init__("Overall Progress")

        self.refresh()

    def setup_ui(self, title, value="--", subtitle=""):
        super().setup_ui(title, value, subtitle)

        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_label = QLabel()
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout().insertWidget(3, self.progress_bar)
        self.layout().insertWidget(4, self.progress_label)

    def refresh(self):
        solved = self.config.get("solved_problems")
        total = self.config.get("total_problems")

        percentage = 0
        if total > 0:
            percentage = int((solved / total) * 100)

        self.set_value(f"{percentage}%")

        self.progress_bar.setValue(percentage)
        self.progress_label.setText(f"{solved} / {total} Problems Solved")