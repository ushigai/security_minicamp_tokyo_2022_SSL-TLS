from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import urandom
from time import time


def EncryptAlice(message, seckey):
    cipher = AES.new(key=seckey, mode=AES.MODE_CBC, iv=iv)
    ct = cipher.encrypt(pad(message, AES.block_size))
    return ct

def DecryptBob(cipher_text, seckey):
    cipher = AES.new(key=seckey, mode=AES.MODE_CBC, iv=iv)
    message = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return message


start = time()
seckey, iv = urandom(16), urandom(16)
message = b"Hello_private_key_cryptography!!!"
print("message: ", message)

cipher_text = EncryptAlice(message, seckey)
print("cipher_text: ", cipher_text)

message_ = DecryptBob(cipher_text, seckey)
print("message_: ", message_)


print(time() - start)
