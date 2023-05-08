"""
@Auth ： youngZ
@File ：featureMatching.py
图像特征匹配逻辑处理
"""

import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from cv2 import cv2

from userInterface import featureMatchingUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = featureMatchingUI.Ui_MainWindow()  # 获取子窗口对象
        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 事件初始化

        self.cv_srcImage = None  # cv读取的原图片
        self.cv_dealtImage = None  # 处理后的图片，类型为cv2
        self.cv_selectImage = None  # 查询图片
        self.dst_img = None  # 处理后的图片 类型为QImage，保存图片时使用

    # 绑定事件
    def ui_init(self):
        self.ui.pushButton_choose_p.clicked.connect(self.open_image)  # 点击选择训练图片
        self.ui.pushButton_choose_s.clicked.connect(self.choose_select_image)  # 点击选择查询图片
        self.ui.pushButton_violate_m.clicked.connect(self.violent_match)  # 点击暴力匹配match
        self.ui.pushButton_violate_k.clicked.connect(self.violent_knn_match)  # 点击暴力匹配knnMacth
        self.ui.pushButton_flann.clicked.connect(self.flann_match)  # 点击FLANN匹配
        self.ui.pushButton_clear.clicked.connect(self.clear)  # 点击清空所有图像

        self.ui.pushButton_save_img.clicked.connect(self.save_image)  # 点击保存图片

    # 选择训练图片
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

    # 选择查询图片
    def choose_select_image(self):
        # 获取图片和图片类型
        img_name, img_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '',
                                                         '图像文件(*.jpg *.bmp *.png *.jpeg)')
        # cv读取图片
        if img_name == "":
            # 未选择图片，弹出消息对话框
            QMessageBox.critical(self, '错误！', '请选择处理图像', QMessageBox.Close)
        else:
            self.cv_selectImage = cv2.imread(img_name)
            # 转换cv_srcImage类型为QImage
            hight, width, channel = self.cv_selectImage.shape
            q_image = None
            # 4通道类型的图
            if channel == 4:
                q_image = cv2.cvtColor(self.cv_selectImage, cv2.COLOR_BGR2RGBA)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
            # 3通道类型的图
            elif channel == 3:
                q_image = cv2.cvtColor(self.cv_selectImage, cv2.COLOR_BGR2RGB)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)
            # 单通道类型的图
            elif channel == 1:
                q_image = QImage(self.cv_selectImage.data, width, hight, QImage.Format_Grayscale8)

            # 将图片显示在label_source_img上面
            self.ui.label_select_img.setPixmap(QPixmap.fromImage(q_image))

    # 点击清空所有图像
    def clear(self):
        self.ui.label_source_img.setText("训练图像")
        self.ui.label_select_img.setText("查询图像")
        self.ui.label_dealt_img.setText("结果图像")

    # match暴力匹配
    def violent_match(self):
        # 复制原图像
        img1 = self.cv_selectImage.copy()  # 查询图像
        img2 = self.cv_srcImage.copy()  # 训练图像
        # 转换为灰度图像
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # 创建ORB检测器
        orb = cv2.ORB_create()
        # 检测关键点和计算描述符
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        # 创建匹配器
        bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=False)
        # 执行特征匹配
        ms = bf.match(des1, des2)
        # 按距离排序
        ms = sorted(ms, key=lambda x: x.distance)
        # 绘制前20个匹配结果
        img = cv2.drawMatches(img1, kp1, img2, kp2, ms[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        # 显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()

    # knn暴力匹配
    def violent_knn_match(self):
        # 复制原图像
        img1 = self.cv_selectImage.copy()  # 查询图像
        img2 = self.cv_srcImage.copy()  # 训练图像
        # 转换为灰度图像
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # 创建ORB检测器
        orb = cv2.ORB_create()
        # 检测关键点和计算描述符
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        # 创建匹配器
        bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=False)
        # 执行特征匹配
        ms = bf.knnMatch(des1, des2, k=2)
        # 应用比例测试选择要使用的匹配结果
        good = []
        for m, n in ms:
            if m.distance < 0.75 * n.distance:  # 因为k=2，所以这里比较两个匹配结果的距离
                good.append(m)
        # 绘制前20个匹配结果
        img = cv2.drawMatches(img1, kp1, img2, kp2, good[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        # 显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()

    # FLANN匹配
    def flann_match(self):
        # 复制原图像
        img1 = self.cv_selectImage.copy()  # 查询图像
        img2 = self.cv_srcImage.copy()  # 训练图像
        # 转换为灰度图像
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # 创建ORB检测器
        orb = cv2.ORB_create()
        # 检测关键点和计算描述符
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        # 定义FLANN参数
        flann_index_lsh = 6
        index_params = dict(algorithm=flann_index_lsh,
                            table_number=6,
                            key_size=12,
                            multi_probe_level=1)
        search_params = dict(checks=50)
        # 创建FLANN匹配器
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        # 执行匹配操作
        matches = flann.match(des1, des2)
        # 关键点和连接线为绿色，单个点为红色
        draw_params = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), matchesMask=None,
                           flags=cv2.DrawMatchesFlags_DEFAULT)
        # 绘制匹配结果
        img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None, **draw_params)
        # 显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()
