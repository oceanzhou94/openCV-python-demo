"""
@Auth ： youngZ
@File ：templateMatch.py
图像模板匹配处理逻辑
"""

from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QMessageBox
from cv2 import cv2
from userInterface import templateMatchUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = templateMatchUI.Ui_MainWindow()  # 获取子窗口对象

        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 事件初始化

        self.cv_srcImage = None  # cv读取的原图片
        self.cv_tmpImage = None  # cv读取的模板图片
        self.cv_dealtImage = None  # 处理后的图片，类型为cv2
        self.dst_img = None  # 处理后的图片 类型为QImage，保存图片时使用

        # 图标
        self.setWindowIcon(QIcon('./dataAccess/icon/icon.ico'))

    # 绑定事件
    def ui_init(self):
        self.ui.pushButton_choose_img.clicked.connect(self.open_image)  # 点击打开图片
        self.ui.pushButton_save_img.clicked.connect(self.save_image)  # 点击保存图片
        self.ui.pushButton_choose_tmpl.clicked.connect(self.choose_tmpl_image)  # 点击选择模板

        self.ui.pushButton_match_s1.clicked.connect(self.signal_match_s1)  # 点击单目标匹配中的方差匹配
        self.ui.pushButton_match_s2.clicked.connect(self.signal_match_s2)  # 点击单目标匹配中的相关匹配
        self.ui.pushButton_match_s3.clicked.connect(self.signal_match_s3)  # 点击单目标匹配中的相关系数匹配

        self.ui.pushButton_match_m1.clicked.connect(self.many_match_m1)  # 点击多目标匹配中的标准方差匹配
        self.ui.pushButton_match_m2.clicked.connect(self.many_match_m2)  # 点击多目标匹配中的标准相关匹配
        self.ui.pushButton_match_m3.clicked.connect(self.many_match_m3)  # 点击多目标匹配中的标准相关系数匹配

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
        hight, width, channel = self.cv_dealtImage.shape
        q_image = None
        # 4通道类型的图
        if channel == 4:
            q_image = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGBA)
            q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
        # 3通道类型的图
        elif channel == 3:
            q_image = cv2.cvtColor(self.cv_dealtImage, cv2.COLOR_BGR2RGB)
            q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)
        # 单通道类型的图
        elif channel == 1:
            q_image = QImage(self.cv_dealtImage.data, width, hight, QImage.Format_Grayscale8)

        # 将图片显示在label_dealt_img上面
        self.dst_img = q_image
        self.ui.label_dealt_img.setPixmap(QPixmap.fromImage(self.dst_img))

    # 选择模板图片
    def choose_tmpl_image(self):
        # 获取图片和图片类型
        img_name, img_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '',
                                                         '图像文件(*.jpg *.bmp *.png *.jpeg)')
        # cv读取图片
        if img_name == "":
            # 未选择图片，弹出消息对话框
            QMessageBox.critical(self, '错误！', '请选择模板图像', QMessageBox.Close)
        else:
            self.cv_tmpImage = cv2.imread(img_name)
            # 转换cv_srcImage类型为QImage
            hight, width, channel = self.cv_tmpImage.shape
            q_image = None
            # 4通道类型的图
            if channel == 4:
                q_image = cv2.cvtColor(self.cv_tmpImage, cv2.COLOR_BGR2RGBA)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB32)
            # 3通道类型的图
            elif channel == 3:
                q_image = cv2.cvtColor(self.cv_tmpImage, cv2.COLOR_BGR2RGB)
                q_image = QImage(q_image.data, width, hight, width * channel, QImage.Format_RGB888)
            # 单通道类型的图
            elif channel == 1:
                q_image = QImage(self.cv_tmpImage.data, width, hight, QImage.Format_Grayscale8)
            # 将图片显示在label_source_img上面
            self.ui.label_tmpl_img.setPixmap(QPixmap.fromImage(q_image))

    # 单目标匹配中的方差匹配
    def signal_match_s1(self):
        # 复制一种原图像
        img = self.cv_srcImage.copy()
        # 转换为单通道灰度图像
        src_gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 转换为单通道灰度图像
        temp_gray = cv2.cvtColor(self.cv_tmpImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 获得模板图像的高度和宽度
        temp_h, temp_w = temp_gray.shape

        # 执行匹配操作，cv2.TM_SQDIFF：以方差结果为依据进行匹配。完全匹配时结果为0，否则为一个很大的值。
        res = cv2.matchTemplate(src_gray, temp_gray, cv2.TM_SQDIFF)

        # 返回最值和位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # 最小值为最佳匹配，获得其位置
        top_left = min_loc
        # 获得匹配范围的右下角位置
        bottom_right = (top_left[0] + temp_w, top_left[1] + temp_h)
        # 绘制匹配范围,蓝色边框
        self.cv_dealtImage = cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 3)
        # 显示匹配结果
        self.show_in_dealt_label()
        # 显示结果数组
        text = "匹配结果数组：\n" + str(res)
        self.ui.label_result.setText(text)

    # 单目标匹配中的相关匹配
    def signal_match_s2(self):
        # 复制一种原图像
        img = self.cv_srcImage.copy()
        # 转换为单通道灰度图像
        src_gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 转换为单通道灰度图像
        temp_gray = cv2.cvtColor(self.cv_tmpImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 获得模板图像的高度和宽度
        temp_h, temp_w = temp_gray.shape

        # 执行匹配操作，cv2.TM_CCORR：相关匹配，将输入图像与模板图像相乘，乘积越大匹配度越高，乘积为0时匹配度最低。
        res = cv2.matchTemplate(src_gray, temp_gray, cv2.TM_CCORR)

        # 返回最值和位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # 最小值为最佳匹配，获得其位置
        top_left = min_loc
        # 获得匹配范围的右下角位置
        bottom_right = (top_left[0] + temp_w, top_left[1] + temp_h)
        # 绘制匹配范围,绿色边框
        self.cv_dealtImage = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        # 显示匹配结果
        self.show_in_dealt_label()
        # 显示结果数组
        text = "匹配结果数组：\n" + str(res)
        self.ui.label_result.setText(text)

    # 单目标匹配中的相关系数匹配
    def signal_match_s3(self):
        # 复制一种原图像
        img = self.cv_srcImage.copy()
        # 转换为单通道灰度图像
        src_gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 转换为单通道灰度图像
        temp_gray = cv2.cvtColor(self.cv_tmpImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 获得模板图像的高度和宽度
        temp_h, temp_w = temp_gray.shape

        # 执行匹配操作，cv2.TM_CCOEFF：相关系数匹配
        res = cv2.matchTemplate(src_gray, temp_gray, cv2.TM_CCOEFF)

        # 返回最值和位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # 最小值为最佳匹配，获得其位置
        top_left = min_loc
        # 获得匹配范围的右下角位置
        bottom_right = (top_left[0] + temp_w, top_left[1] + temp_h)
        # 绘制匹配范围,红色边框
        self.cv_dealtImage = cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 3)
        # 显示匹配结果
        self.show_in_dealt_label()
        # 显示结果数组
        text = "匹配结果数组：\n" + str(res)
        self.ui.label_result.setText(text)

    # 多目标匹配中的标准方差匹配
    def many_match_m1(self):
        # 复制一种原图像
        img = self.cv_srcImage.copy()
        # 转换为单通道灰度图像
        src_gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 转换为单通道灰度图像
        temp_gray = cv2.cvtColor(self.cv_tmpImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 获得模板图像的高度和宽度
        temp_h, temp_w = temp_gray.shape
        # 获得员图像的高度和宽度
        src_h, src_w = src_gray.shape
        # 执行匹配操作，cv2.TM_SQDIFF_NORMED：标准（归一化）方差匹配。
        res = cv2.matchTemplate(src_gray, temp_gray, cv2.TM_SQDIFF_NORMED)
        # 用于保存符合条件的匹配位置
        mloc = []
        # 设置匹配度阈值
        threshold = 0.24
        for i in range(src_h - temp_h):
            for j in range(src_w - temp_w):
                if res[i][j] <= threshold:  # 保存小于阈值的匹配位置
                    mloc.append((j, i))
        for pt in mloc:
            # 标准匹配位置，蓝色矩形
            cv2.rectangle(img, pt, (pt[0] + temp_w, pt[1] + temp_h), (255, 0, 0), 2)

        # 画完线的图像赋值给显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()

        # 显示结果数组
        text = "匹配结果数组：\n" + str(res)
        self.ui.label_result.setText(text)

    # 多目标匹配中的标准相关匹配
    def many_match_m2(self):
        # 复制一种原图像
        img = self.cv_srcImage.copy()
        # 转换为单通道灰度图像
        src_gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 转换为单通道灰度图像
        temp_gray = cv2.cvtColor(self.cv_tmpImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 获得模板图像的高度和宽度
        temp_h, temp_w = temp_gray.shape
        # 获得员图像的高度和宽度
        src_h, src_w = src_gray.shape
        # 执行匹配操作，cv2.TM_CCORR_NORMED：标准（归一化）相关匹配。
        res = cv2.matchTemplate(src_gray, temp_gray, cv2.TM_CCORR_NORMED)
        # 用于保存符合条件的匹配位置
        mloc = []
        # 设置匹配度阈值
        threshold = 0.24
        for i in range(src_h - temp_h):
            for j in range(src_w - temp_w):
                if res[i][j] <= threshold:  # 保存小于阈值的匹配位置
                    mloc.append((j, i))
        for pt in mloc:
            # 标准匹配位置，绿色矩形
            cv2.rectangle(img, pt, (pt[0] + temp_w, pt[1] + temp_h), (0, 255, 0), 2)

        # 画完线的图像赋值给显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()

        # 显示结果数组
        text = "匹配结果数组：\n" + str(res)
        self.ui.label_result.setText(text)

    # 多目标匹配中的标准相关系数匹配
    def many_match_m3(self):
        # 复制一种原图像
        img = self.cv_srcImage.copy()
        # 转换为单通道灰度图像
        src_gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 转换为单通道灰度图像
        temp_gray = cv2.cvtColor(self.cv_tmpImage, cv2.COLOR_BGR2GRAY, dstCn=1)
        # 获得模板图像的高度和宽度
        temp_h, temp_w = temp_gray.shape
        # 获得员图像的高度和宽度
        src_h, src_w = src_gray.shape
        # 执行匹配操作，cv2.TM_CCOEFF_NORMED：标准（归一化）相关系数匹配。
        res = cv2.matchTemplate(src_gray, temp_gray, cv2.TM_CCOEFF_NORMED)
        # 用于保存符合条件的匹配位置
        mloc = []
        # 设置匹配度阈值
        threshold = 0.24
        for i in range(src_h - temp_h):
            for j in range(src_w - temp_w):
                if res[i][j] <= threshold:  # 保存小于阈值的匹配位置
                    mloc.append((j, i))
        for pt in mloc:
            # 标准匹配位置，红色矩形
            cv2.rectangle(img, pt, (pt[0] + temp_w, pt[1] + temp_h), (0, 0, 255), 2)

        # 画完线的图像赋值给显示图像
        self.cv_dealtImage = img
        self.show_in_dealt_label()
        # 显示结果数组
        text = "匹配结果数组：\n" + str(res)
        self.ui.label_result.setText(text)
