from rsa import RSA
from utils import *

r = RSA()

result = modular_exponentiation(3, 654, 706)
result2 = pow(3, 654, 706)

print(result)
print(result2)