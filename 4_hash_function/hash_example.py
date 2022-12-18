import hashlib
import bcrypt

out1 = hashlib.sha256(b"Hello_sha256_hash_function!!!")
print("sha256 output :", out1.hexdigest())

password = b"P@ssw0rd!"
salt = bcrypt.gensalt(rounds=10, prefix=b"2a")
print("bcrypt salt :", salt.decode())
out2 = bcrypt.hashpw(password, salt)

print("bcrypt output :", out2.decode())

salt = bcrypt.gensalt(rounds=10, prefix=b"2a")
print("bcrypt salt :", salt.decode())
out3 = bcrypt.hashpw(password, salt)

print("bcrypt output :", out3.decode())
