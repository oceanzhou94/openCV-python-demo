"""
@Auth ： youngZ
@File ：main.py
程序入口文件
"""
import sys

from PyQt5.QtWidgets import QApplication

from businessLogic import mainWindow


def main():
    # 开启主窗口
    app = QApplication(sys.argv)
    root = mainWindow.MainWindow()
    root.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
