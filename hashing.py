from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from os import urandom

def generate(hash_type:str, generated_password):
    if hash_type == "md5":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        password = md5(urandom(8) + sault_uni).hexdigest()
        generated_password.setPlainText(password)
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
