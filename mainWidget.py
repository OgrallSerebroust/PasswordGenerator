from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout


class MainWidgetPart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        test_label = QLabel("Hello world!")
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(test_label)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        self.setLayout(vbox_1)
