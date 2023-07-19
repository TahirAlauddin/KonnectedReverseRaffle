from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from interface.home import Ui_MainWindow
from trianglearrowwidget import TriangleArrowWidget, NUMBER_TO_LIST_DICT
from circleWidget import CircleWidget
from rafflegrid import RaffleGridWidget
from selectablelabel import SelectableLabel
from utils import *
from licenseExpiryScheduler import LicenseExpiryThread

import ctypes
import csv
import os

if os.name == 'nt':
    myappid = 'tahiralauddin.konnectedreverseraffle.1.1.0' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

SOFTWARE_PROVIDED_IMAGES_NUM = 8


class MainWindow(QMainWindow):
    grid_widget = None
    circle_widget = None
    triangle_widget = None
    restoreButtonPressedEvent = pyqtSignal()
    selectedImage = None
    eventLogo = None
    prize = None
    eventPrizePhoto = None
    backgroundImage = None
    totalEliminatedNumbers = 0
    participants = {}
    licenseKeyValidated = False
    scannerEnabled = False
    eventCompleted = False
    keypadEnabled = True
    licenseExpired = pyqtSignal()

    
    def __init__(self) -> None:
        super().__init__()       
        self.scanned_data = ''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.Ui_Componenets()
        self.licenseExpired.connect(self.onLicenseExpiration)
        thread = LicenseExpiryThread(self, LICENSE_KEY_VALIDATION_LIMIT)
        thread.run()
        self.show()

    def onLicenseExpiration(self):
        QMessageBox.warning(self, 'License Expired', 'Your License has been expired! Please renew a new license to use the software.')
        

    def keyPressEvent(self, event):
        
        # Build the scanned data string
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Handle the full barcode (this is called when the Enter key is sent by the scanner)
            # Clear the scanned data for the next scan
            indexAdminUserPageSelected = self.ui.adminUserStackedWidget.currentIndex()
            if self.scanned_data:
                if self.scannerEnabled:
                    self.eliminateNumber(int(self.scanned_data))
                self.scanned_data = ''
            elif indexAdminUserPageSelected == 1:
                self.ui.eliminateButton.click()
            elif indexAdminUserPageSelected == 0:
                indexAdminPageSelected = self.ui.adminPageStackedWidget.currentIndex()
                if indexAdminPageSelected == 0:
                    self.ui.saveAndRunEventButton.click()
                elif indexAdminPageSelected == 1:
                    self.ui.saveAssignNumberTableButton.click()
                elif indexAdminPageSelected == 2:
                    self.ui.saveLicenseKeyButton.click()

        else:
            # Append the scanned character to the scanned_data string
            self.scanned_data += event.text()


    def Ui_Componenets(self):
        self.ui.adminUserStackedWidget.setCurrentIndex(0)
        # Mouse Press Events
        #? Navigation Menu
        self.ui.adminSectionPushButton.clicked.connect(lambda x: self.ui.adminPageStackedWidget.setCurrentIndex(0))
        self.ui.userListPushButton.clicked.connect(lambda x: self.ui.adminPageStackedWidget.setCurrentIndex(1))
        self.ui.licensePushButton.clicked.connect(lambda x: self.ui.adminPageStackedWidget.setCurrentIndex(2))
        
        #? Admin Page
        self.ui.eliminateButton.clicked.connect(self.eliminateNumberByLineEdit)
        self.ui.saveAssignNumberTableButton.clicked.connect(self.addParticipants)
        self.ui.addCustomImageButton.clicked.connect(self.addCustomImage)
        self.ui.saveLicenseKeyButton.clicked.connect(self.saveLicenseKey)
        # self.ui.goToAdminPageButton.clicked.connect(self.resetEvent)

        #? User List Page
        self.ui.saveAndRunEventButton.clicked.connect(self.saveAndRun)
        self.ui.uploadCSVButton.clicked.connect(self.uploadCSV)
        self.ui.downloadCSVButton.clicked.connect(self.downloadCSV)
        self.ui.addRowButton.clicked.connect(self.addRow)
        self.ui.removeRowButton.clicked.connect(self.removeRow)
        
        #? Frames
        self.ui.uploadLogoFrame.mousePressEvent = lambda x: self.uploadLogo()
        self.ui.uploadPrizePhotoFrame.mousePressEvent = lambda x: self.uploadPrizePhoto()

        # Add Items
        self.ui.selectThemeComboBox.addItems(get_themes_names())
        self.addSelectableBackgroundImages()
        # Restrictions
        self.ui.eliminateNumberSpinBox.setMinimum(1)
        self.ui.eliminateNumberSpinBox.setMaximum(300)
        self.ui.gridSizeSpinBox.setMinimum(50)
        self.ui.gridSizeSpinBox.setMaximum(400)

        # Sizes
        self.setMinimumWidth(900)
        self.showMaximized()

        # Defaults
        self.ui.adminPageStackedWidget.setCurrentIndex(0)
        self.ui.adminUserStackedWidget.setCurrentIndex(0)
        self.ui.keypadCheckBox.setChecked(True)

        if not self.ui.keypadCheckBox.isChecked():
            self.ui.eliminateButton.setEnabled(False)
            self.ui.eliminateButton.setStyleSheet("background-color: grey;")
            self.ui.eliminateButton.setToolTip("The button is disabled.")

        # Licensing
        license_key = get_license_key_from_config()
        if license_key:
            self.licenseKeyValidated = True
            self.ui.saveLicenseKeyButton.setText('Update License Key')


    def saveLicenseKey(self):
        licenseKey = self.ui.licenseKeyLineEdit.text()
        table = get_dynamodb_table()
        licenseCreatedDate = license_key_is_valid(licenseKey, table)
        if licenseCreatedDate:
            self.licenseKeyValidated = True
            set_license_key_in_config(licenseKey, licenseCreatedDate)
            QMessageBox.information(self, 'Successfully Validated', 'License Key is validated. Now, you may use the software.')
            self.ui.adminPageStackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, 'Invalid License Key', 'Sorry we couln\'t validate the license key. Please try again.')
            self.ui.licenseKeyLineEdit.setText('')


    def addCustomImage(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Logo', '.', 'Images (*.png;*.jpg)')
        if file:
            self.removeUploadedBackgroundImage()
            selectableImage = self.addSelectableBackgroundImage(file, 4, 0, columnSpan=2, custom_image=True)
            self.selectableBackgroundImages.insert(SOFTWARE_PROVIDED_IMAGES_NUM, selectableImage)
            selectableImage.setMaximumSize(QSize(self.width()//4, self.height()//4))


    def removeUploadedBackgroundImage(self):
        if len(self.selectableBackgroundImages) > SOFTWARE_PROVIDED_IMAGES_NUM:
            self.selectableBackgroundImages[8].close()


    def uploadLogo(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Logo', '.', 'Images (*.png;*.jpg)')
        if file:
            self.eventLogo = file
            pixmap = QPixmap(file)
            new_pixmap = pixmap.scaled(150, 200, Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.uploadLogoPixmapLabel.setPixmap(new_pixmap)
            
  
    def getTableContent(table):
        result = []
        for row in range(table.rowCount()):
            try:
                number = table.item(row, 0).text()
                name = table.item(row, 1).text()
            except:
                # If reading the data from tables throws error, it means the cell were empty
                continue

            if not number.isdigit():
                raise Exception(f'Incorrect Data Type for number ')
            
            result.append([number, name])
        return result
        

    def downloadCSV(self):
        participants = MainWindow.getTableContent(self.ui.tableWidget)
        desktop_path = get_users_desktop_folder()
        with open(os.path.join(desktop_path, 'participants.csv'), 'w') as participants_file:
            writer = csv.writer(participants_file, delimiter=',', lineterminator='\n')
            writer.writerows(participants)

        QMessageBox.information(self, 'Data Downloaded', 'Participants data saved in participants.csv successfully on Desktop!')
            

    def uploadCSV(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select CSV File', '.', 'CSV (*.csv)')
        if file:       
            reader = csv.reader(open(file))
            # Read data from each row
            error_occured = False
            participants = []
            for row in reader:
                try:
                    row_data = [
                        str(row[0]),
                        str(row[1]),
                    ]
                    if row[0] and MainWindow.is_float_or_int(row[0]):
                        participants.append(row_data)
                except IndexError:
                    if len(participants) < 1:
                        participants.append(['', ''])
                        error_occured = True

            if error_occured:
                QMessageBox.critical(window, 'Error in CSV File', 
    'The program couldn\'t read the CSV file. Make sure there are exactly 2 columns with proper data types and format.')
                return
            
            self.addCSVToTable(participants)

    
    def is_float_or_int(value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def addCSVToTable(self, participants):
        table = self.ui.tableWidget

        table.setRowCount(len(participants))
        table.setColumnCount(len(participants[0]))

        mainTableHeader = table.horizontalHeader()
        mainTableHeader.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        mainTableHeader.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        for idx, service in enumerate(participants):
            table.setItem(idx, 0, QTableWidgetItem(service[0]))
            table.setItem(idx, 1, QTableWidgetItem(service[1]))       
        

    def uploadPrizePhoto(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Logo', '.', 'Images (*.png;*.jpg)')
        if file:
            self.eventPrizePhoto = file
            pixmap = QPixmap(file)
            new_pixmap = pixmap.scaled(150, 200, Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.uploadPrizePhotoPixmapLabel.setPixmap(new_pixmap)
            

    def addSelectableBackgroundImages(self):
        """
        Adds selectable background images to the user interface.
        
        Initializes the `self.selectableBackgroundImages` list and populates it with instances of `SelectableLabel` 
        objects representing the selectable background images. 
        The function iterates over a predefined list of image paths and calls the `addSelectableBackgroundImage` 
        function for each image, passing the image path, row, and column values. The resulting `SelectableLabel` 
        objects are appended to the `self.selectableBackgroundImages` list.
        """
        self.selectableBackgroundImages = []
        image_paths = ['gaming - small.jpg', 'sports - small.jpg', 'car - small.jpg', 
                       'school - small.jpg', 'medical - small.jpg', 'agriculture - small.jpg',
                        'music - small.jpg', 'home - small.jpg']
        
        for row in range(4):
            for column in range(2):
                image_path = image_paths[row*2 + column]
                image_path = fr"images\selectable images\{image_path}"
                
                selectableBackgroundImage = self.addSelectableBackgroundImage(image_path, row, column)
                self.selectableBackgroundImages.append(selectableBackgroundImage)


    def addSelectableBackgroundImage(self, image_path, row, column, columnSpan=1, custom_image=False):
        """
        Adds a single selectable background image to the user interface.
        
        Creates an instance of `SelectableLabel` and configures it with the specified image path, row, column, and column span.
        Scales down the image to fit the desired width and height based on the available screen space.
        The resulting `SelectableLabel` object is added to the UI grid layout and returned.
        
        Args:
            image_path (str): The path to the image file.
            row (int): The row index of the grid layout where the image should be placed.
            column (int): The column index of the grid layout where the image should be placed.
            columnSpan (int, optional): The number of columns the image should span in the grid layout. Default is 1.
        
        Returns:
            selectableBackgroundImage (SelectableLabel): The created `SelectableLabel` object representing the selectable background image.
        """  
        selectableBackgroundImage = SelectableLabel(parent=self.ui.scrollAreaWidgetContents,
                                                    image_path=image_path, window=self,
                                                    custom_image=custom_image)
        selectableBackgroundImage.setScaledContents(True)
        selectableBackgroundImage.setFocusPolicy(Qt.NoFocus)
        if os.name != 'nt':
            image_path = image_path.replace('\\', '/')
        original_pixmap = QPixmap(image_path)
        # Calculate the desired scaled size based on the available screen space
        desired_width = self.width()  // 2  # Divide available width equally among the images
        desired_height = self.height() // 2  # Divide available height equally among the images

        # Scale down the image while maintaining aspect ratio
        scaled_pixmap = original_pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)

        selectableBackgroundImage.setPixmap(scaled_pixmap)
        selectableBackgroundImage.setObjectName(f"backgroundImage{row*column+1}Label")
        self.ui.gridLayout_2.addWidget(selectableBackgroundImage, row, column, 1, columnSpan)

        return selectableBackgroundImage


    # Functions for Add, Remove
    def addRow(self):
        tableWidget = self.ui.tableWidget
        rowCount = tableWidget.rowCount()
        tableWidget.setRowCount(rowCount + 1)
        tableWidget.setItem(rowCount + 1, 0, QTableWidgetItem())
        tableWidget.setItem(rowCount + 1, 1, QTableWidgetItem())
        tableWidget.setItem(rowCount + 1, 2, QTableWidgetItem())
        tableWidget.setItem(rowCount + 1, 3, QTableWidgetItem())
        
    def removeRow(self):
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

    def addParticipants(self):
        table = self.ui.tableWidget
        result = []
        for row in range(table.rowCount()):
            try:
                number = table.item(row, 0).text()
                name = table.item(row, 1).text()
            except:
                # If reading the data from tables throws error, it means the cell were empty
                QMessageBox.critical(self, 'Incomplete Information', f'You must provide both number and name at row # {row+1}')
                return
            
            # If either quanity or cost is not a number, throw an error
            if not number.isdigit():
                QMessageBox.critical(self, 'Invalid Information', f'Incorrect Data Type for `number`')
                return 
            
            result.append([number, name])
        
        self.participants = {int(number): name for number, name in result}
        self.ui.adminPageStackedWidget.setCurrentIndex(0)


    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.scale_images()
        if self.selectedImage:
            self.selectedImage.setStyleSheet(f'border: {self.selectedImage.maximumWidth()//15}px solid white;')


        return super().resizeEvent(a0)
    

    def scale_images(self):
        for selectableBackgroundImage in self.selectableBackgroundImages:
            selectableBackgroundImage.setMaximumSize(QSize(self.width()//4, self.height()//4))


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


    def selectBackgroundImage(self, selectableLabel, custom_image):
        
        if custom_image:
            image_path = selectableLabel.image_path
        else:
            image_path = selectableLabel.image_path.split(' - small')[0] + '.jpg'

        print(image_path)
        self.backgroundImage = image_path
        for selectableImage in self.selectableBackgroundImages:
            selectableImage.setStyleSheet('')
        selectableLabel.setStyleSheet(f'border: {selectableLabel.maximumWidth()//15}px solid white;')
        self.selectedImage = selectableLabel


    def saveAndRun(self):
        # Licensing
        if not self.licenseKeyValidated:
            QMessageBox.warning(self, 'License Required', 'Please provide license key in order to use this software.')
            return False
        
        # Enable or Disable Scanner
        if self.ui.barcodeCheckBox.isChecked():
            self.scannerEnabled = True

        # Get data from frontend/interface
        date_format = "%B %d, %Y"
        selectedTheme =  self.ui.selectThemeComboBox.currentText()
        eventName = self.ui.eventNameLineEdit.text()
        location = self.ui.locationLineEdit.text()
        adsBannerMessage = self.ui.adsBannerMessageLineEdit.text()
        eliminationMessage = self.ui.eliminationMessageLineEdit.text()
        eventDate = self.ui.dateEdit.date().toPyDate().strftime(date_format)
        self.totalParticipants = grid_size = self.ui.gridSizeSpinBox.value()
        self.prize = self.ui.prizeLineEdit.text()

        # #TODO: For development, remove this block later
        # selectedTheme = 'Midnight Oasis'
        # selectedTheme = "Serene Sunrise"
        # selectedTheme = 'Enchanted Forest'
        # selectedTheme = "Coastal Breeze"
        # selectedTheme = "Urban Jungle"
        # selectedTheme = "Electric Dreams"
        # selectedTheme = "Vintage Charm"
        # selectedTheme = "Industrial Chic"
        # eventName = 'Test eventName'
        # location = 'Test location'
        # adsBannerMessage = 'Test adsBannerMessage'
        # eliminationMessage = 'Test eliminationMessage'
        # self.backgroundImage = ':backgroundImages/images/selectable images/gaming.jpg'
        # self.backgroundImage = ':backgroundImages/images/selectable images/agriculture.jpg'
        # self.eventPrizePhoto = 'images/selectable images/sports - small.jpg'
        # self.eventLogo = ':/logo/images/logo/TCB LOGO-GOLD.png'
        # self.prize = 'BMW Model X'
        # eventDate = datetime(2023, 6, 5).date().strftime(date_format)
        # self.totalParticipants = grid_size = 150
        
        
        # If any of the required field is empty, return
        if not all([selectedTheme, self.backgroundImage,
                   self.eventPrizePhoto, self.eventLogo, 
                   eventName, location, adsBannerMessage, 
                   eliminationMessage, eventDate]):
            QMessageBox.warning(self, 'Incomplete Information', 'Please provide the required information')
            return
        
        if not self.participants:
            QMessageBox.warning(self, 'Incomplete Information', 'Please provide participants number and name in User List Page.')
            return

        
        # Restricted user input
        if (grid_size < 50) or (grid_size > 300):
            QMessageBox.critical(self, 'Invalid Input', 'Grid size must be greater than 50 and less than 300.')
            return
        
        if grid_size > len(self.participants):
            QMessageBox.critical(self, 'Invalid Input', 'Grid Size cannot be more than the number of participants provided. Please add more participants in User List Page.')
            return

                    
        self.ui.adminUserStackedWidget.setCurrentIndex(1)

        themes = get_themes()
        self.theme = theme = themes[selectedTheme]
        

        #? Add Canvas Widgets
        # Add Number Circle
        self.circle_widget = CircleWidget(circle_radius=80, text='100', bg_color=theme[0], fg_color=theme[3], border_color=theme[2])
        self.circle_widget.setMinimumSize(QSize(200, 180))
        layout = self.ui.numberBallCanvasFrameLayout
        layout.addWidget(self.circle_widget)
        
        # Triangle Logic
        self.num_text_list = MainWindow.find_closest_key(grid_size)
        
        # Add Triangle Widget
        self.triangle_widget = TriangleArrowWidget(theme[0], theme[3], theme[2], self.num_text_list)
        self.triangle_widget.setMinimumSize(QSize(200, 220))
        layout = self.ui.triangleBallsRemainingFrameLayout
        layout.addWidget(self.triangle_widget)
        # Add Grid Widget
        self.grid_widget = RaffleGridWidget()
        self.grid_widget_items = self.grid_widget.add_widget_items(grid_size, theme[0], theme[3], theme[2])
        self.ui.raffleGridLayout.addWidget(self.grid_widget)

        #? Set images
        # Set background image
        self.ui.userPageContentFrame.set_image(self.backgroundImage)
        # Set logo        
        eventLogoIcon = QIcon()
        eventLogoIcon.addPixmap(QPixmap(self.eventLogo), 
                        QIcon.Normal, QIcon.Off)
        self.ui.eventLogoBtn.setIcon(eventLogoIcon)
        # Set prize photo
        pixmap = QPixmap(self.eventPrizePhoto)
        newPixmap = pixmap.scaled(600, 600, Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.prizePhotoLabel.setPixmap(newPixmap)

        #? Set Text
        self.ui.eventTitleLabel.setText(f'{eventName} - {eventDate}')
        self.ui.adsBannerMessageLabel.setText(adsBannerMessage)
        self.ui.eliminationMessageLabel.setText("Eliminated Player will show here")
        self.ui.eliminatedNumberLabel.setText("X")

        self.ui.userStackedWidget.setCurrentIndex(0)

            
    def find_closest_key(grid_size):
        # find the smallest key that is greater than or equal to grid_size
        for key in sorted(NUMBER_TO_LIST_DICT.keys()):
            if key >= grid_size:
                return NUMBER_TO_LIST_DICT[key]
        # return the last element if grid_size is greater than all keys
        return NUMBER_TO_LIST_DICT[max(NUMBER_TO_LIST_DICT.keys())]



    def eliminateNumberByLineEdit(self):
        eliminatedNumber = self.ui.eliminateNumberSpinBox.value()
        self.eliminateNumber(eliminatedNumber)

    def eliminateNumber(self, eliminatedNumber):
        if self.eventCompleted:
            return
        
        if len(self.grid_widget_items) < eliminatedNumber:
            return
        
        grid_widget_item = self.grid_widget_items[eliminatedNumber-1]
        grid_widget_item.update_stylesheet(f"background: {self.theme[1]}; color: {self.theme[3]}; border: 1px solid {self.theme[2]}")
        grid_widget_item.update_stylesheet(f"background: transparent; color: transparent; border: none; ")
        eliminatedParticipant = self.participants.pop(eliminatedNumber, None)

        # If already eliminated or invalid input then ignore it
        if not eliminatedParticipant:
            return 
        
        # Elimination Logic
        self.showEliminatedParticipant(eliminatedNumber, eliminatedParticipant)
        self.totalEliminatedNumbers += 1
        

        recentCount = self.ui.recentListWidget.count()

        # Create a new item with the desired text.
        item = QListWidgetItem(str(eliminatedNumber))

        #? Remove limit on recentCount
        # if recentCount >= 5:
        #     # If there are already 5 items, remove the last one.
        #     self.ui.recentListWidget.takeItem(4)

        # Insert the new item at the top.
        self.ui.recentListWidget.insertItem(0, item)

        # Move Triangle Arrow
        participantsLeft = len(self.grid_widget_items) - self.totalEliminatedNumbers

        try:
            if participantsLeft <= int(self.num_text_list[self.triangle_widget.arrowSection+1]):
                self.triangle_widget.moveArrowRelatively(1)
        except IndexError:
            # It is perfectly fine to have this error. 
            # IndexError will be raised when there are no more sections below the current section
            pass

        if self.totalEliminatedNumbers + 1 == self.totalParticipants:
            # 1 participant left, announce winner
            self.announceWinner()

    def showEliminatedParticipant(self, eliminatedNumber: int, eliminatedParticipant: str):
        self.circle_widget.update_number(eliminatedNumber)
        self.ui.eliminatedNumberLabel.setText(str(eliminatedNumber))
        self.ui.eliminationMessageLabel.setText(f'{eliminatedParticipant} eliminated')

    def announceWinner(self):
        if self.participants:
            num = list(self.participants.keys())[0]
            self.ui.winnerLabel.setText(f'#{num} {self.participants[num]}')
            self.ui.prizeLabel.setText(f'Prize: {self.prize}')
                
        self.ui.userStackedWidget.setCurrentIndex(1)
        self.eventCompleted = True

    def resetEvent(self):
        self.ui.adminUserStackedWidget.setCurrentIndex(0)


def pre_requisites():
    import fonts #? Important line
    fonts_path = ['Manrope-Bold.ttf', 'Manrope-Light.ttf', 'Manrope-Regular.ttf']
    # checks if font is installed on computer 
    if not check_font_exists('Manrope'):
        for font in fonts_path:
            # Generate path dynamically for windows and mac
            #? Load fonts 
            load_font(font)

    # Config file must be available
    if not os.path.exists('config.json'):
        with open('config.json', 'w') as config_file:
            config_file.write('{}')
    
    # Themes file must be available
    if not os.path.exists('themes.json'):
        with open('themes.json', 'w') as themes_file:
            themes_file.write('{"Midnight Oasis": ["#001f3f", "#20466B", "#1abc9c", "#ffd700", "#005CB8"]}')

    
def main():
    pre_requisites() # Make sure everything is setup
    global window, app
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
