
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class GridCanvasWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(GridCanvasWidget, self).__init__(*args, **kwargs)
        self.square = (500, 'red', 'square')
        self.grid = None
        self.text = '108'
        self.text_font_size = 80
        self.text_location = 500
        self.grid_text_color = 'white'
        self.setFixedSize(self.square[0], self.square[0])
        # self.setBackgroundImage('image.jpg')
        self.addGrid(8,10)

        
    def setBackgroundImage(self, imagePath):
        self.backgroundImage = QPixmap(imagePath)
        print("Image")
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        if hasattr(self, 'backgroundImage'):
            painter.drawPixmap(self.rect(), self.backgroundImage)

        painter.setBrush(QColor(self.square[1]))
        painter.drawRect(0, 0, self.width(), self.height())  # Draw a square with the current widget's size


        if self.grid:
            font = QFont()
            font.setPointSize(15 * min(self.width(), self.height()) / 500)  # Adjust size based on widget size
            painter.setFont(font)
            painter.setPen(QColor('black'))  # Set pen color for grid
            cell_width = self.width() / self.grid[0]  # Calculate cell width based on widget size
            cell_height = self.height() / self.grid[1]  # Calculate cell height based on widget size
            # Draw vertical lines and horizontal lines
            num = 1
            for i in range(self.grid[0]):
                for j in range(self.grid[1]):
                    # Draw vertical line
                    painter.drawLine(int(i * cell_width), 0, int(i * cell_width), self.height())
                    # Draw horizontal line
                    painter.drawLine(0, int(j * cell_height), self.width(), int(j * cell_height))
                    # Set pen color for text
                    painter.setPen(QColor(self.grid_text_color))  # Change to desired color
                    # Calculate center coordinates
                    center_x = (i * cell_width) + (cell_width / 2)
                    center_y = (j * cell_height) + (cell_height / 2)
                    # Draw text
                    painter.drawText(QRectF(center_x - 10, center_y - 10, 20, 20),
                                    Qt.AlignCenter, str(num))
                    num += 1
                    # Reset pen color for grid
                    painter.setPen(QColor('black'))
                    


    def addGrid(self, rows, columns):
        self.grid = (rows, columns)
        self.update()  # Trigger repaint

    def removeGrid(self):
        self.grid = None
        self.update()  # Trigger repaint


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(100, 100, 800, 600)

        self.canvas = GridCanvasWidget()
        self.canvas.addGrid(8,10)
        self.canvas.update()
        self.canvas.setStyleSheet("border: 3px solid black;")

        self.button = QPushButton('Press me')

        self.label = QLabel('This is a label')
        self.label2 = QLabel('This is a label')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label, alignment=Qt.AlignTop)
        self.layout.addWidget(self.canvas, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label2, alignment=Qt.AlignTop)
        self.layout.setSpacing(10)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("background: pink")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

