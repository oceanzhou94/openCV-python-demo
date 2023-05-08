"""
@Auth ： youngZ
@File ：featureDetectionUI.py
图像角检测和特征检测UI
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 90, 320, 220))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_Harris = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Harris.setGeometry(QtCore.QRect(75, 40, 170, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Harris.setFont(font)
        self.pushButton_Harris.setObjectName("pushButton_Harris")
        self.pushButton_SubPix = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_SubPix.setGeometry(QtCore.QRect(75, 100, 170, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_SubPix.setFont(font)
        self.pushButton_SubPix.setObjectName("pushButton_SubPix")
        self.pushButton_ShiTomasi = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ShiTomasi.setGeometry(QtCore.QRect(75, 160, 170, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_ShiTomasi.setFont(font)
        self.pushButton_ShiTomasi.setObjectName("pushButton_ShiTomasi")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 90, 451, 220))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_sift = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_sift.setGeometry(QtCore.QRect(10, 100, 170, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_sift.setFont(font)
        self.pushButton_sift.setObjectName("pushButton_sift")
        self.pushButton_fast = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_fast.setGeometry(QtCore.QRect(10, 40, 170, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_fast.setFont(font)
        self.pushButton_fast.setObjectName("pushButton_fast")
        self.pushButton_orb = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_orb.setGeometry(QtCore.QRect(10, 160, 170, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_orb.setFont(font)
        self.pushButton_orb.setObjectName("pushButton_orb")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(200, 30, 251, 191))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_result = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_result.setGeometry(QtCore.QRect(10, 10, 4000, 4000))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_result.setFont(font)
        self.label_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_result.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_result.setObjectName("label_result")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_img.setGeometry(QtCore.QRect(100, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_choose_img.setFont(font)
        self.pushButton_choose_img.setObjectName("pushButton_choose_img")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(550, 340, 450, 400))
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(False)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(-20, 0, 4000, 4000))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_dealt_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_dealt_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_dealt_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_dealt_img.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_dealt_img.setObjectName("label_dealt_img")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_img.setGeometry(QtCore.QRect(780, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_save_img.setFont(font)
        self.pushButton_save_img.setObjectName("pushButton_save_img")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 340, 450, 400))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(-20, 0, 4000, 4000))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_source_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_source_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_source_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_source_img.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_source_img.setObjectName("label_source_img")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "图像特征检测"))
        self.groupBox.setTitle(_translate("MainWindow", "图像角检测"))
        self.pushButton_Harris.setText(_translate("MainWindow", "哈里斯角检测"))
        self.pushButton_SubPix.setText(_translate("MainWindow", "优化哈里斯角检测"))
        self.pushButton_ShiTomasi.setText(_translate("MainWindow", "Shi-Tomasi角检测"))
        self.groupBox_2.setTitle(_translate("MainWindow", "图像特征检测"))
        self.pushButton_sift.setText(_translate("MainWindow", "SIFT关键点检测"))
        self.pushButton_fast.setText(_translate("MainWindow", "FAST关键点检测"))
        self.pushButton_orb.setText(_translate("MainWindow", "ORB关键点检测"))
        self.label_result.setText(_translate("MainWindow", "结果显示"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.label_dealt_img.setText(_translate("MainWindow", "处理后图像"))
        self.pushButton_save_img.setText(_translate("MainWindow", "保存图片"))
        self.label_source_img.setText(_translate("MainWindow", "原图像"))
