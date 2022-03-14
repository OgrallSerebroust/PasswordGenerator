from hashlib import md5
from os import urandom

def generate(hash_type:str, generated_password):
    if hash_type == "md5":
        sault_uni = urandom(32) #TODO LOCAL PARAMETER
        password = md5(urandom(8) + sault_uni).hexdigest()
        generated_password.setText(password)
    with open("hello.txt", "w") as file:
        file.write(str(password))
