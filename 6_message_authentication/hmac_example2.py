from hashlib import md5 
from Crypto.Util.number import *
from binascii import  hexlify, unhexlify 

msg = b"Hi There"
key = 0x0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b
key_len = 128

opad, ipad = int("5c"*64, 16), int("36"*64, 16)

okeypad = long_to_bytes((key << (512 - key_len)) ^ opad)
ikeypad = long_to_bytes((key << (512 - key_len)) ^ ipad)

mac = md5(okeypad + md5(ikeypad + msg).digest())
print(mac.hexdigest())
# digest = 0x9294727a3638bb1c13f48ef8158bfc9d
