from Crypto.Cipher import AES
import os


def encrypt(key,iv,text):
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ciphertext, mac = cipher.encrypt_and_digest(text)
    return ciphertext, mac

def decrypt(key,iv,ciphertext,mac):
    plaintext = 0
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext,mac)
    except (ValueError, KeyError):
        exit("Error")
    return plaintext


key = os.urandom(16)
nonce = os.urandom(12)
data = b"This is super secret message."

ciphertext, mac = encrypt(key,nonce,data)
print(ciphertext, mac)

ciphertext += b"hogehoge"

plaintext = decrypt(key,nonce,ciphertext,mac)
print(plaintext)
