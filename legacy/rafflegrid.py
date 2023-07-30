from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import get_number_of_rows

class GridItem(QWidget):
    def __init__(self, number, background_color, foreground_color, border_color, *args, **kwargs):
        super(GridItem, self).__init__(*args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.inner_widget = QWidget()
        inner_layout = QVBoxLayout()
        self.inner_widget.setLayout(inner_layout)
        inner_layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(str(number))
        label.setAlignment(Qt.AlignCenter)
        inner_layout.addWidget(label)
        self.inner_widget.setStyleSheet(f"background: {background_color}; color: {foreground_color}; \
font: 100 25pt 'Manrope Bold'; border: 1px solid {border_color}")  # Adjust styling here

        self.layout().addWidget(self.inner_widget)

    def update_stylesheet(self, stylesheet):
        self.inner_widget.setStyleSheet(stylesheet) 



class RaffleGridWidget(QWidget):

    def __init__(self):
        super().__init__()
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)


    def add_widget_items(self, grid_size, background_color, foreground_color, border_color):

        if grid_size <= 50:
            column_size = 8
        elif grid_size <= 150:
            column_size = 10
        elif grid_size <= 250:
            column_size = 12
        elif grid_size <= 350:
            column_size = 15
        else:
            column_size = 20

        row_size = get_number_of_rows(grid_size, column_size)
        num = 1
        widgets = []
        for row in range(row_size):
            for column in range(column_size):
                if num > grid_size:
                    break # Remove this line if you don't want to skip any tile
                    item = GridItem('', background_color, foreground_color, border_color)
                    item.setMinimumSize(QSize(30,30))
                    self.layout.addWidget(item, row, column)
                    continue 
                    
                item = GridItem(num, background_color, foreground_color, border_color)
                item.setMinimumSize(QSize(40,40))
                # item.setMaximumHeight(30)
                self.layout.addWidget(item, row, column)
                widgets.append(item)
                num += 1
        
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacerItem, row+1, column)
        
        return widgets

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
