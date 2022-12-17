from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

message = b'To be signed'
h = SHA256.new(message)
print(h.hexdigest())
key = RSA.import_key(open('privkey.pem').read())
signature = pss.new(key).sign(h)

key = RSA.import_key(open('pubkey.pem').read())
verifier = pss.new(key)

try:
    verifier.verify(h, signature)
    print("The signature is authentic.")
except (ValueError, TypeError):
    print("The signature is not authentic.")
