"""
@Auth ： youngZ
@File ：featureDetection.py
图像角检测和特征检测逻辑处理
"""
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QMessageBox
from cv2 import cv2

from userInterface import featureDetectionUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = featureDetectionUI.Ui_MainWindow()  # 获取子窗口对象
        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 事件初始化

        self.cv_srcImage = None  # cv读取的原图片
        self.cv_dealtImage = None  # 处理后的图片，类型为cv2
        self.cv_selectImage = None  # 查询图片
        self.dst_img = None  # 处理后的图片 类型为QImage，保存图片时使用

    # 绑定事件
    def ui_init(self):
        self.ui.pushButton_choose_img.clicked.connect(self.open_image)  # 点击打开图片
        self.ui.pushButton_save_img.clicked.connect(self.save_image)  # 点击保存图片

        self.ui.pushButton_Harris.clicked.connect(self.corner_harris)  # 点击哈里斯角检测
        self.ui.pushButton_SubPix.clicked.connect(self.corner_subpix)  # 点击优化哈里斯角检测
        self.ui.pushButton_ShiTomasi.clicked.connect(self.good_features_to_track)  # 点击Shi-Tomasi角检测
        self.ui.pushButton_fast.clicked.connect(self.fast_detection)  # 点击FAST关键点检测
        self.ui.pushButton_sift.clicked.connect(self.sift_detection)  # 点击SIFT关键点检测
        self.ui.pushButton_orb.clicked.connect(self.orb_detection)  # 点击ORB关键点检测

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

    # 哈里斯角检测器
    def corner_harris(self):
        # 复制图像
        img = self.cv_srcImage.copy()
        # 转换为灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 转换为浮点类型
        gray = np.float32(gray)
        # 执行角检测
        dst = cv2.cornerHarris(gray, 10, 5, 0.001)
        # 将角设置为红色
        img[dst > 0.02 * dst.max()] = [0, 0, 255]
        # 显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()

    # 优化哈里斯角检测
    def corner_subpix(self):
        # 复制图像
        img = self.cv_srcImage.copy()
        # 转换为灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 转换为浮点类型
        gray = np.float32(gray)
        # 查找哈里斯角
        dst = cv2.cornerHarris(gray, 8, 7, 0.04)
        # 二值化阈值处理
        r, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
        # 转换为整型
        dst = np.uint8(dst)
        # 查找质点坐标
        r, l, s, cxys = cv2.connectedComponentsWithStats(dst)
        # 定义优化查找条件
        cif = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
        # 执行优化查找
        corners = cv2.cornerSubPix(gray, np.float32(cxys), (5, 5), (-1, -1), cif)
        # 堆叠构造新数组，便于标注角
        res = np.hstack((cxys, corners))
        # 转换为整型
        res = np.int0(res)
        # 将哈里斯角对应像素设置为红色
        img[res[:, 1], res[:, 0]] = [0, 0, 255]
        # 将优化结果像素设置为绿色
        img[res[:, 3], res[:, 2]] = [0, 255, 0]
        # 转换为RGB格式
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()

    # Shi-Tomasi角检测
    def good_features_to_track(self):
        # 复制图像
        img = self.cv_srcImage.copy()
        # 转换为灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 转换为浮点类型
        gray = np.float32(gray)
        # 检测角，最多6个
        corners = cv2.goodFeaturesToTrack(gray, 6, 0.1, 100)
        # 转换为整型
        corners = np.int0(corners)
        for i in corners:
            x, y = i.ravel()
            cv2.circle(img, (x, y), 4, (0, 255, 0), -1)  # 用圆点标注找到的角，红色
        # 转换为RGB格式
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()

    # FAST关键点检测
    def fast_detection(self):
        # 复制图像
        img = self.cv_srcImage.copy()
        # 创建FAST检测器
        fast = cv2.FastFeatureDetector_create()
        # 设置阈值，默认阈值为10
        fast.setThreshold(20)
        # 检测关键点，不使用掩模
        kp = fast.detect(img, None)
        # 绘制关键点
        img = cv2.drawKeypoints(img, kp, None, color=(0, 0, 255))
        # 文字结果
        n = 0
        text = ""
        for p in kp:
            text += f"第{n + 1}个关键点，坐标：{p.pt}， 响应强度：{p.response}，邻域大小：{p.size}，角度： {p.angle}\n"
            n += 1

        # 显示结果
        self.ui.label_result.setText(text)
        self.cv_dealtImage = img
        self.show_in_dealt_label()

    # SIFT关键点检测
    def sift_detection(self):
        # 复制图像
        img = self.cv_srcImage.copy()
        # 转换为灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 创建SIFT对象
        sift = cv2.SIFT_create()
        # 检测关键点
        kp = sift.detect(gray, None)
        # 绘制关键点
        img = cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # 转换为RGB图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 文字结果
        n = 0
        text = ""
        for p in kp:
            text += f"第{n + 1}个关键点，坐标：{p.pt}， 响应强度：{p.response}，邻域大小：{p.size}，角度： {p.angle}\n"
            n += 1
        # 显示图像
        self.ui.label_result.setText(text)
        self.cv_dealtImage = img
        self.show_in_dealt_label()

    # ORB关键点检测
    def orb_detection(self):
        # 复制图像
        img = self.cv_srcImage.copy()
        # 创建ORB检测器对象
        orb = cv2.ORB_create()
        # 检测关键点
        kp = orb.detect(img, None)
        # 绘制关键点
        img = cv2.drawKeypoints(img, kp, None, color=(0, 0, 2550))
        # 文字结果
        n = 0
        text = ""
        for p in kp:
            text += f"第{n + 1}个关键点，坐标：{p.pt}， 响应强度：{p.response}，邻域大小：{p.size}，角度： {p.angle}\n"
            n += 1
        # 显示绘制了特征点的图像
        self.ui.label_result.setText(text)
        self.cv_dealtImage = img
        self.show_in_dealt_label()


