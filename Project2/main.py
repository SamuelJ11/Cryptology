from rsa import RSA
from utils import *

r = RSA()

result = modular_exponentiation(2, 1234, 789)
result2 = pow(2, 1234, 789)

print(result)
print(result2)