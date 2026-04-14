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
    
def is_prime(modulus):
    '''
    Fermat's primality test is not enough as it is fooled by Carmichael numbers, so we also implement 
    the Miller Rabin primality test to verify the result obtained from Fermat's primality test is 
    at least a strong pseudoprime
    '''

    prime = True
    fermatexp = modulus - 1

    if (modulus % 2 == 0):
        prime = False
        print(f"{modulus} is trivially composite as it is even")
        return prime

    base = random.randint(2, modulus - 2)
    gcd = math.gcd(base, modulus)
    if (gcd != 1):
        prime = False
        print(f"Failed Fermat's test; {modulus} is definitely composite")
        print(f"A non-trivial factor of {modulus} is; {gcd}")
        return prime
    value = modular_exponentiation(base, fermatexp, modulus)
    if value != 1:
        prime = False
        print(f"Failed Fermat's test; {modulus} is definitely composite")
        return prime

    millerexp = modulus - 1
    k = 0
    while(millerexp % 2 == 0):
        k += 1
        millerexp /= 2

    print(millerexp)
    print(k)

    alpha = random.randint(2, modulus - 2)
    value = modular_exponentiation(alpha, millerexp, modulus)
    if(value == 1):
        print(f"Passed first round of Miller-Rabin; {modulus} is probably prime")
        return prime
        
    i = 1
    flag = (i < k)
    while(value != (modulus - 1) and flag == True):        
        value = modular_exponentiation(value, 2, modulus)
        if (value == 1):
            prime = False
            print(f"Failed round {i + 1} of Miller-Rabin; {modulus} is definitely composite")
            print(f"A non-trivial factor of {modulus} is; {math.gcd(value - 1, modulus)}")
            return prime
        
        i += 1
        flag = (i < k)

    if (value == -1 or flag == False):
        print(f"Passed all {i + 1} round of Miller-Rabin; {modulus} is probably prime")
        return prime

    '''
    
    Miller-Rabin Primality Test

    Let n > 1 be an odd integer. Write n - 1 = 2^k * m where m is odd.

    Choose a random integer a with 1 < a < n - 1.
    Compute b0 = a^m mod n.
    If b0 is congruent to 1 or -1 mod n, then stop and declare n is probably prime.
    Otherwise compute b1 = b0^2 mod n.
    If b1 is congruent to 1 mod n, then n is composite. Also gcd(b0 - 1, n) gives a nontrivial factor of n.
    If b1 is congruent to -1 mod n, then stop and declare n is probably prime.

    Continue squaring:
    bi+1 = bi^2 mod n

    At each step:

    If bi is congruent to -1 mod n, then stop and declare n is probably prime.
    If bi is congruent to 1 mod n before ever seeing -1, then n is composite.
    If you reach b(k-1) and never encountered -1, and b(k-1) is not congruent to -1 mod n, then n is composite.

    print(f"Failed Miller-Rabin: a non-trivial factor of {modulus} is; {math.gcd(val0 - 1, modulus)}")
    
    '''

    return prime

def inverse(number, modulus):
    pass

def export_keys(keyname):

    pass

def compute_D(e, p, q):

    pass