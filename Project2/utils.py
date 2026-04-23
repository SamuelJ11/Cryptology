import string, sys, random, math
from pathlib import Path

MAXRAND = 12
MINRAND = 4
STREAMLENGTH = 20

def generate_prime():
    '''
    This function generates a random prime integer within the range of (MINRAND, MAXRAND)
    '''   
    
    # Initialize p within the given constraints
    p = random.randint(MINRAND, MAXRAND)
   
    # Ensure p is not trivially composite and verify its "probably" prime 
    while not (candidate_prime(p) and is_prime(p)):
        p = random.randint(MINRAND, MAXRAND)

    return p

def blumblumshub():
    '''
    This function generates a random binary sequence by operating on the quadratic residues in the Blum Group of a number 'n', 
    which we define to be the product of two randomly-generated primes 'p' and 'q', such that p ≡ q ≡ 3 (mod 4).  
    '''
    
    # Generate distinct primes p and q and ensure p ≡ q ≡ 3 mod 4
    p = generate_prime()
    while(p % 4 != 3):
        p = generate_prime()
        
    q = generate_prime()
    while(q % 4 != 3 or q == p):
        q = generate_prime()
        
    # Compute the modulus of the seed for the blumblumslub bitstream generator
    n = p * q    
   
    # Generate a random seed that is coprime to n
    seed = random.randint(MINRAND, n - 1)    
    while(gcd_recursive(seed, n) != 1):
        seed = random.randint(MINRAND, n - 1)
        
    print(f"Chose {seed} as a proto-seed before squaring (mod {n})")

    seed = modular_exponentiation(seed, 2, n)
    print(f"Found a seed ({seed}) that is within the Blum Group B({n})")
    
    # Generate the ordered sequence of the sub-cycle
    bitstream = [seed]
    for i in range(1, STREAMLENGTH):
        bitstream.append(modular_exponentiation(bitstream[i-1], 2, n))
        
    # Convert the sequence into a binary stream taking the LSB of each number
    for i in range(len(bitstream)):
        lsb = bitstream[i] % 2
        bitstream[i] = lsb
        
    return bitstream
    
def candidate_prime(number):
    '''
    This function generates "candidate" primes, aka numbers that don't immediately fail trivial composite tests.
    The output of this function is used by the blumblumshub() function and the is_prime() function to avoid 
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
        
        # Check if {number} is a perfect square
        root = math.isqrt(number)
        if (root ** 2 == number):
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
    This function tests {modulus} for primality by running the input through Fermat's primality test, 
    then feeding the result into the Miller-Rabin primality test to verify the result obtained is at least 
    a strong pseudoprime.
    '''
   
    alpha = random.randint(2, modulus - 2)
    
    # First apply a stronger preliminary primality check  
    if (not candidate_prime(modulus)):
        print(f"Failed a trivial composite test; {modulus} is definitely composite\n")
        return False            
    else:
        fermatexp = modulus - 1  

        # Ensure alpha is coprime to {modulus}      
        gcd = gcd_recursive(alpha, modulus)
        
        # Fermat's little theorem check: pow(a, n-1, n) ≡ 1 for a prime modulus n
        # If gcd != 1, or the congruence !≡ -1, then {modulus} is definitely composite 
        if (gcd != 1 or modular_exponentiation(alpha, fermatexp, modulus) != 1):
            print(f"Failed Fermat's test; {modulus} is definitely composite\n")
            return False
        else:
            # Passed Fermat test for this base (does not guarantee primality)
            print(f"Passed Fermat test with modulus = {modulus} and with base = {alpha}")
            
            # Proceed to the stronger probabilistic Miller-Rabin test 
            print("Proceeding to Miller-Rabin test")

    # For the Miller-Rabin test, write {modulus - 1} as 2^k * q where q is odd   
    millerexp = modulus - 1
    k = 0
    while(millerexp % 2 == 0):
        k += 1
        millerexp //= 2

    value = modular_exponentiation(alpha, millerexp, modulus)

    # Check for value ≡ 1 or -1 before entering the loop
    if value == 1 or value == modulus - 1:
        print(f"Passed Miller-Rabin test; {modulus} is probably prime\n")
        return True     
    
    # Repeatedly square to check if value ≡ -1    
    i = 1
    while(i < k):
        
        # Declare {modulus} prime and return immediately if value ≡ -1
        if value == modulus - 1:
            print(f"Passed Miller-Rabin test; {modulus} is probably prime\n")
            return True

        # If we reach 1 prematurely, {modulus} is definitely composite
        if value == 1:
            print(f"Failed Miller-Rabin test; {modulus} is definitely composite\n")
            return False
        
        # Update the value and loop condition for the next iteration
        value = modular_exponentiation(value, 2, modulus)
        i += 1    
    
    print(f"Made it to final stage of Miller-Rabin test; {modulus} is probably prime\n")
    return True

def gcd_recursive(a, b):
    '''
    This function recursively computes the GCD of {a} and {b} by repeatedly replacing the larger number 
    with the remainder of its division by the smaller number until the remainder is zero.
    '''
    
    # If {b} is zero, it means {a} divided the previous number perfectly, and since every number divides 
    # zero the greatest number that divides both {a} and zero is simply {a}.
    if b == 0:
        return a
    else:        
        # Replace the dividend with the divisor, the divisor with the remainder, and recursivley call 
        # the function with these updated parameters until the base case is reached
        return gcd_recursive(b, a % b)
        
def eea_recursive(a, b):
    '''
    This function servers as a helper for mod_recursive(); it recursively computes the modular 
    inverse of {a} (mod {b}). At every step, we are trying to solve the equation GCD = (a * s) + (b * t), 
    where {a} and {b} are the dividends and divisors, and s and t are the Bezout coefficients
    that allow us to ultimately find the modular inverse.  Most crucially, s' and t' are the s and t 
    values that the level below found; they are "incoming" answers the function uses while ascending 
    from the recursion.
    '''   
 
    # Base Case: remainder is 0 because a = 1 and b = 0
    if b == 0:        
        return a, 1, 0
    
    # At each recursive stage, the new value of {a} is assigned the old value of {b}, and 
    # the old value of {b} is assigned the old value of {a} (mod old {b})
    gcd, s_prime, t_prime = eea_recursive(b, a % b)
    
    # Before we can update s' and t', we need to know how many times our current {b} divided into {a}
    q = a // b
    
    # s' and t' are just the "old s" and "old t" from the level below, and we are now using them to 
    # build the "new S" and "new T"
    s = t_prime
    t = s_prime - (q * t_prime)
    
    return gcd, s, t

    '''
    Recursion is hard ... here is concrete example involving a trace for eea_recursive(26, 55)
    
    1. THE TOP CALL (Step 1): a = 26, b = 55
       * q = 26 // 55 = 0
       * This call waits for Step 2 (55, 26) to return.

    2. STEP 2: a = 55, b = 26
       * q = 55 // 26 = 2
       * This call waits for Step 3 (26, 3) to return.

    3. STEP 3: a = 26, b = 3
       * q = 26 // 3 = 8
       * This call waits for Step 4 (3, 2) to return.

    4. STEP 4: a = 3, b = 2
       * q = 3 // 2 = 1
       * This call waits for Step 5 (2, 1) to return.

    5. STEP 5: a = 2, b = 1
       * q = 2 // 1 = 2
       * This call waits for the BASE CASE (1, 0).

    6. THE BASE CASE (The Floor): a = 1, b = 0
       * Returns: gcd = 1, s = 1, t = 0.

    -------------------------------------------------------
    THE ASCENT (Calculating s and t as we go back up)
    -------------------------------------------------------

    7. BACK TO STEP 5 (a=2, b=1):
       * Catches: s_prime = 1, t_prime = 0.  (q was 2)
       * s = t_prime = 0
       * t = s_prime - (q * t_prime) = 1 - (2 * 0) = 1
       * Returns: (1, 0, 1)

    8. BACK TO STEP 4 (a=3, b=2):
       * Catches: s_prime = 0, t_prime = 1.  (q was 1)
       * s = t_prime = 1
       * t = s_prime - (q * t_prime) = 0 - (1 * 1) = -1
       * Returns: (1, 1, -1)

    9. BACK TO STEP 3 (a=26, b=3):
       * Catches: s_prime = 1, t_prime = -1. (q was 8)
       * s = t_prime = -1
       * t = s_prime - (q * t_prime) = 1 - (8 * -1) = 9
       * Returns: (1, -1, 9)

    10. BACK TO STEP 2 (a=55, b=26):
        * Catches: s_prime = -1, t_prime = 9.  (q was 2)
        * s = t_prime = 9
        * t = s_prime - (q * t_prime) = -1 - (2 * 9) = -19
        * Returns: (1, 9, -19)

    11. BACK TO THE TOP (a=26, b=55):
        * Catches: s_prime = 9, t_prime = -19. (q was 0)
        * s = t_prime = -19
        * t = s_prime - (q * t_prime) = 9 - (0 * -19) = 9
        * Returns: (1, -19, 9)

    FINAL RESULT:
    gcd = 1, s = -19, t = 9
    Equation: 1 = (26 * -19) + (55 * 9)
    -19 % 55 = 36
    '''

def mod_inverse(a, n):
    gcd, s, t = eea_recursive(a, n)
    
    if gcd != 1:
        print(f"Error: Operation impossible; modular inverse does not exist for {a} (mod {n})")
        return -1
    else:
        print(f"Solved for {a}(s) + {n}(t) ≡ 1 (mod {n}):")
        print(f"The inverse of {a} (mod {n}) is {s % n}")
        return s % n
    
def totient(modulus, p, q):
    
    # We assume {modulus} = {p} * {q}, with p and q distinct primes    
    totient = int(modulus*((1 - 1/p)*(1 - 1/q)))
    
    return totient

def export_keys(keyname):

    pass