from rsa import RSA
from utils import *
import sys

MINDIFF = 32

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
    
main()