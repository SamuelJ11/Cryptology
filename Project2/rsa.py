import string
import utils
from pathlib import Path

class RSA:
     
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.d = None
        self.e = None
        self.n = None

    def computeN(self):
        
        self.n = self.p * self.q
        
    def computeE(self):
        
        if (self.n == None):
            print("Warning: modulus not yet defined, unable to compute the encyrption exponent.")
            return
        
        encryption_exp = utils.generate_prime()        
        modulus = utils.totient(self.p, self.q)
        
        while (utils.gcd_recursive(encryption_exp, modulus) != 1):
            encryption_exp = utils.generate_prime()
        
        self.e = encryption_exp
    
    def computeD(self):
        
        if (self.n == None):
            print("Warning: modulus not yet defined, unable to compute the decryption exponent.")
            return
        
        modulus = utils.totient(self.p, self.q)
        self.d = utils.mod_inverse(self.e, modulus)
        
    def generate_pubkey(self):
        
        if (self.e == None):
            print("Warning: encryption exponent not yet defined, unable to compute the public key.")
            return
        
        pubkey = (self.e, self.n)
        
        # Write the public key to a seperate file
        with open("pubkey.txt", "w") as pb:
            pb.write(str(pubkey))

    def generate_privkey(self):
        
        if (self.d == None):
            print("Warning: decryption exponent not yet defined, unable to compute the private key.")
            return
        
        privkey = (self.d, self.n)
        
        # Write the private key to a seperate file
        with open("privkey.txt", "w") as pv:
            pv.write(str(privkey))
        
    def encrypt(self, message):
        
        # Encrypt the message
        ciphertext = utils.modular_exponentiation(message, self.e, self.n)
        return ciphertext
        
    def decrypt(self, ciphertext):
        
        # Decrypt the message
        plaintext = utils.modular_exponentiation(ciphertext, self.d, self.n)        
        return plaintext