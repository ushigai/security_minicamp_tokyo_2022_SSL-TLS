import hashlib
import bcrypt

out1 = hashlib.sha256(b"Hello_sha256_hash_function!!!")
print("sha256 output :", out1.hexdigest())

salt = bcrypt.gensalt(rounds=10, prefix=b"2a")
print("bcrypt salt :", salt.decode())
password = b"P@ssw0rd!"
out2 = bcrypt.hashpw(password, salt)

print("bcrypt output :", out2.decode())
