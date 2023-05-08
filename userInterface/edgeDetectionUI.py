"""
@Auth ： youngZ
@File ：edgeDetectionUI.py
图像边缘检测UI
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        font = QtGui.QFont()
        font.setKerning(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_img.setGeometry(QtCore.QRect(860, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_save_img.setFont(font)
        self.pushButton_save_img.setObjectName("pushButton_save_img")
        self.pushButton_choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_img.setGeometry(QtCore.QRect(20, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_choose_img.setFont(font)
        self.pushButton_choose_img.setObjectName("pushButton_choose_img")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 100, 800, 200))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_laplacian = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_laplacian.setGeometry(QtCore.QRect(50, 75, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_laplacian.setFont(font)
        self.pushButton_laplacian.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_laplacian.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_laplacian.setObjectName("pushButton_laplacian")
        self.pushButton_sobel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sobel.setGeometry(QtCore.QRect(300, 75, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_sobel.setFont(font)
        self.pushButton_sobel.setObjectName("pushButton_sobel")
        self.pushButton_canny = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_canny.setGeometry(QtCore.QRect(550, 75, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_canny.setFont(font)
        self.pushButton_canny.setObjectName("pushButton_canny")
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
        self.scrollArea_3.setGeometry(QtCore.QRect(540, 350, 450, 400))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "图像边缘检测"))
        self.pushButton_save_img.setText(_translate("MainWindow", "保存图片"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.groupBox.setTitle(_translate("MainWindow", "图像边缘检测"))
        self.pushButton_laplacian.setText(_translate("MainWindow", "Laplacian边缘检测"))
        self.pushButton_sobel.setText(_translate("MainWindow", "Sobel边缘检测"))
        self.pushButton_canny.setText(_translate("MainWindow", "Canny边缘检测"))
        self.label_source_img.setText(_translate("MainWindow", "原图像"))
        self.label_dealt_img.setText(_translate("MainWindow", "处理后图像"))
