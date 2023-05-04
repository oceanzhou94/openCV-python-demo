"""
@Auth ： youngZ
@File ：makeImageMask.py
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from cv2 import cv2

# 子窗口布局
from userInterface import makeImageMaskUI


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = makeImageMaskUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_init()
        self.cv_srcImage = None

    # 绑定事件
    def ui_init(self):
        self.ui.pushButton_choose_img.clicked.connect(self.open_image)

    # 打开图片并显示原图
    def open_image(self):
        # 获取图片和图片类型
        img_name, img_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '',
                                                         '图像文件(*.jpg *.bmp *.png *.jpeg)')
        self.cv_srcImage = cv2.imread(img_name)

        # cv读取图片
        self.cv_srcImage = cv2.imread(img_name)

        # 调整图片大小--在label中显示正常大小
        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_source_img.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_source_img.height())

        # 将图片显示在label_source_img上面
        self.ui.label_source_img.setPixmap(QPixmap.fromImage(ui_image))
