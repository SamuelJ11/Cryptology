from rsa import RSA
from utils import *
import time


for _ in range(10):
    
    x = generate_prime()
    
    y = generate_prime()
    while y == x:
        y = generate_prime()
    
    if (x > y):
        temp = x
        x = y
        y = temp
    
    mod_inverse(x, y)
    time.sleep(2) 

for _ in range(10):
    sequence = blumblumshub()
    print(f"Taking the LSB of each number in Blum sub-cycle yields: {sequence}\n")    
    time.sleep(2)


for _ in range(20):
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    result = gcd_recursive(x, y)
    
    print(f"The GCD of {x} and {y} is {result}")
    time.sleep(2)
    

for _ in range(10):
    x = random.randint(100, 1000)
    is_prime(x)
    time.sleep(2)