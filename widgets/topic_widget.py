from widgets.card_widget import CardWidget


class TopicWidget(CardWidget):

    def __init__(self, config):
        self.config = config
        super().__init__("Current Topic")
        self.refresh()

    def refresh(self):
        self.set_value(self.config.get("current_topic"))
        self.set_subtitle("Current Focus")