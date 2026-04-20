import string, sys, random, math
from pathlib import Path

MAXRAND = 50
MINRAND = 4

def blumblumslub():
    '''
    This function generates a random binary sequence by operating on the quadratic residues in the Blum group of a number 'n', 
    which we define to be the product of two randomly-generated primes 'p' and 'q', such that p ≡ q ≡ 3 mod 4.  
    '''
    
    # Initialize values for p and q for primality testing
    p = random.randint(MINRAND, MAXRAND)
    while(not candidate_prime(p)):
        p = random.randint(MINRAND, MAXRAND)
        
    q = random.randint(MINRAND, MAXRAND)
    while(not candidate_prime(q)):
        q = random.randint(MINRAND, MAXRAND)
        
    # Perform primality test on p and q and ensure they are congruent to 3 mod 4    
    while(not is_prime(p) or p % 4 != 3):   
        p = random.randint(MINRAND, MAXRAND)
        while(not candidate_prime(p)):
            p = random.randint(MINRAND, MAXRAND)
            
    while(not is_prime(q) or q % 4 != 3):
        q = random.randint(MINRAND, MAXRAND)
        while(not candidate_prime(q)):
            q = random.randint(MINRAND, MAXRAND)
              
    print(f"p = {p} has been vetted and tested to be prime and congruent to 3 (mod 4)")
    print(f"q = {q} has been vetted and tested to be prime and congruent to 3 (mod 4)")
    
    '''
    # Generate the quadratic residues mod p and mod q
    p_residues = set()
    for i in range(1, p + 1):
         p_residues.add(pow(i, 2) % p)
    p_residues.remove(0)
    
    q_residues = set()
    for i in range(1, q + 1):
         q_residues.add(pow(i, 2) % q)
    q_residues.remove(0)
    
    print(f"p_residues = {p_residues}")
    print(f"q_residues = {q_residues}")
    '''
    
    n = p * q    
    print(f"n = {n} has been computed for the modulus of the blumblumshub generator seed")
    
    # Generate a random seed that is coprime to n = p * q for the blumblumslub bitstream generator
    seed = random.randint(MINRAND, n - 1)
    while(not math.gcd(seed, n) == 1):
        seed = random.randint(MINRAND, n - 1)
        
    print(f"Found a seed = {seed} that is coprime to {n}")

    return True

def candidate_prime(number):
    '''
    This function generates "candidate" primes, aka numbers that don't immediately fail trivial composite tests.
    The output of this function is used by the blumblumslub() function and the is_prime() function to avoid 
    calling the computationally expensive modular_exponentiation() function on numbers that fail such tests.
    '''
    
    num_digits = len(str(number))
    last_digit = number % 10
     
    if (last_digit % 2 == 0): # Test for even parity   
        print(f"{number} is even")
        return False
    
    if (last_digit % 5 == 0 and number != 5): # Test for divisibility by 5
        print(f"{number} is disible by 5")
        return False        
    
    sum_of_digits = 0      
    for i in range(0, num_digits):
        sum_of_digits += (number // pow(10, i)) % 10
        
    if (sum_of_digits % 3 == 0 or sum_of_digits % 9 == 0):  # Check if the sum of the digits is divisible by 3 or 9
        print(f"{number} is divisible by 3 or 9")
        return False
        
    alternating_digitsum = 0        
    for i in range(0, num_digits):
        alternating_digitsum +=  ((number // pow(10, i)) % 10) * pow(-1, i)
        
    if (alternating_digitsum % 11 == 0 and number != 11):    # Check if the alternating sum of digits is divisible by 11 
        print(f"{number} is divisible by 11")
        return False
        
    return True

def modular_exponentiation(base, exponent, modulus):
    '''
    This function uses sucessive squaring of powers of {base} and the binary representation of {exponent} to compute 
    the modular exponentiation equivalent to Python's pow(base, exponent, modulus) function.
    '''

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
    '''
    This function converts a number to binary by storing the remainders in a list after repeated division by 2.
    '''

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
    at least a strong pseudoprime.
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