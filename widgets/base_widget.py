from PySide6.QtWidgets import QFrame


class BaseWidget(QFrame):
    def __init__(self):
        super().__init__()

        self.initialize()

    def initialize(self):
        """
        Common initialization for every widget.
        Override in subclasses if needed.
        """
        pass

    def refresh(self):
        """
        Refresh displayed data.
        Widgets can override this.
        """
        pass

    def apply_theme(self):
        """
        Called whenever the application theme changes.
        """
        pass