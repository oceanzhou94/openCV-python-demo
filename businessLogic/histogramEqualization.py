"""
@Auth ： youngZ
@File ：histogramEqualization.py
直方图处理逻辑
"""
import os

import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from cv2 import cv2
import matplotlib.pyplot as plt

# 子窗口布局
from userInterface import histogramEqualizationUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = histogramEqualizationUI.Ui_MainWindow()  # 获取子窗口对象

        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 事件初始化

        self.cv_srcImage = None  # cv读取图片
        self.cv_dealtImage = None  # 处理后的图片，类型为cv2
        self.dst_img = None  # 处理后的图片 类型为QImage

        self.dst_img1 = None  # 对比直方图处理
        self.dst_img2 = None

    # 绑定事件
    def ui_init(self):

        self.ui.pushButton_choose_img.clicked.connect(self.open_image)  # 选择图片
        self.ui.pushButton_save_img.clicked.connect(self.save_image)  # 保存图片
        self.ui.pushButton_hist.clicked.connect(self.draw_histogram)  # 点击绘制直方图
        self.ui.pushButton_calcHist.clicked.connect(self.find_histogram)  # 点击查找直方图
        self.ui.pushButton_calcHist_mask.clicked.connect(self.mask_histogram)  # 点击掩膜直方图
        self.ui.pushButton_NumPy.clicked.connect(self.histogram_numpy)  # 点击NumPy直方图

        self.ui.pushButton_equalizeHist.clicked.connect(self.equalize_hist)  # 点击普通直方图均衡化
        self.ui.pushButton_createCLAHE.clicked.connect(self.create_clahe)  # 点击限制对比度自适应直方图均衡化
        self.ui.pushButton_OpenCV_double.clicked.connect(self.calc_hist_opencv)  # 点击OpenCV二维直方图
        self.ui.pushButton_NumPy_double.clicked.connect(self.calc_hist_numpy)  # 点击numpy二维直方图

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

    # 绘制直方图
    def draw_histogram(self):
        # 复制原图像
        img = self.cv_srcImage.copy()

        # 每次绘制之前清空画布
        plt.clf()

        # 绘制直方图
        plt.hist(img.ravel(), 256)

        # 保存直方图
        plt.savefig("./dataAccess/histogram/histogram_draw.png")

        # 直方图类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/histogram_draw.png")

        # 显示直方图
        self.ui.label_dealt_img.setPixmap(self.dst_img)

        # 删除图片
        os.remove("./dataAccess/histogram/histogram_draw.png")

    # 查找直方图
    def find_histogram(self):
        # 复制原图像
        img = self.cv_srcImage.copy()

        # 每次绘制之前清空画布
        plt.clf()

        histb = cv2.calcHist([img], [0], None, [256], [0, 255])  # 计算B通道直方图
        histg = cv2.calcHist([img], [1], None, [256], [0, 255])  # 计算G通道直方图
        histr = cv2.calcHist([img], [2], None, [256], [0, 255])  # 计算R通道直方图
        plt.plot(histb, color='b')  # 绘制B通道直方图，蓝色
        plt.plot(histg, color='g')  # 绘制G通道直方图，绿色
        plt.plot(histr, color='r')  # 绘制R通道直方图，红色

        # 保存直方图
        plt.savefig("./dataAccess/histogram/histogram_find.png")

        # 直方图类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/histogram_find.png")

        # 显示直方图
        self.ui.label_dealt_img.setPixmap(self.dst_img)

        # 删除图片
        os.remove("./dataAccess/histogram/histogram_find.png")

    # 掩膜直方图
    def mask_histogram(self):
        # 复制原图像
        img = self.cv_srcImage.copy()

        # 按原图大小创建一幅黑色图像
        w, h, d = img.shape
        mask = np.zeros((w, h), np.uint8)

        w1 = np.int0(w / 4)
        w2 = np.int0(w * 0.75)
        h1 = np.int0(h / 4)
        h2 = np.int0(h * 0.75)

        # 每次绘制之前清空画布
        plt.clf()

        mask[w1:w2, h1:h2] = 255  # 设置掩模白色区域
        histb = cv2.calcHist([img], [0], None, [256], [0, 255])  # 计算B通道直方图
        histg = cv2.calcHist([img], [1], None, [256], [0, 255])  # 计算G通道直方图
        histr = cv2.calcHist([img], [2], None, [256], [0, 255])  # 计算R通道直方图
        plt.plot(histb, color='b')  # 绘制B通道直方图，蓝色
        plt.plot(histg, color='g')  # 绘制G通道直方图，绿色
        plt.plot(histr, color='r')  # 绘制R通道直方图，红色

        # 保存直方图
        plt.savefig("./dataAccess/histogram/histogram_mask.png")

        # 直方图类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/histogram_mask.png")

        # 显示直方图
        self.ui.label_dealt_img.setPixmap(self.dst_img)

        # 删除图片
        os.remove("./dataAccess/histogram/histogram_mask.png")

    # NumPy中的直方图
    def histogram_numpy(self):
        # 复制原图像
        img = self.cv_srcImage.copy()

        # 每次绘制之前清空画布
        plt.clf()

        histb, e1 = np.histogram(img.ravel(), 256, [0, 256])  # 计算B通道直方图
        histg, e2 = np.histogram(img[1].ravel(), 256, [0, 256])  # 计算G通道直方图
        histr, e3 = np.histogram(img[2].ravel(), 256, [0, 256])  # 计算R通道直方图
        plt.plot(histb, color='b')  # 绘制B通道直方图，蓝色
        plt.plot(histg, color='g')  # 绘制G通道直方图，绿色
        plt.plot(histr, color='r')  # 绘制R通道直方图，红色

        # 保存直方图
        plt.savefig("./dataAccess/histogram/histogram_numpy.png")

        # 直方图类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/histogram_numpy.png")

        # 显示直方图
        self.ui.label_dealt_img.setPixmap(self.dst_img)

        # 删除图片
        os.remove("./dataAccess/histogram/histogram_numpy.png")

    # 普通直方图均衡化
    def equalize_hist(self):
        # 复制原图像
        img = self.cv_srcImage.copy().ravel()

        # 均衡化
        img2 = cv2.equalizeHist(img)
        # 每次绘制之前清空画布
        plt.clf()
        # 绘制均衡化后图像的直方图
        plt.figure('均衡化后的直方图')
        plt.hist(img2, 256)
        # 保存直方图
        plt.savefig("./dataAccess/histogram/histogram_equal.png")

        # 直方图类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/histogram_equal.png")

        # 显示直方图
        self.ui.label_dealt_img.setPixmap(self.dst_img)

        # 删除图片
        os.remove("./dataAccess/histogram/histogram_equal.png")

    # 限制对比度自适应直方图均衡化
    def create_clahe(self):
        # 复制原图像
        img = self.cv_srcImage.copy().ravel()
        # 均衡化
        img2 = cv2.equalizeHist(img)
        # 创建CLAHE
        clahe = cv2.createCLAHE(clipLimit=5)
        # 应用CLAHE
        img3 = clahe.apply(img2)

        # 每次绘制之前清空画布
        plt.clf()
        # 绘制均衡化后图像的直方图
        plt.figure('均衡化后的直方图')
        plt.hist(img3, 256)

        # 保存直方图
        plt.savefig("./dataAccess/histogram/histogram_clahe.png")

        # 直方图类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/histogram_clahe.png")

        # 显示直方图
        self.ui.label_dealt_img.setPixmap(self.dst_img)

        # 删除图片
        os.remove("./dataAccess/histogram/histogram_clahe.png")

    # OpenCV中的二维直方图
    def calc_hist_opencv(self):
        # 复制原图像
        img = self.cv_srcImage.copy()
        # 转换色彩空间为HSV
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # 计算颜色直方图
        hist = cv2.calcHist([img2], [0, 1], None, [180, 256], [0, 180, 0, 256])

        # 每次绘制之前清空画布
        plt.clf()
        # 绘制颜色直方图
        plt.imshow(hist, interpolation='nearest')
        # 保存直方图
        plt.savefig("./dataAccess/histogram/histogram_opencv.png")

        # 直方图类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/histogram_opencv.png")

        # 显示直方图
        self.ui.label_dealt_img.setPixmap(self.dst_img)

        # 删除图片
        os.remove("./dataAccess/histogram/histogram_opencv.png")

    # NumPy中的二维直方图
    def calc_hist_numpy(self):
        # 复制原图像
        img = self.cv_srcImage.copy()
        # 转换色彩空间为HSV
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        h, s, v = cv2.split(img2)
        # 计算颜色直方图
        hist, x, y = np.histogram2d(h.ravel(), s.ravel(),[180, 256], [[0, 180], [0, 256]])

        # 每次绘制之前清空画布
        plt.clf()
        # 绘制颜色直方图
        plt.imshow(hist, interpolation='nearest')
        # 保存直方图
        plt.savefig("./dataAccess/histogram/histogram_numpy.png")

        # 直方图类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/histogram_numpy.png")

        # 显示直方图
        self.ui.label_dealt_img.setPixmap(self.dst_img)

        # 删除图片
        os.remove("./dataAccess/histogram/histogram_numpy.png")
