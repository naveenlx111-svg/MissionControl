from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QColor, QPainter, QPen, QFont
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QRectF, QTimer

class CircularProgress(QWidget):

    def __init__(self):
        super().__init__()

        self.progress = 0
        self.target_progress = 0
        self.start_progress = 0
        self.animation_step = 0
        self.animation_steps = 40
        self.setMinimumSize(220, 220)

    def set_progress(self, value):
        self.start_progress = self.progress
        self.target_progress = max(0, min(100, value))
        self.animation_step = 0

        if not hasattr(self, "timer"):
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.animate)

        self.timer.start(15)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        size = min(self.width(), self.height()) - 20

        rect = QRectF(
            (self.width() - size) / 2,
            (self.height() - size) / 2,
            size,
            size
        )

        # Background Circle
        pen = QPen(QColor("#2B2B2B"), 16)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawEllipse(rect)

        # Progress Arc
        pen.setColor(QColor("#00C853"))
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)

        painter.drawArc(
            rect,
            90 * 16,
            -round(self.progress * 360 / 100) * 16
        )

        # Percentage
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)

        painter.setFont(font)
        painter.setPen(Qt.GlobalColor.white)

        painter.drawText(
            rect,
            Qt.AlignmentFlag.AlignCenter,
            f"{round(self.progress)}%"
        )

    def animate(self):
        self.animation_step += 1

        if self.animation_step >= self.animation_steps:
            self.progress = self.target_progress
            self.timer.stop()
            self.update()
            return

        t = self.animation_step / self.animation_steps
        self.progress = self.start_progress + (self.target_progress - self.start_progress) * t
        self.update()