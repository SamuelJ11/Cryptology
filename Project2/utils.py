import string, sys, random, math
from pathlib import Path

def blumblumslub():
    
    p = random.randint(0, 100000)
    while(not candidate_prime(p)):
        p = random.randint(0, 100000)
        
    q = random.randint(0, 100000)
    while(not candidate_prime(q)):
        q = random.randint(0, 100000)

    while(not is_prime(p)):
        p = random.randint(0, 100000)
        while(not candidate_prime(p)):
            p = random.randint(0, 100000)
            
    while(not is_prime(q)):
        q = random.randint(0, 100000)
        while(not candidate_prime(q)):
            q = random.randint(0, 100000)
            
    print(f"p = {p} has been vetted and tested to be prime")
    print(f"q = {q} has been vetted and tested to be prime")

    n = p * q

    return n

def candidate_prime(number):
    '''
    This function generates "candidate" primes, aka numbers that don't immediately fail trivial composite tests.
    The output of this function is used by the blumblumslub() function and the is_prime() function to avoid 
    calling the computationally expensive modular_exponentiation() function on numbers that fail such tests.
    '''
    last_digit = number % 10
     
    if (last_digit % 2 == 0): # Test for even parity   
        print(f"{number} is even")
        return False
    elif (last_digit % 5 == 0): # Test for divisibility by 5
        print(f"{number} is disible by 5")
        return False    
    else:
        sum_of_digits = 0
        num_digits = len(str(number))
        
        for i in range(0, num_digits):
            sum_of_digits += (number // pow(10, i)) % 10

        if (sum_of_digits % 3 == 0 or sum_of_digits % 9 == 0):  # Check if the sum of the digits is divisible by 3 or 9
            print(f"{number} is divisible by 3 or 9")
            return False
               
        alternating_digitsum = 0        
        for i in range(0, num_digits):
            alternating_digitsum +=  ((number // pow(10, i)) % 10) * pow(-1, i)
            
        if (alternating_digitsum % 11 == 0):    # Check if the alternating sum of digits is divisible by 11 
            print(f"{number} is divisible by 11")
            return False
        
    return True

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
    alpha = random.randint(2, modulus - 2)
    
    if (not candidate_prime(modulus)):
        return False            
    else:
        fermatexp = modulus - 1        
        gcd = math.gcd(alpha, modulus)
        
        if (gcd != 1 or modular_exponentiation(alpha, fermatexp, modulus) != 1):
            print(f"Failed Fermat's test; {modulus} is definitely composite")
            return False
        else:
            print(f"\nFermat test PASSED for base a = {alpha}")
            print("Proceeding to Miller-Rabin test\n")

    ### Double Check With Miller-Rabin Test
    
    millerexp = modulus - 1
    k = 0
    while(millerexp % 2 == 0):
        k += 1
        millerexp //= 2
        
    value = modular_exponentiation(alpha, millerexp, modulus)
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