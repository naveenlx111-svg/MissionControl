from datetime import datetime

from widgets.card_widget import CardWidget


class CountdownWidget(CardWidget):

    def __init__(self,config):
        self.config = config
        super().__init__("Countdown")
        self.refresh()

    def refresh(self):
        target = self.config.get("target_date")
        target_date = datetime.strptime(target,"%Y-%m-%d")

        days_left = (target_date-datetime.now()).days

        self.set_value(str(max(0,days_left)))
        self.set_subtitle("Days Remaining")