import secrets
import random


print(random.getrandbits(32)) # 32bitの疑似乱数を生成
print(secrets.randbits(32)) # 32bitの暗号論的疑似乱数を生成
