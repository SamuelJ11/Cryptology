import string, sys, operator
from pathlib import Path

FERMAT_TRIALS = 20

def generate_randint():

    pass

def modular_exponentiation(base, exponent, modulus):

    current_exp = 1
    mod_reductions = []
    while (current_exp < exponent):
        result = (base ** current_exp) % modulus
        mod_reductions.insert(0, result)
        current_exp *= 2

    binary_exp = to_binary(exponent)
    iterator = len(binary_exp) - 1

    result = 1
    for i in range(iterator):
        if binary_exp[i] == 1:
            result = (result * mod_reductions[i]) % modulus

    return result

def to_binary(number):

    quotient = number // 2  
    remainder = number % 2  

    bits = []
    i, flag = 0, 1
    while (flag <= number):
        bits.insert(0, remainder)
        remainder = quotient % 2  
        quotient = quotient // 2  
        i += 1
        flag *= 2  

    return bits
    
def is_prime(number):

    pass

def export_keys(keyname):

    pass

def compute_D(e, p, q):

    pass