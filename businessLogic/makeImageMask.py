"""
@Auth ： youngZ
@File ：makeImageMask.py
图像掩膜处理逻辑
"""
import numpy as np
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from cv2 import cv2

# 子窗口布局
from userInterface import makeImageMaskUI


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = makeImageMaskUI.Ui_MainWindow()  # 子窗口实例化
        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 执行绑定事件

        self.cv_srcImage = None  # cv2读取原图
        self.cv_dealtImage = None  # cv2相关处理后的图像
        self.dst_img = None  # 将cv_dealtImage转换成QImage之后的图像

        # 图标
        self.setWindowIcon(QIcon('./dataAccess/icon/icon.ico'))

    # 绑定事件
    def ui_init(self):

        self.ui.pushButton_choose_img.clicked.connect(self.open_image)  # 打开图片并显示
        self.ui.pushButton_save_img.clicked.connect(self.save_image)  # 保存图片

        self.ui.pushButton_Normask.clicked.connect(self.make_default_mask)  # 创建默认掩膜
        self.ui.pushButton_mask.clicked.connect(self.make_user_mask)  # 创建用户自定义掩膜

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
            q_image = None
            # 多通道类型图片
            if len(self.cv_srcImage.shape) == 3:
                hight, width, channel = self.cv_srcImage.shape
                # 4通道类型的图
                if channel == 4:
                    q_image = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGBA)
                    q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
                # 3通道类型的图
                elif channel == 3:
                    q_image = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB)
                    q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)
            # 单通道类型图片
            elif len(self.cv_srcImage.shape) == 2:
                hight, width = self.cv_srcImage.shape
                # 单通道类型的图
                q_image = QImage(self.cv_srcImage.data, width, hight, QImage.Format_Grayscale8)

            # 将图片显示在label_source_img上面
            self.ui.label_source_img.setPixmap(QPixmap.fromImage(q_image))

            # 显示当前图像信息
            self.show_current_img_message()

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
        q_image = None
        # 多通道类型图片
        if len(self.cv_dealtImage.shape) == 3:
            hight, width, channel = self.cv_dealtImage.shape
            # 4通道类型的图
            if channel == 4:
                q_image = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGBA)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
            # 3通道类型的图
            elif channel == 3:
                q_image = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)
        # 单通道类型图片
        elif len(self.cv_dealtImage.shape) == 2:
            hight, width = self.cv_dealtImage.shape
            # 单通道类型的图
            q_image = QImage(self.cv_dealtImage.data, width, hight, QImage.Format_Grayscale8)

        # 将图片显示在label_dealt_img上面
        self.dst_img = q_image
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # 显示当前图像的信息
    def show_current_img_message(self):
        # 获取原图像的高度，宽度，通道数
        hight, width, channle = self.cv_srcImage.shape

        # 确定原图的中心点
        center_h = int(hight / 2)
        center_w = int(width / 2)

        # 中心坐标信息--字符串类型
        center_msg = "\n中心点：" + "(" + str(center_w) + "," + str(center_h) + ")"
        text = "宽度：" + str(width) + " px" + "\n高度：" + str(hight) + " px" + center_msg

        self.ui.label_message.setText(text)

    # 创建默认掩膜
    def make_default_mask(self):
        # 判断是否有图像
        if self.cv_srcImage is None:
            # 消息弹出无图像
            QMessageBox.information(self, "提示", "未选择图像，请先选择图像!", QMessageBox.Close)
        else:
            # 获取原图像的高度，宽度，通道数
            hight, width, channle = self.cv_srcImage.shape

            # 用numpy生成一个全为0的，跟原图一样大小的的二维数组
            mask = np.zeros((hight, width, channle), dtype=np.uint8)
            # 确定原图的中心点
            center_h = int(hight / 2)
            center_w = int(width / 2)
            # 确定移动距离，
            distance_h = int(hight / 4)
            distance_w = int(width / 4)
            # 确定掩膜的尺寸
            mask[center_h - distance_h:center_h + distance_h, center_w - distance_w:center_w + distance_w] = 255
            # 与原图像进行与运算
            self.cv_dealtImage = cv2.bitwise_and(self.cv_srcImage, mask)
            # 显示掩膜后的图像
            self.show_in_dealt_label()

    def make_user_mask(self):
        # 判断是否有图像
        if self.cv_srcImage is None:
            # 消息弹出无图像
            QMessageBox.information(self, "提示", "未选择图像，请先选择图像!", QMessageBox.Close)
        else:
            # 获取原图像的高度，宽度，通道数
            hight, width, channle = self.cv_srcImage.shape

            # 用numpy生成一个全为0的，跟原图一样大小的的二维数组
            mask = np.zeros((hight, width, channle), dtype=np.uint8)
            try:
                # 获取用户设定的相关数据
                user_width = int(int(self.ui.lineEdit_width.text()) / 2)  # 宽度
                user_hight = int(int(self.ui.lineEdit_hight.text()) / 2)  # 高度
                user_x = int(self.ui.lineEdit_X.text())  # X轴坐标
                user_y = int(self.ui.lineEdit_Y.text())  # Y轴坐标

            except Exception as error:
                # 消息弹出错误
                QMessageBox.critical(self, '错误！', "创建掩膜失败，请检查数据！", QMessageBox.Close)
                print("保存失败，错误：", error)

            else:
                # 确定掩膜的尺寸
                mask[user_y - user_hight:user_y + user_hight, user_x - user_width:user_x + user_width] = 255

            # 与原图像进行与运算
            self.cv_dealtImage = cv2.bitwise_and(self.cv_srcImage, mask)

            # 显示掩膜后的图像
            self.show_in_dealt_label()
