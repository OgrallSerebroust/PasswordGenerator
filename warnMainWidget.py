from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QVBoxLayout,
                             QWidget)                         


class MainWidgetPart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        label_of_message = QLabel("Необходимо ввести число(целое) символов!", self)
        button_ok = QPushButton("Понятно", self)
        button_ok.clicked.connect(lambda close_window: parent.close())
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(label_of_message)
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(button_ok)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        vbox_1.addLayout(hbox_2)
        self.setLayout(vbox_1)
