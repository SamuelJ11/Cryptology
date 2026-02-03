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

            (1) form a table with 3 columns.  In the first column, we run the normal Euclidean algorithm

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

## 3.3.1 Division

    • The general rule is that you can divide by a (mod n) when gcd(a, n) = 1 (in other words, when a and n are relatively prime)

    • The division modulo n is based on the concept of modular multiplicative inverse, which is defined below:

        - let a, n be a member of Z.  
        
        - an integer 's' is a multiplicative inverse (mod n) of 'a' iff as ≡ 1 (mod n)

        *essentially, s.a gives a remainder of 1 when divided by n, therefore 's' is the multiplicative inverse of a (mod n)

    • A number 'a' has a multiplicative inverse (mod n) iff gcd(a, n) = 1

    • A useful feature that follows from the above statement is shown below:

        - let a, b, c, n be integers with n ≠ 0 and with gcd(a, n) = 1

        - if a.b ≡ a.c (mod n), then b ≡ c (mod n) 

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
        - then a.s ≡ 1 (mod n), so s is the multiplicative inverse for a (mod n)

        *note that s is denoted a⁻¹

    • To tie it all together, lets revisit the results we obtained for s and t from the extended Euclidean algorithm:

        - gcd(56, 15) = 1 ≡ (-4).56 + 15.15   *where s = -4 and t = 15

        - now, we look at this equation through the "lens" of mod 56 (for example, we could also choose mod 15) 
        
        - in modular arithmetic, any multiple of the modulus becomes 0

            - since (-4).56 is a multiple of 56, it becomes 0 mod (56)    

        - so the equation transposes into:

            - 1 ≡ 0 + 15.15 (mod 56)  -->  1 ≡ 15.15 (mod 56)   

        - recall the definition of a multiplicative inverse:    
        
            - a.s ≡ 1 (mod n)    *s is the multiplicative inverse for a (mod n)

        - the equation we derived fits this model directly:

            - 1 ≡ 15.15 (mod 56)  -->  15.15 ≡ 1 (mod 56)  *here a = 15 and s = 15

            - therefore 15 is the multiplicative inverse for 15 (mod 56)

    • An important property of modular multiplicative inverses is that if 's' is a multiplicative inverse of a (mod n), then so is every integer s + k.n for any integer k

        - e.g., let k = 1, then 15 + 1.56 = 71

        - using a.s ≡ 1 (mod n), we already know that 15.15 ≡ 1 (mod 56), but now we also see that 15.71 ≡ 1 (mod 56), so 71 is also a multiplicative inverse for 1 (mod 56)

    • Summary of steps to solve modular arithmetic equations:

        - if we are tasked with finding a⁻¹ (mod n)

            (1) use the extended Euclidean algorithm for gcd(a, n) to find integers s and t such that a.s + n.t = 1

            (2) a⁻¹ ≡ s (mod n)

        - if we are solving ax ≡ c (mod n) when gcd(a, n) = 1

            (1) use the extended Euclidean algorithm to find integers s and t such that a.s + n.t = 1

            (2) x ≡ cs (mod n)  *if you must, replace the fraction c/a with c.s

        - if we need to solve a congruence of the form ax ≡ b (mod n) when gcd(a, n) = d > 1, the procedure is as follows:

            (1) if d does not divide b, there is no solution

            (2) Assume d|b, consider a new congruence of the form (a/d)x ≡ b/d (mod n/d)

                *since (a/d), (b/d) and (n/d) are integers and gcd (a/d, n/d) = 1, we can solve this congruence by the above procude to obtain the solutions:

                    x₀ + 1(n/d) + x₀ + 2(n/d) + . . .x₀ + (d-1)(n/d)

    • Examples:

        - given 7x ≡ 3 (mod 20), find a⁻¹ (mod 20)

            (1) 
                * here our numbers are 20 and 7

                +-------------------+-----------------+-------------------------------------------------+
                |     Euclidean     |    Rewrite      |                Build Solution                   |
                +-------------------+-----------------+-------------------------------------------------+
                |  20 = 7(2) + 6    | 20 - 7(2) = 6   |  7 - (20 - 7(2)) = 1  -->  (3).7 + (-1).20 = 1  |
                +-------------------+-----------------+-------------------------------------------------+
                |  7 = 6(1) + 1     | 7 - 6(1) = 1    |                  7 - [6] = 1                    |
                +-------------------+-----------------+-------------------------------------------------+
               
                *now we see that s = 3 and t = -1 
                *remember that s = a⁻¹ = 3

            (2)
                a⁻¹ = 3 mod (20)

        - using a⁻¹ found previously, solve 7x ≡ 3 (mod 20)

            (1) x = 3.3 (mod 20)  -->  x = 9 (mod 20)

        - solve 6x ≡ 12 (mod 15)

            (1) find gcd(15, 6)

                - this is 3, so let d = 3

            (2) find a new congruence of the form (a/d)x ≡ b/d (mod n/d)

                - 2x ≡ 4 (mod 5)

            (3) use the extended Euclidean algorithm to find integers s and t such that a.s + n.t = 1

                +-------------------+-----------------+-------------------------------------------------+
                |     Euclidean     |    Rewrite      |                Build Solution                   |
                +-------------------+-----------------+-------------------------------------------------+
                |  5 = (2)2 + 1     | 5 - 2(2) = 1    |              2(-2) + 5(1) = 1                   |
                +-------------------+-----------------+-------------------------------------------------+

                *therefore s = 3 and t = 1
                *we obtained s = 3 via the formula s + k.n obtaining -2 + 5(1) = 3 

            (4) solve for x:

                x = 4.3 (mod 5)  -->  x = 12 (mod 5)    

                * this solution can be simplified by modular reduction.
                * since 5 "fits" into 12 two times, we subtract (5.2) from 12, obtaining 12 - 10 = 2

                x = 2 (mod 5)   *this is only the fist of three solutions!

                * To find all d solutions, you take your first solution and keep adding the simplified modulus (5) until you have d (3) unique answers:

                x = 2 (mod 5)   *first solution
                x = 7 (mod 5)   *second solution
                x = 12 (mod 5)  *third solution

# 3.4 The Chinese Remainder Theorem

    • Recall that if x ≡ 25 (mod 42), we can rewrite it in standard arithmetic as x = 25 + 42k for some integer k.

        - rewriting 42 as 7.6, we obtain x = 25 + 7(6k)

        - this implies that x ≡ 4 (mod 7) and x ≡ 1 (mod 6)

    • Now we can break the original congruence (mod 42) into a system of congruences (mod factors of 42):

                              | x ≡ 4 (mod 7)
        x ≡ 25 (mod 42)  -->  |
                              | x ≡ 1 (mod 6)

    • The Chinese remainder theorem shows that this process can be reversed;

        - suppose gcd (m, n) = 1
        - given integers a and b, there exists exactly one solution x (mod m.n) to the simultaneous congruences

            x ≡ a (mod m),  x ≡ b (mod n)

    • Let's do an example where we solve x ≡ 3 (mod 7), x ≡ 5 (mod 15):

        (1) list the numbers that are congruent to b (mod n) until one of THOSE numbers is found to be congruent to a (mod m):

            5, 20, 35, 50, 65, 80 . . . 

                ↓ (mod 7) ↓

            5, 6, 0, 1, 2, 3 . . .

                * note that 80 ≡ 5 (mod 15) and 80 ≡ 3 (mod 7), so we have found 'c' from the general formula x ≡ c (mod n)

        (2) multiply m.n to find 'n' and form the orginal (combined) congruence 

            7 . 15 = 105

            x ≡ 80 (mod 105)

    • The above method works for small values of m and n, but is really inefficient for larger ones.  Luckily the CRT gives us a systematic way to do this:

        (1) use the Extended Euclidean algorithm to find 's' and 't' such that m.s + n.t = 1

        (2) let x ≡ b.m.s + a.n.t (mod m.n)
         
    • CRT lets you solve a hard congruence mod a composite number by solving easier congruences mod its coprime factors and then recombining the solutions.

    • For example, suppose we want to solve the congruence x² ≡ 1 (mod 35):

        (1) like before we set up a system of congruences:

                                 | x ≡ 1 (mod 7)
            x² ≡ 1 (mod 35) -->  |
                                 | x ≡ 1 (mod 5)    

        (2) notice that each congruence has two solutions:

            x ≡ ±1 (mod 7)

            x ≡ ±1 (mod 5)

            * hence we have four cases to consider:

                Case 1: x ≡ 1 (mod 5), x ≡ 1 (mod 7)

                    obvious solution: x ≡ 1 (mod 35)


                Case 2: x ≡ 1 (mod 5), x ≡ -1 ≡ 6 (mod 7)

                    numbers ≡ 1 (mod 5):  1, 6, 11, 16, 21 . . .
                    numbers ≡ 6 (mod 7):  6, 13, 20, 27, 35 . . .

                    pick 6: x ≡ 6 (mod 35)

                Case 3: x ≡ -1 ≡ 4 (mod 5), x ≡ 1 (mod 7)

                    numbers ≡ 4 (mod 5):  4, 9, 14, 19, 24, 29 . . .
                    numbers ≡ 1 (mod 7):  1, 8, 15, 22, 29 . . .

                    pick 29: x ≡ 29 (mod 35)

                Case 4: x ≡ -1 ≡ 4 (mod 5), x ≡ -1 ≡ 6 (mod 7)

                    numbers ≡ 4 (mod 5):  4, 9, 14, 19, 24, 29, 34 . . .
                    numbers ≡ 6 (mod 7):  6, 13, 20, 27, 34 . . .

                    pick 34: x ≡ 34 (mod 35)

        (3) thus we have 4 solutions:

            x ≡ 1 (mod 35)
            x ≡ 6 (mod 35)
            x ≡ 29 (mod 35)
            x ≡ 34 (mod 35)

    • In general, if 'n' in the formula x ≡ c (mod n) is the product of 'r' distinct primes, then x² ≡ 1 (mod n) has 2ʳ solutions.

# 3.5 Modular Exponentiation

    • Here will be concerning ourselves with numbers of the form xᵃ (mod n)

    • Suppose we want to compute 2¹²³⁴ (mod 789); if we first compute 2¹²³⁴, then reduce (mod 789), we'll be working with very large numbers even though the final answer has only 3 digits.

    • The strategy to solve this uses sucessive squaring (in this case of powers of 2):

        (1) start with 2¹ ≡ 2 (mod 789) and repeatedly square both sides until we reach the highest power of 2 that is less than or equal to your target exponent

            2² ≡ 4              (mod 789)
            2⁴ ≡ 4² ≡ 16        (mod 789)        
            2⁸ ≡ 16² ≡ 256      (mod 789)
            2¹⁶ ≡ 256² ≡ 49     (mod 789)
            2³² ≡ 49² ≡ 34      (mod 789)
            2⁶⁴ ≡ 34² ≡ 367     (mod 789)
            2¹²⁸ ≡ 367² ≡ 559   (mod 789)
            2²⁵⁶ ≡ 559² ≡ 37    (mod 789)
            2⁵¹² ≡ 37² ≡ 580    (mod 789)
            2¹⁰²⁴ ≡ 580² ≡ 286  (mod 789)

        (2) convert the original exponent (1234) to binary

            (1234)₁₀ = (10011010010)₂ = 1024 + 128 + 64 + 16 + 2

            *every '1' in the binary representation corresponds to the power of 2 that we will use in our final congruence

        (3) multiply together the modulo values of all powers of 2 corresponding to 1’s in the binary representation, reducing modulo 789 at each step.

            (10011010010)₂ = 1024 + 128 + 64 + 16 + 2

            2¹²³⁴ ≡ 286 . 559 . 367 . 49 . 4 ≡ 481 (mod 789) 

    • Notice this step required a total of 10 + 4 = 14 multiplications:

        - in general, if we want to compute aᵇ (mod n), this strategy requires no more than 2(log₂b) multiplications (mod n) 
        
        - additionally, we never have to work with numbers larger than n²  