from Crypto.Util.number import *


def GeneratKey():
    p, q = getPrime(512), getPrime(512)
    n = p * q
    e = 65537
    phi = (p - 1)*(q - 1)
    d = inverse(e, phi)
    pubkey = [e, n]
    seckey = [d]
    return pubkey, seckey


def EncryptAlice(message, pubkey):
    e, n = pubkey
    cipher = pow(message, e, n)
    return cipher


def DecryptBob(cipher, pubkey, seckey):
    e, n = pubkey
    d = seckey[0]
    message = pow(cipher, d, n)
    message = long_to_bytes(message)
    return message


message = bytes_to_long(b"Hello_public_key_cryptography!!!")
pubkey, seckey = GeneratKey()
print("message :", message)

cipher = EncryptAlice(message, pubkey)
print("cipher :", cipher)

message_ = DecryptBob(cipher, pubkey, seckey)
print("message_ :", message_)

