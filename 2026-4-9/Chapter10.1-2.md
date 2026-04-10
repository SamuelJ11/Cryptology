# 10.1 Discrete Logarithms

    • In the RSA algorithm, we saw how the difficulty of factoring yields useful cryptosystems. There is another number theory problem, namely discrete logarithms, that has similar applications.

    • For a prime 'p' and non-zero integers α and β, we have an equation:

        β ≡ αˣ (mod p)

        - the problem of finding 'x' is called the discrete log problem
  
    • Moreover, if 'n' is the smallest integer such that:

        αⁿ ≡ 1 (mod p)

        * often α is a primitive root (mod p), therefore every β is a power of α (mod p)

        we may assume 0 <= x < n, and then we denote

        x = 𝓛ₐ(β)

        as the "discrete log of β with respect to α

    • Discrete log behaves in many ways like the usual logarithm; for example, if α is a primitive root (mod p):

        - 𝓛ₐ(β₁β₂) = 𝓛ₐ(β₁) + 𝓛ₐ(β₂) = x₁ + x₂ (mod p - 1)
  
        * the multiplicative group (mod p) has size p - 1 by Fermat's Theorem
    
# 10.2 Computing Discrete Logs

    • First, take α to be a primitive root (mod p), so (p-1) is the smallest positive exponent 'n' such that:

        αⁿ ≡ 1 (mod p)

    • This implies that αⁿ ≡ αᵐ (mod p), and since α is a primitive root mod p, it has order (p-1):

        - this means exponents exponents are taken modulo the group order:

            n ≡ m (mod p-1)

    • We assume that β ≡ αˣ (mod p), and we want to find 'x'; first we will show that its easy to determine if 'x' is even or odd without actually knowing what 'x' is:
        
        * an important fact here that will help you understand the following steps is that since α to be a primitive root (mod p), we know that αᵖ⁻¹ ≡ 1 (mod p)
        * this basically says that the smallest positive exponent that gives us 1 is (p-1)

        - since we know that αᵖ⁻¹ ≡ 1 (mod p), we know that the halfway point obtained by raising α to (p-1)/2 must give a square root of 1.

        - however, the only numbers that equal 1 when squared are 1 and -1, and we know from earlier that (p-1) is the smallest positive exponent that gives us 1, since (p-1)/2 is smaller than (p-1), it must be -1

        * we have shown that if we let r = (p-1)/2, then αʳ ≡ -1 (mod p)

        - since we are trying to solve β ≡ αˣ and we don't know 'x', we can test it by raising our known β to the halfway power:

            βʳ ≡ (αˣ)ʳ ≡ αˣʳ

        - we know that αʳ ≡ -1 (mod p), essentially we have βʳ ≡ (-1)ˣ

        - if we calculate βʳ and obtain 1, 'x' must be even, else 'x' is odd

## 10.2.1 The Pohlig-Hellman Algorithm

    • The proceeding idea was extended by Pohlig and Hellman to give an algorithm to compute discrete logs when (p-1) has only small prime factors.

        - instead of just checking if 'x' is even or odd, we are going to break 'x' down into much smaller pieces based on the factors of p-1
  
    • Before we begin, lets establish what we already know and what we are trying to to do:

        - we are trying to solve β ≡ αˣ (mod p)
        
        - the goal is to find the secret value 'x' 

    • To find 'x' piece-by-piece, we write it out as a product of sums based on the prime factors of (p-1), which we denote as 'q':

        x = x₀ + x₁q + x₂q² + ... for 0 <= xᵢ <= q-1

        * a helpful analogy to understand why we are doing this is to imagine we are writing a number in base-10; then if x = 345, we could write this as 5 + 4(10¹) + 3(10²)
        * in our case, we are using the prime factor 'q' as the "base"
        * each x₀, x₁, x₂ is a "digit" of the number x when written in base 'q'

    • Now, we perform a specific "test" operation on our original equation β ≡ αˣ (mod p):

        - let r = (p-1)/q

        - we raise both sides of the equation to the power of 'r', which gives βʳ ≡ αˣʳ (mod p):

        * here the LHS gives us a value we can observe, and the RHS is simply αˣʳ
  
        - now we replace 'x' in the exponent with the "sum version" of x, so the exponent of α is now 

            r * (x₀ + x₁q + x₂q² + ...) 

        - distributing 'r' to every term in the parentheses, we obtain

            x₀(r) + x₁(q)(r) + x₂(q²)(r) + ...

        * notice the second term is really x₁(q)(p-1)/q, and since the 'q's cancel we are left with x₁(p-1)
        * similarly for the third term we have x₂(q)(p-1) and so on . . .
        * the key observation here is every term after x₀ now has (p-1) as a factor in its exponent
  
    • To recap the previous steps, we started with β ≡ αˣ (mod p), and we replaced 'x' with x₀(p-1)/q + x₁(p-1) + x₂(q)(p-1) + ...:

        - recall that when you have a sum in the exponent, it’s the same as multiplying the bases:
  
        β ≡ α^(x₀(p-1)/q) + α^(x₁(p-1)) + α^(x₂(q)(p-1)) (mod p) ...

        * crucially, we observe that since αᵖ⁻¹ ≡ 1 (mod p), then the second term (α^p-1)^(x₁) is really just (1)ˣ¹
        * similary for the third term we have (α^p-1)^(x₂q), which again is just (1)ˣ², and so on . . .
        * because all the subsequent terms after α^(x₀r) turn into 1, effectively vanishing from the multiplication
         
        - after all the cancellation, we are left with βʳ ≡ α^(x₀r) (mod p)

        - recall that since earlier we let r = (p-1)/q, and we know the values of β, α, p, and q, the only thing we don't know is x₀

        - because x₀ must be a number between 0 and (q-1) (and 'q' is a small prime), we can just try every possible value for x₀ until we find a solution

    • Now that we have found the first digit 'x₀', we set out to find x₁, x₂, ...:

        * to find x₁, we modify our original equation (β ≡ αˣ (mod p))
        * we know that x = x₀ + x₁q + x₂q² + ...

        - since we just found the value of x₀, we can define a new value, let's call it β₁, where we "divide out" the α^(x₀) part:
  
        β₁ ≡ β * α^(-x₀) = α^(x₀ + x₁q + x₂q² + ... -x₀) = α^( x₁q + x₂q² + ...) (mod p)

    • Starting with β₁ = α^(x₁q + x₂q² + ...) (mod p), we perform a new "test" on β₁:

        * let s = (p-1)/q²
        * to make everything except x₁ vanish, we raise β₁ to the power of 's'
  
        - now we have (β₁)ˢ = α^(x₁q + x₂q² + ...)ˢ

        - just like before, we distribute the multiplier s = (p-1)/q² to every term in the sum:
  
            for the x₁ term: (x₁q)*(p-1)/q² = x₁(p-1)/q 

            for the x₂ term: (x₂q²)*(p-1)/q² = x₂(p-1) 

            for the x₃ term: (x₃q³)*(p-1)/q² = x₃(q)(p-1)

            .
            .
            .

        * we observe that for all higher terms (x₂, x₃, ...) each one will be some multiple of (p-1)
        * again we observe that since αᵖ⁻¹ ≡ 1 (mod p), then the third term α^x₂(p-1) is really just (1)ˣ², α^x₃(q)(p-1) = (1)ˣ³, and so on . . .

        - thus we are we left with (β₁)ˢ = α^(x₁(p-1)/q) (mod p)

        - again, we test all values of 'k' such that (β₁)ˢ ≡ α^(k*(p-1)/q), and let x₁ = k
        
    • The key idea here is that once we find all x₀, x₁, x₂ ..., for a specific prime factor 'q' of (p-1) (as in x = x₀ + x₁q + x₂q² + ...), then we have found the value of x (mod qʳ)

        - here 'r' is the multiplicity (or power) of that 'q' in the factorization of (p-1)

        - for example, if r = 1, then we once we find x₀ we stop; if r = 3, we must find x₀, x₁ and x₂, etc.

        - once we have found x₀, x₁, x₂ ... xᵣ₋₁ for a prime factor 'q', we plug them back into the sum:

            A = x₀ + x₁q + x₂q² + ... xᵣ₋₁qʳ⁻¹

        - now we have x ≡ A (mod qʳ)

    • We repeat this entire process for every distinct prime factor (q₁, q₂, ...) of (p-1), so that we have:

        x ≡ A (mod q₁ʳ)

        x ≡ B (mod q₂ˢ)

        .
        .
        .

        * where 'r' and 's' are the multiplicities of the prime factors (q₁, q₂, ...) of (p-1), respectively

    • The final step is to apply the CRT to each of the above congruences, and find the unique number 'x' that solves all of them.

## 10.2.2 Baby Step, Giant Step

    • Compared to Pohlig-Hellman, where we broke the exponent into prime "digits," here we are just breaking the exponent into two manageable chunks: a quotient and a remainder:

        (1) first, pick a number 'N' such that N = ceiling(sqrt(p-1))

            - we assume that in the equation β ≡ αˣ (mod p), 'x' can be written as 

                x = j + N(k)

                * as we will see shortly, 'j' is the "baby step", or the small remainder, and N(k) is the "giant step"
                * by setting N = ceiling(sqrt(p-1)), we are ensuring that both 'j' and 'k' are relatively small to 'N'
               
        (2) now we take our target equation β ≡ αˣ (mod p) and plug in our split version of 'x':

            β ≡ α^(j + N(k)) (mod p)

        (3) to find a match, we use algebra to put the baby part 'j' on one side and the giant part 'N(k)' on the other:

            αʲ ≡ β(α⁻ᴺᵏ) (mod p)

        (4) now we for every possible 'j' (0, 1, 2, ... N - 1), we store the value of αʲ in a list (call it 'A')

        (5) similarly, for every possible 'k' (0, 1, 2, ... N - 1), we store the value of β(α⁻ᴺᵏ) in a seperate list (call it 'B')

        (6) the goal is to find a value that appears in both of these lists:

            - this means that some value from list A (αʲ) = some value from list B (β(α⁻ᴺᵏ))

            - rearranging this equation by multiplying both sides of αʲ ≡ β(α⁻ᴺᵏ) by (αᴺᵏ), we again obtain β ≡ α^(j + N(k)) (mod p)

            - and just like that, the secret x is revealed as x = j + N(k)