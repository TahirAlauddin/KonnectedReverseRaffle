from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from interface.home import Ui_MainWindow
from triangleArrowWidget import TriangleArrowWidget
from circleWidget import CircleWidget
from rafflegrid import RaffleGridWidget
import ctypes
from utils import get_themes, get_themes_names

myappid = 'tahiralauddin.konnectedreverseraffle.1.0.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class SelectableLabel(QLabel):
    def __init__(self, image_path, *args, **kwargs):
        self.window = kwargs.pop('window')
        self.image_path = image_path
        super().__init__(*args, **kwargs)


    def mousePressEvent(self, ev: QMouseEvent) -> None:
        if self.window:
            self.window.selectBackgroundImage(self)
        return super().mousePressEvent(ev)


class MainWindow(QMainWindow):
    grid_widget = None
    circle_widget = None
    triangle_widget = None
    restoreButtonPressedEvent = pyqtSignal()
    selectedImage = None
    eventLogo = None
    eventPrizePhoto = None
    backgroundImage = None
    
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
        #? Frames
        self.ui.uploadLogoFrame.mousePressEvent = lambda x: self.uploadLogo()
        self.ui.uploadPrizePhotoFrame.mousePressEvent = lambda x: self.uploadPrizePhoto()
        #? Others
        self.ui.saveAndRunEventButton.clicked.connect(self.saveAndRun)

        # Add Items
        self.ui.selectThemeComboBox.addItems(get_themes_names())
        self.addSelectableBackgroundImages()

        # Sizes
        self.setMinimumWidth(900)

    def uploadLogo(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Logo', '.', 'Images (*.png;*.jpg)')
        if file:
            self.eventLogo = file

    def uploadPrizePhoto(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Logo', '.', 'Images (*.png;*.jpg)')
        if file:
            self.eventPrizePhoto = file

    def addSelectableBackgroundImages(self):
        self.selectableBackgroundImages = []
        image_paths = ['gaming - small.jpg', 'sports - small.jpg', 'car - small.jpg', 
                       'school - small.jpg', 'medical - small.jpg', 'agriculture - small.jpg',
                        'music - small.jpg', 'home - small.jpg']
        
        for row in range(4):
            for column in range(2):
                image_path = image_paths[row*2 + column]
                
                image_path = fr"images\selectable images\{image_path}"
                selectableBackgroundImage = SelectableLabel(parent=self.ui.scrollAreaWidgetContents, image_path=image_path, window=self)
                selectableBackgroundImage.setScaledContents(True)
                selectableBackgroundImage.setFocusPolicy(Qt.NoFocus)
                original_pixmap = QPixmap(image_path)
                 # Calculate the desired scaled size based on the available screen space
                desired_width = self.width() // 2  # Divide available width equally among the images
                desired_height = self.height() // 2  # Divide available height equally among the images

                # Scale down the image while maintaining aspect ratio
                scaled_pixmap = original_pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)

                selectableBackgroundImage.setPixmap(scaled_pixmap)
                selectableBackgroundImage.setScaledContents(False)
                selectableBackgroundImage.setObjectName(f"backgroundImage{row*column+1}Label")
                self.ui.gridLayout_2.addWidget(selectableBackgroundImage, row, column, 1, 1)
                self.selectableBackgroundImages.append(selectableBackgroundImage)


    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.scale_images()
        if self.selectedImage:
            self.selectedImage.setStyleSheet(f'border: {self.selectedImage.maximumWidth()//15}px solid white;')


        return super().resizeEvent(a0)
    

    def scale_images(self):
        for selectableBackgroundImage in self.selectableBackgroundImages:
            selectableBackgroundImage.setMaximumSize(QSize(self.width()//5, self.height()//4))


    def scale_image_pixmaps(self):
        images_path = list(range(8))
        for selectableBackgroundImage, image_path in zip(self.selectableBackgroundImages, images_path):
                original_pixmap = QPixmap(r"C:\Users\LENOVO\OneDrive\Desktop\Projects\Konnected Reverse Raffle\images\selectable images\car.jpg")
                # Calculate the desired scaled size based on the available screen space
                desired_width = self.width() // 5  # Divide available width equally among the images
                desired_height = self.height() // 3  # Divide available height equally among the images

                # Scale down the image while maintaining aspect ratio
                scaled_pixmap = original_pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)

                selectableBackgroundImage.setPixmap(scaled_pixmap)


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

    def selectBackgroundImage(self, selectableLabel):
        self.backgroundImage = selectableLabel.image_path
        for selectableImage in self.selectableBackgroundImages:
            selectableImage.setStyleSheet('')
        selectableLabel.setStyleSheet(f'border: {selectableLabel.maximumWidth()//15}px solid white;')
        self.selectedImage = selectableLabel


    def saveAndRun(self):
        # Get data from frontend/interface
        selectedTheme =  self.ui.selectThemeComboBox.currentText()
        eventName = self.ui.eventNameLineEdit.text()
        location = self.ui.locationLineEdit.text()
        adsBannerMessage = self.ui.adsBannerMessageLineEdit.text()
        eliminationMessage = self.ui.eliminationMessageLineEdit.text()
        eventPythonDate = self.ui.dateEdit.date().toPyDate()

        #TODO: For development, remove this block later
        selectedTheme = 'Enchanted Forest'
        selectedTheme = 'Midnight Oasis'
        selectedTheme = "Urban Jungle"
        # selectedTheme = "Vintage Charm"
        # selectedTheme = "Electric Dreams"
        # selectedTheme = "Coastal Breeze"
        # selectedTheme = "Industrial Chic"

        eventName = 'Test eventName'
        location = 'Test location'
        adsBannerMessage = 'Test adsBannerMessage'
        eliminationMessage = 'Test eliminationMessage'
        self.backgroundImage = 'images/selectable images/gaming.jpg'
        self.backgroundImage = 'images/selectable images/agriculture.jpg'
        self.eventPrizePhoto = 'images/selectable images/sports - small.jpg'
        self.eventLogo = 'images/selectable images/car - small.jpg'
        from datetime import datetime
        
        date_format = "%B %d, %Y"
        eventPythonDate = datetime(2023, 6, 5).date().strftime(date_format)

        
        # If any of the required field is empty, return
        if not all([selectedTheme, self.backgroundImage,
                   self.eventPrizePhoto, self.eventLogo, 
                   eventName, location, adsBannerMessage, 
                   eliminationMessage, eventPythonDate]):
            QMessageBox.warning(self, 'Incomplete Information', 'Please provide the required information')
            return
        
        self.ui.adminUserStackedWidget.setCurrentIndex(1)

        themes = get_themes()
        theme = themes[selectedTheme]

        # Add Canvas Widgets
        #? Add Number Circle
        self.circle_widget = CircleWidget(circle_radius=80, text='100', bg_color=theme[0], fg_color=theme[3], border_color=theme[2])
        self.circle_widget.setMinimumSize(QSize(200, 180))
        layout = self.ui.numberBallCanvasFrameLayout
        layout.addWidget(self.circle_widget)
        #? Add Triangle Widget
        self.triangle_widget = TriangleArrowWidget(theme[0], theme[3], theme[2])
        self.triangle_widget.setMinimumSize(QSize(200, 220))
        layout = self.ui.triangleBallsRemainingFrameLayout
        layout.addWidget(self.triangle_widget)
        #? Add Grid Widget
        self.grid_widget = RaffleGridWidget('transparent', theme[3], theme[2])
        # self.grid_widget = RaffleGridWidget(theme[0], theme[3], theme[2])
        self.ui.raffleGridLayout.addWidget(self.grid_widget)
        # Set images
        #? Set background image
        self.ui.userPageContentFrame.set_image(f':backgroundImages/{self.backgroundImage}')
        #? Set logo        
        eventLogoIcon = QIcon()
        eventLogoIcon.addPixmap(QPixmap(f":backgroundImages/{self.eventLogo}"), 
                        QIcon.Normal, QIcon.Off)
        self.ui.eventLogoBtn.setIcon(eventLogoIcon)
        #? Set prize photo
        pixmap = QPixmap(self.eventPrizePhoto)
        self.ui.prizePhotoLabel.setPixmap(pixmap)
        self.ui.userStackedWidget.setCurrentIndex(1)


def main():
    global window, app
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

