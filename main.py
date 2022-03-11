from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWidget import MainWidgetPart


class MainWindowPart(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PasswordGenerator2.0")
        self.window_main_part = MainWidgetPart(parent=self)
        self.setCentralWidget(self.window_main_part)


if __name__ == "__main__":
    application = QApplication(argv)
    program = MainWindowPart()
    program.show()
    exit(application.exec_())