"""
@Auth ： youngZ
@File ：sourceImgShow.py
"""
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from cv2 import cv2


def source_img_show(label):
    """
    :param label: pyqt5中图像显示label
    :return: 无
    """
    # 获取图片和图片类型
    img_name, img_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '',
                                                     '图像文件(*.jpg *.bmp *.png *.jpeg)')

    # cv读取图片
    cv_src_image = cv2.imread(img_name)

    # 调整图片大小--在label中显示正常大小
    height, width = cv_src_image.shape[0], cv_src_image.shape[1]
    ui_image = QImage(cv2.cvtColor(cv_src_image, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
    if width > height:
        ui_image = ui_image.scaledToWidth(label.width())
    else:
        ui_image = ui_image.scaledToHeight(label.height())

    # 将图片显示在label_source_img上面
    label.setPixmap(QPixmap.fromImage(ui_image))
