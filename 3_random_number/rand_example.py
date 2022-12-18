import secrets
import random
from time import time


start = time()
_ = [random.getrandbits(32) for i in range(100000)] # 32bitの疑似乱数を生成
print(time() - start)

start = time()
__ = [secrets.randbits(32) for j in range(100000)] # 32bitの暗号論的疑似乱数を生成
print(time() - start)
