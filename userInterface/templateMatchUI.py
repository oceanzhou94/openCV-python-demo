"""
@Auth ： youngZ
@File ：templateMatchUI.py
图像模板匹配UI
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
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
        self.label_source_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_source_img.setObjectName("label_source_img")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(470, 350, 450, 400))
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(False)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_tmpl_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_tmpl_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_tmpl_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_tmpl_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_tmpl_img.setObjectName("label_tmpl_img")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_img.setGeometry(QtCore.QRect(1090, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_save_img.setFont(font)
        self.pushButton_save_img.setObjectName("pushButton_save_img")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(200, 80, 1000, 241))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_choose_tmpl = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_choose_tmpl.setGeometry(QtCore.QRect(20, 90, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_choose_tmpl.setFont(font)
        self.pushButton_choose_tmpl.setObjectName("pushButton_choose_tmpl")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea_5.setGeometry(QtCore.QRect(600, 30, 391, 201))
        self.scrollArea_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_5.setWidgetResizable(False)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.label_result = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_result.setFont(font)
        self.label_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_result.setObjectName("label_result")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 50, 200, 160))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_match_s1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_match_s1.setGeometry(QtCore.QRect(20, 40, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_match_s1.setFont(font)
        self.pushButton_match_s1.setObjectName("pushButton_match_s1")
        self.pushButton_match_s2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_match_s2.setGeometry(QtCore.QRect(20, 80, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_match_s2.setFont(font)
        self.pushButton_match_s2.setObjectName("pushButton_match_s2")
        self.pushButton_match_s3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_match_s3.setGeometry(QtCore.QRect(20, 120, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_match_s3.setFont(font)
        self.pushButton_match_s3.setObjectName("pushButton_match_s3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 50, 200, 160))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_match_m1 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_match_m1.setGeometry(QtCore.QRect(20, 40, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_match_m1.setFont(font)
        self.pushButton_match_m1.setObjectName("pushButton_match_m1")
        self.pushButton_match_m2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_match_m2.setGeometry(QtCore.QRect(20, 80, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_match_m2.setFont(font)
        self.pushButton_match_m2.setObjectName("pushButton_match_m2")
        self.pushButton_match_m3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_match_m3.setGeometry(QtCore.QRect(20, 120, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_match_m3.setFont(font)
        self.pushButton_match_m3.setObjectName("pushButton_match_m3")
        self.pushButton_choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_img.setGeometry(QtCore.QRect(200, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_choose_img.setFont(font)
        self.pushButton_choose_img.setObjectName("pushButton_choose_img")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_4.setGeometry(QtCore.QRect(950, 350, 450, 400))
        self.scrollArea_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setWidgetResizable(False)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 4000, 4000))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.label_dealt_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_dealt_img.setGeometry(QtCore.QRect(0, 0, 2000, 2000))
        self.label_dealt_img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_dealt_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_dealt_img.setObjectName("label_dealt_img")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_source_img.setText(_translate("MainWindow", "原图像"))
        self.label_tmpl_img.setText(_translate("MainWindow", "匹配模板"))
        self.pushButton_save_img.setText(_translate("MainWindow", "保存图片"))
        self.groupBox.setTitle(_translate("MainWindow", "图像模板匹配"))
        self.pushButton_choose_tmpl.setText(_translate("MainWindow", "选择模板"))
        self.label_result.setText(_translate("MainWindow", "匹配结果数组"))
        self.groupBox_2.setTitle(_translate("MainWindow", "单目标匹配"))
        self.pushButton_match_s1.setText(_translate("MainWindow", "方差匹配"))
        self.pushButton_match_s2.setText(_translate("MainWindow", "相关匹配"))
        self.pushButton_match_s3.setText(_translate("MainWindow", "相关系数匹配"))
        self.groupBox_3.setTitle(_translate("MainWindow", "多目标匹配"))
        self.pushButton_match_m1.setText(_translate("MainWindow", "标准方差匹配"))
        self.pushButton_match_m2.setText(_translate("MainWindow", "标准相关匹配"))
        self.pushButton_match_m3.setText(_translate("MainWindow", "标准相关系数匹配"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.label_dealt_img.setText(_translate("MainWindow", "匹配结果"))

