from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CircleWidget(QWidget):
    
    def __init__(self, circle_radius, text, parent=None, text_size=15, bg_color='lime', fg_color='white', border_color='black'):
        super().__init__()
        self.arrowSection = 0
        self.border_color = border_color       
        self.circle_radius = circle_radius
        self.background_color = bg_color
        self.text = text
        self.text_color = fg_color
        self.text_size = text_size

        super().__init__(parent)
        self.setMinimumSize(2 * circle_radius + 10, 2 * circle_radius + 10)  # Set minimum size to accommodate circle

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(QColor(self.border_color), 2))

        # Draw circle
        painter.setBrush(QColor(self.background_color))
        painter.drawEllipse(5, 5, 2 * self.circle_radius, 2 * self.circle_radius)

        # Draw text
        font = QFont()
        font.setPointSize(self.text_size)  # Adjust size as needed
        painter.setFont(font)
        painter.setPen(QColor(self.text_color))  # Set text color

        rect = QRectF(5, 5, 2 * self.circle_radius, 2 * self.circle_radius)  # Adjust position as needed
        painter.drawText(rect, Qt.AlignCenter, str(self.text))
