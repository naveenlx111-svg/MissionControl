from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QProgressBar, QVBoxLayout
from widgets.circular_progress import CircularProgress
from widgets.card_widget import CardWidget


class ProgressWidget(CardWidget):

    def __init__(self, config):
        self.config = config
        super().__init__("Overall Progress")


    def setup_ui(self, title, value="--", subtitle=""):
        super().setup_ui(title, value, subtitle)

        self.progress_ring = CircularProgress()
        self.progress_label = QLabel()

        self.layout().insertWidget(3, self.progress_ring)
        self.layout().insertWidget(4, self.progress_label)
        self.refresh()

    def refresh(self):
        solved = self.config.get("solved_problems")
        total = self.config.get("total_problems")

        percentage = 0
        if total > 0:
            percentage = int((solved / total) * 100)

        self.set_value(f"{percentage}%")

        self.progress_ring.set_progress(percentage)
        self.progress_label.setText(f"{solved} / {total} Problems Solved")