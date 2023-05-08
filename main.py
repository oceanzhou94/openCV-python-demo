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
    app = QApplication(sys.argv)
    splash = QSplashScreen()
    splash.setPixmap(QPixmap("loadPage.jpg"))  # 设置背景图片
    splash.setFont(QFont('微软雅黑', 10))  # 设置字体
    splash.show()
    app.processEvents()  # 处理主进程，不卡顿
    form = loadPage.Form(splash)
    form.show()
    splash.finish(form)  # 主界面加载完成后隐藏
    splash.deleteLater()
    app.exec_()


if __name__ == '__main__':
    main()
