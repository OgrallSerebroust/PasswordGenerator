from PyQt5.QtGui import QColor, QFont, QIcon, QPalette
from PyQt5.QtWidgets import QMainWindow

from warnMainWidget import MainWidgetPart


class MainWindowPart(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#FFFFFF"))
        self.window_main_part = MainWidgetPart(parent=self)
        self.setCentralWidget(self.window_main_part)
        self.setWindowTitle("Warning")
        self.setWindowIcon(QIcon("assets/img/1.png"))
        self.setFont(QFont("", 14))
        self.setPalette(palette)
        with open("source/css/style.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
