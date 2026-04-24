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
            print("Warning: modulus not defined, unable to compute the encyrption exponent")
            return
        
        encryption_exp = utils.generate_prime()        
        modulus = utils.totient(self.n, self.p, self.q)
        
        while (utils.gcd_recursive(encryption_exp, modulus) != 1):
            encryption_exp = utils.generate_prime()
        
        self.e = encryption_exp
    
    def computeD(self, e, n):
        self.d = utils.mod_inverse(e, utils.totient(n))

    def generate_pubkey(self, n, e):
        
        pass

    def generate_privkey(self, n, d):
        
        pass

    def encrypt(self, message, keyname):
        
        pass

    def decrypt(self, ciphertext, keyname):
        
        pass
