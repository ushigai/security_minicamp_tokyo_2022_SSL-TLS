from Crypto.Util.number import *
from time import time


def GeneratKey():
    p, q = getPrime(512), getPrime(512)
    n = p * q
    e = 65537
    phi = (p - 1)*(q - 1)
    d = inverse(e, phi)
    return e, d, n


def EncryptAlice(message, e, n):
    cipher = pow(message, e, n)
    return cipher


def DecryptBob(cipher, e, d, n):
    message = pow(cipher, d, n)
    message = long_to_bytes(message)
    return message


start = time()
message = bytes_to_long(b"Hello_public_key_cryptography!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
e, d, n = GeneratKey()
print("message :", message)

cipher = EncryptAlice(message, e, n)
print("cipher :", cipher)

message_ = DecryptBob(cipher, e, d, n)
print("message_ :", message_)

print(time() - start)
