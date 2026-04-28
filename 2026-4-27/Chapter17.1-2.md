# 17.1 Secret Splitting

    • For the general case, we chooose an integer 'n' larger than all possible messages 'M' that might occur and regard 'M' and 'r' as nummbers (mod n):
    
        - then if we wish to split the secret message 'M' among 'm' people, then we must choose (m-1) random numbers r₁, r₂, ...,rₘ₋₁ (mod n) and give them to (m-1) of the people, and M = Σ k = 1, m-1; (rₖ)

# 17.2 Threshold Schemes

    • In the previous section, we showed how to split a secret message among 'm' people so that all 'm' were needed in order to reconstruct the secret.

        - in this section, we present methods that allow a subset of the people to reconstruct the secret

    • Let 't, w' be positive integers with t <= w:

        - a (t, w)-threshold scheme is a method of sharing a message 'M' among a set of 'w' participants such that any subset consisting of 't' participants can reconstruct the message 'M', but no subset of smaller size can reconstruct 'M'

    • There are two methods for constructing a (t, w) threshold scheme; the Shamir threshold scheme and the Blakely threshold scheme.

## Shamir Threshold Scheme

    • Also known as the Lagrange interpolation scheme, it is based upon some natural extension of the idea that two points are needed to determine a line, three poitns to determine a quadratic, and so on . . .

    • The scheme begins with choosing a prime 'p', which must be larger than all possible messages and also larger than the number 'w' of participants (this prime replaces the integer 'n' from section 17.1).

        - the message 'M' is represented as a number (mod p), and we want to split it among 'w' people in such a way that 't' of them are needed to reconstruct the message

        (1) randomly select (t-1) integers (mod p) and call them

            s₁, s₂, ..., sₜ₋₁

            then the polynomial s(x) = M + s₁(x) + s₂(x²) + ..., sₜ₋₁(xᵗ⁻¹) (mod p) is a polynomial such that s(0) = M (mod p)

        (2) for the 'w' participants, select distinct integers x₁, x₂, ..., x₍w₎ (mod p) 

            for example, 1, 2, ..., w is a reasonable choice for these values, so we give out the pairs

            (1, s(1)), (2, s(2)), ..., (w, s(w)), one to each person

            * at this stage, each person holds one point on the secret curve (xᵢ, s(xᵢ))
            * no one has the full function; the polynomial itself is still unknown to everyone; even if you know some points on the polynomial, there are many valid polynomials consistent with those points, and they produce different possible values of M, so M is mathematically undetermined
             
        (3) now suppose 't' people get together and share their pairs and want to recover the message 'M'; for simplicity of notation lets assume the pairs are (x₁, y₁), (x₂, y₂), ..., (xᵢ, yᵢ)

            suppose we have a polynomial s(x) of degree (t-1) that we would like to reconstruct from the points (x₁, y₁), (x₂, y₂), ..., (xᵢ, yᵢ) where yₖ = s(xₖ)

            this means that yₖ = M + s₁(xₖ) + s₂(xₖ²) + ..., sₜ₋₁(xₖᵗ⁻¹) (mod p) where 1 <= k <= t

            * pause here for an understanding check: this means that each person is giving the value of the hidden polynomial (yₖ) at thier corresponding x value (xₖ)

            * VERY IMPORTANT: s₁, s₂, ..., sₜ₋₁ are the hidden coefficients of the polynomial, chosen randomly by the dealer; each of the 't' participants must combine their shares (points) together and solve for the unique polynomial that fits all 't' points, which then reveals the coefficients—including the constant term s₀ = M (the secret message)

            if we denote s₀ = M, then we may rewrite this as

                +--                        --+  +-   -+    +-  -+
                | 1   x₁   x₁²  ...    x₁ᵗ⁻¹ |  | s₀  |    | y₁ |
                | 1   x₂   x₂²  ...    x₂ᵗ⁻¹ |  | s₁  |    | y₂ |
                | 1   x₃   x₃²  ...    x₃ᵗ⁻¹ |  | s₂  |    | y₃ |
                | .   .     .   .        .   |  |  .  |  ≡ |  . |  (mod p)
                | .   .     .     .      .   |  |  .  |    |  . |
                | .   .     .        .   .   |  |  .  |    |  . |
                | 1   xₜ    xₜ²   ...   xₜᵗ⁻¹  |  | sₜ₋₁ |    |  yₜ | 
                +--                        --+  +-   -+    +-  -+

                             (V)                  (s)        (Y)

            * pause here to check understanding:  lets look at just one equation, lets say for x₃:
  
                y₃ = s(x₃) = M + s₁(x₃) + s₂(x₃²) + ..., sₜ₋₁(x₃ᵗ⁻¹) (mod p)

                we can rewrite this as

                                                | s₀  |  
                                                | s₁  |  
                                                | s₂  |  
                    [1, x₃, x₃², ..., x₃ᵗ⁻¹]  * |  .  |  = y₃
                                                |  .  |  
                                                |  .  |  
                                                | sₜ₋₁ |

                each equation is just a dot product; by stacking all the equations together, we obtained the matrix above

        (4) the matrix we obtained, which we will call 'V', is called the Vandermonde matrix, and since the determinant is non-zero, there is a unique solution to this system of equations

            the determinant is calculated via 

                det V = ∏ 1 <= j < k <= t; (xₖ - xⱼ) 

            and as long as we have distint xₖ's, the system has a unique solution

            * pause here to check understanding: we have the system V . s = y (mod p), and the determinant of V is found by simply taking each pair of the previous x-values from the current one:
  
                (x₂ - x₁)
                (x₃ - x₁)
                (x₃ - x₂)
                    .
                    .
                    .

                so for example, if t = 3, then we have 

                    det V = (x₂ - x₁) * (x₃ - x₁) * (x₃ - x₂)

                crucially, note that the determinant is only ever zero if at at least ONE of these terms are ever zero, which would only happen if (xₖ - xⱼ) = 0, or in other words, 

                    xₖ = xⱼ for some k and j

                this is why we ensure that 'p' need to be prime; if this is the case, then no two xᵢ's will be congruent (mod p) and the above scenario is impossible

                since we ensured that the determinant is non-zero, we can solve the below equation

                    s = V⁻¹ * y

        (5) We now describe an alternative approach that leads to a formula for the reconstruction of the polynomial and hence for the secret message (we’re switching to a cleaner direct formula that avoids matrices entirely)

            our goal is to reconstruct a polynomial s(x) given that we know 't' of its values (xₖ - yₖ) 

            let lₖ(x) = ∏ i = 1 != k, t; (x - xᵢ) / (xₖ - xᵢ) (mod p)

                * this means multiply one factor for every i from 1 to t, except i = k
                          
            here we work with fractions (mod p), so therefore

                     +-
                     | 1 when k = j
            lₖ(xⱼ) ≡  
                     | 0 when k != j
                     +-

            * pause here to check understanding: we want a function such that at x = xₖ, we output 1, and at every other x = xⱼ, we output 0

                this function acts as a "switch" for the kth point

                lets work through a concrete example using t = k = 3:

                    * k = 3 means we are talking about the point (x₃, s(x₃))

                we have x₁ = 1, x₂ = 2, and x₃ = 3  (three x-values because t = 3)

                we build l₃(x) = x - x₁    x - x₂
                                 ------- * ------- = 
                                 x₃ - x₁   x₃ - x₂

                                 x - 1      x - 2
                                 ------- * ------- = 
                                 3 - 1      3 - 2

                                  x - 1    
                                 ------- * (x - 2)
                                    2    

                we can now check the "switch" behavior by confirming that at x = 3, this evaluates to 1, while at x = 1 and x = 2, this evaluates to 0

                * IMPORTANT!! we have shown that l₃(x) acts as a “selector” that is ON only at the third point and OFF everywhere else; essentially at x = xₖ, every factor becomes 1, and at x = xⱼ != xₖ, exactly ONE factor becomes 0, so the whole product becomes 0
                 
    • That entire process we just worked through is called Lagrange Interpolation, for which we can define the Lagrange Interpolation polynomial as 

        p(x) = Σ k = 1, t; (yₖlₖ(x))

        which satisifies the requirement that p(xⱼ) = yⱼ for 1 <= j <= t

        * recall that lₖ(x) is the kth Lagrange basis function, aka the "switch" component for a given input xₖ

        * for example, p(x₁) = y₁l₁(x₁) + y₂l₂(x₁) + ... ≡ y₁ (mod p)

    • We know from the previous approach with the Vandermonde matrix that we had

        y₃ = s(x₃) = M + s₁(x₃) + s₂(x₃²) + ..., sₜ₋₁(x₃ᵗ⁻¹) (mod p)

        we can generalize this as

            yⱼ = s(xⱼ) = M + s₁(xⱼ) + s₂(xⱼ²) + ..., sₜ₋₁(ⱼᵗ⁻¹) (mod p)

        concisely, we have

            s(xⱼ) = yⱼ for 1 <= j <= t

        similarly for the Lagrange Interpolation polynomial we have 
    
            p(xⱼ) = yⱼ for 1 <= j <= t

    • Since both s(x) (from the Vandermonde construction) and p(x) (from Lagrange interpolation) are polynomials of degree at most (t−1) that agree on 't' distinct points, they must be identical, therefore s(x) = p(x).

    • Now, to calculate the secret message 'M', all we have to do is calculate p(x) and evaluate it at x = 0.

## Blakley Threshold Scheme

    • Suppose there are serveral people and we want to arrange that any three can find the secret, but no two can;

        (1) choose a prime 'p' and let x₀ be the secret

        (2) choose y₀, z₀ randomly (mod p) so that we now have a point Q = (x₀, y₀, z₀) in three-dimensional space

            * x₀, y₀, z₀ are unknown to the participants

        (3) each person is given random values 'a' and 'b' such that c = z₀ - ax₀ - by₀

            * each person has a, b, c

        (4) Each person now has an equation of a plane passing through Q:

            z = ax + by + c

    • These three planes will intersect at a point, which must be 'Q'.

    • the three people who want to deduce teh secret can proceed as follows:

        (1) initially, they have three equations aᵢx + bᵢy - z ≡ -cᵢ (mod p)

        (2) these equations are rearranged into a matrix to obtain

            +--         --+   +-  -+     +-   -+
            | a₁  b₁  -1  |   | x₀ |     | -c₁ |
            | a₂  b₂  -1  | * | y₀ |  ≡  | -c₂ |
            | a₃  b₃  -1  |   | z₀ |     | -c₃ |
            +--         --+   +-  -+     +-   -+

            as long as the determinant of this matrix is nonzero (mod p), the matrix can be inverted (mod p) and the secret x₀ can be found

            * row operations would probabably be your best bet here