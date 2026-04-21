from rsa import RSA
from utils import *
import time

for _ in range(10):
    x = random.randint(1, 32)
    xbin = to_binary(x)
    print(f"x = {x} = {xbin}")

print()
    
for _ in range(10):
    sequence = blumblumslub()
    print(sequence)    
    time.sleep(3)
    