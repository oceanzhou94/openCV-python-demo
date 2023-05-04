"""
@Auth ： youngZ
@File ：geometricTransformation.py
图像几何变换逻辑处理
"""
import copy

from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
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

        # 缩放图片点击事件
        self.ui.pushButton_ok_1.clicked.connect(self.picture_scaling_ok)  # 点击确定
        self.ui.pushButton_recover.clicked.connect(self.picture_scaling_recover)  # 点击恢复

        # 保存图片事件
        self.ui.pushButton_save_img.clicked.connect(self.save_image)

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
        self.cv_srcImage = cv2.imread(img_name)

        # 调整图片大小--在label中显示正常大小
        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)

        # 将图片显示在label_source_img上面
        self.ui.label_source_img.setPixmap(QPixmap.fromImage(ui_image))

    # 图片缩放函数
    def picture_scaling_ok(self):
        # 从doubleSpinBox中获取缩放数值倍数
        value = self.ui.doubleSpinBox.value()
        print("缩放倍数：" + str(value))

        # 调整图片缩放大小
        self.cv_dealtImage = cv2.resize(self.cv_srcImage, dsize=None, fx=value, fy=value)

        # 缩放后的大小显示在label上面
        height, width = self.cv_dealtImage.shape[0], self.cv_dealtImage.shape[1]
        self.dst_img = QImage(cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)

        # 将图片显示在label_source_img上面
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # 取消缩放，图片恢复至默认大小
    def picture_scaling_recover(self):
        # 恢复doubleSpinBox中的数值为1
        self.ui.doubleSpinBox.setValue(1)

        # 调整图片缩放大小
        self.cv_dealtImage = cv2.resize(self.cv_srcImage, dsize=None, fx=1, fy=1)

        # 缩放后的图片显示在label上面
        height, width = self.cv_dealtImage.shape[0], self.cv_dealtImage.shape[1]
        self.dst_img = QImage(cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)

        # 将图片显示在label_source_img上面
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # 鼠标按压事件
    def mousePressEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.flag = True

    # 鼠标释放事件
    def mouseReleaseEvent(self, e):
        self.flag = False
        self.movex = ""
        self.movey = ""

    # 鼠标移动事件--实现鼠标拖拽显示图像
    def mouseMoveEvent(self, e):
        if self.flag:
            self.x1 = e.x()
            self.y1 = e.y()
        if self.movex != "" and self.movey != "":
            self.label_x = self.label_x + (self.x1 - self.movex)
            self.label_y = self.label_y + (self.y1 - self.movey)
        self.movex = self.x1
        self.movey = self.y1
        # 使得图片能够随着缩放而不影响大小，# 同时QtCore.QRect确定图形为矩形
        self.ui.label_dealt_img.setGeometry(QtCore.QRect(self.label_x, self.label_y, self.label_w, self.label_h))

    # 将处理后的图片保存到本地
    def save_image(self):
        # 前面是地址，后面是文件类型,得到输入地址的文件名和地址txt(*.txt*.xls);;image(*.png)不同类别
        filepath, filetype = QFileDialog.getSaveFileName(self, "文件保存", "/", 'image(*.png)')

        # save方法保存图片到本地，filepath：保存的名称  PNG：保存的格式，-1：质量因素，值越大质量越高，-1表示默认值
        self.dst_img.save(filepath, 'PNG', -1)

    # 图像旋转逻辑
    def rotation_image_ok(self):

        # 获取原图坐标
        rows, cols = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]

        # 从滑动组件获取旋转角度
        angle = self.ui.horizontalSlider.value()
        print(f"旋转角度：{angle}")

        # 按图像中心点旋转，
        M = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), angle, 1)
        self.cv_dealtImage = cv2.warpAffine(self.cv_srcImage, M, (cols, rows))

        # 缩放后的大小显示在label上面
        height, width = self.cv_dealtImage.shape[0], self.cv_dealtImage.shape[1]
        self.dst_img = QImage(cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)

        # 将图片显示在label_source_img上面
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # 图像旋转恢复
    def rotation_image_recover(self):
        # 直接显示原图
        # 调整图片大小--在label中显示正常大小
        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)

        # 将图片显示在label_dealt_img上面
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(ui_image))

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

        # 缩放后的大小显示在label上面
        height, width = self.cv_dealtImage.shape[0], self.cv_dealtImage.shape[1]
        self.dst_img = QImage(cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB), width, height,
                              QImage.Format_RGB888)

        # 将图片显示在label_dealt_img上面
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # 图片垂直镜像翻转
    def flip_vertical_image(self):
        # flip函数实现图片镜像翻转，参数1：cv读取后的图片，参数2：翻转设置，0表示水平翻转
        self.cv_dealtImage = cv2.flip(self.cv_srcImage, 0)  # 垂直翻转

        # 缩放后的大小显示在label上面
        height, width = self.cv_dealtImage.shape[0], self.cv_dealtImage.shape[1]
        self.dst_img = QImage(cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB), width, height,
                              QImage.Format_RGB888)

        # 将图片显示在label_dealt_img上面
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # 图片对角镜像翻转--同时实现水平和垂直镜像
    def flip_diagonal_image(self):
        # flip函数实现图片镜像翻转，参数1：cv读取后的图片，参数2：翻转设置，-1表示同时水平翻转和垂直翻转
        self.cv_dealtImage = cv2.flip(self.cv_srcImage, -1)  # 对角翻转

        # 缩放后的大小显示在label上面
        height, width = self.cv_dealtImage.shape[0], self.cv_dealtImage.shape[1]
        self.dst_img = QImage(cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB), width, height,
                              QImage.Format_RGB888)

        # 将图片显示在label_dealt_img上面
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))
