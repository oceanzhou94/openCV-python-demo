"""
@Auth ： youngZ
@File ：geometricTransformationUI.py
图像几何变换UI
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(40, 210, 101, 41))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setRange(0.2, 5)  # 设置取值范围(最大值, 最小值)
        self.doubleSpinBox.setValue(1)  # 设置当前值
        self.doubleSpinBox.setDecimals(1)  # 设置小数点后位数
        self.doubleSpinBox.setSingleStep(0.2)  # 步长，每按一下按钮改变的值

        # 设置的groupBox容器,将显示图片的label标签插入到容器里面可以实现图片的拖拽移动效果
        self.groupBox_source_img = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_source_img.setGeometry(QtCore.QRect(0, 330, 450, 400))
        self.groupBox_source_img.setObjectName("groupBox_source_img")

        self.label_source_img = QtWidgets.QLabel(self.groupBox_source_img)
        self.label_source_img.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.label_source_img.setAlignment(QtCore.Qt.AlignTop)  # 设置图片靠上端对齐
        self.label_source_img.setAlignment(QtCore.Qt.AlignLeft)  # 设置图片靠左端对齐
        self.label_source_img.setObjectName("label_source_img")

        # 设置的groupBox容器,将显示图片的label标签插入到容器里面可以实现图片的拖拽移动效果
        self.groupBox_dealt_img = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_dealt_img.setGeometry(QtCore.QRect(550, 330, 450, 400))
        self.groupBox_dealt_img.setObjectName("groupBox_dealt_img")

        self.label_dealt_img = QtWidgets.QLabel(self.groupBox_dealt_img)
        self.label_dealt_img.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_dealt_img.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.label_dealt_img.setAlignment(QtCore.Qt.AlignTop)  # 设置图片靠上端对齐
        self.label_dealt_img.setAlignment(QtCore.Qt.AlignLeft)  # 设置图片靠左端对齐
        self.label_dealt_img.setObjectName("label_dealt_img")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 130, 211, 71))
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton_ok_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok_1.setGeometry(QtCore.QRect(0, 260, 93, 28))
        self.pushButton_ok_1.setObjectName("pushButton_ok_1")

        self.pushButton_recover = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_recover.setGeometry(QtCore.QRect(120, 260, 93, 28))
        self.pushButton_recover.setObjectName("pushButton_recover")

        # 滑动组件
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(310, 230, 200, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMaximum(360)  # 设置最大值
        self.horizontalSlider.setMinimum(0)  # 设置最小值
        self.horizontalSlider.setSingleStep(1)  # 设置单步值
        self.horizontalSlider.setValue(0)  # 设置初始值
        self.horizontalSlider.setObjectName("horizontalSlider")

        # 显示滑动组件的数值
        self.label_value_show = QtWidgets.QLabel(self.centralwidget)
        self.label_value_show.setGeometry(QtCore.QRect(340, 190, 130, 30))
        self.label_value_show.setFrameShape(QtWidgets.QFrame.Box)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(0, 110, 221, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(320, 150, 191, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.pushButton_recover_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_recover_2.setGeometry(QtCore.QRect(420, 260, 93, 28))
        self.pushButton_recover_2.setObjectName("pushButton_no_2")

        self.pushButton_ok_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok_2.setGeometry(QtCore.QRect(300, 260, 93, 28))
        self.pushButton_ok_2.setObjectName("pushButton_ok_2")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 110, 221, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")

        self.pushButton_flip_horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_flip_horizontal.setGeometry(QtCore.QRect(670, 260, 93, 28))
        self.pushButton_flip_horizontal.setObjectName("pushButton_flip_horizontal")

        self.pushButton_flip_vertical = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_flip_vertical.setGeometry(QtCore.QRect(780, 260, 93, 28))
        self.pushButton_flip_vertical.setObjectName("pushButton_flip_vertical")

        self.pushButton_flip_diagonal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_flip_diagonal.setGeometry(QtCore.QRect(890, 260, 93, 28))
        self.pushButton_flip_diagonal.setObjectName("pushButton_flip_diagonal")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(670, 150, 311, 71))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 110, 381, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")

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

        self.label_source_img.raise_()
        self.label_dealt_img.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser_3.raise_()
        self.pushButton_ok_1.raise_()
        self.pushButton_recover.raise_()
        self.pushButton_recover_2.raise_()
        self.pushButton_ok_2.raise_()
        self.pushButton_flip_horizontal.raise_()
        self.pushButton_flip_vertical.raise_()
        self.pushButton_flip_diagonal.raise_()
        self.pushButton_choose_img.raise_()
        self.pushButton_save_img.raise_()
        self.horizontalSlider.raise_()
        self.doubleSpinBox.raise_()

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
        MainWindow.setWindowTitle(_translate("MainWindow", "图像几何变换"))
        self.label_source_img.setText(_translate("MainWindow", "原图像"))
        self.label_dealt_img.setText(_translate("MainWindow", "处理后图像"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">输入需要缩放的倍数</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">大于1表示图像放大</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">小于1表示图像缩小</span></p></body></html>"))
        self.pushButton_ok_1.setText(_translate("MainWindow", "确定"))
        self.pushButton_recover.setText(_translate("MainWindow", "恢复"))
        self.groupBox.setTitle(_translate("MainWindow", "图像缩放变换"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">滑动控制旋转角度</span></p></body></html>"))
        self.pushButton_recover_2.setText(_translate("MainWindow", "恢复"))
        self.pushButton_ok_2.setText(_translate("MainWindow", "确定"))
        self.groupBox_2.setTitle(_translate("MainWindow", "图像旋转变换"))
        self.pushButton_flip_horizontal.setText(_translate("MainWindow", "水平镜像"))
        self.pushButton_flip_vertical.setText(_translate("MainWindow", "垂直镜像"))
        self.pushButton_flip_diagonal.setText(_translate("MainWindow", "对角镜像"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">水平镜像：将图像按左右对称翻转</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">垂直镜像：将图像按上下对称翻转</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">对角镜像：将图像按中心对称翻转</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "图像镜像变换"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_save_img.setText(_translate("MainWindow", "保存图片"))
