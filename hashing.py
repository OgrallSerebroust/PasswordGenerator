from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from os import urandom

from warnMainWindow import MainWindowPart


def generate(hash_type:str, generated_password, count_of_symbols:str, mainWidgetPart):
    password = algorithm_selection(hash_type)
    try: 
        if count_of_symbols == "":
            generated_password.setPlainText(password)
        else:
            generated_password.setPlainText(password[0:int(count_of_symbols)])
    except ValueError:
        mainWidgetPart.program = MainWindowPart()
        mainWidgetPart.program.show()

def algorithm_selection(hash_type:str):
    if hash_type == "md5":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        return md5(urandom(8) + sault_uni).hexdigest()
    if hash_type == "SHA1":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        return sha1(urandom(8) + sault_uni).hexdigest()
    if hash_type == "SHA224":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        return sha224(urandom(8) + sault_uni).hexdigest()
    if hash_type == "SHA256":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        return sha256(urandom(8) + sault_uni).hexdigest()
    if hash_type == "SHA384":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        return sha384(urandom(8) + sault_uni).hexdigest()
    if hash_type == "SHA512":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        return sha512(urandom(8) + sault_uni).hexdigest()
