from Crypto.Util.number import getPrime
from random import getrandbits

x = getPrime(512)
y = getrandbits(256)

p = getPrime(64)
q = getPrime(64)

A_pub = pow(y, p, x) # y^p mod x
B_pub = pow(y, q, x) # y^q mod x

A_sec = pow(B_pub, p, x) # (y^q)^p mod x = y^(q*p) mod x
B_sec = pow(A_pub, q, x) # (y^p)^q mod x = y^(q*p) mod x

SECKEY = pow(y, p*q, x)

assert A_sec == B_sec
assert A_sec == SECKEY

print("AliceとBobが共有した鍵 ", SECKEY)
