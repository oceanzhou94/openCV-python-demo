"""
@Auth ： youngZ
@File ：edgeDetection.py
图像边缘检测处理逻辑
"""

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from cv2 import cv2
from userInterface import edgeDetectionUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = edgeDetectionUI.Ui_MainWindow()  # 获取子窗口对象

        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 事件初始化

        self.cv_srcImage = None  # cv读取图片
        self.cv_dealtImage = None  # 处理后的图片，类型为cv2
        self.dst_img = None  # 处理后的图片 类型为QImage，保存图片时使用

    # 绑定事件
    def ui_init(self):
        # 打开图片并显示事件
        self.ui.pushButton_choose_img.clicked.connect(self.open_image)

        # 保存图片到本地事件
        self.ui.pushButton_save_img.clicked.connect(self.save_image)

        # 边缘检测点击事件
        self.ui.pushButton_laplacian.clicked.connect(self.laplacican_detection)  # laplacian边缘检测点击
        self.ui.pushButton_sobel.clicked.connect(self.sobel_detection)  # Sobel边缘检测点击
        self.ui.pushButton_canny.clicked.connect(self.canny_detection)  # Canny边缘检测点击

    # 打开图片并显示原图
    def open_image(self):
        # 获取图片和图片类型
        img_name, img_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '',
                                                         '图像文件(*.jpg *.bmp *.png *.jpeg)')
        # cv读取图片
        if img_name == "":
            # 未选择图片，弹出消息对话框
            QMessageBox.critical(self, '错误！', '请选择处理图像', QMessageBox.Close)
        else:
            self.cv_srcImage = cv2.imread(img_name)
            # 转换cv_srcImage类型为QImage
            hight, width, channel = self.cv_srcImage.shape
            q_image = None
            # 4通道类型的图
            if channel == 4:
                q_image = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGBA)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
            # 3通道类型的图
            elif channel == 3:
                q_image = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)
            # 单通道类型的图
            elif channel == 1:
                q_image = QImage(self.cv_srcImage.data, width, hight, QImage.Format_Grayscale8)
            # 将图片显示在label_source_img上面
            self.ui.label_source_img.setPixmap(QPixmap.fromImage(q_image))

    # 保存图片到本地
    def save_image(self):
        # 前面是地址，后面是文件类型,得到输入地址的文件名和地址txt(*.txt*.xls);;image(*.png)不同类别
        filepath, filetype = QFileDialog.getSaveFileName(self, "文件保存", "/", 'image(*.png)')

        try:
            # save方法保存图片到本地，filepath：保存的名称  PNG：保存的格式，-1：质量因素，值越大质量越高，-1表示默认值
            self.dst_img.save(filepath, 'PNG', -1)
        except Exception as error:
            # 消息弹出保存失败
            QMessageBox.critical(self, '错误！', "图像保存失败", QMessageBox.Close)
            print("保存失败，错误：", error)
        else:
            # 消息弹出保存成功
            QMessageBox.information(self, "通知", "图像保存成功", QMessageBox.Close)

        # 显示处理后的图片到label_dealt_img

    def show_in_dealt_label(self):
        # 图片转换成QImage类型
        hight, width, channel = self.cv_dealtImage.shape
        q_image = None
        # 4通道类型的图
        if channel == 4:
            q_image = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGBA)
            q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
        # 3通道类型的图
        elif channel == 3:
            q_image = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB)
            q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)
        # 单通道类型的图
        elif channel == 1:
            q_image = QImage(self.cv_dealtImage.data, width, hight, QImage.Format_Grayscale8)

        # 将图片显示在label_dealt_img上面
        self.dst_img = q_image
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # laplacian边缘检测处理函数
    def laplacican_detection(self):
        # laplacian边缘检测
        self.cv_dealtImage = cv2.Laplacian(self.cv_srcImage, cv2.CV_8U)

        # 检测后图片显示
        self.show_in_dealt_label()

    # Sobel边缘检测处理函数
    def sobel_detection(self):
        # sobel边缘检测，
        self.cv_dealtImage = cv2.Sobel(self.cv_srcImage, cv2.CV_8U, 0, 1)

        # 检测后图片显示
        self.show_in_dealt_label()

    # Canny边缘检测处理函数
    def canny_detection(self):
        # 图像灰度化
        gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY)

        # canny边缘检测，参数1：cv读取后的图像，参数2：第一阈值，参数3：第二阈值
        self.cv_dealtImage = cv2.Canny(gray, 100, 300)

        # 图片转换成QImage类型
        hight, width = self.cv_dealtImage.shape[0], self.cv_dealtImage.shape[1]  # 尺寸大小
        # 转换成QImage
        q_image = QImage(self.cv_dealtImage.data, width, hight, width, QImage.Format_Grayscale8)

        # 将图片显示在label_dealt_img上面
        self.dst_img = q_image
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))
