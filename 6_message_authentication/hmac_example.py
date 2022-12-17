import hashlib
import hmac
import os
from binascii import hexlify, unhexlify

key = unhexlify(b"0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b")
message = b"Hi There"

mac = hmac.new(key, message, digestmod=hashlib.md5)
print("digest :", mac.hexdigest())
# digest = 0x9294727a3638bb1c13f48ef8158bfc9d

