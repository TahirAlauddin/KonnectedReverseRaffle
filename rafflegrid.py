from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GridItem(QWidget):
    def __init__(self, number, *args, **kwargs):
        super(GridItem, self).__init__(*args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        inner_widget = QWidget()
        inner_layout = QVBoxLayout()
        inner_widget.setLayout(inner_layout)
        inner_layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(str(number))
        label.setAlignment(Qt.AlignCenter)
        inner_layout.addWidget(label)
        inner_widget.setStyleSheet("border: 1px solid black; background: red; color: white;")  # Adjust styling here

        self.layout().addWidget(inner_widget)


class RaffleGridWidget(QWidget):

    def __init__(self):
        super().__init__()
        
        self.setStyleSheet('border: 1px solid red;')
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        num = 1
        for row in range(8):
            for column in range(10):
                item = GridItem(num)
                item.setMinimumSize(QSize(50,50))
                self.layout.addWidget(item, row, column)
                num += 1


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(100, 100, 800, 600)

        self.gridWidget = RaffleGridWidget()
        self.button = QPushButton('Press me')

        self.label = QLabel('This is a label')
        self.label2 = QLabel('This is a label')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label, alignment=Qt.AlignTop)
        self.layout.addWidget(self.gridWidget, alignment=Qt.AlignCenter)
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
