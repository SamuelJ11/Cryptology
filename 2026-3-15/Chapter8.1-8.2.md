# 8.1 The Basic Algorithm

    • Rijndael is designed for use with keys fo lengths 128, 192 and 256 bits, but for this discussion we'll restrict to 128 bits.

    • For the 128-bit key, the algorithm consists of 10 rounds; eadch round has a round key that is derived from the original key

    • There are 4 basic steps, called "layers", that are used to form the rounds:

        1. The SubBytes Transformation (SB): this nonlinear layer is for resistance to differential and linear cryptanalysis attacks
   
        2. The ShiftRows Transformation (SR): THis linear mixing step causes diffusion of the bits over multiple rounds

        3. The MixColumns Transformation (MC): This layer has a purpose similar to ShiftRows

        4. AddRoundKey (ARK): The round key is XORed with the result of the above layer

    • The overall process looks like this:

        [ Plaintext ]
                |
                v
        +-----------------+
        |  AddRoundKey    |<--- W(0), W(1), W(2), W(3)  (Initial Key)
        +-----------------+
                |
                v
        +=================+
        |    ROUND 1      |
        |  -----------    |
        |   SubBytes      |
        |   ShiftRows     |
        |   MixColumns    |
        |  AddRoundKey    |<--- W(4), W(5), W(6), W(7)
        +=================+
                |
                .
                . (Rounds 2 through 8)
                .
                |
        +=================+
        |    ROUND 9      |
        |  -----------    |
        |   SubBytes      |
        |   ShiftRows     |
        |   MixColumns    |
        |  AddRoundKey    |<--- W(36), W(37), W(38), W(39)
        +=================+
                |
                v
        +=================+
        |    ROUND 10     |
        |  -----------    |
        |   SubBytes      |
        |   ShiftRows     |
        |  AddRoundKey    |<--- W(40), W(41), W(42), W(43)
        +=================+
                |
                v
        [ Ciphertext ]

        *Wᵢ is a 32-bit word (chunk) of the previous round key; W0 - W3 are 4 32-bit words taken from the original key

# 8.2 The Layers 

    • 




