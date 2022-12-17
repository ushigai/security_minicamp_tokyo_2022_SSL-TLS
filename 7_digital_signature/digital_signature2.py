from Crypto.Util.number import *
import hashlib
from binascii import hexlify, unhexlify


def keygen(bits):
    p, q = getPrime(bits//2), getPrime(bits//2)
    n = p * q
    phi = (p - 1)*(q - 1)
    e = 65537
    d = inverse(e, phi)
    return n, d

def sign(m: str, d: int, HashAlgo=hashlib.sha256):
    m = bytes_to_long(HashAlgo(m.encode()).digest())
    s = pow(m, d, n)
    return s

def verify(m: str, s: int, HashAlgo=hashlib.sha256):
    m = bytes_to_long(HashAlgo(m.encode()).digest())
    v = (m == pow(s, 65537, n))
    return v


n, d = keygen(1024)
m = "This is message."

signature = sign(m, d)
print("Signature :", signature)
v = verify(m, signature)

if v:
    print("The signature is authentic.")
else:
    print("The signature is not authentic.")

