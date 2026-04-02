# 9.2 Attacks on RSA 

## 9.2.1 Low Exponent Attacks

    • Suppose Bob wants to be able to decrypt messages quickly, so he chooses a small value of 'd'.

        * the most common practice is choose the value of 'd' first, then find 'e' with de ≡ 1 (mod ϕ(n))
  
    • Then following theorem of M. Wiener shows that often Eve can find 'd' easily:

        (1) suppose p, q are primes with q < p < 2q. 

        (2) let n = pq and let 1 <= d, e < ϕ(n)

        (3) let de ≡ 1 (mod ϕ(n))

        if d < (1/3)n⁰·²⁵, then 'd' can be calculated quickly in (log₂n)ᵏ time

    • To see how the attack works, first we seek to understand the theoretical underpinnings:

        - the goal of this attack is to show that the public fraction (e/n) is almost exactly the same as the secret fraction (k/d)
  
        - if they are close enough, we can use the convergents of the continued fractions to guess (k/d)

        - we know that de ≡ 1 (mod ϕ(n)), and this can rewritten as a simple algebraic equation:

            ed = k*ϕ(n) + 1     * where 'k' is just some integer

        (1) isolate (k/d) by dividing both sides of the above equation by d * ϕ(n)

            ed/dϕ(n) = kϕ(n)/dϕ(n) + 1/dϕ(n)

            simplifying we obtain

            e/ϕ(n) = k/d + 1/dϕ(n)

            * the attacker knows 'e' and 'n', but not ϕ(n) 
            * if the attacker wants to use a continued fraction to find the secret k/d, they need to observe the difference between e/n and k/d

        (2) write out the subtraction of the two fractions and find a common denominator so we can combine them

            e/n - k/d = ed/nd - kn/nd

            combining we obtain

            e/n - k/d = (ed - kn)/nd

            * recall from earlier that we claimed ed = k*ϕ(n) + 1

        (3) substitute ed for  k*ϕ(n) + 1

            e/n - k/d = ((kϕ(n) + 1) - kn) / nd = kϕ(n) - kn + 1 / nd

            * by substituting, we eliminatd the variable 'e' in the numerator since it's a massive, awkward number. 
            * we replaced it with something related to the factors of 'n'
  
            now we look at the numerator and notice that two of the terms have a 'k' in them:

            e/n - k/d = k(ϕ(n) - n) + 1 / nd

            we have isolated ϕ(n) - n, which is important because n and ϕ(n) are almost the same size, so subtracting one from the other results in a much smaller number
            
        (4) here we use the fact that ϕ(n) = (p - 1)(q - 1) and further reduce the expression

            ϕ(n) = pq - p - q + 1

            notice that pq is exactly equal to n?

            ϕ(n) = n - p - q + 1 

            referring back to step 3 where we had e/n - k/d = k[(ϕ(n) - n)] + 1 / nd, we can now substitute for ϕ(n) for the term in [brackets]

            ϕ(n) - n = (n - p - q + 1) - n = -p - q + 1

            finally, we take this result and plug it back into the fraction we obtained from step 3:

            e/n - k/d = k(-p - q + 1) + 1 / nd

        (5) conceptual check

            think about the scales of these numbers:
            
            in a modern RSA key, 'n' is a number with roughly 600 digits

            'p' and 'q' are numbers with roughly 300 digits

            'p' and 'p' are microscopic compared to 'n', and when looking at 

                e/n - k/d = k(-p - q + 1) + 1 / nd

            we see the difference is "only" about 300 digits long, while the denominator (nd) is well over 600 digits long

            this proves mathematically that
            
                e/n - k/d ≈ 0

            in other words, the distance between the fraction we know (e/n) and the secret fraction (k/d) is incredibly tiny

    • To see why a small value of 'd' is relevant to this attack, we seek a basic understanding of Legendre's Theorem:

        * reference cont-fracs.md to brush up on continued fractions as it is needed to understand the discussion below

        - Legendre proved that if the difference between a number 'x' (typically expressed as a rational number) and a fraction (y/z) is less than (1/2z²):
  
            abs(x - y/z) < 1/2z²

        -  then that fraction (y/z) must be one of the convergents of x 
  
        * Wiener did the heavy lifting to find exact point at which d becomes too small

            d < (1/3)n⁰·²⁵
  
        - so for Eve's low exponent attack to work, we need 
  
            abs(e/n - k/d) < 1/2d²
  
        - from this we see that if 'd' is small, for example d = 11, then the target window is 1/242, which is relatively large

        - if 'd' is large (like 2048 bits large), then 1/2d² becomes an impossibly tiny number

        - therefore, while increasing 'd' does bring the secret fraction k/d closer to the public e/n, it simultaneously makes the mathematical 'requirement' for k/d to be a convergent of e/n much stricter
  
    • Now we can work through the textbook example to drive this home:

        (1) setup

            let n = 1966981193543797

            let e = 323815174542919

            the continued fraction of e/n is thus

            [0; 6, 13, 2, 3, 1, 3, 1, 9, 1, 36, 5, 2, 1, 6, 1, 43, 13, 1, 10, 11, 2, 1, 9, 5]

            * this continued fractions was obtained by repeatedly dividing the old denominator by the new remainder
  
        (2) use the list of integers (continued fraction) to build the convergents

            recall that de ≡ 1 (mod ϕ(n)), which can be can rewritten as ed = k*ϕ(n) + 1

            * since ϕ(n) is even, k(ϕ(n)) + 1 is "one more than an even number", so this means 'ed' is odd
  
            * if 'ed' is odd, then both 'e' and 'd' must be odd, allowing us to discard even values of 'd'

            if we let 'Cₜ' be the "candidate totient", we can solve ed = k*ϕ(n) + 1 for such a value via

                Cₜ = (ed - 1)/k

            (1) test the first convergent (C₁) in the canditate totient formula

                * note the C₀ = a₀ = 0

                C₁ = a₀ + 1/a₁ = 0 + 1/6 = 1/6, 
                
                * 6 is even so we discard this choice

            (2) test the second convergent (C₂) in the canditate totient formula

                C₂ = a₀ + 1/(a₁ + 1/a₂) = 0 + 1/(6 + 1/13) = 1/(79/13) = 13/79

                * substituting (k, d) for (13, 79) in the formula we obtain (e(79) - 1) / 13 which is not an integer, so this cannot be ϕ(n) and we discard this choice
  
            (3) test the third convergent (C₃) in the canditate totient formula

                C₃ = a₀ + 1/(a₁ + 1/(a₂ + 1/a₃)) = 0 + 1/(6 + 1/(13 + 1/2)) = 1/(6 + 1/(27/2)) = 1/(6 + 2/27) = 1/(164/27) = 27/164

                * 6 is even so we discard this choice
  
            .
            .
            .

            (7) continuing this process we finally settle on the seventh convergent C₇ = 578/3511

                substituting (k, d) for (578, 3511) in the formula we obtain (e(578) - 1) / 3511, which is in fact an integer

                this gives Cₜ = 1966981103495136 as the canditate for ϕ(n)

        (3) find the roots of X² - X(n - Cₜ + 1) + n to test the value of ϕ(n) using the Quadratic Formula

            * note the above polynomial is possibly X² - X(n - ϕ(n) + 1) + n
            * recall that ϕ(n) = n - p - q + 1:

            (1) X² - X(n - (n - p - q + 1) + 1) + n

            (2) X² - X(n - n + p + q - 1 + 1) + n

            (3) X² - X(p + q) + n

            since n = pq:

            (4) X² - X(p + q) + pq      
            
            (5) X² - Xp - Xq + pq

            (6) (X - p)(X - q)

                * if the 'k' and 'd' we found are correct, this quadratic equation will spit out two integers when solved using the Quadratic Formula

            (7) using the values from the textbook example, since 

                n = 1966981193543797 and Cₜ = 1966981103495136

                we can calculate the sum term (p + q) in step 4, which is the coefficient for 'X'

                p + q = n - ϕ(n) + 1 = (1966981193543797 - 1966981103495136 + 1) = 90048662

                now we set up our polynomial for the Quadratic Formula:

                X² - (90048662)X + 1966981193543797 = 0

            (8) use the Quadratic Formula on the polynomial above

                X = [(90048662) ± sqrt((90048662)² - 4(1)(1966981193543797))] / 2(1)

                solving for both roots r₁ and r₂ we obtain

                r₁ = 3751722031
                r₂ = 524287

        (4) verify Cₜ by multiplying r₁ and r₂ to obtain 'n'

            * we verify that r₁ * r₂ = n, thus Eve has successfully factored the modulus using a Low Exponent Attack

## 9.2.2 Short Plaintext

    •