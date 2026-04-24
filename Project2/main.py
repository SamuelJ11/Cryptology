from rsa import RSA
from utils import *
import sys

MINDIFF = 10 ** 95

def main():
    
    ### VALIDATE PROGRAM USAGE AND FILE PATH ###

    if len(sys.argv) != 2:
        print("Usage: myscript.py <filename>")
        return
    
    filename = str(sys.argv[1])
    cwd = Path().resolve() 
    filepath = cwd.joinpath(filename)   

    if filepath.exists() == False:
        print(f"{filename} could not be found in the current working directory")
        return
    
    message = int(filepath.read_text())
    
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
    
    ### ENCRYPTION ###
    
    print(f"The original message before encryption is {message}\n")
    
    encryption_exp = pub_key[0]
    ciphertext = modular_exponentiation(message, encryption_exp, shared_modulus)
    
    print(f"The message after encryption is {ciphertext}\n")   
    
    ### DECRYPTION ###
    
    decryption_exp = priv_key[0]
    plaintext = modular_exponentiation(ciphertext, decryption_exp, shared_modulus)
    print(f"The message after decryption is {plaintext}\n") 
    
main()