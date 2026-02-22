# 5.0 Stream Ciphers

    • The problem with stream ciphers is that they provide secrecy (hiding the content), but they don't provide integrity (proving the content hasn't been messed with).

    • Suppose Eve knows where the word “good” occurs in a plaintext that has been encrypted with a stream cipher; she doesn't know the Keystream, but she knows (or guesses) that the message contains the word "good."

    • Eve wants to change "good" to "evil". To do this, she calculates the "difference" between the two words by XORing them together:

        - Let "good" = 1011
        - Let "evil" = 0011
        - Let the key = 1100 (only the sender and reciever know this)

        - the sender XORs the plaintext with the keystream to create the ciphertext:

            good ⊕ key = 0111 (this is what Eve intercepts)

        - Eve knows the original message is 1011 ("good") and wants it to be 0011 ("evil"), so she XORs them together to find the difference (bit-flipping mask)

            good ⊕ evil = 1000

    • Now Eve takes the ciphertext she intercepted and XORs it with her swap mask, sending the result to the reciever

        -  good ⊕ swap = 1111 (modified ciphertext)

    • The receiver then decrypts the unknowingly modified ciphertext (1111) with the key via"

        - 1111 ⊕ key = 0011 ("evil")

# 5.1 Pseudorandom Bit Generation

    • The one-time pad and many other cryptographic applications require sequences of random bits.

        - most computers have a method for generating random numbers that is readily available to the user (e.g., the rand() function in C)

    • The rand() function and many other pseudorandom number generators are based on linear congruential generators. 
    
        - a linear congruential generator produces a sequence of numbers x₁, x₂ . . . where

            xₙ = axₙ₋₁ + b (mod m)

        - here x₀ is the initial seed, while a, b and m are the parameters that govern the relationship

        - the sequence of the last bits of xₙ’s is then taken as the generated sequence of 0s and 1s

            e.g., consider m = 13, a = 2, b = 5 and x₀ = 6; then we generate the sequence:

                6, 4, 0, 5, 2, 9, 10, 12, 1 . . .

                with the corresponding sequence of bits:

                0, 0, 0, 1, 0, 1, 0, 0, 1, . . .

    • The use of pseudorandom number generators based on linear congruential generators is suitable for experimental purposes, but is highly discouraged for cryptographic purposes

    • The first reliable method of pseudorandom bit generation uses one-way functions

        - a one-way function f(x) is a mathematical parocess that is easy to "go forward" aka put in 'x' and get 'y', but computationally infeasible to "go backward" aka obtain 'x' from a given 'y'

    • Suppose that we have such a one-way function 'f' and a random seed 's', and we define xⱼ = f(s + j) for some counter j = 1, 2, 3, . . .

        * by adding j, we ensure that the input to the function is different every single time 

    • If we let bⱼ be the least significant bit of xⱼ, then the sequence b₀, b₁ . . . will be a pseudorandom sequence of bits

    • Another method of generating random bits is to use an intractable problem from number theory.

        - one of the most popular cryptographically secure pseudorandom number generators is the Blum-Blum-Shub (BBS) pseudorandom bit generator

    • First we define "quadratic residues":

        Let 'n' be a positive integer. An integer 'a' is called a quadratic residue (mod n) if there exists an integer 'x' such that  x² ≡ a (mod n) 

        - for example, lets consider all numbers (mod 7):

            {0, 1, 2, 3, 4, 5, 6, 7}

        - the results obtained from squaring each of those numbers and reducing (mod 7) are the quadratic residues (mod 7):

            0² ≡ 0 (mod n) 
            1² ≡ 1 (mod n) 
            2² ≡ 4 (mod n) 
            3² ≡ 2 (mod n) 
            4² ≡ 2 (mod n) 
            5² ≡ 4 (mod n) 
            6² ≡ 1 (mod n) 

            thus the quadratic residues (mod 7) are {0, 1, 2, 4}

    • In the BBS, we define:

        - n = p.q

        - the Blum group: Bₙ = {x ∈ Zₙ∗ | x is a quadratic residue (mod p AND q)}

            Zₙ∗ = integers coprime to 'n'

            * in other words, x ∈ Bₙ if there exist integers a, b such that x ≡ a² (mod p) AND x ≡ b² (mod q)

        - the generator xⱼ₊₁ = (xⱼ)² (mod n)

    • The sequence only works nicely if every xⱼ is coprime to 'n' and is a quadratic residue (mod p) and (mod q) (aka xⱼ is in the Blum group Bₙ)

        - for example, lets pick small primes for intuition:

            p = 7, p = 11 (both are congruent to 3 (mod 4))

        - quadratic residues (mod 7): {0, 1, 2, 4}

        - quadratic residues (mod 11): {0, 1, 3, 4, 5, 9}

        - a number x is in the Blum group B₇₇ if x (mod 7) ∈ {1, 2, 4} and x (mod 11) ∈ {1, 3, 4, 5, 9}

            * note that 0 is excluded from both sets since numbers ∈ Zₙ∗ must be coprime to n, and 0 is only coprime to 1 and -1

        - the SIZE of the Blum group is given by (p - 1)(q - 1) / 4

            * here the size of B₇₇ is 15, so there are 15 numbers in this Blum group

    • In general, if we start the BBS generator with x₀ ∈ Bₙ, then xⱼ₊₁ = (xⱼ)² (mod n) will always remain inside Bₙ

    • BBS needs the squaring function f(x) = x² (mod n) to behave like a permutation on the Blum group

        - for reasons that are outside my comprehension, this only happens when n = pq with p ≡ q ≡ 3 (mod 4)

        - when this condition is met, each number in Bₙ has exactly ONE square root in Bₙ

    • To see an example of the last point, lets consider B₇₇ which is {1, 4, 9, 15, 16, 23, 25, 36, 37, 53, 58, 60, 64, 67, 71}

        - compute x² (mod 77) for each element:

                x       x² (mod 77)
            =======================
                1           1
                4           16
                9           4
                15          71
                16          25
                25          9
                36          64
                37          60
                53          37
                58          53
                60          58
                64          15
                67          23
                71          36

            - notice since n = pq with p ≡ q ≡ 3 (mod 4), every number in B₇₇ maps a different unique number in B₇₇, thus fullfilling the requirements of Blum-Blum-Shub
            
    • Now we can look at a concrete example using a Blum-Blum-Shub generator for B₇₇:

        - suppose we start with x = 9, then the initial seed is x₀ = x² (mod 77) = 4
        
        - thus the values for x₁, x₂ . . . are:
            
            16, 25, 9, 4, 16, . . .

        - taking the least significant bit of x₀, x₁, x₂ . . . is easily done by checking whether the number is odd or even, produces the sequence:

            0, 0, 1, 1, 0, 0, . . .

# 5.2 Linear Feedback Shift Register Sequences         

    • In this section, all congruences are (mod 2)

    • Consider a linear recurrence relation of length 'm'

    ​   xₘ₊ₙ = c₀xₙ + c₁xₙ₊₁ + c₂xₙ₊₂ + . . . cₘ₋₁xₙ₊ₘ₋₁ (mod 2), where

        - xₘ₊ₙ = the next bit we are trying to calculate

        - m = "memory" aka how many previous bits the system looks back at to decide what the next one will be

        - c₀, c₁ . . . = the switches which are coefficients of either 0 or 1; if 1, that previous bit is switched on; if 0 it's ignored

    • Adding up all the "switched on" bits, if the total is odd, the next bit is 1, if even, the next bit is 0

        - the resulting sequence of 0s and 1s can be used as a key for encryption

    • For example, the sequence below can modelled by a linear recurrence relation:

        0100001001011001111100011011 . . . 

        can be modelled by xₙ₊₅ = xₙ + xₙ₊₂

    • The pattern's length is determined by 'm'; a sequence of length 'm' can create a pattern that doesn't repeat for up to 2ᵐ - 1 terms

    • If you increase the memory to m = 31, you only need 62 bits of information (31 for the seed + 31 for the rule), which can produce more than two billion bits of key!

        - this method can be implemented very easily in hardware using what is known as a linear feedback shift register   

    • Unfortunately, the preceding encryption method succumbs easily to a known plaintext attack.

        - by adding or subtracting the plaintext from the ciphertext (mod 2) we obtain bits of the key

    • For example, suppose we know that the initial segment of the key is given by:

        011010111100 which is part of the larger sequence:

        0110101111000100110101111 . . .
                       | <- starts repeating here (period 15)

        - first we must determine the length of the recurrence before we can find the coefficients

    • To find the length of the sequence, we start by assuming length 2, and supposing the recurrence is:

        xₙ₊₂ = c₀xₙ + c₁xₙ₊₁

        let n = 1, n = 2 be starting points for calculating x₃ and x₄, respectively

        x₁ = 0, x₂ = 1, x₃ = 1, x₄ = 0

    • Now we form a series of 'm' = 2 equations:

        x₃ = 1 ≡ c₀(0) + c₁(1)   (n = 1)
        x₄ = 0 ≡ c₀(1) + c₁(1)   (n = 2)

        - in matrix form, this is:

        |0 1| * |c₀| = |1|  
        |1 1|   |c₁|   |0|  

        * honestly easier to set up an augmented matrix and use row reduction to solve for c₀, c₁

        - solving we obtain c₀ = c₁ = 1, making the recurrence:

            xₙ₊₂ = xₙ + xₙ₊₁

        - unfortunately our assumption is incorrect since x₆ ≠ x₄ + x₅

    • Now we try a length of 'm' = 3:

        xₙ₊₃ = c₀xₙ + c₁xₙ₊₁ + c₂xₙ₊₂

        with the observed values x₁ = 0, x₂ = 1, x₃ = 1, x₄ = 0, x₅ = 1, x₆ = 0

        again, let n = 1, n = 2 and n = 3 be starting points for calculating x₄, x₅, x₆

        x₄ = 0 ≡ c₀(0) + c₁(1) + c₂(1) (n = 1)
        x₅ = 1 ≡ c₀(1) + c₁(1) + c₂(0) (n = 2)
        x₆ = 0 = c₀(1) + c₁(0) + c₂(1) (n = 3)

        - converting to matrix we obtain:

        |0 1 1|   |c₀|   |0|
        |1 1 0| * |c₁| = |1|
        |1 0 1|   |c₂|   |0|

        - since every column in the matrix sums to 0 (mod 2), the determinant is 0 (mod 2) and thus the matrix is not invertible
        
        - this means the matrix cannot be inverted to solve for the coefficients, meaning the equation has no UNIQUE solution

    • Eventually we end up trying 'm' = 4, and correctly arrive at the linear recurrence defined by xₙ₊₄ = xₙ + xₙ₊₁

        - verify this: 2⁴ - 1 = 15, which indeed matches the period we found earlier

    • If several consecutive values of 'm' yield 0 determinants stop; the last 'm' to yield a non-zero determinant is probably the length of the recurrence 

    • We conclude this discussion with the following theorem:

        - let x₁, x₂, . . . be the sequence of bits produced by a linear recurrence relation (mod 2) 
        
        - let 'm' be the length of a shortest such equation. Then det(Mₘ) ≡ 1 (mod 2), and det(Mₙ) ≡ 0 (mod 2) for every n > m                                                   