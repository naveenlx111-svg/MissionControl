from datetime import datetime
from PySide6.QtCore import Signal
from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QDateEdit,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
)

class SettingsDialog(QDialog):

    settings_saved = Signal()
    def __init__(self, config):
        super().__init__()

        self.config = config

        self.setWindowTitle("Settings")
        self.resize(400, 300)

        self.create_widgets()
        self.create_layout()
        self.load_data()
        self.save_btn.clicked.connect(self.save_settings)
        self.cancel_btn.clicked.connect(self.close)

    def create_widgets(self):

        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)

        self.total_problems = QSpinBox()
        self.total_problems.setMaximum(100000)

        self.daily_goal = QSpinBox()
        self.daily_goal.setMaximum(1000)

        self.topic = QLineEdit()

        self.save_btn = QPushButton("Save")
        self.cancel_btn = QPushButton("Cancel")

    def create_layout(self):

        layout = QVBoxLayout(self)

        form = QFormLayout()

        form.addRow("Target Date", self.date_edit)
        form.addRow("Total Problems", self.total_problems)
        form.addRow("Daily Goal", self.daily_goal)
        form.addRow("Current Topic", self.topic)

        layout.addLayout(form)

        buttons = QHBoxLayout()

        buttons.addStretch()
        buttons.addWidget(self.save_btn)
        buttons.addWidget(self.cancel_btn)

        layout.addLayout(buttons)

    def load_data(self):

        target = datetime.strptime(
            self.config.get("target_date"),
            "%Y-%m-%d"
        )

        self.date_edit.setDate(
            QDate(target.year, target.month, target.day)
        )

        self.total_problems.setValue(
            self.config.get("total_problems")
        )

        self.daily_goal.setValue(
            self.config.get("daily_goal")
        )

        self.topic.setText(
            self.config.get("current_topic")
        )
    def save_settings(self):

        self.config.set("target_date",
            self.date_edit.date().toString("yyyy-MM-dd"))

        self.config.set("total_problems",
            self.total_problems.value())

        self.config.set("daily_goal",
            self.daily_goal.value())

        self.config.set("current_topic",
            self.topic.text())

        self.config.save()
        self.settings_saved.emit()

        self.accept()