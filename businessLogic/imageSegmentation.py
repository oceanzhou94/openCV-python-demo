"""
@Auth ： youngZ
@File ：imageSegmentation.py
图像分割和融合处理逻辑
"""
import os

import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QMessageBox
from cv2 import cv2
from matplotlib import pyplot as plt

from userInterface import imageSegmentationUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = imageSegmentationUI.Ui_MainWindow()  # 获取子窗口对象
        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 事件初始化

        self.cv_srcImage = None  # cv读取的原图片
        self.cv_dealtImage = None  # 处理后的图片，类型为cv2
        self.cv_midImage = None  # 图像2
        self.dst_img = None  # 处理后的图片 类型为QImage，保存图片时使用

        self.normal_fusion = None  # 普通融合的结果
        self.pyramid_fusion = None  # 金字塔融合的结果

    # 绑定事件
    def ui_init(self):
        self.ui.pushButton_choose_img.clicked.connect(self.open_image)  # 点击打开图片
        self.ui.pushButton_save_img.clicked.connect(self.save_image)  # 点击保存图片

        self.ui.pushButton_distance.clicked.connect(self.distance_convert)  # 点击距离转换
        self.ui.pushButton_watershed.clicked.connect(self.watershed)  # 点击分水岭分割
        self.ui.pushButton_grabCut.clicked.connect(self.grab_cut)  # 点击前景提取
        self.ui.pushButton_clear.clicked.connect(self.label_clear)  # 点击画布清空
        self.ui.pushButton_choose1.clicked.connect(self.open_image)  # 点击图片选择1
        self.ui.pushButton_choose2.clicked.connect(self.choose_image)  # 点击图片选择2
        self.ui.pushButton_fusion_n.clicked.connect(self.image_fusion_normal)  # 点击普通融合
        self.ui.pushButton_fusion_g.clicked.connect(self.image_fusion_pyramid)  # 点击金字塔融合

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
        q_image = None
        if len(self.cv_dealtImage.shape) == 3:
            # 多通道类型图片
            hight, width, channel = self.cv_dealtImage.shape
            # 4通道类型的图
            if channel == 4:
                q_image = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGBA)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
            # 3通道类型的图
            elif channel == 3:
                q_image = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)

        elif len(self.cv_dealtImage.shape) == 2:
            # 单通道类型图片
            hight, width = self.cv_dealtImage.shape
            # 单通道类型的图
            q_image = QImage(self.cv_dealtImage.data, width, hight, QImage.Format_Grayscale8)

        # 将图片显示在label_dealt_img上面
        self.dst_img = q_image
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # 距离转换
    def distance_convert(self):
        # 复制原图像
        img = self.cv_srcImage.copy()
        # 转换为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Otsu阈值处理
        ret, img_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # 定义形态变换卷积核
        kernel = np.ones((3, 3), np.uint8)
        # 形态变换：开运算
        img_open = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        # 距离转换
        img_dist = cv2.distanceTransform(img_open, cv2.DIST_L2, 5)
        # 图像类型转换成uint8
        img_dist = cv2.convertScaleAbs(img_dist)
        # 归一化处理
        img_dist = cv2.normalize(img_dist, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8UC1)

        # 显示图像
        self.cv_dealtImage = img_dist
        self.show_in_dealt_label()

    # 分水岭算法分割图像
    def watershed(self):
        # 复制原图像
        img = self.cv_srcImage.copy()
        # 转换为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Otsu阈值处理
        ret, img_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # 定义形态变换卷积核
        kernel = np.ones((3, 3), np.uint8)
        # 形态变换：开运算
        img_open = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        # 膨胀操作，确定背景
        img_background = cv2.dilate(img_open, kernel, iterations=3)
        # 距离转换
        img_dist = cv2.distanceTransform(img_open, cv2.DIST_L2, 0)
        # 对距离转换结果进行阈值处理
        ret, img_fg = cv2.threshold(img_dist, 0.7 * img_dist.max(), 255, 2)
        # 转换为整数，获得前景
        img_fg = np.uint8(img_fg)
        # 标记阈值处理结果
        ret, markers = cv2.connectedComponents(img_fg)
        # 确定位置未知区域
        unknown = cv2.subtract(img_background, img_fg)
        # 加1使背景不为0
        markers = markers + 1
        # 将未知区域设置为0
        markers[unknown == 255] = 0
        # 执行分水岭算法分割图像
        imgwater = cv2.watershed(img, markers)
        plt.imshow(imgwater)  # 以灰度图像格式显示匹配结果
        plt.title('watershed')
        plt.axis('off')
        # 将原图中被标记点设置为绿色
        img[imgwater == -1] = [0, 255, 0]
        # 保存直方图
        plt.savefig("./dataAccess/histogram/watershed.png")
        # 类型转换成QPixmap
        self.dst_img = QPixmap("./dataAccess/histogram/watershed.png")
        # 显示
        self.ui.label_dealt_img.setPixmap(self.dst_img)
        # 删除图片
        os.remove("./dataAccess/histogram/watershed.png")

    # 前景提取功能
    def grab_cut(self):
        # 复制原图像
        img = self.cv_srcImage.copy()
        # 定义原始掩模
        mask = np.zeros(img.shape[:2], np.uint8)
        bg = np.zeros((1, 65), np.float64)
        fg = np.zeros((1, 65), np.float64)
        # 根据原图设置包含前景的矩形大小
        rect = (50, 50, 400, 300)
        # 第1次提取前景,矩形模式
        cv2.grabCut(img, mask, rect, bg, fg, 5, cv2.GC_INIT_WITH_RECT)
        # 读取已标注的掩模图像
        imgmask = cv2.imread('./dataAccess/testImage/test_hehua2.jpg')
        # cv2.imshow('mask image', imgmask)
        # 转换为单通道灰度图像
        mask2 = cv2.cvtColor(imgmask, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 根据掩模图像，将掩模图像中白黑色像素对应的原始掩模像素设置为0
        mask[mask2 == 0] = 0
        # 根据掩模图像，将掩模图像中白色像素对应的原始掩模像素设置为1
        mask[mask2 == 255] = 1
        # 第2次提取前景，掩模模式
        cv2.grabCut(img, mask, None, bg, fg, 5, cv2.GC_INIT_WITH_MASK)
        # 将返回的掩模中像数值为0或2像素设置为0（确认为背景），
        # 所有1或3的像素设置为1（确认为前景）
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        # 将掩模与原图像相乘获得分割出来的前景图像
        img = img * mask2[:, :, np.newaxis]
        # 显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()

    # 画布清空
    def label_clear(self):
        self.ui.label_source_img.setText("清空图像")
        self.ui.label_mid_img.setText("清空图像")
        self.ui.label_dealt_img.setText("清空图像")

    # 图片选择2
    def choose_image(self):
        # 获取图片和图片类型
        img_name, img_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '',
                                                         '图像文件(*.jpg *.bmp *.png *.jpeg)')
        # cv读取图片
        if img_name == "":
            # 未选择图片，弹出消息对话框
            QMessageBox.critical(self, '错误！', '请选择处理图像', QMessageBox.Close)
        else:
            self.cv_midImage = cv2.imread(img_name)
            # 转换cv_srcImage类型为QImage
            hight, width, channel = self.cv_midImage.shape
            q_image = None
            # 4通道类型的图
            if channel == 4:
                q_image = cv2.cvtColor(self.cv_midImage, cv2.COLOR_BGR2RGBA)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
            # 3通道类型的图
            elif channel == 3:
                q_image = cv2.cvtColor(self.cv_midImage, cv2.COLOR_BGR2RGB)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)
            # 单通道类型的图
            elif channel == 1:
                q_image = QImage(self.cv_midImage.data, width, hight, QImage.Format_Grayscale8)

            # 将图片显示在label_source_img上面
            self.ui.label_mid_img.setPixmap(QPixmap.fromImage(q_image))

    # 图像融合
    def image_fusion(self):
        # 复制两张图像
        img_left = self.cv_srcImage.copy()
        img_right = self.cv_midImage.copy()

        # 生成图像1的高斯金字塔，向下采样6次
        img = img_left.copy()
        img_left_gaus = [img]
        for i in range(6):
            img = cv2.pyrDown(img)
            img_left_gaus.append(img)
        # 生成图像2的高斯金字塔，向下采样6次
        img = img_right.copy()
        img_right_gaus = [img]
        for i in range(6):
            img = cv2.pyrDown(img)
            img_right_gaus.append(img)
        # 生成图像1的拉普拉斯金字塔，6层
        img_left_laps = [img_left_gaus[5]]
        for i in range(5, 0, -1):
            img = cv2.pyrUp(img_left_gaus[i])
            lap = cv2.subtract(img_left_gaus[i - 1], img)  # 两个图像大小不同时，做减法会出错
            img_left_laps.append(lap)
        # 生成图像2的拉普拉斯金字塔，6层
        img_right_laps = [img_right_gaus[5]]
        for i in range(5, 0, -1):
            img = cv2.pyrUp(img_right_gaus[i])
            lap = cv2.subtract(img_right_gaus[i - 1], img)
            img_right_laps.append(lap)
        # 拉普拉斯金字塔拼接：图像1每层左半部分与和图像2每层右半部分拼接
        cols = None
        img_laps = []
        for la, lb in zip(img_left_laps, img_right_laps):
            rows, cols, dpt = la.shape
            ls = la.copy()
            ls[:, int(cols / 2):] = lb[:, int(cols / 2):]
            img_laps.append(ls)
        # 从拉普拉斯金字塔恢复图像
        img = img_laps[0]
        for i in range(1, 6):
            img = cv2.pyrUp(img)
            img = cv2.add(img, img_laps[i])

        # 图像1原图像的半部分与和图像2原图像的右左半部分直接拼接
        direct = img_left.copy()
        direct[:, int(cols / 2):] = img_right[:, int(cols / 2):]

        self.normal_fusion = direct
        self.pyramid_fusion = img

    # 普通融合
    def image_fusion_normal(self):
        # 执行融合
        self.image_fusion()
        # 赋值
        self.cv_dealtImage = self.normal_fusion
        # 显示图像
        self.show_in_dealt_label()

    # 金字塔融合
    def image_fusion_pyramid(self):
        # 执行融合
        self.image_fusion()
        # 赋值
        self.cv_dealtImage = self.pyramid_fusion
        # 显示图像
        self.show_in_dealt_label()
