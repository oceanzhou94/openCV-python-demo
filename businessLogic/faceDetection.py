"""
@Auth ： youngZ
@File ：faceDetection.py
人脸识别逻辑处理
"""
import cv2.cv2 as cv2
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 子窗口布局
from userInterface import faceDetectionUI


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = faceDetectionUI.Ui_Form()
        self.ui.setupUi(self)
        self.cv_srcImage = None
        self.FaceDetect = FaceDetect()
        self.ui_init()
        self.face_cascade = cv2.CascadeClassifier('./dataAccess/static/cascade.xml')

    # 使用信号槽触发事件
    def ui_init(self):
        self.ui.pushButton_video_captrue.clicked.connect(self.video_captrue)
        self.ui.pushButton_open_file.clicked.connect(self.open_file)
        self.FaceDetect.DetectOneFrame.connect(self.update_frame_to_label)

    def open_file(self):
        # 图像选择对话框--选择图片
        file_path, file_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '', '图像文件(*.jpg *.bmp *.png)')

        # cv读取图片
        self.cv_srcImage = cv2.imread(file_path)

        gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))

        for (x, y, w, h) in faces:
            cv2.rectangle(self.cv_srcImage, (x, y), (x + w, y + w), (0, 255, 0), 5)
        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)

        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_1.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_1.height())
        self.ui.label_image_1.setPixmap(QPixmap.fromImage(ui_image))

    # 摄像头捕获
    def video_captrue(self):
        if not self.FaceDetect.working:
            self.FaceDetect.working = True
            self.FaceDetect.start()
        else:
            self.FaceDetect.working = None
            self.ui.label_image_1.setText('停止捕捉')

    def update_frame_to_label(self, frame):
        self.ui.label_image_1.setPixmap(QPixmap.fromImage(frame))


class FaceDetect(QThread):
    DetectOneFrame = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.working = None

    def run(self):
        face_cascade = cv2.CascadeClassifier('./dataAccess/static/cascade.xml')
        capture = cv2.VideoCapture(0)
        while self.working:
            ret, frame_color = capture.read()
            (height, width, channels) = frame_color.shape
            frame_color = cv2.flip(frame_color, flipCode=1)  # 镜像
            gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame_color, (x, y), (x + w, y + w), (255, 255, 0), 4)
            ui_image = QImage(cv2.cvtColor(frame_color, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
            self.DetectOneFrame.emit(ui_image)
        capture.release()
        print('结束人脸检测')

