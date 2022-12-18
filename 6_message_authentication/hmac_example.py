import hashlib
import hmac
import os
from binascii import hexlify, unhexlify
from Crypto.Util.number import *

key =b"Jefe"
message =b"what do ya want for nothing?"

mac = hmac.new(key, message, digestmod=hashlib.md5)
print("digest :", mac.hexdigest())
# digest = 0x9294727a3638bb1c13f48ef8158bfc9d
# digest =        0x750c783e6ab0b503eaa86e310a5db738

