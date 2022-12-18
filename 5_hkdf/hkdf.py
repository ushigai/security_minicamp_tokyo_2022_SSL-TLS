from binascii import hexlify, unhexlify
from Crypto.Util.number import *
from math import ceil
import hmac
import binascii
import hashlib


def HMAC(key, data, HashAlgo=hashlib.sha256):
    return hmac.new(key, data, HashAlgo).digest()

def hkdf(length, ikm, salt, info):
    prk = HMAC(salt, ikm)
    T, okm = b"", b"" 
    for i in range(ceil(length / 32)):
        T = HMAC(prk, T + info + bytes([i + 1]))
        okm += T
    return hexlify(prk), hexlify(okm[:length])


IKM  = unhexlify(b"0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b")
salt = unhexlify(b"000102030405060708090a0b0c")
info = unhexlify(b"f0f1f2f3f4f5f6f7f8f9")
L    = 42


prk, okm = hkdf(L, IKM, salt, info)

print("PRK :", prk)
print("OKM :", okm)
