"""
@Auth ： youngZ
@File ：geometricTransformation.py
图像几何变换逻辑处理
"""
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from cv2 import cv2

# 子窗口布局
from userInterface import geometricTransformationUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = geometricTransformationUI.Ui_MainWindow()  # 获取子窗口对象

        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 事件初始化

        self.cv_srcImage = None  # cv读取图片
        self.cv_dealtImage = None  # 处理后的图片，类型为cv2
        self.dst_img = None  # 处理后的图片 类型为QImage

        self.label_w = self.ui.label_dealt_img.width()  # 获取显示处理后图片控件的宽度
        self.label_h = self.ui.label_dealt_img.height()  # 获取显示处理后图片控件的高度
        self.label_x = self.ui.label_dealt_img.x()  # 获取显示处理后图片控件的坐标
        self.label_y = self.ui.label_dealt_img.y()  # 获取显示处理后图片控件的y轴坐标

        self.movex = ""  # 鼠标移动后X轴的位置
        self.movey = ""  # 鼠标移动后Y轴的位置

    # 绑定事件
    def ui_init(self):
        # 打开图片并显示事件
        self.ui.pushButton_choose_img.clicked.connect(self.open_image)
        # 保存图片事件
        self.ui.pushButton_save_img.clicked.connect(self.save_image)

        # 缩放图片点击事件
        self.ui.pushButton_ok_1.clicked.connect(self.picture_scaling_ok)  # 点击确定
        self.ui.pushButton_recover.clicked.connect(self.picture_scaling_recover)  # 点击恢复

        # 旋转图片事件
        self.ui.pushButton_ok_2.clicked.connect(self.rotation_image_ok)  # 点击确定
        self.ui.pushButton_recover_2.clicked.connect(self.rotation_image_recover)  # 点击恢复

        # 滑动控件显示数值事件
        self.ui.horizontalSlider.valueChanged.connect(self.slider_value_show)

        # 图片镜像事件
        self.ui.pushButton_flip_horizontal.clicked.connect(self.flip_horizontal_image)  # 水平镜像
        self.ui.pushButton_flip_vertical.clicked.connect(self.flip_vertical_image)  # 水平镜像
        self.ui.pushButton_flip_diagonal.clicked.connect(self.flip_diagonal_image)  # 对角翻转

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

    # 保存图像
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

    # 图片缩放函数
    def picture_scaling_ok(self):
        # 从doubleSpinBox中获取缩放数值倍数
        value = self.ui.doubleSpinBox.value()
        print("缩放倍数：" + str(value))

        # 调整图片缩放大小
        self.cv_dealtImage = cv2.resize(self.cv_srcImage, dsize=None, fx=value, fy=value)

        # 显示图像
        self.show_in_dealt_label()

    # 取消缩放，图片恢复至默认大小
    def picture_scaling_recover(self):
        # 恢复doubleSpinBox中的数值为1
        self.ui.doubleSpinBox.setValue(1)

        # 调整图片缩放大小
        self.cv_dealtImage = cv2.resize(self.cv_srcImage, dsize=None, fx=1, fy=1)

        # 显示图像
        self.show_in_dealt_label()

    # 图像旋转逻辑
    def rotation_image_ok(self):

        # 获取原图坐标
        rows, cols = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]

        # 从滑动组件获取旋转角度
        angle = self.ui.horizontalSlider.value()
        print(f"旋转角度：{angle}")

        # 按图像中心点旋转，
        center = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), angle, 1)
        self.cv_dealtImage = cv2.warpAffine(self.cv_srcImage, center, (cols, rows))

        # 显示图像
        self.show_in_dealt_label()

    # 图像旋转恢复
    def rotation_image_recover(self):
        # 直接显示原图
        self.cv_dealtImage = self.cv_srcImage.copy()

        # 显示图像
        self.show_in_dealt_label()

    # 实时显示滑动控件的数值
    def slider_value_show(self):
        # 读取当前滑动条值
        value = self.ui.horizontalSlider.value()

        # 强制类型转换，label框需要str类型值
        show_str = "旋转角度：" + str(value) + "°"

        # 显示数值
        self.ui.label_value_show.setText(show_str)

    # 图片水平镜像翻转
    def flip_horizontal_image(self):
        # flip函数实现图片镜像翻转，参数1：cv读取后的图片，参数2：翻转设置，1表示水平翻转
        self.cv_dealtImage = cv2.flip(self.cv_srcImage, 1)  # 水平翻转

        # 显示图像
        self.show_in_dealt_label()

    # 图片垂直镜像翻转
    def flip_vertical_image(self):
        # flip函数实现图片镜像翻转，参数1：cv读取后的图片，参数2：翻转设置，0表示水平翻转
        self.cv_dealtImage = cv2.flip(self.cv_srcImage, 0)  # 垂直翻转

        # 显示图像
        self.show_in_dealt_label()

    # 图片对角镜像翻转--同时实现水平和垂直镜像
    def flip_diagonal_image(self):
        # flip函数实现图片镜像翻转，参数1：cv读取后的图片，参数2：翻转设置，-1表示同时水平翻转和垂直翻转
        self.cv_dealtImage = cv2.flip(self.cv_srcImage, -1)  # 对角翻转

        # 显示图像
        self.show_in_dealt_label()
