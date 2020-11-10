import numpy as np
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def GetBytesImage():

    key = b'1234123412341234'
    print(key.__sizeof__())
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    with open("5.bmp", "rb") as imageFile:
        datas = base64.b64encode(imageFile.read())
        imageFile.close()

    ct = encryptor.update(datas[:48]) + encryptor.finalize()
    c = datas[48:] + datas[:datas.__len__()]
    newdatas = ct.hex().encode('utf8')
    newdatas = newdatas.__add__(c)

    newdatas.decode('utf8')
    m = base64.b64decode(newdatas)
    fh = open("3.bmp", "wb")
    fh.write(m)
    fh.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GetBytesImage()