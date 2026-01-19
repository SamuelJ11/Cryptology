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
                            
                
            




    
    