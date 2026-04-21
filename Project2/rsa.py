import string, utils
from pathlib import Path

class RSA:
     
    def __init__(self):
        self.p = 3
        self.q = 5
        self.d = 7

    def computeN(self):
        pass
    
    def compute_E(self):
        
        pass
    
    def compute_D(self, e):

        pass

    def generate_pubkey(self, n, e):
        
        pass

    def generate_privkey(self, n, d):
        
        pass

    def encrypt(self, message, keyname):
        
        pass

    def decrypt(self, ciphertext, keyname):
        
        pass
