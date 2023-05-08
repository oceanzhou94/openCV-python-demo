import time

from PyQt5.QtCore import Qt

from businessLogic import mainWindow


class Form(mainWindow.MainWindow):
    def __init__(self, splash):
        super(Form, self).__init__()
        self.resize(800, 600)

        self.splash = splash

        self.load_data()

    def load_data(self):
        for i in range(100):
            time.sleep(0.01)
            self.splash.showMessage(f'加载中...{str(i)}%', Qt.AlignLeft | Qt.AlignBottom, Qt.black)
