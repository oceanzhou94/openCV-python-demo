"""
@Auth ： youngZ
@File ：characterCoding.py
人物图像打码逻辑处理
"""
import numpy as np
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
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
        self.cv_dealtImage = None  # cv2相关处理后的图像
        self.dst_img = None  # 将cv_dealtImage转换成QImage之后的图像

        # 图标
        self.setWindowIcon(QIcon('./dataAccess/icon/icon.ico'))

    # 绑定事件
    def ui_init(self):

        self.ui.pushButton_choose_img.clicked.connect(self.open_image)  # 打开图片
        self.ui.pushButton_save_img.clicked.connect(self.save_image)  # 保存图片

        self.ui.pushButton_face_coding.clicked.connect(self.face_coding)  # 面部打码
        self.ui.pushButton_face_reco.clicked.connect(self.face_recognize)  # 面部框线
        self.ui.pushButton_eye_reco.clicked.connect(self.eyes_recognize)  # 眼部框线
        self.ui.pushButton_eye_coding.clicked.connect(self.eyes_coding)  # 眼部打码

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

    # 人物面部打码逻辑实现
    def face_coding(self):
        # 判断是否有图像
        if self.cv_srcImage is None:
            # 消息弹出无图像
            QMessageBox.information(self, "提示", "未选择图像，请先选择图像!", QMessageBox.Close)
        else:
            # 复制原图象
            self.cv_dealtImage = self.cv_srcImage.copy()
            # 读取模型文件
            face_cascade = cv2.CascadeClassifier('./dataAccess/static/haarcascade_frontalface_alt.xml')

            """
            参数1：image–待检测图片，一般为灰度图像加快检测速度；
            参数2：objects–被检测物体的矩形框向量组；
            参数3：scaleFactor–表示在前后两次相继的扫描中，搜索窗口的比例系数。（默认为1.1）即每次搜索窗口依次扩大10%，该值越大计算的越快，人脸检测也越差;
            参数4：minNeighbors–表示构成检测目标的相邻矩形的最小个数(默认为3个)。
            """
            # 执行人脸识别模型
            faces = face_cascade.detectMultiScale(self.cv_dealtImage, scaleFactor=1.2, minNeighbors=2)

            # 进行人脸画框
            for x, y, w, h in faces:
                # 获取人脸的位置
                frame_box = self.cv_dealtImage[y:y + h, x:x + w]
                # 缩小十倍
                frame_box = frame_box[::10, ::10]
                # x轴和y轴同时拉伸10倍，回复原来的大小
                frame_box = np.repeat(frame_box, 10, axis=0)
                frame_box = np.repeat(frame_box, 10, axis=1)
                # 获得原脸框的宽高
                a, b = self.cv_dealtImage[y:y + h, x:x + w].shape[:2]
                # 让马赛克的宽高与原脸宽的宽高一样，不让会报错
                self.cv_dealtImage[y:y + h, x:x + w] = frame_box[:a, :b]

            # 显示图像
            self.show_in_dealt_label()

    # 人脸面部识别--画框
    def face_recognize(self):
        # 判断是否有图像
        if self.cv_srcImage is None:
            # 消息弹出无图像
            QMessageBox.information(self, "提示", "未选择图像，请先选择图像!", QMessageBox.Close)
        else:
            # 复制原图像
            self.cv_dealtImage = self.cv_srcImage.copy()
            # 读取模型文件
            face_cascade = cv2.CascadeClassifier('./dataAccess/static/haarcascade_frontalface_alt.xml')
            """
            参数1：image–待检测图片，一般为灰度图像加快检测速度；
            参数2：objects–被检测物体的矩形框向量组；
            参数3：scaleFactor–表示在前后两次相继的扫描中，搜索窗口的比例系数。（默认为1.1）即每次搜索窗口依次扩大10%，该值越大计算的越快，人脸检测也越差;
            参数4：minNeighbors–表示构成检测目标的相邻矩形的最小个数(默认为3个)。
            """
            faces = face_cascade.detectMultiScale(self.cv_dealtImage, scaleFactor=1.2, minNeighbors=2)
            # 进行人脸画框
            for x, y, w, h in faces:
                cv2.rectangle(self.cv_dealtImage, (x, y), (x + w, y + h), [0, 0, 255], 2)

            # 显示图像
            self.show_in_dealt_label()

    # 人物眼睛框线
    def eyes_recognize(self):
        # 判断是否有图像
        if self.cv_srcImage is None:
            # 消息弹出无图像
            QMessageBox.information(self, "提示", "未选择图像，请先选择图像!", QMessageBox.Close)
        else:
            # 复制原图像
            self.cv_dealtImage = self.cv_srcImage.copy()
            # 将图像转为灰度
            gray = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2GRAY)
            # 加载级联分类器
            eye_cascade = cv2.CascadeClassifier('./dataAccess/static/haarcascade_eye.xml')
            # 执行检测器
            eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
            for (ex, ey, ew, eh) in eyes:
                # 眼睛画框
                cv2.rectangle(self.cv_dealtImage, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # 显示图像
            self.show_in_dealt_label()

    # 人物眼睛打码
    def eyes_coding(self):
        # 判断是否有图像
        if self.cv_srcImage is None:
            # 消息弹出无图像
            QMessageBox.information(self, "提示", "未选择图像，请先选择图像!", QMessageBox.Close)
        else:
            # 复制原图像
            self.cv_dealtImage = self.cv_srcImage.copy()

            # 灰度转换
            gray = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2GRAY)

            eye_cascade = cv2.CascadeClassifier('./dataAccess/static/haarcascade_eye.xml')

            # 人脸检测
            rects = eye_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
            if len(rects) > 0:
                for rect in rects:
                    x, y, w, h = rect
                    # 打码：使用高斯噪声替换识别出来的人眼所对应的像素值
                    self.cv_dealtImage[y + 10:y + h - 10, x:x + w, 0] = np.random.normal(size=(h - 20, w))
                    self.cv_dealtImage[y + 10:y + h - 10, x:x + w, 1] = np.random.normal(size=(h - 20, w))
                    self.cv_dealtImage[y + 10:y + h - 10, x:x + w, 2] = np.random.normal(size=(h - 20, w))

            # 显示图像
            self.show_in_dealt_label()
