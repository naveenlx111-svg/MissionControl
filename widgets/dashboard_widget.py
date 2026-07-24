from PySide6.QtWidgets import QWidget, QGridLayout

from widgets.card_widget import CardWidget
from utils.date_utils import days_remaining


class DashboardWidget(QWidget):

    def __init__(self, config):
        super().__init__()

        self.config = config

        self.setup_ui()
        self.refresh()

    def setup_ui(self):
        layout = QGridLayout(self)

        self.countdown_card = CardWidget(
            "Countdown",
            "--",
            "Days Remaining"
        )

        self.problems_card = CardWidget(
            "Problems",
            "--",
            "Remaining"
        )

        self.daily_goal_card = CardWidget(
            "Daily Goal",
            "--",
            "Problems Today"
        )

        self.topic_card = CardWidget(
            "Current Topic",
            "--",
            "Current Focus"
        )

        layout.addWidget(self.countdown_card, 0, 0)
        layout.addWidget(self.problems_card, 0, 1)
        layout.addWidget(self.daily_goal_card, 1, 0)
        layout.addWidget(self.topic_card, 1, 1)

    def refresh(self):
        self.countdown_card.set_value(
            days_remaining(
                self.config.get("target_date")
            )
        )

        remaining_problems = (
            self.config.get("total_problems")
            - self.config.get("solved_problems")
        )

        self.problems_card.set_value(remaining_problems)

        self.daily_goal_card.set_value(
            self.config.get("daily_goal")
        )

        self.topic_card.set_value(
            self.config.get("current_topic")
        )