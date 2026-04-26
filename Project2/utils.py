import string, sys, random, math
from pathlib import Path

MAXRAND = 10 ** 100 - 1
MINRAND = 10 ** 99
STREAMLENGTH = 20 # deprecated

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
    This function generates a pseudorandom binary sequence using the
    recurrence:

        xᵢ = (xᵢ₋₁)² (mod n)

    where n = p * q, with p and q are distinct large primes satisfying:
    
        p ≡ q ≡ 3 (mod 4)

    The initial seed x₀ is chosen uniformly at random such that
    gcd(x₀, n) = 1, and is then squared once to ensure it lies in
    the quadratic residue subgroup (mod n), or more informally referred
    to as the "Blum Group" of n

    Each output bit is derived from the least significant bit of xᵢ.

    Important note:   
    Although cryptographically secure, BBS is computationally slow and is
    not used in modern production systems, where faster CSPRNGs are preferred. 
    This implementation is included purely for the amusement of the curious
    programmer, but is not used within this program.    
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
    if (last_digit % 2 == 0 and number != 2):   
        return False 
    
    '''
    Some of the below tests have been commented out because they are too aggressive; the goal is to 
    show how some composite numbers pass Fermat's primality test with Fermat-liar bases, but go on
    to correctly get flagged as composite by the Miller-Rabin test
    '''
    
    if (num_digits > 1 or number == 9):      
        
        # Test for divisibility by 5 for multi-digit numbers
        if (last_digit % 5 == 0): 
            return False              
        '''
        # Calculate the sum of the digits of a number
        sum_of_digits = 0      
        for i in range(0, num_digits):
            sum_of_digits += (number // pow(10, i)) % 10
            
        # Check if a multi-digit number's sum of digits is divisible by 3 or 9
        if (sum_of_digits % 3 == 0 or sum_of_digits % 9 == 0):
            print(f"Failed a trivial composite test; {number} is divisible by 3 or 9\n")   
            return False
        
        alternating_digitsum = 0        
        for i in range(0, num_digits):
            alternating_digitsum +=  ((number // pow(10, i)) % 10) * pow(-1, i)
            
        # Check if the alternating sum of digits is divisible by 11    
        if (alternating_digitsum % 11 == 0):
            print(f"Failed a trivial composite test; {number} is divisible by 11\n")     
            return False
        '''
           
        # Check if {number} is a perfect square
        root = math.isqrt(number)
        if (root ** 2 == number):
            return False
            
    return True

def modular_exponentiation(base, exponent, modulus):
    '''
    This function uses successive squaring of powers of {base} and the binary representation of {exponent} to compute 
    the modular exponentiation equivalent to Python's pow(base, exponent, modulus) function.
    '''
    
    # Precompute powers of base corresponding to powers of 2 and store them in a 
    # list as base^(1), base^(2), base^(4), base^(8), ... (all mod modulus)    
    mod_reductions = []    
    
    # We start with {base} mod {modulus} and sucessively square the base until the 
    # current exponent exceeds the the final exponent 
    current_val = base % modulus 

    current_exp = 1    
    while (current_exp <= exponent):
        mod_reductions.insert(0, current_val)
        current_val = (current_val ** 2) % modulus
        
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
    a strong pseudo-prime.
    '''
   
    alpha = random.randint(2, modulus - 2)
    
    # First apply a basic preliminary primality check  
    if (not candidate_prime(modulus)):
        return False            
    else:
        fermatexp = modulus - 1  

        # Ensure alpha is coprime to {modulus}      
        gcd = gcd_recursive(alpha, modulus)
        
        # Fermat's little theorem check: pow(a, n-1, n) ≡ 1 for a prime modulus n
        # If gcd != 1, or the congruence !≡ -1, then {modulus} is definitely composite 
        if (gcd != 1 or modular_exponentiation(alpha, fermatexp, modulus) != 1):
            return False
        else:
            # Passed Fermat test for this base (does not guarantee primality)
            # print(f"Passed Fermat test with\n   modulus = {modulus}\n   base = {alpha}")
            pass
            # Proceed to the stronger probabilistic Miller-Rabin test 
            # print("Proceeding to Miller-Rabin test . . .")

    # For the Miller-Rabin test, write {modulus - 1} as 2^k * q where q is odd   
    millerexp = modulus - 1
    k = 0
    while(millerexp % 2 == 0):
        k += 1
        millerexp //= 2

    value = modular_exponentiation(alpha, millerexp, modulus)

    # Check for value ≡ 1 or -1 before entering the loop
    if value == 1 or value == modulus - 1:
        # print(f"Passed Miller-Rabin test; {modulus} is probably prime\n")
        return True     
    
    # Repeatedly square to check if value ≡ -1    
    i = 1
    while(i < k):
        
        # Update the value and loop condition for the next iteration
        value = modular_exponentiation(value, 2, modulus)
        i += 1 
        
        # Declare {modulus} prime and return immediately if value ≡ -1
        if value == modulus - 1:
            # print(f"Passed Miller-Rabin test; {modulus} is probably prime\n")
            return True

        # If we reach 1 prematurely, {modulus} is definitely composite
        if value == 1:
            # print(f"Failed Miller-Rabin test; {modulus} is definitely composite\n")
            return False
        
    print(f"Failed Miller-Rabin test; {modulus} is definitely composite\n")
    return False

def gcd_recursive(number, modulus):
    '''
    This function recursively computes the GCD of {number} and {modulus} by repeatedly replacing the larger number 
    with the remainder of its division by the smaller number until the remainder is zero.
    '''
    
    # If {modulus} is zero, it means {number} divided the previous number perfectly, and since every number 
    # divides zero, the greatest number that divides both {number} and zero is simply {number}.
    if modulus == 0:
        return number
    else:        
        # Replace the dividend with the divisor, the divisor with the remainder, and recursivley call 
        # the function with these updated parameters until the base case is reached
        return gcd_recursive(modulus, number % modulus)
        
def eea_recursive(number, modulus):
    '''
    This function servers as a helper for mod_recursive(); it recursively computes the modular 
    inverse of a (mod b). At every step, we are trying to solve the equation GCD = (a * s) + (b * t), 
    where a and b are the dividends and divisors, and s and t are the Bezout coefficients
    that allow us to ultimately find the modular inverse.  Most crucially, s' and t' are the s and t 
    values that the level below found; they are "incoming" answers the function uses while ascending 
    from the recursion.
    '''   
 
    # Base Case: remainder is 0 because {number} = 1 and {modulus} = 0
    if modulus == 0:        
        return number, 1, 0
    
    # At each recursive stage, the new value of {number} is assigned the old value of {modulus}, and 
    # the old value of {modulus} is assigned the old value of {number} (mod old {modulus})
    gcd, s_prime, t_prime = eea_recursive(modulus, number % modulus)
    
    # Before we can update s' and t', we need to know how many times our current {modulus} divided into {number}
    q = number // modulus
    
    # s' and t' are just the "old s" and "old t" from the level below, and we are now using them to 
    # build the "new S" and "new T"
    s = t_prime
    t = s_prime - (q * t_prime)
    
    return gcd, s, t

def mod_inverse(number, modulus):
    '''
    This is an interface function for the eea_recursive() function. It simply returns the
    relevant part of that function's output (the Bezout coefficient of {a} reduced (mod n)).
    '''
    
    gcd, s, t = eea_recursive(number, modulus)
    
    if gcd != 1:
        print(f"Error: Operation impossible; modular inverse does not exist for {number} (mod {modulus})")
        sys.exit()
    else:
        return s % modulus
    
def totient(p, q):
    '''
    This function computes the amount of integers coprime to {modulus} using Euler's Product Formula
    '''
    
    # We assume modulus = {p} * {q}, with p and q distinct primes    
    totient = (p - 1) * (q - 1)
    return totient

def read_file():
    '''
    This function validates the file path for the message and ensures it exists in the current directory
    '''
    
    ## Import and read filename for analysis
    filename = str(sys.argv[1])
    cwd = Path().resolve() 
    filepath = cwd.joinpath(filename) 

    ## Check if the path for the provided filename exists in the current directory
    if filepath.exists() == False:
        print(f"{filename} could not be found in the current working directory")
        sys.exit()
    
    message = int(filepath.read_text())
    return message

def write_file(filename, file):
    '''
    This function writes {file} to a file named {filename}.txt
    '''
    
    with open(str(filename), "w") as f:
        f.write(str(file))