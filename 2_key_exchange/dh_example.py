from Crypto.Util.number import getPrime
from random import getrandbits

x = getPrime(512)
y = getrandbits(256)

p = getPrime(64)
q = getPrime(64)

A_pub = pow(y, p, x)
B_pub = pow(y, q, x)

A_sec = pow(B_pub, p, x)
B_sec = pow(A_pub, q, x)

SECKEY = pow(y, p*q, x)

assert A_sec == B_sec
assert A_sec == SECKEY

print("AliceとBobが共有した鍵 ", SECKEY)
