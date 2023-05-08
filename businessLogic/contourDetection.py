"""
@Auth ： youngZ
@File ：contourDetection.py
图像轮廓检测处理逻辑
"""
import numpy as np
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QMessageBox
from cv2 import cv2
from userInterface import contourDetectionUI


class SubWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__(parent=None)

        self.ui = contourDetectionUI.Ui_MainWindow()  # 获取子窗口对象

        self.ui.setup_ui(self)  # 子窗口初始化
        self.ui_init()  # 事件初始化

        self.cv_srcImage = None  # cv读取图片
        self.cv_dealtImage = None  # 处理后的图片，类型为cv2
        self.dst_img = None  # 处理后的图片 类型为QImage，保存图片时使用

        self.contours = None  # 轮廓
        self.hierarchy = None  # 层次
        self.white_image = None  # 白色图像

        # 图标
        self.setWindowIcon(QIcon('./dataAccess/icon/icon.ico'))

    # 绑定事件
    def ui_init(self):
        # 打开图片并显示事件
        self.ui.pushButton_choose_img.clicked.connect(self.open_image)

        # 保存图片到本地事件
        self.ui.pushButton_save_img.clicked.connect(self.save_image)

        # 按钮点击事件
        self.ui.pushButton_find.clicked.connect(self.find_contour)  # 点击查找轮廓按钮
        self.ui.pushButton_polylines.clicked.connect(self.draw_contour)  # 点击绘制轮廓按钮
        self.ui.pushButton_moments.clicked.connect(self.get_moments)  # 点击轮廓的矩
        self.ui.pushButton_area.clicked.connect(self.get_areas)  # 点击轮廓的面积
        self.ui.pushButton_length.clicked.connect(self.get_length)  # 点击轮廓长度
        self.ui.pushButton_approxPolyDP.clicked.connect(self.draw_approx_poly)  # 点击近似多边形
        self.ui.pushButton_convexHull.clicked.connect(self.convex_hull)  # 点击轮廓的凸包
        self.ui.pushButton_boundingRect.clicked.connect(self.draw_bounding_rect)  # 点击直边界矩形
        self.ui.pushButton_minAreaRect.clicked.connect(self.draw_min_area_rect)  # 点击旋转矩形
        self.ui.pushButton_minEnclosingCircle.clicked.connect(self.draw_min_enclosing_circle)  # 点击最小外包圆
        self.ui.pushButton_fitEllipse.clicked.connect(self.draw_fit_ellipse)  # 点击拟合椭圆
        self.ui.pushButton_fitLine.clicked.connect(self.draw_fit_line)  # 点击拟合直线
        self.ui.pushButton_minEnclosingTriangle.clicked.connect(self.draw_min_enclosing_triangle)  # 点击最小外包三角形

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

    # 查找轮廓并输出相应的数据
    def find_contour(self):
        # 将其转换为灰度图像
        gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY)

        # 二值化阈值处理
        ret, img2 = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

        # 查找轮廓，返回值有3个，取后两个
        self.contours = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]  # 轮廓
        self.hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[2]  # 层次

        # 相关数据写入表格
        item_type_contours = QTableWidgetItem(str(type(self.contours)))  # 轮廓类型
        self.ui.tableWidget.setItem(0, 0, item_type_contours)

        item_value_contours = QTableWidgetItem(str(len(self.contours)))  # 轮廓个数
        self.ui.tableWidget.setItem(1, 0, item_value_contours)

        item_type_hierarchy = QTableWidgetItem(str(type(self.hierarchy)))  # 层次类型
        self.ui.tableWidget.setItem(2, 0, item_type_hierarchy)

    # 绘制轮廓到label_dealt_img显示
    def draw_contour(self):
        # 将其转换为灰度图像
        gray = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY)

        # 二值化阈值处理
        ret, img2 = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

        # 查找轮廓，返回值有3个，取后两个
        self.contours = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]  # 轮廓
        self.hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[2]  # 层次

        # 相关数据写入表格
        item_type_contours = QTableWidgetItem(str(type(self.contours)))  # 轮廓类型
        self.ui.tableWidget.setItem(0, 0, item_type_contours)

        item_value_contours = QTableWidgetItem(str(len(self.contours)))  # 轮廓个数
        self.ui.tableWidget.setItem(1, 0, item_value_contours)

        item_type_hierarchy = QTableWidgetItem(str(type(self.hierarchy)))  # 层次类型
        self.ui.tableWidget.setItem(2, 0, item_type_hierarchy)

        # 按原图大小创建一幅白色图像
        self.white_image = np.zeros(self.cv_srcImage.shape, np.uint8) + 255

        # 绘制轮廓,参数1：白色图像，参数二：轮廓，参数3：-1表示绘制所有轮廓，参数4：绘制颜色BGR，参数5：画笔粗细
        self.cv_dealtImage = cv2.drawContours(self.white_image, self.contours, -1, (255, 0, 0), 2)

        # 显示轮廓图像
        self.show_in_dealt_label()

    # 输出轮廓的矩
    def get_moments(self):
        # 先调用绘制轮廓
        self.draw_contour()

        # 遍历所有轮廓
        text = ""
        for n in range(len(self.contours)):
            # 得到每个轮廓的矩
            m = cv2.moments(self.contours[n])
            # 输出轮廓矩
            # 在label中显示
            text += f"轮廓{n}的矩：{m}\n"
            self.ui.label_result.setText(text)

    # 输出轮廓的面积
    def get_areas(self):
        # 先调用绘制轮廓
        self.draw_contour()

        text = ""
        # 遍历所有轮廓
        for n in range(len(self.contours)):
            # 计算轮廓面积
            m = cv2.contourArea(self.contours[n])
            text += f"轮廓{n}的面积：{m}\n"

        self.ui.label_result.setText(text)

    # 输出轮廓的长度
    def get_length(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        text = ""
        # 遍历所有轮廓
        for n in range(len(self.contours)):
            # 计算轮廓长度
            m = cv2.arcLength(self.contours[n], True)
            text += f"轮廓{n}的长度：{m}\n"

        self.ui.label_result.setText(text)

    # 绘制轮廓的近似多边形
    def draw_approx_poly(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        # epsilon为精度，表示近似多边形接近轮廓的最大距离
        epsilon = 0.1

        # 计算轮廓长度
        arcl = cv2.arcLength(self.contours[0], True)

        eps = epsilon * arcl
        self.cv_dealtImage = self.white_image.copy()
        # 获得近似多边形，参数1：轮廓，参数2：精度，参数3：True表示轮廓是封闭的
        app = cv2.approxPolyDP(self.contours[0], eps, True)

        self.ui.label_result.setText("近似多边形：\n" + str(app))

        # 绘制近似轮廓
        self.cv_dealtImage = cv2.drawContours(self.cv_dealtImage, [app], -1, (0, 255, 0), 2)

        # 显示轮廓图像
        self.show_in_dealt_label()

    # 绘制轮廓的凸包
    def convex_hull(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        # 计算凸包，返回值是一个numpy.ndarray对象，包含了凸包的关键点
        # returnPoints为True（默认值）时，返回的hull中包含的是凸包关键点的坐标
        hull_coord = cv2.convexHull(self.contours[0])

        # returnPoints为False时，返回的是凸包关键点在轮廓中的索引。
        hull_index = cv2.convexHull(self.contours[0], returnPoints=False)

        # 绘制凸包
        cv2.polylines(self.cv_dealtImage, [hull_coord], True, (0, 255, 0), 2)

        # 显示相关数据
        text = "凸包的坐标:\n" + str(hull_coord) + "\n凸包的索引:\n" + str(hull_index)
        self.ui.label_result.setText(text)

        # 显示轮廓图像
        self.show_in_dealt_label()

    # 绘制直边界矩形
    def draw_bounding_rect(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        # 计算直边界矩形
        ret = cv2.boundingRect(self.contours[0])

        text = "直边界矩形四元组\n(矩形左上角x坐标,矩形左上角y坐标,矩形的宽度,矩形的高度)\n" + str(ret)
        self.ui.label_result.setText(text)

        pt1 = (ret[0], ret[1])
        pt2 = (ret[0] + ret[2], ret[1] + ret[3])
        # 绘制直边界矩形
        cv2.rectangle(self.cv_dealtImage, pt1, pt2, (0, 255, 0), 2)

        # 显示结果图像
        self.show_in_dealt_label()

    # 绘制旋转矩形：可容纳轮廓的面积最小的矩形
    def draw_min_area_rect(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        # 计算最小矩形
        # ret为返回的旋转矩形，它是一个三元组，其格式为
        # ((矩形中心点x坐标, 矩形中心点y坐标), (矩形的宽度, 矩形的高度),矩形的旋转角度)。
        ret = cv2.minAreaRect(self.contours[0])

        text = "(矩形中心点x坐标, 矩形中心点y坐标), (矩形的宽度, 矩形的高度),矩形的旋转角度)\n" + str(ret)
        self.ui.label_result.setText(text)

        # 计算矩形顶点
        rect = cv2.boxPoints(ret)
        # 转换为整数
        rect = np.int0(rect)
        # 绘制旋转矩形
        cv2.drawContours(self.cv_dealtImage, [rect], 0, (0, 255, 0), 2)

        # 显示结果图像
        self.show_in_dealt_label()

    # 绘制最小外包圆
    def draw_min_enclosing_circle(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        # 计算最小外包圆
        (x, y), radius = cv2.minEnclosingCircle(self.contours[0])
        # 圆心坐标
        center = (int(x), int(y))
        # 圆的半径
        radius = int(radius)
        # 绘制最小外包圆
        cv2.circle(self.cv_dealtImage, center, radius, (0, 255, 0), 2)

        text = "圆心坐标：" + str(center) + "\n圆的半径：" + str(radius)
        self.ui.label_result.setText(text)
        # 显示结果图像
        self.show_in_dealt_label()

    # 绘制拟合椭圆
    def draw_fit_ellipse(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        # 计算拟合椭圆
        ellipse = cv2.fitEllipse(self.contours[0])
        # 绘制拟合椭圆
        cv2.ellipse(self.cv_dealtImage, ellipse, (0, 255, 0), 2)
        # 显示结果图像
        self.show_in_dealt_label()

    # 绘制拟合直线
    def draw_fit_line(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        rows, cols = self.cv_srcImage.shape[:2]
        # 计算拟合直线
        [vx, vy, x, y] = cv2.fitLine(self.contours[0], cv2.DIST_L2, 0, 0.01, 0.01)

        lefty = int((-x * vy / vx) + y)
        righty = int(((cols - x) * vy / vx) + y)
        # 绘制拟合直线
        cv2.line(self.cv_dealtImage, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
        # 显示结果图像
        self.show_in_dealt_label()

    # 绘制最小外包三角形
    def draw_min_enclosing_triangle(self):
        # 先调用绘制轮廓函数
        self.draw_contour()

        # 计算最小外包三角形
        # retval为最小外包三角形的面积，triangle为最小外包三角形
        retval, triangle = cv2.minEnclosingTriangle(self.contours[0])
        triangle = np.int0(triangle)

        # 绘制最小外包三角形
        cv2.polylines(self.cv_dealtImage, [triangle], True, (0, 255, 0), 2)

        text = "最小外包三角形面积：\n" + str(retval)
        self.ui.label_result.setText(text)

        # 显示结果图像
        self.show_in_dealt_label()
