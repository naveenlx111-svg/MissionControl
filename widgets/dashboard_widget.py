from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy
from widgets.progress_widget import ProgressWidget
from widgets.daily_goal_widget import DailyGoalWidget
from widgets.topic_widget import TopicWidget
from widgets.countdown_widget import CountdownWidget

class DashboardWidget(QWidget):

    def __init__(self, config):
        super().__init__()

        self.config = config

        self.setup_ui()
        self.refresh()

    def setup_ui(self):
        layout = QGridLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(20)

        self.countdown_card = CountdownWidget(self.config)

        self.problems_card = ProgressWidget(self.config)

        self.daily_goal_card = DailyGoalWidget(self.config)

        self.topic_card = TopicWidget(self.config)
        cards = [
            self.countdown_card,
            self.problems_card,
            self.daily_goal_card,
            self.topic_card,
        ]

        for card in cards:
            card.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Expanding
            )

        layout.addWidget(self.countdown_card, 0, 0)
        layout.addWidget(self.problems_card, 0, 1)
        layout.addWidget(self.daily_goal_card, 1, 0)
        layout.addWidget(self.topic_card, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)

    def refresh(self):
        self.config.reload()
        
        self.countdown_card.refresh()
        self.problems_card.refresh()
        self.daily_goal_card.refresh()
        self.topic_card.refresh()