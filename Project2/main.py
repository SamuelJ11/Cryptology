from rsa import RSA
from utils import *
import time

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
    rsa.computeD()

main()