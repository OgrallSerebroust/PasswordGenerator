from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout


class MainWidgetPart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        test_label = QLabel("Hello world!")
        count_of_signs = QLineEdit(self)
        count_of_signs.setPlaceholderText("Введите желаемую длину пароля:")
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(test_label)
        hbox_1.addWidget(count_of_signs)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        self.setLayout(vbox_1)
