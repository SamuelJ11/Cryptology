from rsa import RSA
from utils import *
import sys

MINIMUMDIFF = 10 ** 95

def main():
    
    ### VALIDATE PROGRAM USAGE AND FILE PATH ###

    if len(sys.argv) != 2:
        print("Usage: myscript.py <filename>")
        return
    
    message = read_file()
    print(f"The original message before encryption is {message}\n")
    
    ### KEY SETUP ###
    
    p = generate_prime()
    q = generate_prime()
    
    while abs(p - q) < MINIMUMDIFF:
        p = generate_prime()
        q = generate_prime()

    rsa = RSA(p, q)

    rsa.computeN()
    rsa.computeE()
    rsa.computeD()
    
    ### ENCRYPTION ###
    
    rsa.generate_pubkey()
    ciphertext = rsa.encrypt(message)
    print(f"The message after encryption is {ciphertext}\n") 

    # Write the ciphertext to a seperate file
    write_file("ciphertext.txt", ciphertext)
    
    ### DECRYPTION ###
    
    rsa.generate_privkey()
    plaintext = rsa.decrypt(ciphertext)
    print(f"The message after decryption is {plaintext}") 
    
    # Write the plaintext to a seperate file
    write_file("plaintext.txt", plaintext)
    
main()