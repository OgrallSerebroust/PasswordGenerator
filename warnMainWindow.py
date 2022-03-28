from email.mime import application
from PyQt5.QtWidgets import QMainWindow
from warnMainWidget import MainWidgetPart


class MainWindowPart(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_main_part = MainWidgetPart(parent=self)
        self.setCentralWidget(self.window_main_part)
        self.setWindowTitle("Warning")