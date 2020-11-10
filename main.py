import numpy as np
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import os
def ECB():

    #key = b'1234123412341234'
    key=os.urandom(32)
    print(key.__sizeof__())
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    with open("5.bmp", "rb") as imageFile:
        datas = base64.b64encode(imageFile.read())
        imageFile.close()
    ct = encryptor.update(datas+datas[:12]) + encryptor.finalize()
    newdatas = ct.hex().encode('utf8')
    newdatas.decode('utf8')
    m = base64.b64decode(newdatas)
    fh = open("3.bmp", "wb")
    fh.write(m)
    fh.close()
    os.system("dd if=5.bmp of=3.bmp bs=1 count=54 conv=notrunc")

def CBC():

    key = os.urandom(32)
    print(key.__sizeof__())
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    with open("5.bmp", "rb") as imageFile:
        datas = base64.b64encode(imageFile.read())
        imageFile.close()

    ct = encryptor.update(datas.__add__(datas[:12])) + encryptor.finalize()
    newdatas = ct.hex().encode('utf8')
    newdatas.decode('utf8')
    m = base64.b64decode(newdatas)
    fh = open("6.bmp", "wb")
    fh.write(m)
    fh.close()
    os.system("dd if=5.bmp of=6.bmp bs=1 count=54 conv=notrunc")

if __name__ == '__main__':
    ECB()
    CBC()