from rsa import RSA
from utils import *
import sys, time

MINDIFF = 10 ** 4

def main():
    
    ### VALIDATE PROGRAM USAGE AND FILE PATH ###

    # Check for valid program usage
    if len(sys.argv) != 2:
        print("Usage: myscript.py <filename>")
        return
    
    ## Import and read filename for analysis
    filename = str(sys.argv[1])
    cwd = Path().resolve() 
    filepath = cwd.joinpath(filename)   

    ## Check if the path for the provided filename exists in the current directory
    if filepath.exists() == False:
        print(f"{filename} could not be found in the current working directory")
        return
    
    message = int(filepath.read_text())
    
    '''
    
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
    
    ### ENCRYPTION ###
    
    print(f"The original message before encryption is {message}\n")    
    encryption_exp = pub_key[0]
    shared_modulus = pub_key[1]
    
    ciphertext = modular_exponentiation(message, encryption_exp, shared_modulus)
    print(f"The message after encryption is {ciphertext}\n")   
    
    ### DECRYPTION ###
    
    decryption_exp = priv_key[0]
    plaintext = modular_exponentiation(ciphertext, decryption_exp, shared_modulus)
    print(f"The message after decryption is {plaintext}\n") 
    
    '''
    
    for _ in range(10):
        
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
        
        encryption_exp = pub_key[0]
        shared_modulus = pub_key[1]
        decryption_exp = priv_key[0]
        
        print(f"The value of n is {rsa.n}")
        print(f"Using p = {rsa.p} and q = {rsa.q}, the value of totient(n) is {totient(rsa.p, rsa.q)}\n")
        
        ciphertext = modular_exponentiation(message, encryption_exp, shared_modulus)
        print(f"The message after encryption is {ciphertext}\n")  

        plaintext = modular_exponentiation(ciphertext, decryption_exp, shared_modulus)
        print(f"The message after decryption is {plaintext}\n")
        
        time.sleep(2)
    
main()