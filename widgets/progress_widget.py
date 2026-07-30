from widgets.circular_progress import CircularProgress
from widgets.card_widget import CardWidget
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QProgressBar,QVBoxLayout,QLabel,QPushButton,QHBoxLayout

class ProgressWidget(CardWidget):
    problem_updated = Signal()
    def __init__(self, config):
        self.config = config
        super().__init__("Overall Progress")


    def setup_ui(self, title, value="--", subtitle=""):
        super().setup_ui(title, value, subtitle)

        self.progress_ring = CircularProgress()
        self.progress_label = QLabel()

        self.plus_btn = QPushButton("+1")
        self.minus_btn = QPushButton("-1")
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.minus_btn)
        button_layout.addWidget(self.plus_btn)
        self.plus_btn.clicked.connect(self.increment)
        self.minus_btn.clicked.connect(self.decrement)

        self.layout().insertWidget(3, self.progress_ring)
        self.layout().insertWidget(4, self.progress_label)
        self.layout().insertLayout(5, button_layout)
        self.refresh()

    def increment(self):
        solved = self.config.get("solved_problems", 0)
        total = self.config.get("total_problems", 0)
        if solved < total:
            self.config.set("solved_problems", solved + 1)
            self.refresh()
            self.problem_updated.emit()

    def decrement(self):
        solved = self.config.get("solved_problems", 0)
        if solved > 0:
            self.config.set("solved_problems", solved - 1)
            self.refresh()
            self.problem_updated.emit()

    def refresh(self):
        solved = self.config.get("solved_problems")
        total = self.config.get("total_problems")

        percentage = 0
        if total > 0:
            percentage = int((solved / total) * 100)

        self.set_value(f"{percentage}%")

        self.progress_ring.set_progress(percentage)
        self.progress_label.setText(f"{solved} / {total} Problems Solved")