from rsa import RSA
from utils import *
import time

'''
for _ in range(10):

x = generate_prime()

y = generate_prime()
while y == x:
    y = generate_prime()

if (x > y):
    temp = x
    x = y
    y = temp

for _ in range(10):
    sequence = blumblumshub()
    print(f"Taking the LSB of each number in Blum sub-cycle yields: {sequence}\n")    
    time.sleep(2)

for _ in range(5):
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    
    temp = x
    x = y
    y = temp
    
    result = mod_inverse(x, y)    
    time.sleep(2)
''' 

def main():
    
    p = generate_prime()
    q = generate_prime()
    
    if (p < q):
        temp = p
        p = q
        q = temp
        
    while(p - q < 10 ** 95):
        p = generate_prime()
        q = generate_prime()

    rsa = RSA(p, q)

    rsa.computeN()
    rsa.computeE()

main()