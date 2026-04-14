from rsa import RSA
from utils import *

import random

for _ in range(200):
    base = random.randint(1, 1000000)
    exp = random.randint(2, 10000000)
    mod = random.randint(3, 1000000)

    a = modular_exponentiation(base, exp, mod)
    b = pow(base, exp, mod)

    print(a == b)