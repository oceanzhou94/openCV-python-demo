"""
@Auth ： youngZ
@File ：mainWindow.py
"""
from PyQt5.QtWidgets import QMainWindow

from userInterface import mainWindowUI

from businessLogic import makeImageMask
from businessLogic import characterCoding
from businessLogic import faceDetection
from businessLogic import geometricTransformation


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)
        # 布局初始化
        self.ui = mainWindowUI.Ui_MainWindow()
        self.ui.setupUi(MainWindow=self)

        # 子窗口实例化命名空间
        self.characterCoding = None  # 人物图像打码子窗口对象
        self.makeImageMask = None  # 创建图像掩膜子窗口对象
        self.faceDetection = None  # 人脸识别和检测子窗口对象
        self.geometricTransformation = None  # 图像几何变换子窗口对象

        # 信号与槽定义
        self.signal_and_slot()

    # 定义触发事件
    def signal_and_slot(self):
        self.ui.pushButton_1.clicked.connect(self.push_button_1)
        self.ui.pushButton_2.clicked.connect(self.push_button_2)
        self.ui.pushButton_3.clicked.connect(self.push_button_3)
        self.ui.pushButton_12.clicked.connect(self.push_button_12)

    # 按钮1-人物图像打码触发事件
    def push_button_1(self):
        self.characterCoding = characterCoding.SubWindow()
        self.characterCoding.show()

    # 按钮2-创建图像掩膜触发事件
    def push_button_2(self):
        self.makeImageMask = makeImageMask.SubWindow()
        self.makeImageMask.show()

    # 按钮3-图像几何变换触发事件
    def push_button_3(self):
        self.geometricTransformation = geometricTransformation.SubWindow()
        self.geometricTransformation.show()

    # 按钮12-人脸识别检测触发事件
    def push_button_12(self):
        self.faceDetection = faceDetection.SubWindow()
        self.faceDetection.show()
