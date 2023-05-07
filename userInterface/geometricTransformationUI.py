"""
@Auth ： youngZ
@File ：geometricTransformationUI.py
图像几何变换UI
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 797)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(0, 110, 240, 201))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 220, 81))
        self.textBrowser.setObjectName("textBrowser")

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(70, 120, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setRange(0.2, 5)  # 设置取值范围(最大值, 最小值)
        self.doubleSpinBox.setValue(1)  # 设置当前值
        self.doubleSpinBox.setDecimals(1)  # 设置小数点后位数
        self.doubleSpinBox.setSingleStep(0.2)  # 步长，每按一下按钮改变的值
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        self.pushButton_ok_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok_1.setGeometry(QtCore.QRect(10, 170, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ok_1.setFont(font)
        self.pushButton_ok_1.setObjectName("pushButton_ok_1")
        self.pushButton_recover = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_recover.setGeometry(QtCore.QRect(130, 170, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_recover.setFont(font)
        self.pushButton_recover.setObjectName("pushButton_recover")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 110, 240, 201))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(25, 40, 190, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 130, 200, 31))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMaximum(360)  # 设置最大值
        self.horizontalSlider.setMinimum(0)  # 设置最小值
        self.horizontalSlider.setSingleStep(1)  # 设置单步值
        self.horizontalSlider.setValue(0)  # 设置初始值
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.pushButton_ok_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_ok_2.setGeometry(QtCore.QRect(10, 170, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ok_2.setFont(font)
        self.pushButton_ok_2.setObjectName("pushButton_ok_2")
        self.pushButton_recover_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_recover_2.setGeometry(QtCore.QRect(130, 170, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_recover_2.setFont(font)
        self.pushButton_recover_2.setObjectName("pushButton_recover_2")
        self.label_value_show = QtWidgets.QLabel(self.groupBox_2)
        self.label_value_show.setGeometry(QtCore.QRect(50, 90, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_value_show.setFont(font)
        self.label_value_show.setFrameShape(QtWidgets.QFrame.Box)
        self.label_value_show.setObjectName("label_value_show")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 110, 380, 201))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 40, 320, 81))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_flip_horizontal = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_flip_horizontal.setGeometry(QtCore.QRect(20, 140, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_flip_horizontal.setFont(font)
        self.pushButton_flip_horizontal.setObjectName("pushButton_flip_horizontal")
        self.pushButton_flip_vertical = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_flip_vertical.setGeometry(QtCore.QRect(140, 140, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_flip_vertical.setFont(font)
        self.pushButton_flip_vertical.setObjectName("pushButton_flip_vertical")
        self.pushButton_flip_diagonal = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_flip_diagonal.setGeometry(QtCore.QRect(260, 140, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_flip_diagonal.setFont(font)
        self.pushButton_flip_diagonal.setObjectName("pushButton_flip_diagonal")
        self.pushButton_choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_img.setGeometry(QtCore.QRect(50, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_choose_img.setFont(font)
        self.pushButton_choose_img.setObjectName("pushButton_choose_img")
        self.pushButton_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_img.setGeometry(QtCore.QRect(820, 20, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save_img.setFont(font)
        self.pushButton_save_img.setObjectName("pushButton_save_img")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 340, 450, 400))
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
        self.scrollArea_3.setGeometry(QtCore.QRect(540, 340, 450, 400))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "图像缩放变换"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:600; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">输入需要缩放的倍数</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">大于1表示图像放大</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">小于1表示图像缩小</span></p></body></html>"))
        self.pushButton_ok_1.setText(_translate("MainWindow", "确定"))
        self.pushButton_recover.setText(_translate("MainWindow", "恢复"))
        self.groupBox_2.setTitle(_translate("MainWindow", "图像旋转变换"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:600; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">滑动控制旋转角度</span></p></body></html>"))
        self.pushButton_ok_2.setText(_translate("MainWindow", "确定"))
        self.pushButton_recover_2.setText(_translate("MainWindow", "恢复"))
        self.label_value_show.setText(_translate("MainWindow", "旋转角度："))
        self.groupBox_3.setTitle(_translate("MainWindow", "图像镜像变换"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:600; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">水平镜像：将图像按左右对称翻转</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">垂直镜像：将图像按上下对称翻转</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">对角镜像：将图像按中心对称翻转</span></p></body></html>"))
        self.pushButton_flip_horizontal.setText(_translate("MainWindow", "水平镜像"))
        self.pushButton_flip_vertical.setText(_translate("MainWindow", "垂直镜像"))
        self.pushButton_flip_diagonal.setText(_translate("MainWindow", "对角镜像"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_save_img.setText(_translate("MainWindow", "保存图片"))
        self.label_source_img.setText(_translate("MainWindow", "原图像"))
        self.label_dealt_img.setText(_translate("MainWindow", "处理后图像"))
