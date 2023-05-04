"""
@Auth ： youngZ
@File ：makeImageMaskUI.py
创建图像掩膜处理UI
"""

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 原图
        self.label_source_img = QtWidgets.QLabel(self.centralwidget)
        self.label_source_img.setGeometry(QtCore.QRect(0, 250, 450, 400))
        self.label_source_img.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_source_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_source_img.setObjectName("label")

        # 处理后图片
        self.label_dealt_img = QtWidgets.QLabel(self.centralwidget)
        self.label_dealt_img.setGeometry(QtCore.QRect(550, 250, 450, 400))
        self.label_dealt_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dealt_img.setObjectName("label_2")

        # 选择图片按钮
        self.pushButton_choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_img.setGeometry(QtCore.QRect(175, 60, 100, 50))
        self.pushButton_choose_img.setObjectName("pushButton")

        # 创建掩膜按钮
        self.pushButton_make_mask = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_make_mask.setGeometry(QtCore.QRect(450, 60, 100, 50))
        self.pushButton_make_mask.setObjectName("pushButton_2")

        # 保存图片按钮
        self.pushButton__save_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton__save_img.setGeometry(QtCore.QRect(725, 60, 100, 50))
        self.pushButton__save_img.setObjectName("pushButton_3")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "创建图像掩膜"))
        self.label_source_img.setText(_translate("MainWindow", "原图"))
        self.label_dealt_img.setText(_translate("MainWindow", "处理后图片"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_make_mask.setText(_translate("MainWindow", "创建掩膜"))
        self.pushButton__save_img.setText(_translate("MainWindow", "保存图片"))
