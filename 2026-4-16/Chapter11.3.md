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

    • We now define some variables and functions used in SHA-256.

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

    • We now begin our discussion of the SHA-256 process

        (1) SHA-256 begins by taking the original message and padding it with the bit 1 followed by a sequence of 0 bits, enough to make the new message 64 bits short of the next highest multiple of 512

        (2) Next, we append the 64-bit representation of the length 'T' of the message

            - for example, if the original message has 2800 bits, we add a 1 and 207 0s to obtain a new message of length 

                3008 = 6 x 512 - 64

            - since 2800 = 101011110000₂, we append 52 zeroes followed by 101011110000 to obtain a message length of 3072

        (3) Break the message with padding into 'N' blocks of length 512:

            M(¹) || M(²) || ... M(ⁿ) 

            - in the hash algorithm, each 512-bit block M(ⁱ) is divided into 32-bit blocks:

            M(ⁱ) = M₀(ⁱ) || M₁(ⁱ) || ... || M₁₅(ⁱ)

## The Algorithm

    1:  for i from 1 to N do
            ▷ This initializes the registers with the (i – 1)st intermediate hash value
    2:      a ← H₁⁽ⁱ⁻¹⁾
    3:      b ← H₂⁽ⁱ⁻¹⁾
    4:      c ← H₃⁽ⁱ⁻¹⁾
    5:      d ← H₄⁽ⁱ⁻¹⁾
    6:      e ← H₅⁽ⁱ⁻¹⁾
    7:      f ← H₆⁽ⁱ⁻¹⁾
    8:      g ← H₇⁽ⁱ⁻¹⁾
    9:      h ← H₈⁽ⁱ⁻¹⁾
    10:     for k from 0 to 15 do
    11:         Wₖ ← Mₖ⁽ⁱ⁾       ▷ This is where the message blocks are entered.
    12:     for j₁ from 16 to 63 do
    13:         Wⱼ₁ ← σ₁(Wⱼ₁₋₂) + Wⱼ₁₋₇ + σ₀(Wⱼ₁₋₁₅) + Wⱼ₁₋₁₆
    14:     for j from 0 to 63 do
    15:         T₁ ← h + Σ₁(e) + Ch(e, f, g) + Kⱼ + Wⱼ
    16:         T₂ ← Σ₀(a) + Maj(a, b, c)
    17:         h ← g
    18:         g ← f
    19:         f ← e
    20:         e ← d + T₁
    21:         d ← c
    22:         c ← b
    23:         b ← a
    24:         a ← T₁ + T₂
    25:     H₁⁽ⁱ⁾ ← a + H₁⁽ⁱ⁻¹⁾    ▷ These are the ith intermediate hash values
    26:     H₂⁽ⁱ⁾ ← b + H₂⁽ⁱ⁻¹⁾
    27:     H₃⁽ⁱ⁾ ← c + H₃⁽ⁱ⁻¹⁾
    28:     H₄⁽ⁱ⁾ ← d + H₄⁽ⁱ⁻¹⁾
    29:     H₅⁽ⁱ⁾ ← e + H₅⁽ⁱ⁻¹⁾
    30:     H₆⁽ⁱ⁾ ← f + H₆⁽ⁱ⁻¹⁾
    31:     H₇⁽ⁱ⁾ ← g + H₇⁽ⁱ⁻¹⁾
    32:     H₈⁽ⁱ⁾ ← h + H₈⁽ⁱ⁻¹⁾
    33: H(m) = H₁⁽ᴺ⁾ || H₂⁽ᴺ⁾ || H₃⁽ᴺ⁾ || H₄⁽ᴺ⁾ || H₅⁽ᴺ⁾ || H₆⁽ᴺ⁾ || H₇⁽ᴺ⁾ || H₈⁽ᴺ⁾
    34: return H(m)

    • An explanation of the algorithm is given below:

        - lines 2 - 9: the algorithm sets up 8 working "variables" or registers named a, b, c, d, e, f, g, h.  for the very first block (i = 1), these are loaded with the fixed IV constants H₁(⁰) through H₈(⁰).  subsequent blocks are loaded with the output of the previous block's hashing pass

        * note that 'N' in the for-loop condition is the number of 512-bit blocks

        - lines 10 - 11: the first 16 words (W₀ through W₁₅) are just copies of the raw message block split up:

            Wₖ = Mₖ⁽ⁱ⁾  for k = 0, 1, ..., 15

        - lines 12–13: The remaining 48 words (W₁₆ through W₆₃) are generated mathematically using a formula that mixes previous words together using σ₀ and σ₁

        * A 512-bit block only gives us sixteen 32-bit words
        * The inner loop (for j from 0 to 63) runs exactly 64 rounds for every single block (for every i from 1 to N)
        * For this reason, this phase expands those 16 words into 64 words for the for-loop starting on line 14

        - lines 14 - 16: This is begginning of the compression round; in every single round two temporary variables T₁ and T₂ are calculated using the current values of the registers, a round constant Kⱼ, and the current round's message word Wⱼ

        - lines 17 - 24: here the register values shift down like a conveyor belt:

            'h' becomes whatever 'g' was
            'g' becomes whatever 'f' was
            'f' becomes whatever 'e' was
            'e' becomes d + T₁ (injecting the scrambled data halfway through)
                    .
                    .
                    .
            'a' becomes T₁ + T₂ (injecting the newly scrambled data at the top)

            * by doing this 64 times, a single change to even one bit of the message completely randomizes the states of all 8 registers

        - lines 25 - 32: once the 64 rounds are finished, we have a heavily scrambled set of registers 'a' through 'h'. Now we take those register values and add them (mod 2³²) back to the values the block started with 

        - lines 33 - 34: After every single 512-bit block ('N' blocks total) has gone through this 4-phase lifecycle, the very last intermediate hash values are concatenated together side-by-side

            H(m) = H₁⁽ᴺ⁾ || H₂⁽ᴺ⁾ || H₃⁽ᴺ⁾ || H₄⁽ᴺ⁾ || H₅⁽ᴺ⁾ || H₆⁽ᴺ⁾ || H₇⁽ᴺ⁾ || H₈⁽ᴺ⁾