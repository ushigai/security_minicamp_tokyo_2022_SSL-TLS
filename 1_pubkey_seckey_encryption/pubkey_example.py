from Crypto.Util.number import *


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


message = bytes_to_long(b"Hello_public_key_cryptography!!!")
e, d, n = GeneratKey()
print("message :", message)

cipher = EncryptAlice(message, e, n)
print("cipher :", cipher)

message_ = DecryptBob(cipher, e, d, n)
print("message_ :", message_)

