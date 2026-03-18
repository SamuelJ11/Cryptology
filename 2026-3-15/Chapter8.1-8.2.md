# 8.1 The Basic Algorithm

    • Rijndael is designed for use with keys of lengths 128, 192 and 256 bits, but for this discussion we'll restrict to 128 bits.

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

    • The 128 input bits are grouped into 16 bytes of eight bits each, which are then arranged into a 4 x 4 matric:

        | a₀,₀ a₀,₁ a₀,₂ a₀,₃ |
        | a₁,₀ a₁,₁ a₁,₂ a₁,₃ |                    
        | a₂,₀ a₂,₁ a₂,₂ a₂,₃ |
        | a₃,₀ a₃,₁ a₃,₂ a₃,₃ |

    • Recall section 3.11 on finite fields, specifically GF(2⁸):

        - the elements of this field are bytes, which consist of eight-bits

        - they can be added by XOR and multiplied, but in the latter case must be reduced (mod X⁸ + X⁴ + X³ + X + 1)

        - each byte 'b' except the zero byte has a multiplicative inverse; that is, there is a byte b' such that b.b' = 00000001
  
    • Since we can do arithmetic operations of bytes, we can work with matrices whose entries are bytes.

## 8.2.1 The SubBytes Transformation

    • In this step, each of the bytes in the matrix is changed to another byte by the S-Box defined below:

        99  124 119 123 242 107 111 197 48  1   103 43  254 215 171 118 
        202 130 201 125 250 89  71  240 173 212 162 175 156 164 114 192 
        183 253 147 38  54  63  247 204 52  165 229 241 113 216 49  21  
        4   199 35  195 24  150 5   154 7   18  128 226 235 39  178 117 
        9   131 44  26  27  110 90  160 82  59  214 179 41  227 47  132 
        83  209 0   237 32  252 177 91  106 203 190 57  74  76  88  207 
        208 239 170 251 67  77  51  133 69  249 2   127 80  60  159 168 
        81  163 64  143 146 157 56  245 188 182 218 33  16  255 243 210 
        205 12  19  236 95  151 68  23  196 167 126 61  100 93  25  115 
        96  129 79  220 34  42  144 136 70  238 184 20  222 94  11  219 
        224 50  58  10  73  6   36  92  194 211 172 98  145 149 228 121 
        231 200 55  109 141 213 78  169 108 86  244 234 101 122 174 8   
        186 120 37  46  28  166 180 198 232 221 116 31  75  189 139 138 
        112 62  181 102 72  3   246 14  97  53  87  185 134 193 29  158 
        225 248 152 17  105 217 142 148 155 30  135 233 206 85  40  223 
        140 161 137 13  191 230 66  104 65  153 45  15  176 84  187 22

        * write a byte as 8 bits (abcdefgh)

        * look for entry in the 'abcd' row and 'efgh' column (numbered from 0 to 15)

        * this entry, when converted to binary, is the output
  
    • For example, if the input byte is 10001011, we do the following:

        1. look in row (1000)₂ aka the eighth row
        2. look in column (1011)₂ aka the eleventh column
        3. the output is (61)₁₀ aka (00111101)₂

    • The output of the SubBytes is again a 4 x 4 matrix of bytes, call it:

        | b₀,₀ b₀,₁ b₀,₂ b₀,₃ |
        | b₁,₀ b₁,₁ b₁,₂ b₁,₃ |                    
        | b₂,₀ b₂,₁ b₂,₂ b₂,₃ |
        | b₃,₀ b₃,₁ b₃,₂ b₃,₃ |

## 8.2.2 The ShiftRows Transformation

    • The four rows of the matrix obtained previously are shifted cyclically to the left by offsets of 0, 1, 2 and 3 to obtain:

        | c₀,₀ c₀,₁ c₀,₂ c₀,₃ |         | b₀,₀ b₀,₁ b₀,₂ b₀,₃ |
        | c₁,₀ c₁,₁ c₁,₂ c₁,₃ |    =    | b₁,₁ b₁,₂ b₁,₃ b₁,₀ |--+              
        | c₂,₀ c₂,₁ c₂,₂ c₂,₃ |         | b₂,₂ b₂,₃ b₂,₀ b₂,₁ |--|-----+  
        | c₃,₀ c₃,₁ c₃,₂ c₃,₃ |         | b₃,₃ b₃,₀ b₃,₁ b₃,₂ |--|-----|-----+
                                                                 |     |     |
                                            (shifted matrix)     | (1) | (2) | (3)
                                                                 |     |     |
                                        | b₀,₀ b₀,₁ b₀,₂ b₀,₃ |  |     |     |
                                        | b₁,₀ b₁,₁ b₁,₂ b₁,₃ |--+     |     |          
                                        | b₂,₀ b₂,₁ b₂,₂ b₂,₃ |--------+     |
                                        | b₃,₀ b₃,₁ b₃,₂ b₃,₃ |--------------+

                                            (original matrix)


        * The row index tells you the shift amount:

            - row 0: left shift by 0
            - row 1: left shift by 1
            - row 2: left shift by 2
            - row 3: left shift by 3
  
## 8.2.3 The MixColumns Transformation

    • The output of the previous matrix from the ShiftRows step is a 4 x 4 matrix (cᵢⱼ) with entries in GF(2⁸)

        - that byte is interpreted as a polynomial of degree 7 (see 3.11 notes if confused)

    • Now left-multiply this matrix with entries in GF(2⁸) to produce the output (dᵢⱼ):


        | 00000010  00000011  00000001  00000001 |   | c₀,₀ c₀,₁ c₀,₂ c₀,₃ |     | d₀,₀ d₀,₁ d₀,₂ d₀,₃ |
        | 00000001  00000010  00000011  00000001 | . | c₁,₀ c₁,₁ c₁,₂ c₁,₃ |  =  | d₁,₀ d₁,₁ d₁,₂ d₁,₃ |
        | 00000001  00000001  00000010  00000011 |   | c₂,₀ c₂,₁ c₂,₂ c₂,₃ |     | d₂,₀ d₂,₁ d₂,₂ d₂,₃ |
        | 00000011  00000001  00000001  00000010 |   | b₃,₀ b₃,₁ b₃,₂ b₃,₃ |     | d₃,₀ d₃,₁ d₃,₂ d₃,₃ |

        * this MixColumns matrix is designed for diffusion (spreading the influence of a single byte across many others)

        * reference the polynomial template from 3.11 to understand the following:

            b₇X⁷ + b₆X⁶ + b₅X⁵ + b₄X⁴ + b₃X³ + b₂X² + b₁X + b₀

        * you'll notice the matrix only uses three values (00000001, 00000010, 00000011):

            1. 00000001: this is the identity, multiplying a polynomial by 1 (aka b₀) does nothing
   
            2. 00000010: this is just X, multiplying by X is just a left shift of the bits and appending 0; if an overflow occurs, reduce (mod X⁸ + X⁴ + X³ + X + 1)

            3. 00000011: this is X + 1, and since 3 = 2 ⊕ 1, multiplying by 3 is the same as multiplying by 2, then XORing that result with the original value
   
        * also notice that each row of the MixColumns matrix is just a right-shift of the row above it; this makes it very easy to implement in hardware because you only need to build the logic for one row and then reuse it
  
            - the name for this type of matrix is called a "circulant matrix"

## 8.2.4 The RoundKey Addition
  
    • The round key, derived from the key in a process that we'll describe later, consists of 128 bits arranged in a 4 x 4 matrix (kᵢⱼ).
  
        - this is XORed with the output of the MixColumns step:

            | d₀,₀ d₀,₁ d₀,₂ d₀,₃ |      | k₀,₀ k₀,₁ k₀,₂ k₀,₃ |     | e₀,₀ e₀,₁ e₀,₂ e₀,₃ |
            | d₁,₀ d₁,₁ d₁,₂ d₁,₃ |  ⊕  | k₁,₀ k₁,₁ k₁,₂ k₁,₃ |  =  | e₁,₀ e₁,₁ e₁,₂ e₁,₃ |                     
            | d₂,₀ d₂,₁ d₂,₂ d₂,₃ |      | k₂,₀ k₂,₁ k₂,₂ k₂,₃ |     | e₂,₀ e₂,₁ e₂,₂ e₂,₃ |
            | d₃,₀ d₃,₁ d₃,₂ d₃,₃ |      | k₃,₀ k₃,₁ k₃,₂ k₃,₃ |     | e₃,₀ e₃,₁ e₃,₂ e₃,₃ |

            * the matrix we obtained is the final output of the round

## 8.2.5 The Key Schedule

    • The original key consists of 128 bits, which are arranged into a 4 x 4 matrix of bytes.

        - this matrix is expanded by adjoining 40 more columns, as follows:
  
        1. label the first four columns W(0), W(1), W(2), W(3)
   
        2. the new columns are generated recursively: suppose columns up through W(i - 1) have been defined. 
    
            if 'i' is not a multiple of 4, then W(i) = W(i - 4) ⊕ W(i - 1)

            else W(i) = W(i - 4) ⊕ T(W(i - 1))

            where T(W(i - 1)) is the transformation of W(i - 1) obtained as follows:

            1). let the elements of the column W(i - 1) be a, b, c, d
            2). shift these cyclically to obtain b, c, d, a
            3). replace each of these bytes with the corresponding element in the S-box from the SubBytes step to get 4 bytes e, f, g, h
            4). compute the round constant via r(i) = 00000010⁽ⁱ⁻⁴⁾⁄⁴ in GF(2⁸)
            5). now T(W(i - 1)) is the column vector [e ⊕ r(i), f, g, h]

    • In this way, columns W(4), . . . W(43) are generated from the initial four columns

        - the round key for the 'ith' round consists of the columns W(4i), W(4i + 1), W(4i + 2), W(4i + 3)

        - this matches exactly what we had from before:
  
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