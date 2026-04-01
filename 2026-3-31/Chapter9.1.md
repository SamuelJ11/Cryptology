# 9.1 The RSA Algorithm

    • This is the first public key crypto system we will discuss, which solves the key exchange problem.

    • The algorithm works by first having Bob choose two large primes 'p' and 'q' such that n = pq.

    • Bob then chooses an exponent 'e' such that gcd(e, ϕ(n)) = 1.

        - this is equivalent to saying gcd(e, (p-1)(q-1)) = 1
  
    • Bob's public key is thus (n, e), and the values of 'p' and 'q' are kept private.

    • When Alice recieves Bob's public key, Alice encrypts her message to Bob via:

        c = mᵉ (mod n)

    • When bob recieves Alice's encrypted message, he needs to compute the value of 'd' in the equation below:

        m = cᵈ (mod n)

        (1) the idea is that we want decryption to undo encryption, that means we want
  
            cᵈ ≡ (mᵉ)ᵈ ≡ m (mod n)

        - or equivalently

            mᵉᵈ ≡ m (mod n)

        (2) recall Euler's Theorem, which states that if gcd(m, n) = 1, then
  
            mᶲ⁽ⁿ⁾ ≡ 1 (mod n)

            * where ϕ(n) = (p-1)(q-1)
  
        - since we want mᵉᵈ ≡ m (mod n), we can simplify by mutliplying both sides the inverse of 'm' (mod n) to obtain

            mᵉᵈ⁻¹ ≡ 1 (mod n)

        (3) from (1) and (2), we use the fact since mᵉᵈ ≡ m (mod n) and mᵉᵈ⁻¹ ≡ 1 (mod n), then necessarily 

            ed ≡ 1 (mod ϕ(n))

            * remember from chapter 3: "if you want to work (mod n), you should work (mod ϕ(n)) in the exponent" '
            * this effectively proves that ed-1 ≡ 0 (mod ϕ(n)), or equivalently ed ≡ 1 (mod ϕ(n))

    • To tie this all together, lets work through a small exmaple:

        (1) working with small values of 'p', 'q' and a relatively large value of e, suppose that we are given

            p = 11
            q = 7
            e = 17

        (2) we compute n = pq = 77, therefore

            ϕ(n) = (p-1)(q-1) = 60

        (3) we can encrypt a small message using the public key (n, e) via c = mᵉ (mod n); lets encyrpt the letter 'm' 

            m = 13  *using the same letter encoding scheme we've been working with

            c = mᵉ (mod n) ≡ 13¹⁷ (mod 77)

            * reference HW3 problem 3 part 2 to understand the reduction steps below:

            use the modular exponentiation algorithm (successive squaring) until we reach 17 or the powers of 13 repeat

            13¹ ≡ 13 (mod 77)
            13² ≡ 15 (mod 77)
            13⁴ ≡ 71 (mod 77)
            13⁸ ≡ 36 (mod 77)
            13¹⁶ ≡ 64 (mod 77)
            13¹⁷ ≡ 62 (mod 77)

            thus the ciphertext c = 13¹⁷ was simplified to 62 (mod 77)

        (4) now we can solve for 'd' from the equation m = cᵈ (mod n)

            we set out to solve m = 62ᵈ (mod n)

            to do this, we need to find the value of 'd' such that mᵉᵈ ≡ m (mod n)

            earlier we found that this is equivalent to 'd' satisfying ed ≡ 1 (mod ϕ(n))

            * IMPORTANT: here we know that ϕ(n) = 60 because we know the values of 'p' and 'q'
            * if 'n' were a large number and we did not know 'p' and 'q', it would be computationally infeasible to compute ϕ(n) and thus 'd'
            * the security in RSA rests in the previous fact; hence the importance of keeping 'p' and 'q' private
  
            now we have ed ≡ 1 (mod 60), which we can rewrite to solve for 'd' as d ≡ e⁻¹ (mod 60)

            we solve d ≡ e⁻¹ (mod 60) using the Extended Euclidean Algorithm to find integers 's' and 't' such that s(60) + t(17) = 1

            +-------------------------+-----------------------+-----------------------------------+
            |     Euclidean           |    Rewrite            |         Build Solution            |         
            +-------------------------+-----------------------+-----------------------------------+
            |   60 = 17(3) + 9        |     60 - 17(3) = 9    |       (2)(60) + (-7)17 = 1        |
            +-------------------------+-----------------------+-----------------------------------+
            |   17 = 9(1) + 8         |      17 - 9 = 8       |        (2)[9] - (1)17 = 1         |
            +-------------------------+-----------------------+-----------------------------------+
            |   9 = 8(1) + 1          |      9 - 8 = 1        |           9 - [8] = 1             |
            +-------------------------+-----------------------+-----------------------------------+ 

            * here we see that s = 2 and t = -7

            we verify that 17(-7) ≡ 1 (mod 60), indeed it is

            therefore d = -7 ≡ 53 (mod 60)

        (5) finally, we decrypt the message

            we set out to solve m = cᵈ (mod n), where n = 77 (from step 2), c = 62 (from step 3) and d = 53 (from step 4)  

            thus we have m = 62⁵³ (mod 77), which again we follow the procedure from HW3 to reduce (mod 77)

            * steps a & b are already done, so we go to the final step
  
            (c) use the modular exponentiation algorithm (successive squaring) until we reach 62 or the powers of 62 repeat

            62¹ ≡ 62 (mod 77)
            62² ≡ 71 (mod 77)
            62⁴ ≡ 36 (mod 77)
            62⁸ ≡ 64 (mod 77)
            62¹⁶ ≡ 15 (mod 77)
            62³² ≡ 71 (mod 77)
            
            here we see that powers of 62 repeat every 30, we can reduce the exponent (mod 30):

            53 ≡ 23 (mod 30)

            23 = 16 + 4 + 2 + 1;

            62¹⁶ * 62⁴ = 62²⁰ = 15 * 36 ≡ 1 (mod 77)

            62²⁰ * 62² = 62²² = 1 * 71 ≡ 71 (mod 77)

            62²² * 62¹ = 62²³ = 71 * 62 ≡ 13 (mod 77)

            since 13 corresponds to 'm', we have successfully decrypted the message!