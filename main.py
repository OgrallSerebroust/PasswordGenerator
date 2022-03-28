from sys import argv, exit

from PyQt5.QtGui import QColor, QFont, QIcon, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory

from mainWidget import MainWidgetPart


class MainWindowPart(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#FFFFFF"))
        self.setWindowTitle("PasswordGenerator2.0")
        self.setWindowIcon(QIcon("assets/img/1.png"))
        self.window_main_part = MainWidgetPart(parent=self)
        self.setCentralWidget(self.window_main_part)
        self.setFont(QFont("", 14))
        self.setPalette(palette)
        with open("source/css/style.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())


if __name__ == "__main__":
    application = QApplication(argv)
    application.setStyle(QStyleFactory.create("Fusion"))
    program = MainWindowPart()
    program.show()
    exit(application.exec_())
