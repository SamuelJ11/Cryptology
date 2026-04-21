from rsa import RSA
from utils import *
import time

for _ in range(10):
    x = random.randint(4, 64)
    is_prime(x)
    time.sleep(2)
    
'''
for _ in range(10):
    sequence = blumblumslub()
    print(sequence)    
    time.sleep(3)
    
'''