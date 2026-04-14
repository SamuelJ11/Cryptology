import string, sys, random, math
from pathlib import Path

def blumblumslub():

    pass

def modular_exponentiation(base, exponent, modulus):

    current_exp = 1
    mod_reductions = []
    while (current_exp <= exponent):
        result = (base ** current_exp) % modulus
        mod_reductions.insert(0, result)
        current_exp *= 2

    binary_exp = to_binary(exponent)
    iterator = len(binary_exp)

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
    
def is_prime(modulus):
    '''
    Fermat's primality test is not enough as it is fooled by Carmichael numbers, so we also implement 
    the Miller Rabin primality test to verify the result obtained from Fermat's primality test is 
    at least a strong pseudoprime
    '''

    if (modulus <= 3):
        print("Please input an integer greater than 3")
        return
    
    fermatexp = modulus - 1
    fermatalpha = random.randint(2, modulus - 2)

    if (modulus % 2 == 0):
        print(f"{modulus} is trivially composite as it is even")
    else:
        gcd = math.gcd(fermatalpha, modulus)
        if (gcd != 1 or modular_exponentiation(fermatalpha, fermatexp, modulus) != 1):
            print(f"Failed Fermat's test; {modulus} is definitely composite")
            return False
        else:
            return True

    ### Double Check With Miller-Rabin Test

    millerexp = modulus - 1
    milleralpha = random.randint(2, modulus - 2)
    k = 0
    while(millerexp % 2 == 0):
        k += 1
        millerexp //= 2

    value = modular_exponentiation(milleralpha, millerexp, modulus)
    if(value == 1):
        print(f"Passed Miller-Rabin test; {modulus} is probably prime")
        return True
        
    i = 1
    flag = (i <= k)
    while(value != (modulus - 1) and flag == True):        
        value = modular_exponentiation(value, 2, modulus)
        if (value == 1):
            print(f"Failed Miller-Rabin test; {modulus} is definitely composite")
            return False
        i += 1
        flag = (i < k)

    if (value == (modulus - 1)):
        print(f"Passed Miller-Rabin test; {modulus} is probably prime")
        return True
    
def inverse(number, modulus):
    pass

def export_keys(keyname):

    pass

def compute_D(e, p, q):

    pass