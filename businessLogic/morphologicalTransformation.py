"""
@Auth ： youngZ
@File ：morphologicalTransformation.py
图像形态变换逻辑处理
"""
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from cv2 import cv2
from userInterface import morphologicalTransformationUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = morphologicalTransformationUI.Ui_MainWindow()  # 获取子窗口对象

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

        # 基本形态操作点击事件
        self.ui.pushButton_erosion.clicked.connect(self.erode_image)  # 点击腐蚀操作
        self.ui.pushButton_dilate.clicked.connect(self.dilate_image)  # 点击膨胀操作
        self.ui.pushButton_open.clicked.connect(self.opening_operation_image)  # 点击开运算操作
        self.ui.pushButton_close.clicked.connect(self.closing_operation_image)  # 点击闭运算操作
        self.ui.pushButton_grads.clicked.connect(self.gradient_operation_image)  # 点击梯度运算操作
        self.ui.pushButton_black.clicked.connect(self.black_hat_operation_image)  # 点击黑帽运算操作
        self.ui.pushButton_topHat.clicked.connect(self.top_hat_operation_image)  # 点击礼帽运算操作

        # 滑动控件显示数值事件
        self.ui.horizontalSlider_base.valueChanged.connect(self.base_slider_value_show)  # 基本操作中的滑动
        self.ui.horizontalSlider_high.valueChanged.connect(self.high_slider_value_show)  # 高级操作中的滑动

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
            print("通道数：", channel)
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
        self.dst_img.save(filepath, 'PNG', -1)

    # 显示处理后的图片到label_dealt_img
    def show_in_dealt_label(self):
        # 图片转换成QImage类型
        hight, width, channel = self.cv_dealtImage.shape
        print("通道数：", channel)
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

    # 实时显示滑动控件base的数值
    def base_slider_value_show(self):
        # 读取当前滑动条值
        value = self.ui.horizontalSlider_base.value()

        # 强制类型转换，label框需要str类型值
        show_str = "当前大小:" + str(value) + "x" + str(value)

        # 显示数值
        self.ui.label_current_value.setText(show_str)

    # 实时显示滑动控件high的数值
    def high_slider_value_show(self):
        # 读取当前滑动条值
        value = self.ui.horizontalSlider_high.value()

        # 强制类型转换，label框需要str类型值
        show_str = "当前大小:" + str(value) + "x" + str(value)

        # 显示数值
        self.ui.label_current_value_2.setText(show_str)

    # 腐蚀操作并将操作后的图片显示
    def erode_image(self):
        # 从滑动组件获取核心大小
        value = self.ui.horizontalSlider_base.value()
        print(f"核心大小：{value}")

        # 定义核心
        kernel = np.ones((value, value), np.uint8)

        # 腐蚀操作，迭代5次，参数1：cv读取后的二值化图像，参数二：内核数，参数3：迭代次数
        self.cv_dealtImage = cv2.erode(self.cv_srcImage, kernel, iterations=5)

        # 显示处理后图像
        self.show_in_dealt_label()

    # 膨胀操作并将操作后的图片显示
    def dilate_image(self):
        # 从滑动组件获取核心大小
        value = self.ui.horizontalSlider_base.value()
        print(f"核心大小：{value}")

        # 定义核心
        kernel = np.ones((value, value), np.uint8)

        # 腐蚀操作，迭代5次，参数1：cv读取后的二值化图像，参数2：内核数，参数3：迭代次数
        self.cv_dealtImage = cv2.dilate(self.cv_srcImage, kernel, iterations=5)

        # 显示处理后图像
        self.show_in_dealt_label()

    # 开运算操作并将操作后的图片显示
    def opening_operation_image(self):
        # 从滑动组件获取核心大小
        value = self.ui.horizontalSlider_high.value()
        print(f"核心大小：{value}")

        # 定义核心
        kernel = np.ones((value, value), np.uint8)

        # 设置形态操作类型，表示操作类型为开运算
        operation = cv2.MORPH_OPEN

        # 形态操作，参数1：cv读取后的二值化图像，参数2：形态操作类型，参数3：内核大小，参数4：迭代次数
        self.cv_dealtImage = cv2.morphologyEx(self.cv_srcImage, operation, kernel, iterations=5)

        # 显示处理后图像
        self.show_in_dealt_label()

    # 闭运算操作并将操作后的图片显示
    def closing_operation_image(self):
        # 从滑动组件获取核心大小
        value = self.ui.horizontalSlider_high.value()
        print(f"核心大小：{value}")

        # 定义核心
        kernel = np.ones((value, value), np.uint8)

        # 设置形态操作类型，表示操作类型为闭运算
        operation = cv2.MORPH_CLOSE

        # 形态操作，参数1：cv读取后的二值化图像，参数2：形态操作类型，参数3：内核大小，参数4：迭代次数
        self.cv_dealtImage = cv2.morphologyEx(self.cv_srcImage, operation, kernel, iterations=5)

        # 显示处理后图像
        self.show_in_dealt_label()

    # 梯度运算操作并将操作后的图片显示
    def gradient_operation_image(self):
        # 从滑动组件获取核心大小
        value = self.ui.horizontalSlider_high.value()
        print(f"核心大小：{value}")

        # 定义核心
        kernel = np.ones((value, value), np.uint8)

        # 设置形态操作类型，表示操作类型为梯度运算
        operation = cv2.MORPH_GRADIENT

        # 形态操作，参数1：cv读取后的二值化图像，参数2：形态操作类型，参数3：内核大小，参数4：迭代次数
        self.cv_dealtImage = cv2.morphologyEx(self.cv_srcImage, operation, kernel, iterations=1)

        # 显示处理后图像
        self.show_in_dealt_label()

    # 黑帽运算操作并将操作后的图片显示
    def black_hat_operation_image(self):
        # 从滑动组件获取核心大小
        value = self.ui.horizontalSlider_high.value()
        print(f"核心大小：{value}")

        # 定义核心
        kernel = np.ones((value, value), np.uint8)

        # 设置形态操作类型，表示操作类型为黑帽运算
        operation = cv2.MORPH_BLACKHAT

        # 形态操作，参数1：cv读取后的二值化图像，参数2：形态操作类型，参数3：内核大小，参数4：迭代次数
        self.cv_dealtImage = cv2.morphologyEx(self.cv_srcImage, operation, kernel, iterations=5)

        # 显示处理后图像
        self.show_in_dealt_label()

    # 礼帽运算操作并将操作后的图片显示
    def top_hat_operation_image(self):
        # 从滑动组件获取核心大小
        value = self.ui.horizontalSlider_high.value()
        print(f"核心大小：{value}")

        # 定义核心
        kernel = np.ones((value, value), np.uint8)

        # 设置形态操作类型，表示操作类型为礼帽运算
        operation = cv2.MORPH_TOPHAT

        # 形态操作，参数1：cv读取后的二值化图像，参数2：形态操作类型，参数3：内核大小，参数4：迭代次数
        self.cv_dealtImage = cv2.morphologyEx(self.cv_srcImage, operation, kernel, iterations=5)

        # 显示处理后图像
        self.show_in_dealt_label()

