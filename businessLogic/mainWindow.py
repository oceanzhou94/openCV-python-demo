"""
@Auth ： youngZ
@File ：mainWindow.py
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from userInterface import mainWindowUI

from businessLogic import characterCoding, edgeDetection
from businessLogic import faceDetection
from businessLogic import geometricTransformation
from businessLogic import makeImageMask, morphologicalTransformation
from businessLogic import contourDetection
from businessLogic import histogramEqualization
from businessLogic import templateMatch
from businessLogic import imageSegmentation
from businessLogic import featureDetection
from businessLogic import featureMatching
from businessLogic import about


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)
        # 布局初始化

        self.ui = mainWindowUI.Ui_MainWindow()
        self.ui.setup_ui(MainWindow=self)

        # 子窗口实例化命名空间
        self.characterCoding = None  # 人物图像打码子窗口对象
        self.makeImageMask = None  # 创建图像掩膜子窗口对象
        self.faceDetection = None  # 人脸识别和检测子窗口对象
        self.geometricTransformation = None  # 图像几何变换子窗口对象
        self.morphologicalTransformation = None  # 图像形态变换子窗口对象
        self.edgeDetection = None  # 图像边缘检测子窗口对象
        self.contourDetection = None  # 图像轮廓检测子窗口对象
        self.histogramEqualization = None  # 直方图均衡化子窗口对象
        self.templateMatch = None  # 图像模板匹配子窗口对象
        self.imageSegmentation = None  # 图像分割功能子窗口对象
        self.featureDetection = None  # 图像检测功能子窗口对象
        self.featureMatching = None  # 图像特征匹配子窗口对象
        self.about = None  # 关于子窗口对象

        # 图标
        self.setWindowIcon(QIcon('./dataAccess/icon/icon.ico'))

        # 信号与槽定义
        self.signal_and_slot()

    # 定义触发事件
    def signal_and_slot(self):
        self.ui.pushButton_1.clicked.connect(self.push_button_1)
        self.ui.pushButton_2.clicked.connect(self.push_button_2)
        self.ui.pushButton_3.clicked.connect(self.push_button_3)
        self.ui.pushButton_4.clicked.connect(self.push_button_4)
        self.ui.pushButton_5.clicked.connect(self.push_button_5)
        self.ui.pushButton_6.clicked.connect(self.push_button_6)
        self.ui.pushButton_7.clicked.connect(self.push_button_7)
        self.ui.pushButton_8.clicked.connect(self.push_button_8)
        self.ui.pushButton_9.clicked.connect(self.push_button_9)
        self.ui.pushButton_10.clicked.connect(self.push_button_10)
        self.ui.pushButton_11.clicked.connect(self.push_button_11)
        self.ui.pushButton_12.clicked.connect(self.push_button_12)
        self.ui.pushButton_exit.clicked.connect(self.push_button_exit)
        self.ui.pushButton_about.clicked.connect(self.push_button_about)

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

    # 按钮4-图像形态变换触发事件
    def push_button_4(self):
        self.morphologicalTransformation = morphologicalTransformation.SubWindow()
        self.morphologicalTransformation.show()

    # 按钮5-直方图均衡化触发事件
    def push_button_5(self):
        self.histogramEqualization = histogramEqualization.SubWindow()
        self.histogramEqualization.show()

    # 按钮6-图像边缘检测触发事件
    def push_button_6(self):
        self.edgeDetection = edgeDetection.SubWindow()
        self.edgeDetection.show()

    # 按钮7-图像轮廓检测触发事件
    def push_button_7(self):
        self.contourDetection = contourDetection.SubWindow()
        self.contourDetection.show()

    # 按钮8-图像模板匹配触发事件
    def push_button_8(self):
        self.templateMatch = templateMatch.SubWindow()
        self.templateMatch.show()

    # 按钮9-图像分割功能触发事件
    def push_button_9(self):
        self.imageSegmentation = imageSegmentation.SubWindow()
        self.imageSegmentation.show()

    # 按钮10-图像检测功能触发事件
    def push_button_10(self):
        self.featureDetection = featureDetection.SubWindow()
        self.featureDetection.show()

    # 按钮11-图像特征匹配触犯事件
    def push_button_11(self):
        self.featureMatching = featureMatching.SubWindow()
        self.featureMatching.show()

    # 按钮12-人脸识别检测触发事件
    def push_button_12(self):
        self.faceDetection = faceDetection.SubWindow()
        self.faceDetection.show()

    # 退出程序按钮
    def push_button_exit(self):
        sys.exit()

    # 关于按钮
    def push_button_about(self):
        self.about = about.SubWindow()
        self.about.show()



