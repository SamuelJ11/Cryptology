from rsa import RSA
from utils import *
import sys

MINDIFF = 10 ** 95

def main():
    
    ### VALIDATE PROGRAM USAGE ###
    
    if len(sys.argv) != 2:
        print("Usage: myscript.py <filename>")
        return
    
    ### KEY SETUP ###
    
    p = generate_prime()
    q = generate_prime()
    
    while abs(p - q) < MINDIFF:
        p = generate_prime()
        q = generate_prime()

    rsa = RSA(p, q)

    rsa.computeN()
    rsa.computeE()
    rsa.computeD()

    pub_key = rsa.generate_pubkey()
    priv_key = rsa.generate_privkey()
    
    shared_modulus = rsa.n
    
    message = read_message()
    
    ### ENCRYPTION ###
    
    print(f"The original message before encryption is {message}\n")
    
    ciphertext = rsa.encrypt(message)
    print(f"The message after encryption is {ciphertext}\n")   
    
    ### DECRYPTION ###
    
    plaintext = rsa.decrypt(ciphertext)
    print(f"The message after decryption is {plaintext}\n") 
    
main()