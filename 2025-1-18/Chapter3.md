# 3.1 Basic Notions

    • N = the set of all natural numbers
    • Z = the set of all integers
    • Q = the set of all rational numbers
    • Zₙ = the set of all natural numbers less than n

## 3.1.1 Divisibility

    • We say that a divides b if there is an integer k such that b = ak, denoted a|b

    • The following properties of divisibility are useful:

        (1) for every a ≠ 0, a|0 and a|0.  Also, 1|b for every b
        (2) if a|b and b|c, then a|c
        (3) if a|b, and a|c, then a|(sb + tc) for all integers s and t

## 3.1.2 Prime Numbers

    • A number p > 1 is prime if the only positive integers dividing p are 1 and p.

        - numbers that aren't prime are called composite

    • Let π(x) be the number of primes less than x:

        - then π(x) = x / ln(x)

        - also the number of n-digit primes can be estimated via π(10ⁿ) - π(10ⁿ⁻¹) = 10ⁿ/ln(10ⁿ) - 10ⁿ⁻¹/ln(10ⁿ⁻¹)

    • The fundamental theorem of arithmetic tells us that every positive integer greater than 1 is a product of primes, and this factorization into primes is unique, up to reordering the factors

    • There is an important property of primes:

        - Lemma: if p is a prime and p divides a product of integers ab, then either p|a or p|b (or more generally p must divide one of the factors)

## 3.1.3 Greatest Common Divisor

    • The greatest common divisor of a and b is denoted gcd(a, b)

    • We say that a and b are relatively prime if gcd(a, b) = 1

    • There are two standard ways of finding the gcd:

        (1) factor a and b into primes and for each prime number, look at the powers that it appears in the factorizations of a and b (take the smaller of the two), and finally put these prime powers together to get the gcd

            - example:

                576 = 2⁶3²
                135 = 3³5

                gcd(576, 135) = 3² = 9

        (2) if a and b are large numbers, it might not be feasible to factor them, so we use the Euclidean algorithm shown below:

            * assume a is greater than b
            
            1. divide a by b and represent a in the form a = q₁b + r₁

            * if r₁ = 0, then b|a and the gcd is b

            2. if r₁ ≠ 0, then continue by representing b in the form b = q₂r₁ + r₂

            3. continue until the remainder is zero, giving the following sequence of steps:

                a = q₁b + r₁
                b = q₂r₁ + r₂
                r₁ = q₃r₂ + r₃
                .   .   .
                .   .   .
                .   .   .
                rₖ₋₁ = qₖ₊₁rₖ

                example: consider gcd(415, 35)

                a = 11(35) + 30     *r₁ = 30
                b = q₂(30) + r₂     *here q₂ = 1 and r₂ = 5
                30 = q₃(5) + r₃    *here q₃ = 6 and r₃ = 0
               
                *once the remainder is zero, the last nonzero remainder is the gcd

                gcd(415, 35) = 5

# 3.2 The Extended Euclidean Algorithm

    • Recall Bezout's theorem that claimed that gcd(a, b) can be expressed as a linear combination of a and b; there exists integers s and t such that gcd(a, b) = as + bt

        - example:  gcd(45, 13) = 45 . (-2) + 13 . 7 = 1

    • The Extended Euclidean Algorithm will tell us how to find x and y, using gcd (56, 15) as an example

        - the process looks something like this:

            (1) form a table with 2 rows and 3 columns.  In the first column, we run the normal Euclidean algorithm

                +-------------------+-----------------+----------------+
                |     Euclidean     |    Rewrite      | Build Solution |
                +-------------------+-----------------+----------------+
                |  56 = 15(3) + 11  |                 |                |
                +-------------------+-----------------+----------------+
                |  15 = 11(1) + 4   |                 |                |
                +-------------------+-----------------+----------------+
                |  11 = 4(2) + 3    |                 |                |
                +-------------------+-----------------+----------------+
                |  4 = 3(1) + 1     |                 |                |
                +-------------------+-----------------+----------------+

            (2) in the second column, we simply rewrite the equations from the Euclidean Algorithm, replacing (=) with (-) and replacing (+) with (=)

                +-------------------+-----------------+----------------+
                |     Euclidean     |    Rewrite      | Build Solution |
                +-------------------+-----------------+----------------+
                |  56 = 15(3) + 11  | 56 - 15(3) = 11 |                |
                +-------------------+-----------------+----------------+
                |  15 = 11(1) + 4   | 15 - 11(1) = 4  |                |
                +-------------------+-----------------+----------------+
                |  11 = 4(2) + 3    | 11 - 4(2) = 3   |                |
                +-------------------+-----------------+----------------+
                |  4 = 3(1) + 1     | 4 - 3(1) = 1    |                |
                +-------------------+-----------------+----------------+

            (3) finally, working backwards from the last row upwards, we build the solution

                * treat numbers that are NOT in parenthesis as variables (e.g., (2)11 + (3)11 = (5)11, NOT 55)
                * using this logic, we rewrite the second number on the LHS of the equation (in square brackets) in the corresponding row of the second column as a linear combination of the numbers on the LHS from the column above it:

                +-------------------+-----------------+---------------------------------------------------------------------------------------+
                |     Euclidean     |    Rewrite      |    Build Solution                                                                     |
                +-------------------+-----------------+---------------------------------------------------------------------------------------+
                |  56 = 15(3) + 11  | 56 - 15(3) = 11 | (3)15 - (4)(56 - (3)15) = 1  -->  (3)15 + (12)15 - (4)56 = 1  -->  (15)15 - (4)56 = 1 |
                +-------------------+-----------------+---------------------------------------------------------------------------------------+
                |  15 = 11(1) + 4   | 15 - 11(1) = 4  | 3(15 - 11) - 11 = 1  -->  (3)15 - (3)11 - 11 = 1  -->  (3)15 - (4)[11] = 1            |                  
                +-------------------+-----------------+---------------------------------------------------------------------------------------+
                |  11 = 4(2) + 3    | 11 - 4(2) = 3   | 4 - (11 - 4(2)) = 1  -->  4 - 11 + 4(2) = 1  -->  3[4] - 11 = 1                       |
                +-------------------+-----------------+---------------------------------------------------------------------------------------+
                |  4 = 3(1) + 1     | 4 - 3(1) = 1    |                             4 - [3] = 1                                               |
                +-------------------+-----------------+---------------------------------------------------------------------------------------+

                * the last step shows us that s = -4 and t = 15, giving 1 = 56(-4) + 15(15)     

# 3.3 Congruences

    • One of the most basic and useful notions in number theory is modular arithmetic, or congruences

    • Let a, b, n be integers with n ≠ 0

        - we say that a ≡ b (mod n) iff n(a-b)    "a is congruent to b mod n if a - b is a multiple of n"

        - example: 

            32 ≡ 7 (mod 5) because (32 - 7) is divisible by 5

            17 ≡ 17 (mod 13) because (17 - 17) is divisible by 13 (or any number)

    • Another way to view congruence is two numbers that are congruent mod n yield the same remainders when divided by n

    • Some useful properties of congruence are shown below:

        (1) a ≡ 0 (mod n) iff n|a
        (2) a ≡ a (mod n)
        (3) a ≡ b (mod n) iff b ≡ a (mod n)
        (4) if a ≡ b and b ≡ c (mod n), then a ≡ c (mod n)   

    • example:

        solve x + 7 ≡ 3 (mod 17)     "When x + 7 is divided by 17, the remainder is 3"

        (1) isolate x: x ≡ −4 (mod 17)

        (2) convert negative number to a positive equivalent modulo 17: 

            - here we must think of a number between 0 and 16 that has the same remainder as -4 when divided by 17

                - add 17 until we get a nice positive number: -4 + 17 = 13
            
            - since -4 ≡ 13 (mod 17), we obtain the final solution x ≡ 13 (mod 17)

# 3.3.1 Division

    • The general rule is that you can divide by a (mod n) when gcd(a, n) = 1 (in other words, when a and n are relatively prime)

    • The division modulo n is based on the concept of modular multiplicative inverse, which is defined below:

        - let a, n be a member of Z.  
        
        - an integer s is a multiplicative inverse modulo n of a iff as ≡ 1 (mod n)

        *essentially, (s)a gives a remainder of 1 when divided by n, therefore s is the modular inverse of a (mod n)

    • A number a has a modular inverse mod n if and only if gcd(a, n) = 1

    • A useful feature that follows from the above statement is shown below:

        - let a, b, c, n be integers with n ≠ 0 and with gcd(a, n) = 1

        - if ab ≡ ac (mod n), then b ≡ c (mod n) 

    • For example, lets solve 2x + 7 ≡ 3 (mod 17):

        (1) 2x ≡ -4 (mod 17)       *we notice gcd(2, 17) = 1, so 2 has an inverse mod 17 and we can divide both sides of the congruence by 2
        (2) x ≡ -2 (mod 17)
        (3) x ≡ 15 (mod 17)
   
    • Another slightly harder example, lets solve 5x + 6 ≡ 13 (mod 11)

        (1) 5x ≡ 7 (mod 11)         *again, gcd(5, 11) = 1, so 5 has an inverse mod 11.  
                                    *however, we notice that since 5 does not divide 7, we can use a congruence trick to perform the same steps as before
                                    *since 7 ≡ 18 ≡ 29 ≡ 40 ≡ . . . (mod 11), we can simply replace 7 with 40 since 5 now divides 40
        (2) 5x ≡ 40 (mod 11)
        (3) x ≡ 8 (mod 11)

    • The below propostion is a rephrasing of the definition of modular multiplicative inverses:  

        - suppose gcd(a, n) = 1 
        - let s and t be integers such that as + nt = 1 (where s and t are found from the extended Euclidean algorithm)
        - then as ≡ 1 (mod n), so s is the multiplicative inverse for a (mod n)

        *note that s is denoted a⁻¹


                            
                
            




    
    