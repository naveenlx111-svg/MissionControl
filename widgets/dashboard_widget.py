from PySide6.QtWidgets import QWidget, QGridLayout
from widgets.card_widget import CardWidget


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