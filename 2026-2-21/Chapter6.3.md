# 6.3 Modes of Operation

    • There are times where it is necessary to encrypt messages that are either longer or shorter than the cipher’s block length.

    • There are five common modes of operations for block ciphers, each one discussed separately below.

## 6.3.1 Electronic Codebook (ECB)

    • The natural manner for using a block cipher is to break a long piece of plaintext into appropriately sized blocks of plaintext and process each block separately with the encryption function Eₖ

        - this is known as the electronic codebook (ECB) mode of operation

    • The problem with this approach is that the same plaintext block always maps to the same ciphertext block

        - the ciphertext then reveals certain patterns, which can potentially allow the attacker to alter the message by constructing a false ciphertext message and inserting it into the data stream

## 6.3.2 Cipher Block Chaining (CBC)

    • One method for reducing the problems that occur in ECB mode is to use chaining; this is a feedback mechanism where the encryption of a block depends on the encryption of the previous blocks:

        Cⱼ = Eₖ(Pⱼ ⊕ Cⱼ₋₁)

        * Ciphertext block j - 1 is XORed with plaintext block j BEFORE encryption

        Pⱼ = Dₖ(Cⱼ) ⊕ Cⱼ₋₁

        * Ciphertext block j - 1 is XORed with plaintext block j AFTER decryption

    • When referencing figure 6.1 in the textbook, we see the encryption process for C₁ modelled as:

        C₁ = Eₖ(Pⱼ ⊕ C₀)

        * here C₀ is often called the initialization vector (IV)

    • Choosing a fixed value for the initialization vector is never a good idea as the same plaintexts will produce the same ciphertexts.

        - in practice, this problem is handled by always choosing C₀ randomly and sending C₀ in the clear along with the first ciphertext C₁

## 6.3.3 Cipher Feedback (CFB)

    • One of the problems with both the​​ CBC and ECB methods is that encryption (and hence decryption) cannot begin until a complete block of plaintext data is available. 

        - the cipher feedback mode operates in a manner that is very similar to the way in which LFSRs are used to encrypt plaintext

        * recall that for LFSRs, the key (aka 'seed') is used to initializes the LFSR, which generates a bit sequence (the pad / keystream) that is XORed with the plaintext to yield the ciphertext

    • Rather than use linear recurrences to generate the keystream, however, the CFB uses the output of the block cipher (Eₖ) to create those 'k' bit keystreams

        - for the discussion that follows we focus on the eight-bit version of CFB

    • Let's assume our block cipher encrypts blocks of 64-bits and outputs blocks of 64-bits, but this time the plaintext is broken into 8-bit chunks

        (1) start with a 64-bit initialization vector X₁

        (2) X₁ is fed into the encryption function Eₖ, and the 8 leftmost bits of this output is stored in O₁, denoted 'L₈(Eₖ(X₁))'

        (3) O₁ is XORed with the first 8 bits of the plaintext P₁ to get the first 8 bits of the ciphertext C₁, denoted 'C₁ = P₁ ⊕ O₁' 

            * the following steps are where the "feedback" in the "Cipher Feedback" comes from

        (4) the 8 leftmost bits of the original X₁ are dropped, the remaining 56 rightmost bits (R₅₆) are shifted to the left, and C₁ is appended to R₅₆, denoted 'X₂ = R₅₆(X₁) || C₁'

        (5) the previous step generated a new 64-bit block X₂, and the cycle continues

    • Notice that in this mode, the plaintext Pⱼ never actually goes into the encryption function Eₖ
    
        - we only encrypt the "Register" Xⱼ to create a stream of random-looking bits Oⱼ to scramble the plaintext 8 bits at a time

        - decryption is accomplished via:

            Pⱼ = Cⱼ ⊕ L₈(Eₖ(Xⱼ)) 
            Xⱼ₊₁ = R₅₆(Xⱼ) || Cⱼ

    •  We note that decryption does not involve the decryption function Dₖ, meaning that encryption CANNOT be parallelized but decryption CAN be

## Output Feedback (OFB)

    • The CBC and CFB modes of operation exhibit a drawback in that errors propagate for a duration of time corresponding to the block size of the cipher.

        - one advantage of the OFB mode is that it avoids error propagation

    • We again assume 64-bit block sizes encrypting 8 bits at a time

        (1) X₁ is the 64-bit initialization vector (IV) and is fed into Eₖ, denoted 'Eₖ(X₁)'

        (2) the leftmost 8 bits of the result obtained from the previous step (denoted 'L₈(Eₖ(X₁))') is again assigned to O₁

        (3) O₁ is XORed with the first 8 bits of the plaintext P₁ to produce the first 8 bits of the ciphertext C₁, denoted ('C₁ = P₁ ⊕ O₁')

            * so far, this is the same as what we were doing in CFB

        (4) however, rather than use appending C₁ to the rightmost bits of X₁, OFB appends O₁, denoted ('X₂ = R₅₆(X₁) || O₁')

    • Just like with CFB, we do not need the decryption function Dₖ, and decryption is done very simply via Pⱼ = Cⱼ ⊕ Oⱼ

    • With OFB, the generation of the output keystream Oⱼ does not depend on the plaintext, so the keystream can be generated in advance

        - additionally, errors do not propogate througout the ciphertext

        - the only disadvantage is neither encryption nor decryption can be parallelized

## 6.3.5 Counter (CTR)

    • Just like OFB, CTR creates an output key stream that is XORed with chunks of plaintext to produce ciphertext.

        -  the main difference between CTR and OFB lies in the fact that the output stream Oⱼ is not linked to previous output streams

    • The first 3 steps of CTR are the same as CFB and OFB, namely:

        (1) start with a 64-bit initialization vector X₁

        (2) X₁ is fed into the encryption function Eₖ, and the 8 leftmost bits of this output is stored in O₁, denoted 'L₈(Eₖ(X₁))'

        (3) O₁ is XORed with the first 8 bits of the plaintext P₁ to get the first 8 bits of the ciphertext C₁, denoted 'C₁ = P₁ ⊕ O₁' 

    • Now, rather than update the register X₂ to contain the output of the block cipher, we simply take X₂ = X₁ + 1

        - in this way, X₂ does not depend on previous output

    • In general, the procedure for CTR is:

        Xⱼ = Xⱼ₋₁ + 1
        Oⱼ = L₈(Eₖ(Xⱼ))
        Cⱼ = Pⱼ ⊕ Oⱼ

        * see figure 6.4 for a clear example of this

    • Because each ciphertext block is calculated independently using a simple incremention of Xⱼ, CTR is said to be fully parallelizable