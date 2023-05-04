"""
@Auth ： youngZ
@File ：characterCoding.py
人物图像打码逻辑处理
"""
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from cv2 import cv2

# 子窗口布局
from userInterface import characterCodingUI


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self.ui = characterCodingUI.Ui_MainWindow()  # 获取子窗口对象
        self.ui.setup_ui(self)  # 子窗户初始化
        self.ui_init()  # 事件初始化
        self.cv_srcImage = None  # cv2读取原图
        self.dst_img = None  # cv2读取处理后图像

    # 绑定事件
    def ui_init(self):
        # 绑定打开图片并显示事件
        self.ui.pushButton_choose_img.clicked.connect(self.open_image)

        # 绑定人脸打码并显示打码后的图像事件
        self.ui.pushButton_character_coding.clicked.connect(self.face_coding)

        # 绑定保存处理后的图片事件
        self.ui.pushButton_save_img.clicked.connect(self.save_image)

    # 打开图片并显示原图
    def open_image(self):
        # 获取图片和图片类型
        img_name, img_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '',
                                                         '图像文件(*.jpg *.bmp *.png *.jpeg)')
        self.cv_srcImage = cv2.imread(img_name)

        # cv读取图片
        self.cv_srcImage = cv2.imread(img_name)

        # 调整图片大小--在label中显示正常大小
        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_source_img.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_source_img.height())

        # 将图片显示在label_source_img上面
        self.ui.label_source_img.setPixmap(QPixmap.fromImage(ui_image))

    # 将处理后的图片保存到本地
    def save_image(self):
        # 前面是地址，后面是文件类型,得到输入地址的文件名和地址txt(*.txt*.xls);;image(*.png)不同类别
        filepath, filetype = QFileDialog.getSaveFileName(self, "文件保存", "/", 'image(*.png)')

        # save方法保存图片到本地，filepath：保存的名称  PNG：保存的格式，-1：质量因素，值越大质量越高，-1表示默认值
        self.dst_img.save(filepath, 'PNG', -1)

    # 人物面部打码逻辑实现
    def face_coding(self):
        # 读取模型文件
        face = cv2.CascadeClassifier('./dataAccess/static/haarcascade_frontalface_alt.xml')
        """
        参数1：image–待检测图片，一般为灰度图像加快检测速度；
        参数2：objects–被检测物体的矩形框向量组；
        参数3：scaleFactor–表示在前后两次相继的扫描中，搜索窗口的比例系数。（默认为1.1）即每次搜索窗口依次扩大10%，该值越大计算的越快，人脸检测也越差;
        参数4：minNeighbors–表示构成检测目标的相邻矩形的最小个数(默认为3个)。
        """
        # 执行模型，左上顶点（x，y）和w（宽），h（高）
        faces = face.detectMultiScale(self.cv_srcImage, scaleFactor=1.2, minNeighbors=2)
        print(faces)

        # 进行人脸画框
        for x, y, w, h in faces:
            # 获取人脸的位置
            frame_box = self.cv_srcImage[y:y + h, x:x + w]
            # 缩小十倍
            frame_box = frame_box[::10, ::10]
            # x轴和y轴同时拉伸10倍，回复原来的大小
            frame_box = np.repeat(frame_box, 10, axis=0)
            frame_box = np.repeat(frame_box, 10, axis=1)
            # 获得原脸框的宽高
            a, b = self.cv_srcImage[y:y + h, x:x + w].shape[:2]
            # 让马赛克的宽高与原脸宽的宽高一样，不让会报错
            self.cv_srcImage[y:y + h, x:x + w] = frame_box[:a, :b]

        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        self.dst_img = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = self.dst_img.scaledToWidth(self.ui.label_dealt_img.width())
        else:
            ui_image = self.dst_img.scaledToHeight(self.ui.label_dealt_img.height())

        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(ui_image))

    # 人脸面部识别--画框
    def face_recognize(self):

        # 读取模型文件
        face = cv2.CascadeClassifier('./dataAccess/static/haarcascade_frontalface_alt.xml')
        """
        参数1：image–待检测图片，一般为灰度图像加快检测速度；
        参数2：objects–被检测物体的矩形框向量组；
        参数3：scaleFactor–表示在前后两次相继的扫描中，搜索窗口的比例系数。（默认为1.1）即每次搜索窗口依次扩大10%，该值越大计算的越快，人脸检测也越差;
        参数4：minNeighbors–表示构成检测目标的相邻矩形的最小个数(默认为3个)。
        """
        faces = face.detectMultiScale(self.cv_srcImage, scaleFactor=1.2, minNeighbors=2)
        print(faces)
        # 进行人脸画框
        for x, y, w, h in faces:
            cv2.rectangle(self.cv_srcImage, (x, y), (x + w, y + h), [0, 0, 255], 2)

        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_dealt_img.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_dealt_img.height())

        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(ui_image))
