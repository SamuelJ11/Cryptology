• In 1973, the National Bureau of Standards (NBS), later to become the National Institute of Standards and Technology (NIST), issued a public request seeking a cryptographic algorithm to become a national standard. 

• IBM submitted an algorithm called LUCIFER in 1974; the NBS forwarded it to the National Security Agency, which reviewed it and, after some modifications, returned a version that was essentially the Data Encryption Standard (DES) algorithm. 

• In 1975, NBS released DES, as well as a free license for its use, and in 1977 NBS made it the official data encryption standard.

• DES is a block cipher; namely it breaks the plaintext into blocks of 64 bits, and encrypts each block separately

    - the actual mechanics of how this is done is often called a Feistel system, after Horst Feistel, who was part of the IBM team that developed LUCIFER

• DES lasted for a long time, but became outdated. Brute force searches, though expensive, can now break the system. Therefore, NIST replaced it with the system AES (see Chapter 8) in the year 2000

# 7.2 A Simplified DES-Type Algorithm

    • Since the blocks are encrypted separately, we assume throughout the present discussion that the full message consists of only one block.

    • The message has 12 bits and is written in the form L₀R₀, where L₀ consists of the first six bits and R₀ consists of the last six bits
    
    • The key 'K' has 9 bits, the 'ith' round of the algorithm transforms an input Lᵢ₋₁Rᵢ₋₁ to the output LᵢRᵢ using an eight bit key 'Kᵢ' derived from 'K'.

    • The main part of the encryption process is a function f(Rᵢ₋₁, Kᵢ) that takes a 6-bit input Rᵢ₋₁ and an eight bit input Kᵢ and produces a six-bit output

    • The output for the ith round is defined as follows:

        Lᵢ = Rᵢ₋₁ and Rᵢ = Lᵢ₋₁ ⊕ f(Rᵢ₋₁, Kᵢ)

        * see figure 7.1 

    • This operation is performed for 'n' rounds producing the ciphertext LₙRₙ

    • The decryption process begins with taking LₙRₙ and switching left and right to obtain RₙLₙ

    • The same Feistel round function is used, but the keys are applied in reverse order Kₙ, Kₙ₋₁, ..., K₁

        - if we input (RₙLₙ), the output becomes [Lₙ] [Rₙ ⊕ f(Lₙ, Kₙ)]

        *since we know from the encryption process that Lₙ = Rₙ₋₁ and Rₙ = Lₙ₋₁ ⊕ f(Rₙ₋₁, Kₙ), we can plug this into the above equation:

            [Rₙ₋₁] [Lₙ₋₁ ⊕ f(Rₙ₋₁, Kₙ) ⊕ f(Rₙ₋₁, Kₙ)]
            
        * here we notice [Lₙ₋₁ ⊕ f(Rₙ₋₁, Kₙ) ⊕ f(Rₙ₋₁, Kₙ)] simplifies to [Lₙ₋₁ ⊕ 0] = [Lₙ₋₁]

        - thus we obtain [Rₙ₋₁] [Lₙ₋₁]

    • Continuing we see that the decryption process leads us back to R₀L₀, and switching the left and right halves gives us the original plaintext L₀R₀

    Since the blocks are encrypted separately, we assume throughout the present discussion that the full message consists of only one block.

    • The message has 12 bits and is written in the form L₀R₀, where L₀ consists of the first six bits and R₀ consists of the last six bits
    
    • The key 'K' has 9 bits, the 'ith' round of the algorithm transforms an input Lᵢ₋₁Rᵢ₋₁ to the output LᵢRᵢ using an eight bit key 'Kᵢ' derived from 'K'.

    • The main part of the encryption process is a function f(Rᵢ₋₁, Kᵢ) that takes a 6-bit input Rᵢ₋₁ and an eight bit input Kᵢ and produces a six-bit output

    • The output for the ith round is defined as follows:

        Lᵢ = Rᵢ₋₁ and Rᵢ = Lᵢ₋₁ ⊕ f(Rᵢ₋₁, Kᵢ)

        * see figure 7.1 

    • This operation is performed for 'n' rounds producing the ciphertext LₙRₙ

    • The decryption process begins with taking LₙRₙ and switching left and right to obtain RₙLₙ

    • The same Feistel round function is used, but the keys are applied in reverse order Kₙ, Kₙ₋₁, ..., K₁

        - if we input (RₙLₙ), the output becomes [Lₙ] [Rₙ ⊕ f(Lₙ, Kₙ)]

        *since we know from the encryption process that Lₙ = Rₙ₋₁ and Rₙ = Lₙ₋₁ ⊕ f(Rₙ₋₁, Kₙ), we can plug this into the above equation:

            [Rₙ₋₁] [Lₙ₋₁ ⊕ f(Rₙ₋₁, Kₙ) ⊕ f(Rₙ₋₁, Kₙ)]
            
        * here we notice [Lₙ₋₁ ⊕ f(Rₙ₋₁, Kₙ) ⊕ f(Rₙ₋₁, Kₙ)] simplifies to [Lₙ₋₁ ⊕ 0] = [Lₙ₋₁]

        - thus we obtain [Rₙ₋₁] [Lₙ₋₁]

    • Continuing we see that the decryption process leads us back to R₀L₀, and switching the left and right halves gives us the original plaintext L₀R₀
    
    • The function used for 'f' is an expander; it takes an input of six bits and outputs eight bits (see figure 7.2)

        - for example, this could me that the third input bit yields both the fourth and the sixth output bits, and the fourth input bit yields both the 3rd and 5th output bit, with the mappings defined by the following dictionary (note this dictionary is only used for reference)

        bit_mappings = {
            1st -> 1st
            2nd -> 2nd
            3rd -> 4th, 6th
            4th -> 3rd, 5th
            5th -> 7th
            6th -> 8th
        }

        e.g., 011001 -> 01010101

    • The main components of the function are called S-boxes, here we use two:

              |101 010 001 110 011 100 111 000|  
        S₁ =  |001 100 110 010 000 111 101 011|

              |100 000 110 101 111 001 011 010|
        S₂ =  |101 011 000 111 110 010 001 100|  

    • The input for an S-box has four bits; the first bit specifies the row, the other three specify the column:

        - e.g., input 1010 for S₁ means we look at the first row, third column, which yields the output of 110

    • The key 'K' consists of nine bits, but recall that the key Kᵢ for the ith round of encryption is obtained by using eight bits of 'K', starting with the ith bit:

        - e.g., if K = 010011001, then K₄ = 01100101

        * note there here we are indexing from 1, and after five bits we reached the end of 'K', so the last two bits were obtained from the beggining of 'K'
    
    • We can now describe f(Rᵢ₋₁, Kᵢ):

        - the input Rᵢ₋₁ consists of six bits, which is expanded to 8 bits via the expander function

        - the result is then XORed with Kᵢ to produce another 8-bit number

        - the first four bits are sent to S₁, and the last four bits are sent to S₂

            - each S-box outputs three bits, which are concatenated to form a six-bit number

        - this result is f(Rᵢ₋₁, Kᵢ) * see figure 7.3, it explains this very well

    • To make this clear, suppose we have Rᵢ₋₁ = 100110 and Kᵢ = 01100101

        (1) E(100110) = 10101010

        (2) 10101010 ⊕ 01100101 = 11001111

        (3) first four bits are sent to S₁, last four bits are sent to S₂:

            S₁[1, 4] = 000      *using zero-based indexing here

            S₂[1, 7] = 100

        (4) concatenating the output yields f(Rᵢ₋₁, Kᵢ) = 000100

    • Now we have all the peices to describe what happens in one full round of the encryption process:

        - recall that encryption is done via Lᵢ = Rᵢ₋₁ and Rᵢ = Lᵢ₋₁ ⊕ f(Rᵢ₋₁, Kᵢ)

        - suppose the input is Lᵢ₋₁Rᵢ₋₁ = 011100100110 (12 bit input), and Kᵢ = 01100101 (same as before)

        - then we already calculated that f(Rᵢ₋₁, Kᵢ) = 000100

        - this result (000100) is then XORed with Lᵢ₋₁ (011100) yielding 011000

        - altogether, we have Lᵢ = 100110, Rᵢ = 011000, and concatenation yields LᵢRᵢ = 100110011000

    • The output obtained previously becomes the input for the next round.