"""
@Auth ： youngZ
@File ：morphologicalTransformationUI.py
图像形态变换处理UI
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_dealt_img = QtWidgets.QLabel(self.centralwidget)
        self.label_dealt_img.setGeometry(QtCore.QRect(550, 340, 450, 400))
        self.label_dealt_img.setFrameShape(QtWidgets.QFrame.Box)
        self.label_dealt_img.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_dealt_img.setObjectName("label_dealt_img")

        self.pushButton_choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_img.setGeometry(QtCore.QRect(20, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_choose_img.setFont(font)
        self.pushButton_choose_img.setObjectName("pushButton_choose_img")

        self.pushButton_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_img.setGeometry(QtCore.QRect(860, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save_img.setFont(font)
        self.pushButton_save_img.setObjectName("pushButton_save_img")

        self.label_source_img = QtWidgets.QLabel(self.centralwidget)
        self.label_source_img.setGeometry(QtCore.QRect(0, 340, 450, 400))
        self.label_source_img.setFrameShape(QtWidgets.QFrame.Box)
        self.label_source_img.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_source_img.setObjectName("label_source_img")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 341, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")

        self.horizontalSlider_base = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_base.setGeometry(QtCore.QRect(70, 110, 200, 40))
        self.horizontalSlider_base.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_base.setMaximum(10)  # 设置最大值
        self.horizontalSlider_base.setMinimum(1)  # 设置最小值
        self.horizontalSlider_base.setSingleStep(1)  # 设置单步值
        self.horizontalSlider_base.setValue(1)  # 设置初始值
        self.horizontalSlider_base.setObjectName("horizontalSlider_base")

        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(70, 30, 200, 30))
        self.textEdit.setObjectName("textEdit")

        self.label_value_min = QtWidgets.QLabel(self.groupBox)
        self.label_value_min.setGeometry(QtCore.QRect(10, 110, 50, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_value_min.setFont(font)
        self.label_value_min.setFrameShape(QtWidgets.QFrame.Box)
        self.label_value_min.setAlignment(QtCore.Qt.AlignCenter)
        self.label_value_min.setObjectName("label_value_min")

        self.label__value_max = QtWidgets.QLabel(self.groupBox)
        self.label__value_max.setGeometry(QtCore.QRect(280, 110, 50, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label__value_max.setFont(font)
        self.label__value_max.setFrameShape(QtWidgets.QFrame.Box)
        self.label__value_max.setAlignment(QtCore.Qt.AlignCenter)
        self.label__value_max.setObjectName("label__value_max")

        self.pushButton_erosion = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_erosion.setGeometry(QtCore.QRect(40, 170, 93, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_erosion.setFont(font)
        self.pushButton_erosion.setObjectName("pushButton_erosion")

        self.pushButton_dilate = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_dilate.setGeometry(QtCore.QRect(190, 170, 93, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_dilate.setFont(font)
        self.pushButton_dilate.setObjectName("pushButton_dilate")

        self.label_current_value = QtWidgets.QLabel(self.groupBox)
        self.label_current_value.setGeometry(QtCore.QRect(100, 70, 131, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_current_value.setFont(font)
        self.label_current_value.setFrameShape(QtWidgets.QFrame.Box)
        self.label_current_value.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_current_value.setObjectName("label_current_value")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(550, 90, 450, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")

        self.pushButton_open = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_open.setGeometry(QtCore.QRect(60, 150, 93, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setObjectName("pushButton_open")

        self.pushButton_close = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_close.setGeometry(QtCore.QRect(290, 150, 93, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")

        self.pushButton_grads = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_grads.setGeometry(QtCore.QRect(180, 190, 93, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_grads.setFont(font)
        self.pushButton_grads.setObjectName("pushButton_grads")

        self.pushButton_black = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_black.setGeometry(QtCore.QRect(60, 190, 93, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_black.setFont(font)
        self.pushButton_black.setObjectName("pushButton_black")

        self.pushButton_topHat = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_topHat.setGeometry(QtCore.QRect(290, 190, 93, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_topHat.setFont(font)
        self.pushButton_topHat.setObjectName("pushButton_topHat")

        self.label__value_max_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label__value_max_2.setGeometry(QtCore.QRect(330, 100, 50, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label__value_max_2.setFont(font)
        self.label__value_max_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label__value_max_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label__value_max_2.setObjectName("label__value_max_2")

        self.horizontalSlider_high = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_high.setGeometry(QtCore.QRect(120, 100, 200, 40))
        self.horizontalSlider_high.setMaximum(10)  # 设置最大值
        self.horizontalSlider_high.setMinimum(1)  # 设置最小值
        self.horizontalSlider_high.setSingleStep(1)  # 设置单步值
        self.horizontalSlider_high.setValue(1)  # 设置初始值
        self.horizontalSlider_high.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_high.setObjectName("horizontalSlider_base_high")

        self.label_current_value_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_current_value_2.setGeometry(QtCore.QRect(150, 60, 131, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_current_value_2.setFont(font)
        self.label_current_value_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_current_value_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_current_value_2.setObjectName("label_current_value_2")

        self.label_value_min_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_value_min_2.setGeometry(QtCore.QRect(60, 100, 50, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_value_min_2.setFont(font)
        self.label_value_min_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_value_min_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_value_min_2.setObjectName("label_value_min_2")

        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 20, 200, 30))
        self.textEdit_2.setObjectName("textEdit_2")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_dealt_img.setText(_translate("MainWindow", "处理后图像"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_save_img.setText(_translate("MainWindow", "保存图片"))
        self.label_source_img.setText(_translate("MainWindow", "原图像"))
        self.groupBox.setTitle(_translate("MainWindow", "基本形态操作"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">滑动设定内核的大小</span></p></body></html>"))
        self.label_value_min.setText(_translate("MainWindow", "1"))
        self.label__value_max.setText(_translate("MainWindow", "10"))
        self.pushButton_erosion.setText(_translate("MainWindow", "腐蚀操作"))
        self.pushButton_dilate.setText(_translate("MainWindow", "膨胀操作"))
        self.label_current_value.setText(_translate("MainWindow", "当前大小："))
        self.groupBox_2.setTitle(_translate("MainWindow", "高级形态操作"))
        self.pushButton_open.setText(_translate("MainWindow", "开运算"))
        self.pushButton_close.setText(_translate("MainWindow", "闭运算"))
        self.pushButton_grads.setText(_translate("MainWindow", "梯度运算"))
        self.pushButton_black.setText(_translate("MainWindow", "黑帽运算"))
        self.pushButton_topHat.setText(_translate("MainWindow", "礼帽运算"))
        self.label__value_max_2.setText(_translate("MainWindow", "10"))
        self.label_current_value_2.setText(_translate("MainWindow", "当前大小："))
        self.label_value_min_2.setText(_translate("MainWindow", "1"))
        self.textEdit_2.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">滑动设定内核的大小</span></p></body></html>"))