import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from interface.home import Ui_MainWindow
from trianglearrowwidget import TriangleArrowWidget
from circleWidget import CircleWidget
from rafflegrid import RaffleGridWidget
import ctypes


myappid = 'tahiralauddin.konnectedreverseraffle.1.0.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(QMainWindow):
    grid_widget = None
    circle_widget = None
    triangle_widget = None
    restoreButtonPressedEvent = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Ui_Componenets()
        self.show()

    def Ui_Componenets(self):
        self.ui.adminUserStackedWidget.setCurrentIndex(0)
        # Mouse Press Events
        #? Navigation Menu
        self.ui.adminSectionPushButton.clicked.connect(lambda x: self.ui.adminPageStackedWidget.setCurrentIndex(0))
        self.ui.userListPushButton.clicked.connect(lambda x: self.ui.adminPageStackedWidget.setCurrentIndex(1))
        self.ui.licensePushButton.clicked.connect(lambda x: self.ui.adminPageStackedWidget.setCurrentIndex(2))
        #? Others
        self.ui.saveAndRunEventButton.clicked.connect(self.saveAndRun)


    def removeCanvasesFromWindow(self):
        if self.triangle_widget:
            self.ui.triangleBallsRemainingFrameLayout.removeWidget(self.triangle_widget)
            self.triangle_widget = None
        if self.circle_widget:
            self.ui.numberBallCanvasFrame.removeWidget(self.circle_widget)
            self.circle_widget = None
        if self.grid_widget:
            self.ui.raffleGridLayout.removeWidget(self.grid_widget)
            self.grid_widget = None


    def saveAndRun(self):
        self.ui.adminUserStackedWidget.setCurrentIndex(1)

        # Add Canvas Widgets
        #? Add Number Circle
        self.circle_widget = CircleWidget(circle_radius=80, text='100', bg_color='lime', fg_color='white', border_color='red')
        self.circle_widget.setMinimumSize(QSize(200, 180))
        layout = self.ui.numberBallCanvasFrameLayout
        layout.addWidget(self.circle_widget)
        #? Add Triangle Widget
        self.triangle_widget = TriangleArrowWidget('lime', 'white', 'black')
        self.triangle_widget.setMinimumSize(QSize(200, 220))
        layout = self.ui.triangleBallsRemainingFrameLayout
        layout.addWidget(self.triangle_widget)
        #? Add Grid Widget
        self.grid_widget = RaffleGridWidget()
        self.ui.raffleGridLayout.addWidget(self.grid_widget)


def main():
    global window, app
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

