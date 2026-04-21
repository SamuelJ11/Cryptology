import string, sys, random, math
from pathlib import Path

MAXRAND = 12
MINRAND = 4
STREAMLENGTH = 20

def blumblumslub():
    '''
    This function generates a random binary sequence by operating on the quadratic residues in the Blum Group of a number 'n', 
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
        
    # Compute the modulus of the seed for the blumblumslub bitstream generator
    n = p * q    
   
    # Generate a random seed that is coprime to n and ensure it is at most n - 2
    seed = random.randint(MINRAND, n - 2)    
    while(math.gcd(seed, n) != 1):
        seed = random.randint(MINRAND, n - 2)

    seed = modular_exponentiation(seed, 2, n)

    # Define the size of the Blum Group to print a sequence of this length 
    blumsize = ((p-1)*(q-1)) // 4
    print(f"Found a seed ({seed}) that is within the Blum Group B({n}), which has size {blumsize}")
    
    # Generate the ordered sequence of the sub-cycle
    bitstream = [seed]
    for i in range(1, STREAMLENGTH):
        bitstream.append(pow(bitstream[i-1], 2, n))
        
    return bitstream
    
def candidate_prime(number):
    '''
    This function generates "candidate" primes, aka numbers that don't immediately fail trivial composite tests.
    The output of this function is used by the blumblumslub() function and the is_prime() function to avoid 
    calling the computationally expensive modular_exponentiation() function on numbers that fail such tests.
    '''
    
    num_digits = len(str(number))
    last_digit = number % 10
    
    # Test for even parity
    if (last_digit % 2 == 0):    
        return False
    
    if (num_digits > 1 and number != 11):      
     
        # Test for divisibility by 5
        if (last_digit % 5 == 0): 
            return False        
        
        sum_of_digits = 0      
        for i in range(0, num_digits):
            sum_of_digits += (number // pow(10, i)) % 10
            
        # Check if the sum of the digits is divisible by 3 or 9
        if (sum_of_digits % 3 == 0 or sum_of_digits % 9 == 0):  
            return False
            
        alternating_digitsum = 0        
        for i in range(0, num_digits):
            alternating_digitsum +=  ((number // pow(10, i)) % 10) * pow(-1, i)
            
        # Check if the alternating sum of digits is divisible by 11    
        if (alternating_digitsum % 11 == 0):     
            return False
            
    return True

def modular_exponentiation(base, exponent, modulus):
    '''
    This function uses sucessive squaring of powers of {base} and the binary representation of {exponent} to compute 
    the modular exponentiation equivalent to Python's pow(base, exponent, modulus) function.
    '''
    
    # Precompute powers of base corresponding to powers of 2:
    # base^(1), base^(2), base^(4), base^(8), ... (all mod modulus)    
    mod_reductions = []  
      
    current_exp = 1
    while (current_exp <= exponent):
        result = (base ** current_exp) % modulus
        mod_reductions.insert(0, result)
        current_exp *= 2
        
    # Convert exponent into binary form to determine which powers to include
    binary_exp = to_binary(exponent)
    iterator = len(binary_exp)
    
    # Reconstruct result by multiplying selected powers of two (mod modulus)
    result = 1
    for i in range(iterator):
        if binary_exp[i] == 1:
            result = (result * mod_reductions[i]) % modulus

    return result

def to_binary(number):
    '''
    This function converts a number to binary by storing the remainders in a list after repeated division by 2.
    '''

    # Initialize the quotient and remainder values
    quotient = number // 2  
    remainder = number % 2  
    
    # Build binary representation from least significant bit upward    
    bits = []
    
    # Iterate through powers of 2 to extract each bit position
    flag = 1
    while (flag <= number):
        
        # Prepend current least significant bit
        bits.insert(0, remainder)
        
        # Shift number right by one binary position
        remainder = quotient % 2  
        quotient = quotient // 2 

        # Move to next power of 2
        flag *= 2 

    return bits
    
def is_prime(modulus):
    '''
    Fermat's primality test is not enough as it is fooled by Carmichael numbers, so we also implement 
    the Miller Rabin primality test to verify the result obtained from Fermat's primality test is 
    at least a strong pseudoprime.
    '''
   
    alpha = random.randint(2, modulus - 2)
    
    # First apply a stronger preliminary primality check  
    if (not candidate_prime(modulus)):
        return False            
    else:
        fermatexp = modulus - 1  

        # Ensure alpha is coprime to {modulus}      
        gcd = math.gcd(alpha, modulus)
        
        # Fermat's little theorem check: pow(a, n-1, n) ≡ 1 for a prime modulus n
        # If gcd != 1, or the congruence !≡ -1, then {modulus} is definitely composite 
        if (gcd != 1 or modular_exponentiation(alpha, fermatexp, modulus) != 1):
            print(f"Failed Fermat's test; {modulus} is definitely composite")
            return False
        else:
            # Passed Fermat test for this base (does not guarantee primality)
            print(f"Passed Fermat test for base alpha = {alpha}")
            
            # Proceed to the stronger probabilistic Miller-Rabin test 
            print("Proceeding to Miller-Rabin test")

    # For the Miller-Rabin test, write {modulus - 1} as 2^k * q where q is odd   
    millerexp = modulus - 1
    k = 0
    while(millerexp % 2 == 0):
        k += 1
        millerexp //= 2
        
    value = modular_exponentiation(alpha, millerexp, modulus)
    
    # First check: is value ≡ 1? If so, {modulus} passes this round
    if(value == 1):
        print(f"Passed Miller-Rabin test; {modulus} is probably prime\n")
        return True
    
    # Otherwise, repeatedly square to look for a value ≡ -1
    
    i = 1
    while(i <= k):
        
        # Compute successive powers: value^(2^i) mod {modulus} via repeated squaring
        nextpow2 = 2 ** i        
        nextvalue = modular_exponentiation(value, nextpow2, modulus)
        
        # If we hit 1 prematurely, {value} is a non-trivial square root of 1, meaning {modulus} is composite
        if (value == 1):
            print(f"Failed Miller-Rabin test; {modulus} is definitely composite")
            return False
        
        i += 1
        
    # If we ever hit -1, this round passes
    if (value == (modulus - 1)):
        print(f"Passed Miller-Rabin test; {modulus} is probably prime\n")
        return True
        
    
def inverse(number, modulus):
    pass

def export_keys(keyname):

    pass

def compute_D(e, p, q):

    pass