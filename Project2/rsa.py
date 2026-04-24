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
        self.pubkey = None
        self.privkey = None

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
        
        self.pubkey = (self.e, self.n)

    def generate_privkey(self):
        
        if (self.d == None):
            print("Warning: decryption exponent not yet defined, unable to compute the private key.")
            return
        
        self.privkey = (self.d, self.n)

    def encrypt(self, message):
        
        # Encrypt the message
        ciphertext = utils.modular_exponentiation(message, self.pubkey[0], self.pubkey[1])
        return ciphertext

    def decrypt(self, ciphertext):
        
        # Decrypt the message
        plaintext = utils.modular_exponentiation(ciphertext, self.privkey[0], self.privkey[1])
        return plaintext