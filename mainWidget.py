from PyQt5.QtWidgets import (QComboBox, QHBoxLayout, QLineEdit, QPlainTextEdit,
                             QPushButton, QVBoxLayout, QWidget)

from hashing import generate


class MainWidgetPart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        algorithm_selection = QComboBox(self)
        algorithm_selection.addItems(["md5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512"])
        line_edit_count_of_symbols = QLineEdit()
        line_edit_count_of_symbols.setPlaceholderText("Количество символов")
        button_confirm = QPushButton("Сгенерировать!", self)
        button_confirm.clicked.connect(lambda preparation: generate(algorithm_selection.currentText(), generated_password, line_edit_count_of_symbols.text(), self))
        generated_password = QPlainTextEdit(self)
        generated_password.setPlaceholderText("Здесь появится ваш свежесгенерированный пароль...")
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(algorithm_selection)
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(line_edit_count_of_symbols)
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(button_confirm)
        hbox_4 = QHBoxLayout()
        hbox_4.addWidget(generated_password)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        vbox_1.addLayout(hbox_2)
        vbox_1.addLayout(hbox_3)
        vbox_1.addLayout(hbox_4)
        self.setLayout(vbox_1)
