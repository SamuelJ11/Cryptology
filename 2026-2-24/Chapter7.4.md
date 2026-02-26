# 7.4: DES

    • The previous discussion involved a simplified version of DES that used a 12-bit block size and 9-bit key, but here we are working the actual 64-bit block size and 56-bit key for DES.

        - note that we are still assuming the plaintext is just one block (64 bits)

    • DES divides the 64-bit key into 8 groups of 8 bits:
    
        [7 key bits + 1 parity bit]
        [7 key bits + 1 parity bit]
        [7 key bits + 1 parity bit]
        ...
        (total 8 groups)

        - so the 56-bit key is expanded to 64 bits, with the 8 parity bits there to make sure each group has an odd number of 1s

    • The algorithm starts with a plaintext 'm' of 64 bits and consists of four main stages:

        STAGE 1 (PREPROCESSING): DERIVE L₀R₀ and the 56-bit key 

        (1) the bits of 'm' are permuted by a fixed initial permutation (IP) to obtain m₀ = IP(m)

            - the initial permutation table is as follows:

            58 50 42 34 26 18 10 2 60 52 44 36 28 20 12 4 
            62 54 46 38 30 22 14 6 64 56 48 40 32 24 16 8
            57 49 41 33 25 17 9  1 59 51 43 35 27 19 11 3
            61 53 45 37 29 21 13 5 63 55 47 39 31 23 15 7

            - this means that the 58th bit of m becomes the first bit of m₀, etc

        - write m₀ as L₀R₀, where L₀ = first 32 bits, R₀ = last 32 bits

        (2) removing the parity bits (bits 8, 16, 24, 32, 40, 48, 56, 64) from the 64-bit key 'K' and permute the bits based on the key permutation table:

            57 49 41 33 25 17  9 1  58 50 42 34 26 18
            10 2  59 51 43 35 27 19 11 3  60 52 44 36
            63 55 47 39 31 23 15 7  62 54 46 38 30 22
            14 6  61 53 45 37 29 21 13 5  28 20 12 4

            - this means that the 57th bit of the original 'K' is now the first, etc

            - write the 56-bit result as C₀D₀ (28 bits each)

            * IMPORTANT CLARIFICATION: C₀D₀ is created ONCE in this stage because it serves as the "seed" for all the round keys that follow in stage 2

        STAGE 2: THE KEY SCHEDULE AND FEISTEL FUNCTION 

        for 1 <= i <= 16 {

            Lᵢ = Rᵢ₋₁
            Rᵢ = Lᵢ₋₁ ⊕ f(Rᵢ₋₁, Kᵢ)

            * here we describe how to obtain the 48-bit Kᵢ starting with the 64-bit 'K':

            (1) derive the round key Kᵢ
            
                - start with the preprocessed 56-bit key C₀D₀

                - let Cᵢ = LSᵢ(Cᵢ₋₁) and Dᵢ = LSᵢ(Dᵢ₋₁), where LSᵢ means left shift the input one or two places to the left, according to the table below

                Round (i): 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
                Shift:     1 1 2 2 2 2 2 2 1 2  2  2  2  2  2  2

                - of this 56-bit string CᵢDᵢ, 48 bits are chosen according to the table below:

                14 17 11 24 1  5  3  28 15 6  21 10
                23 19 12 4  26 8  16 7  27 20 13 2
                41 52 31 37 47 55 30 40 51 45 33 48

                - this means that the 14th bit of the original CᵢDᵢ becomes the first, etc

                - the output is Kᵢ (48-bit string obtained from the key 'K')
                
           (2) define the feistel function f(Rᵢ₋₁, Kᵢ)

                - first, the 32-bit 'R' is expanded to the 48-bit E(R) by the expansion perumutation table:

                    32 1  2  3  4  5  4  5  6  7  8  9
                    8  9  10 11 12 13 12 13 14 15 16 17
                    16 17 18 19 20 21 20 21 22 23 24 25
                    24 25 26 27 28 29 28 29 30 31 32 1

                    - this means that the first bit of E(R) is the 32nd bit of 'R', etc

                - compute E(R) ⊕ Kᵢ, and write it as 8 six-bit blocks B₁, B₂, . . . B₈

                    - take note of the eight S-boxes below:

                    S-box 1
                    14 4 13 1 2 15 11 8 3 10 6 12 5 9 0 7
                    0 15 7 4 14 2 13 1 10 6 12 11 9 5 3 8
                    4 1 14 8 13 6 2 11 15 12 9 7 3 10 5 0
                    15 12 8 2 4 9 1 7 5 11 3 14 10 0 6 13

                    S-box 2
                    15 1 8 14 6 11 3 4 9 7 2 13 12 0 5 10
                    3 13 4 7 15 2 8 14 12 0 1 10 6 9 11 5
                    0 14 7 11 10 4 13 1 5 8 12 6 9 3 2 15
                    13 8 10 1 3 15 4 2 11 6 7 12 0 5 14 9

                    S-box 3
                    10 0 9 14 6 3 15 5 1 13 12 7 11 4 2 8
                    13 7 0 9 3 4 6 10 2 8 5 14 12 11 15 1
                    13 6 4 9 8 15 3 0 11 1 2 12 5 10 14 7
                    1 10 13 0 6 9 8 7 4 15 14 3 11 5 2 12

                    S-box 4
                    7 13 14 3 0 6 9 10 1 2 8 5 11 12 4 15
                    13 8 11 5 6 15 0 3 4 7 2 12 1 10 14 9
                    10 6 9 0 12 11 7 13 15 1 3 14 5 2 8 4
                    3 15 0 6 10 1 13 8 9 4 5 11 12 7 2 14

                    S-box 5
                    2 12 4 1 7 10 11 6 8 5 3 15 13 0 14 9
                    14 11 2 12 4 7 13 1 5 0 15 10 3 9 6 8
                    4 2 1 11 10 13 7 8 15 9 12 5 6 3 0 14
                    11 8 12 7 1 14 2 13 6 15 0 9 10 4 5 3

                    S-box 6
                    12 1 10 15 9 2 6 8 0 13 3 4 14 7 5 11
                    10 15 4 2 7 12 9 5 6 1 13 14 0 11 3 8
                    9 14 15 5 2 8 12 3 7 0 4 10 1 13 11 6
                    4 3 2 12 9 5 15 10 11 14 1 7 6 0 8 13

                    S-box 7
                    4 11 2 14 15 0 8 13 3 12 9 7 5 10 6 1
                    13 0 11 7 4 9 1 10 14 3 5 12 2 15 8 6
                    1 4 11 13 12 3 7 14 10 15 6 8 0 5 9 2
                    6 11 13 8 1 4 10 7 9 5 0 15 14 2 3 12

                    S-box 8
                    13 2 8 4 6 15 11 1 10 9 3 14 5 0 12 7
                    1 15 13 8 10 3 7 4 12 5 6 11 0 14 9 2
                    7 11 4 1 9 12 14 2 0 6 10 13 15 3 5 8
                    2 1 14 7 4 10 8 13 15 12 9 0 3 5 6 11

                - Referencing the S-boxes above, we note Bₘ for Sₘ, and that the row of the S-box is specified by b₁b₆, while the column is denoted by b₂b₃b₄b₅

                    - e.g, if B₃ = 001001, we look at the third S-box at row (01)₂, column(0100)₂, which is the SECOND row FIFTH column, yielding (3)₁₀ = (0011)₂

                    - therefore the output of S₃ is 0011, and we repeat this process for the remaining seven 4-bit outputs C₁, C₂ . . . C₈

                - Perumute the string C₁C₂ . . . C₈ according to the permutation table below:

                    16 7 20 21 29 12 28 17 1 15 23 26 5 18 31 10
                    2  8 24 14 32 27 3  9 19 13 30 6 22 11 4  25

                    - this means that the 16th bit of the original C₁C₂ . . . C₈ is now the first, etc

                    - the resulting 32-bit string is f(Rᵢ₋₁, Kₘ)

        } end of stage 2 for-loop

        STAGE 3 (POST PROCESSING): 

        (1) switch left and right to obtain R₁₆L₁₆, then apply the inverse of the initial permutation to get the ciphertext c = IP⁻¹(R₁₆L₁₆)