from widgets.card_widget import CardWidget

class DailyGoalWidget(CardWidget):

    def __init__(self,config):
        self.config = config
        super().__init__("Today's Goal")
        self.refresh()

    def refresh(self):
        goal = self.config.get("daily_goal")
        completed = self.config.get("today_completed")

        remaining = max(0,goal-completed)
        self.set_value(f"{completed}/{goal}")
        self.set_subtitle(f"{remaining} Remaining")
        