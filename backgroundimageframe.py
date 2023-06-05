from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class BackgroundImageFrame(QFrame):
    def __init__(self, parent, image_path=None):
        super().__init__(parent=parent)
        
        # Set the widget's properties
        self.setAutoFillBackground(True)
        self.set_image(image_path)
        

    def set_image(self, image_path):
        
        # Create the background pixmap
        if image_path:
            pixmap = QPixmap(image_path)
            # Scale the pixmap to fit or fill the allocated space
            pixmap = pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            # Set the pixmap as the widget's background
            self.setPixmap(pixmap)

            
    def setPixmap(self, pixmap):
        # Override the setPixmap method to draw the pixmap as the background
        self._pixmap = pixmap
        self.update()
        
    def paintEvent(self, event):
        # Override the paintEvent method to draw the pixmap as the background
        if self._pixmap:
            painter = QPainter(self)
            painter.drawPixmap(self.rect(), self._pixmap)
        super().paintEvent(event)

        