"""
@Auth ： youngZ
@File ：main.py
程序入口文件
"""
import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QSplashScreen

from tools import loadPage


def main():
    # 启动app
    app = QApplication(sys.argv)
    # 启动画面
    splash = QSplashScreen()

    # 启动画面设置背景图片
    splash.setPixmap(QPixmap('./dataAccess/image/loadPage.jpg'))
    # 启动画面设置字体
    splash.setFont(QFont('微软雅黑', 10))
    # 开启启动画面
    splash.show()
    form = loadPage.Form(splash)
    form.show()
    splash.finish(form)  # 主界面加载完成后隐藏
    splash.deleteLater()

    # 打开样式表
    with open('userInterface/styleQss/button.qss', 'r', encoding='UTF-8') as style:
        qss_style = style.read()
    # 应用样式表
    app.setStyleSheet(qss_style)
    app.processEvents()  # 处理主进程，不卡顿
    app.exec_()


if __name__ == '__main__':
    main()
