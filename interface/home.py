# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\user_interface\home.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 650)
        MainWindow.setMinimumSize(QtCore.QSize(0, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/images/logo/tcb132x132.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.stylesheet = QtWidgets.QWidget(MainWindow)
        self.stylesheet.setStyleSheet("* {\n"
"font: 75 12pt \"Manrope\";\n"
"}\n"
"\n"
"#contentFrame {\n"
"background-color: white;\n"
"}\n"
"\n"
"/*********************************/\n"
"/* Admin Page */\n"
"\n"
"/* LINEEDITS */\n"
"QLineEdit {\n"
"border: 1px solid rgb(167, 167, 167);\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"}\n"
"\n"
"/* DateEdits */\n"
"QDateEdit {\n"
"border: 1px solid rgb(167, 167, 167);\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"}\n"
"QDateEdit::up-button {\n"
"    image: url(:/icons/images/icons/icons-collapse-arrow.png);\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    image: url(:/icons/images/icons/icons-expand-arrow.png);\n"
"}\n"
"\n"
"\n"
"QDateEdit::up-button:hover,\n"
"QDateEdit::down-button:hover {\n"
"    /* Define the hover effect properties */\n"
"    /* For example, change the icon\'s color */\n"
"    background-color: rgb(207, 207, 207)\n"
"}\n"
"\n"
"QDateEdit::up-button:pressed,\n"
"QDateEdit::down-button:pressed {\n"
"    /* Define the hover effect properties */\n"
"    /* For example, change the icon\'s color */\n"
"    background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"\n"
"/* FRAMES */\n"
"#adminPageNavigationFrame {\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"#uploadLogoFrame, #uploadPrizePhotoFrame {\n"
"background-color: white;\n"
"}\n"
"\n"
"/* BUTTONS */\n"
"#adminPageNavigationFrame QPushButton {\n"
"background-color: rgb(24, 112, 255);\n"
"border-radius: 5px;\n"
"border: none;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"#adminPageNavigationFrame QPushButton::pressed {\n"
"background-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"/* LABELS */\n"
"#uploadLogoLabel,  #uploadPrizePhotoLabel  {\n"
"color: rgb(0, 170, 255);\n"
"}\n"
"#settingsLabel {\n"
"font: 75 16pt \"Manrope\";\n"
"color: white;\n"
"margin-bottom: 20px;\n"
"}\n"
"\n"
"\n"
"/*********************************/\n"
"/* Grid Page */\n"
"/* BUTTONS */\n"
"#eventLogoBtn {\n"
"background: transparent;\n"
"border: none\n"
"}\n"
"/* FRAMES */\n"
"#eventTitleFrame {\n"
"background-color: rgb(99, 200, 148);\n"
"}\n"
"/* LABELS */\n"
"#eliminatedNumberLabel {\n"
"padding: 10px;\n"
"background-color: rgb(0, 170, 255);\n"
"color: white;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"}\n"
"#eliminationMessageLabel {\n"
"border: 1px solid rgb(0, 170, 255);\n"
"}\n"
"#recentLabel {\n"
"font-size: 20px;\n"
"}\n"
"/* OTHERS */\n"
"#recentListWidget {\n"
"padding-top: 5px;\n"
"padding-left: 20px;\n"
"border: 1px solid white;\n"
"border-color: rgb(85, 170, 255);\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"}")
        self.stylesheet.setObjectName("stylesheet")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.stylesheet)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.contentFrame = QtWidgets.QFrame(self.stylesheet)
        self.contentFrame.setStyleSheet("")
        self.contentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFrame.setObjectName("contentFrame")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.contentFrame)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.adminUserStackedWidget = QtWidgets.QStackedWidget(self.contentFrame)
        self.adminUserStackedWidget.setObjectName("adminUserStackedWidget")
        self.adminPage = QtWidgets.QWidget()
        self.adminPage.setObjectName("adminPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.adminPage)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.adminPageNavigationFrame = QtWidgets.QFrame(self.adminPage)
        self.adminPageNavigationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adminPageNavigationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adminPageNavigationFrame.setObjectName("adminPageNavigationFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.adminPageNavigationFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.settingsLabel = QtWidgets.QLabel(self.adminPageNavigationFrame)
        self.settingsLabel.setObjectName("settingsLabel")
        self.verticalLayout_2.addWidget(self.settingsLabel)
        self.adminSectionPushButton = QtWidgets.QPushButton(self.adminPageNavigationFrame)
        self.adminSectionPushButton.setObjectName("adminSectionPushButton")
        self.verticalLayout_2.addWidget(self.adminSectionPushButton)
        self.userListPushButton = QtWidgets.QPushButton(self.adminPageNavigationFrame)
        self.userListPushButton.setObjectName("userListPushButton")
        self.verticalLayout_2.addWidget(self.userListPushButton)
        self.licensePushButton = QtWidgets.QPushButton(self.adminPageNavigationFrame)
        self.licensePushButton.setObjectName("licensePushButton")
        self.verticalLayout_2.addWidget(self.licensePushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.adminPageNavigationFrame)
        self.adminPageContentFrame = QtWidgets.QFrame(self.adminPage)
        self.adminPageContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adminPageContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adminPageContentFrame.setObjectName("adminPageContentFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.adminPageContentFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.adminPageStackedWidget = QtWidgets.QStackedWidget(self.adminPageContentFrame)
        self.adminPageStackedWidget.setObjectName("adminPageStackedWidget")
        self.adminSectionPage = QtWidgets.QWidget()
        self.adminSectionPage.setObjectName("adminSectionPage")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.adminSectionPage)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.adminSectionPageLeftFrame = QtWidgets.QFrame(self.adminSectionPage)
        self.adminSectionPageLeftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adminSectionPageLeftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adminSectionPageLeftFrame.setObjectName("adminSectionPageLeftFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.adminSectionPageLeftFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uploadLogoFrame = QtWidgets.QFrame(self.adminSectionPageLeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadLogoFrame.sizePolicy().hasHeightForWidth())
        self.uploadLogoFrame.setSizePolicy(sizePolicy)
        self.uploadLogoFrame.setMinimumSize(QtCore.QSize(200, 150))
        self.uploadLogoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploadLogoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uploadLogoFrame.setObjectName("uploadLogoFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.uploadLogoFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uploadLogoPixmapLabel = QtWidgets.QLabel(self.uploadLogoFrame)
        self.uploadLogoPixmapLabel.setObjectName("uploadLogoPixmapLabel")
        self.verticalLayout_5.addWidget(self.uploadLogoPixmapLabel)
        self.uploadLogoLabel = QtWidgets.QLabel(self.uploadLogoFrame)
        self.uploadLogoLabel.setObjectName("uploadLogoLabel")
        self.verticalLayout_5.addWidget(self.uploadLogoLabel, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_4.addWidget(self.uploadLogoFrame)
        self.uploadPrizePhotoFrame = QtWidgets.QFrame(self.adminSectionPageLeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadPrizePhotoFrame.sizePolicy().hasHeightForWidth())
        self.uploadPrizePhotoFrame.setSizePolicy(sizePolicy)
        self.uploadPrizePhotoFrame.setMinimumSize(QtCore.QSize(200, 150))
        self.uploadPrizePhotoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploadPrizePhotoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uploadPrizePhotoFrame.setObjectName("uploadPrizePhotoFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.uploadPrizePhotoFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.uploadPrizePhotoPixmapLabel = QtWidgets.QLabel(self.uploadPrizePhotoFrame)
        self.uploadPrizePhotoPixmapLabel.setObjectName("uploadPrizePhotoPixmapLabel")
        self.verticalLayout_6.addWidget(self.uploadPrizePhotoPixmapLabel)
        self.uploadPrizePhotoLabel = QtWidgets.QLabel(self.uploadPrizePhotoFrame)
        self.uploadPrizePhotoLabel.setObjectName("uploadPrizePhotoLabel")
        self.verticalLayout_6.addWidget(self.uploadPrizePhotoLabel, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_4.addWidget(self.uploadPrizePhotoFrame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.spinBox = QtWidgets.QSpinBox(self.adminSectionPageLeftFrame)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_4.addWidget(self.spinBox)
        self.saveAndRunEventButton = QtWidgets.QPushButton(self.adminSectionPageLeftFrame)
        self.saveAndRunEventButton.setObjectName("saveAndRunEventButton")
        self.verticalLayout_4.addWidget(self.saveAndRunEventButton)
        self.horizontalLayout_4.addWidget(self.adminSectionPageLeftFrame)
        self.adminSectionPageRightFrame = QtWidgets.QFrame(self.adminSectionPage)
        self.adminSectionPageRightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adminSectionPageRightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adminSectionPageRightFrame.setObjectName("adminSectionPageRightFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.adminSectionPageRightFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.adminSectionPageRightFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.eventNameLabel = QtWidgets.QLabel(self.frame)
        self.eventNameLabel.setObjectName("eventNameLabel")
        self.gridLayout.addWidget(self.eventNameLabel, 0, 0, 1, 1)
        self.eventNameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.eventNameLineEdit.setObjectName("eventNameLineEdit")
        self.gridLayout.addWidget(self.eventNameLineEdit, 0, 1, 1, 1)
        self.locationLabel = QtWidgets.QLabel(self.frame)
        self.locationLabel.setObjectName("locationLabel")
        self.gridLayout.addWidget(self.locationLabel, 1, 0, 1, 1)
        self.locationLineEdit = QtWidgets.QLineEdit(self.frame)
        self.locationLineEdit.setObjectName("locationLineEdit")
        self.gridLayout.addWidget(self.locationLineEdit, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.eliminationMessageLineEdit = QtWidgets.QLineEdit(self.frame)
        self.eliminationMessageLineEdit.setObjectName("eliminationMessageLineEdit")
        self.gridLayout.addWidget(self.eliminationMessageLineEdit, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.adsBannerMessageLineEdit = QtWidgets.QLineEdit(self.frame)
        self.adsBannerMessageLineEdit.setObjectName("adsBannerMessageLineEdit")
        self.gridLayout.addWidget(self.adsBannerMessageLineEdit, 4, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.frame)
        self.entryCheckBoxesFrame = QtWidgets.QFrame(self.adminSectionPageRightFrame)
        self.entryCheckBoxesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.entryCheckBoxesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entryCheckBoxesFrame.setObjectName("entryCheckBoxesFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.entryCheckBoxesFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.entryCheckBoxesFrame)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.checkBox = QtWidgets.QCheckBox(self.entryCheckBoxesFrame)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.entryCheckBoxesFrame)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_5.addWidget(self.checkBox_2)
        self.verticalLayout_7.addWidget(self.entryCheckBoxesFrame)
        self.selectThemeFrame = QtWidgets.QFrame(self.adminSectionPageRightFrame)
        self.selectThemeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selectThemeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selectThemeFrame.setObjectName("selectThemeFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.selectThemeFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comboBox = QtWidgets.QComboBox(self.selectThemeFrame)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_6.addWidget(self.comboBox)
        self.verticalLayout_7.addWidget(self.selectThemeFrame)
        self.adminPageBackgroundImageFrame = QtWidgets.QFrame(self.adminSectionPageRightFrame)
        self.adminPageBackgroundImageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adminPageBackgroundImageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adminPageBackgroundImageFrame.setObjectName("adminPageBackgroundImageFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.adminPageBackgroundImageFrame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(self.adminPageBackgroundImageFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 81, 68))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.backgroundImage1Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.backgroundImage1Label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.backgroundImage1Label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backgroundImage1Label.setText("")
        self.backgroundImage1Label.setPixmap(QtGui.QPixmap(".\\user_interface\\../../../../../../../Downloads/simon-berger-aZjw7xI3QAA-unsplash.jpg"))
        self.backgroundImage1Label.setScaledContents(False)
        self.backgroundImage1Label.setObjectName("backgroundImage1Label")
        self.gridLayout_2.addWidget(self.backgroundImage1Label, 0, 0, 1, 1)
        self.backgroundImage1Label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.backgroundImage1Label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.backgroundImage1Label_2.setText("")
        self.backgroundImage1Label_2.setPixmap(QtGui.QPixmap(".\\user_interface\\../../../../../../../Downloads/simon-berger-aZjw7xI3QAA-unsplash.jpg"))
        self.backgroundImage1Label_2.setObjectName("backgroundImage1Label_2")
        self.gridLayout_2.addWidget(self.backgroundImage1Label_2, 0, 1, 1, 1)
        self.backgroundImage1Label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.backgroundImage1Label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.backgroundImage1Label_4.setText("")
        self.backgroundImage1Label_4.setPixmap(QtGui.QPixmap(".\\user_interface\\../../../../../../../Downloads/simon-berger-aZjw7xI3QAA-unsplash.jpg"))
        self.backgroundImage1Label_4.setObjectName("backgroundImage1Label_4")
        self.gridLayout_2.addWidget(self.backgroundImage1Label_4, 1, 1, 1, 1)
        self.backgroundImage1Label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.backgroundImage1Label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.backgroundImage1Label_3.setText("")
        self.backgroundImage1Label_3.setPixmap(QtGui.QPixmap(".\\user_interface\\../../../../../../../Downloads/simon-berger-aZjw7xI3QAA-unsplash.jpg"))
        self.backgroundImage1Label_3.setObjectName("backgroundImage1Label_3")
        self.gridLayout_2.addWidget(self.backgroundImage1Label_3, 1, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)
        self.pushButton_6 = QtWidgets.QPushButton(self.adminPageBackgroundImageFrame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_8.addWidget(self.pushButton_6)
        self.verticalLayout_7.addWidget(self.adminPageBackgroundImageFrame)
        self.horizontalLayout_4.addWidget(self.adminSectionPageRightFrame)
        self.adminPageStackedWidget.addWidget(self.adminSectionPage)
        self.userListSectionPage = QtWidgets.QWidget()
        self.userListSectionPage.setObjectName("userListSectionPage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.userListSectionPage)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.userListSectionPage)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.tableWidget = QtWidgets.QTableWidget(self.userListSectionPage)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_9.addWidget(self.tableWidget)
        self.frame_2 = QtWidgets.QFrame(self.userListSectionPage)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.verticalLayout_9.addWidget(self.frame_2)
        self.adminPageStackedWidget.addWidget(self.userListSectionPage)
        self.licenseListSectionPage = QtWidgets.QWidget()
        self.licenseListSectionPage.setObjectName("licenseListSectionPage")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.licenseListSectionPage)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.licenseListSectionPage)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.licenseListSectionPage)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_10.addWidget(self.lineEdit)
        self.pushButton_5 = QtWidgets.QPushButton(self.licenseListSectionPage)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_10.addWidget(self.pushButton_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.adminPageStackedWidget.addWidget(self.licenseListSectionPage)
        self.verticalLayout_3.addWidget(self.adminPageStackedWidget)
        self.horizontalLayout_2.addWidget(self.adminPageContentFrame)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.adminUserStackedWidget.addWidget(self.adminPage)
        self.userPage = QtWidgets.QWidget()
        self.userPage.setObjectName("userPage")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.userPage)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.userPageLeftPane = QtWidgets.QFrame(self.userPage)
        self.userPageLeftPane.setMinimumSize(QtCore.QSize(200, 0))
        self.userPageLeftPane.setMaximumSize(QtCore.QSize(200, 16777215))
        self.userPageLeftPane.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.userPageLeftPane.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userPageLeftPane.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userPageLeftPane.setObjectName("userPageLeftPane")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.userPageLeftPane)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.eventLogoBtn = QtWidgets.QPushButton(self.userPageLeftPane)
        self.eventLogoBtn.setStyleSheet("")
        self.eventLogoBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\user_interface\\../images/logo/TCB LOGO-GOLD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eventLogoBtn.setIcon(icon1)
        self.eventLogoBtn.setIconSize(QtCore.QSize(150, 60))
        self.eventLogoBtn.setObjectName("eventLogoBtn")
        self.verticalLayout_12.addWidget(self.eventLogoBtn)
        self.numberBallCanvasFrame = QtWidgets.QFrame(self.userPageLeftPane)
        self.numberBallCanvasFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.numberBallCanvasFrame.setStyleSheet("")
        self.numberBallCanvasFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.numberBallCanvasFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.numberBallCanvasFrame.setObjectName("numberBallCanvasFrame")
        self.numberBallCanvasFrameLayout = QtWidgets.QVBoxLayout(self.numberBallCanvasFrame)
        self.numberBallCanvasFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.numberBallCanvasFrameLayout.setSpacing(0)
        self.numberBallCanvasFrameLayout.setObjectName("numberBallCanvasFrameLayout")
        self.verticalLayout_12.addWidget(self.numberBallCanvasFrame)
        self.triangleBallsRemainingFrame = QtWidgets.QFrame(self.userPageLeftPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.triangleBallsRemainingFrame.sizePolicy().hasHeightForWidth())
        self.triangleBallsRemainingFrame.setSizePolicy(sizePolicy)
        self.triangleBallsRemainingFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.triangleBallsRemainingFrame.setStyleSheet("")
        self.triangleBallsRemainingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.triangleBallsRemainingFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.triangleBallsRemainingFrame.setObjectName("triangleBallsRemainingFrame")
        self.triangleBallsRemainingFrameLayout = QtWidgets.QVBoxLayout(self.triangleBallsRemainingFrame)
        self.triangleBallsRemainingFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.triangleBallsRemainingFrameLayout.setSpacing(0)
        self.triangleBallsRemainingFrameLayout.setObjectName("triangleBallsRemainingFrameLayout")
        self.verticalLayout_12.addWidget(self.triangleBallsRemainingFrame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem4)
        self.recentNumbersDrawnFrame = QtWidgets.QFrame(self.userPageLeftPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentNumbersDrawnFrame.sizePolicy().hasHeightForWidth())
        self.recentNumbersDrawnFrame.setSizePolicy(sizePolicy)
        self.recentNumbersDrawnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.recentNumbersDrawnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.recentNumbersDrawnFrame.setObjectName("recentNumbersDrawnFrame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.recentNumbersDrawnFrame)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.recentLabel = QtWidgets.QLabel(self.recentNumbersDrawnFrame)
        self.recentLabel.setObjectName("recentLabel")
        self.verticalLayout_13.addWidget(self.recentLabel)
        self.recentListWidget = QtWidgets.QListWidget(self.recentNumbersDrawnFrame)
        self.recentListWidget.setStyleSheet("background-color: white;")
        self.recentListWidget.setObjectName("recentListWidget")
        item = QtWidgets.QListWidgetItem()
        self.recentListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.recentListWidget.addItem(item)
        self.verticalLayout_13.addWidget(self.recentListWidget)
        self.verticalLayout_12.addWidget(self.recentNumbersDrawnFrame)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 1)
        self.verticalLayout_12.setStretch(2, 1)
        self.verticalLayout_12.setStretch(3, 1)
        self.verticalLayout_12.setStretch(4, 1)
        self.horizontalLayout_3.addWidget(self.userPageLeftPane)
        self.userPageContentFrame = QtWidgets.QFrame(self.userPage)
        self.userPageContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userPageContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userPageContentFrame.setObjectName("userPageContentFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.userPageContentFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.userPageContentFrameTopPane = QtWidgets.QFrame(self.userPageContentFrame)
        self.userPageContentFrameTopPane.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userPageContentFrameTopPane.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userPageContentFrameTopPane.setObjectName("userPageContentFrameTopPane")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.userPageContentFrameTopPane)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.eventTitleFrame = QtWidgets.QFrame(self.userPageContentFrameTopPane)
        self.eventTitleFrame.setStyleSheet("")
        self.eventTitleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eventTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eventTitleFrame.setObjectName("eventTitleFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.eventTitleFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.eventTitleLabel = QtWidgets.QLabel(self.eventTitleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventTitleLabel.sizePolicy().hasHeightForWidth())
        self.eventTitleLabel.setSizePolicy(sizePolicy)
        self.eventTitleLabel.setObjectName("eventTitleLabel")
        self.horizontalLayout_8.addWidget(self.eventTitleLabel)
        self.line = QtWidgets.QFrame(self.eventTitleFrame)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.adsBannerMessageLabel = QtWidgets.QLabel(self.eventTitleFrame)
        self.adsBannerMessageLabel.setStyleSheet("")
        self.adsBannerMessageLabel.setObjectName("adsBannerMessageLabel")
        self.horizontalLayout_8.addWidget(self.adsBannerMessageLabel)
        self.verticalLayout_11.addWidget(self.eventTitleFrame)
        self.eliminationMessageFrame = QtWidgets.QFrame(self.userPageContentFrameTopPane)
        self.eliminationMessageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eliminationMessageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eliminationMessageFrame.setObjectName("eliminationMessageFrame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.eliminationMessageFrame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.eliminatedNumberLabel = QtWidgets.QLabel(self.eliminationMessageFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eliminatedNumberLabel.sizePolicy().hasHeightForWidth())
        self.eliminatedNumberLabel.setSizePolicy(sizePolicy)
        self.eliminatedNumberLabel.setStyleSheet("")
        self.eliminatedNumberLabel.setObjectName("eliminatedNumberLabel")
        self.horizontalLayout_9.addWidget(self.eliminatedNumberLabel)
        self.eliminationMessageLabel = QtWidgets.QLabel(self.eliminationMessageFrame)
        self.eliminationMessageLabel.setStyleSheet("")
        self.eliminationMessageLabel.setObjectName("eliminationMessageLabel")
        self.horizontalLayout_9.addWidget(self.eliminationMessageLabel)
        self.verticalLayout_11.addWidget(self.eliminationMessageFrame)
        self.verticalLayout.addWidget(self.userPageContentFrameTopPane)
        self.userStackedWidget = QtWidgets.QStackedWidget(self.userPageContentFrame)
        self.userStackedWidget.setObjectName("userStackedWidget")
        self.gridPage = QtWidgets.QWidget()
        self.gridPage.setObjectName("gridPage")
        self.raffleGridLayout = QtWidgets.QVBoxLayout(self.gridPage)
        self.raffleGridLayout.setObjectName("raffleGridLayout")
        self.userStackedWidget.addWidget(self.gridPage)
        self.announcementPage = QtWidgets.QWidget()
        self.announcementPage.setObjectName("announcementPage")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.announcementPage)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_3 = QtWidgets.QFrame(self.announcementPage)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_14.addWidget(self.frame_3, 0, QtCore.Qt.AlignVCenter)
        self.userStackedWidget.addWidget(self.announcementPage)
        self.verticalLayout.addWidget(self.userStackedWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.horizontalLayout_3.addWidget(self.userPageContentFrame)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.adminUserStackedWidget.addWidget(self.userPage)
        self.verticalLayout_32.addWidget(self.adminUserStackedWidget)
        self.horizontalLayout.addWidget(self.contentFrame)
        self.horizontalLayout.setStretch(0, 5)
        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)
        self.adminUserStackedWidget.setCurrentIndex(1)
        self.adminPageStackedWidget.setCurrentIndex(0)
        self.userStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Konnected Reverse Raffle"))
        self.settingsLabel.setText(_translate("MainWindow", "Settings"))
        self.adminSectionPushButton.setText(_translate("MainWindow", "Admin"))
        self.userListPushButton.setText(_translate("MainWindow", "User List"))
        self.licensePushButton.setText(_translate("MainWindow", "License"))
        self.uploadLogoPixmapLabel.setText(_translate("MainWindow", "LOGO"))
        self.uploadLogoLabel.setText(_translate("MainWindow", "[UPLOAD LOGO]"))
        self.uploadPrizePhotoPixmapLabel.setText(_translate("MainWindow", "Prize Photo"))
        self.uploadPrizePhotoLabel.setText(_translate("MainWindow", "[UPLOAD IMAGE]"))
        self.saveAndRunEventButton.setText(_translate("MainWindow", "Save && Run"))
        self.eventNameLabel.setText(_translate("MainWindow", "Event Name:"))
        self.locationLabel.setText(_translate("MainWindow", "Location:"))
        self.label_8.setText(_translate("MainWindow", "Date:"))
        self.label_9.setText(_translate("MainWindow", "Out Message:"))
        self.eliminationMessageLineEdit.setPlaceholderText(_translate("MainWindow", "Eliminated"))
        self.label_10.setText(_translate("MainWindow", "Ads Banner Message"))
        self.adsBannerMessageLineEdit.setPlaceholderText(_translate("MainWindow", "Thanks for your support"))
        self.label_11.setText(_translate("MainWindow", "Entry:"))
        self.checkBox.setText(_translate("MainWindow", "Keypad"))
        self.checkBox_2.setText(_translate("MainWindow", "Barcode"))
        self.pushButton_6.setText(_translate("MainWindow", "Add Custom Image"))
        self.label_6.setText(_translate("MainWindow", "Assign Number to Name"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.pushButton_2.setText(_translate("MainWindow", "Upload CSV"))
        self.pushButton_3.setText(_translate("MainWindow", "Download CSV"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.label_7.setText(_translate("MainWindow", "Enter License Here"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.recentLabel.setText(_translate("MainWindow", "Recent"))
        __sortingEnabled = self.recentListWidget.isSortingEnabled()
        self.recentListWidget.setSortingEnabled(False)
        item = self.recentListWidget.item(0)
        item.setText(_translate("MainWindow", "233"))
        item = self.recentListWidget.item(1)
        item.setText(_translate("MainWindow", "223"))
        self.recentListWidget.setSortingEnabled(__sortingEnabled)
        self.eventTitleLabel.setText(_translate("MainWindow", "Event Title - Sep 10, 2023"))
        self.adsBannerMessageLabel.setText(_translate("MainWindow", "Thanks for your support!"))
        self.eliminatedNumberLabel.setText(_translate("MainWindow", "108"))
        self.eliminationMessageLabel.setText(_translate("MainWindow", "Sarah Anderson Eliminated!"))
import resources_rc