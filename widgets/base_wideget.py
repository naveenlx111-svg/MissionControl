from PySide6.QtWidgets import QFrame


class BaseWidget(QFrame):
    def __init__(self):
        super().__init__()

        self.initialize()

    def initialize(self):
        """
        Widget lifecycle.
        Override this in child classes.
        """
        self.create_widgets()
        self.create_layout()
        self.connect_signals()
        self.refresh()

    def create_widgets(self):
        pass

    def create_layout(self):
        pass

    def connect_signals(self):
        pass

    def refresh(self):
        pass