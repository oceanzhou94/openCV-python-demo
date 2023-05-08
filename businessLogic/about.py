"""
@Auth ： youngZ
@File ：about.py
关于
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

# 子窗口布局
from userInterface import aboutUI


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = aboutUI.Ui_MainWindow()
        self.ui.setupUi(self)
        # 图标
        self.setWindowIcon(QIcon('./dataAccess/icon/icon.ico'))
