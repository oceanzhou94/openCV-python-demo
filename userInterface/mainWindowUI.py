"""
@Auth ： youngZ
@File ：mainWindowUI.py
主窗口UI
"""
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    # 初始化主界面
    def setupUi(self, MainWindow):
        # 主窗口对象名称
        MainWindow.setObjectName("MainWindow")
        # 主窗口尺寸大小
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 主界面大标题
        self.label_big_title = QtWidgets.QLabel(self.centralwidget)
        self.label_big_title.setGeometry(QtCore.QRect(100, 0, 600, 100))

        # 大标题格式设计
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_big_title.setFont(font)
        self.label_big_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_big_title.setObjectName("label_big_title")

        # 按钮1-人物图像打码
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 150, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton")

        # 按钮2-图像掩膜处理
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 150, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        # 按钮3-图像几何变换
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 150, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        # 按钮4-图像形态变换
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 240, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        # 按钮5-直方图均衡化
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 240, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        # 按钮6-图像边缘检测
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 240, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        # 按钮7-图像轮廓检测
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 330, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        # 按钮8-图像模板匹配
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 330, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")

        # 按钮9-图像分割功能
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 330, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")

        # 按钮10-图像检测功能
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 420, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")

        # 按钮11-图像特征匹配
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(300, 420, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")

        # 按钮12-人脸识别检测
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(550, 420, 200, 60))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenCV图像处理演示程序"))
        self.label_big_title.setText(_translate("MainWindow", "OpenCV图像处理演示界面"))
        self.pushButton_1.setText(_translate("MainWindow", "人物图像打码"))
        self.pushButton_2.setText(_translate("MainWindow", "图像掩膜处理"))
        self.pushButton_3.setText(_translate("MainWindow", "图像几何变换"))
        self.pushButton_4.setText(_translate("MainWindow", "图像形态变换"))
        self.pushButton_5.setText(_translate("MainWindow", "直方图均衡化"))
        self.pushButton_6.setText(_translate("MainWindow", "图像边缘检测"))
        self.pushButton_7.setText(_translate("MainWindow", "图像轮廓检测"))
        self.pushButton_8.setText(_translate("MainWindow", "图像模板匹配"))
        self.pushButton_9.setText(_translate("MainWindow", "图像分割融合"))
        self.pushButton_10.setText(_translate("MainWindow", "图像特征检测"))
        self.pushButton_11.setText(_translate("MainWindow", "图像特征匹配"))
        self.pushButton_12.setText(_translate("MainWindow", "动态人脸识别"))
