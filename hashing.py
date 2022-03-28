from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from os import urandom
from sys import argv

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

from warnMainWindow import MainWindowPart


def generate(hash_type:str, generated_password, count_of_symbols:str, mainWidgetPart):
    if hash_type == "md5":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        password = md5(urandom(8) + sault_uni).hexdigest()
        try: 
            if count_of_symbols == "":
                generated_password.setPlainText(password)
            else:
                generated_password.setPlainText(password[0:int(count_of_symbols)])
        except ValueError:
            mainWidgetPart.program = MainWindowPart()
            mainWidgetPart.program.show()
            #warn_exception.setText("Необходимо ввести число(целое) символов!")
            #warn_exception.setStyleSheet("""
                #color: #343A90;
                #background: #FFFFFF;
            #""")
            #warn_exception.setWindowIcon(QIcon("assets/img/1.png"))
            #warn_exception.setFont(QFont("", 14))
            #warn_exception.setIcon(QMessageBox.Warning)
    if hash_type == "SHA1":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        password = sha1(urandom(8) + sault_uni).hexdigest()
        generated_password.setPlainText(password)
    if hash_type == "SHA224":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        password = sha224(urandom(8) + sault_uni).hexdigest()
        generated_password.setPlainText(password)
    if hash_type == "SHA256":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        password = sha256(urandom(8) + sault_uni).hexdigest()
        generated_password.setPlainText(password)
    if hash_type == "SHA384":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        password = sha384(urandom(8) + sault_uni).hexdigest()
        generated_password.setPlainText(password)
    if hash_type == "SHA512":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        password = sha512(urandom(8) + sault_uni).hexdigest()
        generated_password.setPlainText(password)
