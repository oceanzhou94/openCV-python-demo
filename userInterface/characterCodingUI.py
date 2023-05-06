"""
@Auth ： youngZ
@File ：characterCodingUI.py
人物图像打码处理UI
"""

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 350, 450, 400))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_source_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_source_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_source_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_source_img.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_source_img.setObjectName("label_source_img")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(550, 350, 450, 400))
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(False)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_dealt_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_dealt_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_dealt_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_dealt_img.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_dealt_img.setObjectName("label_dealt_img")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.pushButton_choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_img.setGeometry(QtCore.QRect(175, 60, 100, 50))
        self.pushButton_choose_img.setObjectName("pushButton")

        self.pushButton_character_coding = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_character_coding.setGeometry(QtCore.QRect(450, 60, 100, 50))
        self.pushButton_character_coding.setObjectName("pushButton_2")

        self.pushButton_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_img.setGeometry(QtCore.QRect(725, 60, 100, 50))
        self.pushButton_save_img.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人物图像打码"))
        self.label_source_img.setText(_translate("MainWindow", "原图"))
        self.label_dealt_img.setText(_translate("MainWindow", "处理后图片"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_character_coding.setText(_translate("MainWindow", "人物打码"))
        self.pushButton_save_img.setText(_translate("MainWindow", "保存图片"))
