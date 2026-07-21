from PySide6.QtWidgets import QWidget, QGridLayout
from widgets.card_widget import CardWidget
from utils.date_utils import days_remaining

class DashboardWidget(QWidget):

    def __init__(self,config):
        super().__init__()
        self.config = config
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)

        countdown = CardWidget(
            "Countdown",
            "154",
            "Days Remaining"
        )

        problems = CardWidget(
            "Problems",
            "623",
            "Remaining"
        )

        daily_goal = CardWidget(
            "Daily Goal",
            "10",
            "Problems Today"
        )

        topic = CardWidget(
            "Current Topic",
            "Dynamic Programming",
            "Current Focus"
        )

        layout.addWidget(countdown, 0, 0)
        layout.addWidget(problems, 0, 1)
        layout.addWidget(daily_goal, 1, 0)
        layout.addWidget(topic, 1, 1)
    def refresh(self):
        self.countdown_card.set_value(
                days_remaining(
                    self.config.get("target_date")
                )
            )

        self.problems_card.set_value(
            self.config.get("total_problems")
            - self.config.get("solved_problems")
        )

        self.daily_goal_card.set_value(
            self.config.get("daily_goal")
        )

        self.topic_card.set_value(
            self.config.get("current_topic")
        )
