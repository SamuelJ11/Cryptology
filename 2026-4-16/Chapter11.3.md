# 11.3 The Merkle-Damgård Construction

    • Until recently, most hash functions used a form of the Merkle-Damgård construction;

        - the main ingredient is a function 'f', usually called a compression function

        - 'f' takes two bitstrings as inputs, call them 'H' and 'M' and outputs a bitstring 

            H' = f(H, M)

        - 'M' could have length 512 and 'H' length 256, and H' would thus be 256

        - SHA 256 uses 'H' with size 256 bytes

    • We now describe the Merkle-Damgård process:

        (1) the message 'M' that is to be hashed is broken into 'n' blocks of length 512

            M₀ || M₁ || M₂ || ... || Mₙ₋₁

        (2) an initial value 'IV' is set, then the blocks are fed one by one into 'f' and the final output is the hash value

                    M₀        M₁        M₂        M₃                 Mₙ₋₁
                    │         │         │         │                   │
                    ▼         ▼         ▼         ▼                   ▼
            IV ──►  ┌─┐  ───► ┌─┐  ───► ┌─┐  ───► ┌─┐  ── - - - ───►  ┌─┐ ──► H(M)
                    │f│       │f│       │f│       │f│                 │f│
                    └─┘       └─┘       └─┘       └─┘                 └─┘

            * the blocks are read from the message one at a time and stirred into the mix with the previous blocks. The final result is the hash value

# 11.4 SHA-2

    • There are only a few hash functions that are used in practice. The most notable of these are the Secure Hash Algorithm (SHA) family, the Message Digest (MD) family, and the RIPEMD-160 message digest algorithm.

        - collisions have been found for MD5, and the strength of MD5 is now less certain

    • The Secure Hash Algorithm was developed by the National Security Agency (NSA) and given to the National Institute of Standards and Technology (NIST).

        - SHA-1 is now being replaced by a series of more secure versions called SHA-2; which still use the Merkle-Damgård construction

        - the SHA-2 family consists of six algorithms: SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256

    • We now begin our discussion of SHA-256.

        - SHA-256 produces a 256-bit hash and is built upon the same design principles as the Merkle-Damgård Construction, where the original message 'M' is broken into a set of fixed-size blocks

            M₀ || M₁ || M₂ || ... || Mₙ₋₁

        - the message blocks are then processed via a sequence of rounds that use a compression function h' that combines the current block and the result from the previous round:

            Xⱼ = h'(Xⱼ₋₁, Mⱼ)

        - the final Xₙ is the message digest

        - In the description of the hash algorithm, we need the following binary operations

          * ∧ is bitwise 'and'
          * ∨ is bitwise 'or'
          * ¬ is bitwise 'not'
          * + is bitwise addition
          * Rⁿ(X) is the rotation of X to the right by 'n' positions (the end wraps around to the beginning)
          * Sⁿ(X) is the shift of X to the right by 'n' positions (this is a logical right shift, not arithmetic)

        - we also define the following functions that operate on 32-bit strings:

          * Ch(X, Y, Z)  = (X ∧ Y) ⊕ (¬X ∧ Z)
          * Maj(X, Y, Z) = (X ∧ Y) ⊕ (X ∧ Z) ⊕ (Y ∧ Z)
          * Σ₀(X)        = R²(X) ⊕ R¹³(X) ⊕ R²²(X)
          * Σ₁(X)        = R⁶(X) ⊕ R¹¹(X) ⊕ R²⁵(X)
          * σ₀(X)        = R⁷(X) ⊕ R¹⁸(X) ⊕ S³(X)
          * σ₁(X)        = R¹⁷(X) ⊕ R¹⁹(X) ⊕ S¹⁰(X)

        - these are carefully chosen bit-scrambling functions 

        - now we choose the initial hash values

            H₁(⁰) = 6A09E667    H₂(⁰) = BB67AE85    H₃(⁰) = 3C6EF372    H₄(⁰) = A54FF53A
            H₅(⁰) = 510E527F    H₆(⁰) = 9B05688C    H₇(⁰) = 1F83D9AB    H₈(⁰) = 5BE0CD19

        * SHA-256 internally maintains 8 working 32-bit words H₁, H₂, ..., H₈, each is 32 bits (8 x 32 = 256)
        * the (⁰) designates the round number, so H₂(⁰) means the initial value of state word H₂ (before any processing)
        * these initial hash values are obtained by using the first eight digits of the fractional parts of the square roots of the first eight primes, expressed in hexadecimal

        - we also need sixty-four 32-bit words

            K₀  = 428A2F98,     K₁  = 71374491,    …,     K₆₃ = C67178f2

        - these are the first eight hexadecimal digits of the fractional parts of the cube roots of the first 64 primes

## Padding and Preprocessing

    • 