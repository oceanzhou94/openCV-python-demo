"""
@Auth ： youngZ
@File ：faceDetection.py
人脸识别逻辑处理
"""

import qimage2ndarray
from PyQt5 import QtCore
from cv2 import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

# 子窗口布局
from userInterface import faceDetectionUI


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = faceDetectionUI.Ui_MainWindow()  # 子窗口实例化对象
        self.ui.setup_ui(self)  # 子窗口对象初始化
        self.ui_init()  # 信号事件初始化

        self.cap = None  # 摄像头数据
        self.image = None  # 捕获的图像
        self.timer_camera = QtCore.QTimer()  # 定时器

    # 使用信号槽触发事件
    def ui_init(self):
        self.ui.pushButton_open.clicked.connect(self.open_capture)  # 打开摄像头
        self.ui.pushButton_close.clicked.connect(self.close_capture)  # 关闭摄像头
        self.ui.pushButton_face_open.clicked.connect(self.open_face)  # 开启识别
        self.ui.pushButton_face_close.clicked.connect(self.close_face)  # 关闭识别
        self.ui.pushButton_get_image.clicked.connect(self.get_image)  # 截取图片
        self.ui.pushButton_save_image.clicked.connect(self.save_image)  # 保存图像
        self.ui.pushButton_clear_image.clicked.connect(self.clear_image)  # 清除图像

    # 打开摄像头
    def open_capture(self):
        self.cap = cv2.VideoCapture(0)
        # 设置格式解决延迟问题
        self.cap.set(cv2.cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        # 定时器每50ms刷新一次图像
        self.timer_camera.start(20)
        # 设置超时的操作
        self.timer_camera.timeout.connect(self.show_camera)
        # 设置状态为开启
        self.ui.label_cap.setText("摄像头状态：开启")

    # 关闭摄像头
    def close_capture(self):
        # 计时器停止
        self.timer_camera.stop()
        # 释放摄像头
        self.cap.release()
        # label不显示图像
        self.ui.label.setText("摄像头已关闭")
        # 设置状态为关闭
        self.ui.label_cap.setText("摄像头状态：关闭")

    # 截取图片
    def get_image(self):
        # 计时器停止，但是显示关闭前的图片
        self.timer_camera.stop()

    # 显示摄像头捕获到的图像
    def show_camera(self):
        # 从视频流中读取
        ret, img = self.cap.read()
        # 水平翻转
        img = cv2.flip(img, 1)
        # 转换成RGB格式
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.image = qimage2ndarray.array2qimage(img)
        # label中显示
        self.ui.label.setPixmap(QPixmap(self.image))

    # 清除图像
    def clear_image(self):
        # 消息弹窗
        QMessageBox.critical(self, "操作提醒", "图像已清除！", QMessageBox.Close)
        self.open_capture()

    # 保存图片到本地
    def save_image(self):
        # 前面是地址，后面是文件类型,得到输入地址的文件名和地址txt(*.txt*.xls);;image(*.png)不同类别
        filepath, filetype = QFileDialog.getSaveFileName(self, "文件保存", "/", 'image(*.png)')
        try:
            # save方法保存图片到本地，filepath：保存的名称  PNG：保存的格式，-1：质量因素，值越大质量越高，-1表示默认值
            self.image.save(filepath, 'PNG', -1)
        except Exception as error:
            # 消息弹出保存失败
            QMessageBox.critical(self, '错误！', "图像保存失败", QMessageBox.Close)
            print("保存失败，错误：", error)
        else:
            # 消息弹出保存成功
            QMessageBox.information(self, "通知", "图像保存成功", QMessageBox.Close)

    # 人脸检测
    def face_detection(self):
        # opencv的人脸识别库
        face_cascade = cv2.CascadeClassifier("./dataAccess/static/haarcascade_frontalface_alt.xml")
        # 从视频流中读取
        ret, img = self.cap.read()
        # 水平翻转
        img = cv2.flip(img, 1)
        # 灰度化处理
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 执行人脸识别模型
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))
        # 画矩形框
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 人脸部分画蓝色框
        # 显示
        # 视频色彩转换回RGB，这样才是现实的颜色
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 把读取到的视频数据变成QImage形式
        q_img = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
        self.image = q_img
        # 往显示视频的Label里显示QImage
        self.ui.label.setPixmap(QPixmap.fromImage(q_img))

    # 开启人脸检测
    def open_face(self):
        try:
            self.cap.isOpened()
        except Exception as error:
            # 弹窗提醒
            QMessageBox.critical(self, "开启失败", "请先开启摄像头", QMessageBox.Close)
            print(error)
        else:
            # 设置定时器操作为人脸识别
            self.timer_camera.timeout.connect(self.face_detection)
            # 弹窗提醒
            QMessageBox.information(self, "操作提醒", "人脸检测功能已打开", QMessageBox.Close)
            # 设置状态为开启
            self.ui.label_face.setText("人脸识别状态：开启")

    # 关闭人脸检测
    def close_face(self):
        # 设置定时器操作为摄像头
        self.timer_camera.timeout.connect(self.show_camera)
        # 弹窗提醒
        QMessageBox.information(self, "操作提醒", "人脸检测功能关闭", QMessageBox.Close)
        # 设置状态为开启
        self.ui.label_face.setText("人脸识别状态：关闭")
