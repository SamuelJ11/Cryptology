# 6.0 Stream Ciphers

    • In many classical cryptosystems such as the shift, affine and substitution ciphers, a given letter in the ciphertext always comes from exactly one letter in the plaintext

        - this greatly facilitates finding the key using frequency analysis

    • Block ciphers avoid these problems by encrypting blocks of several letters or numbers simultaneously:

        - a single change in a plaintext block should change potentially all the characters in the corresponding ciphertext block

    • Claude Shannon gave two properties that a good cryptosystems should have in order to hinder statistical analysis:

        (1) Diffusion: if we change a character of the plaintext, then several characters of the ciphertext should change, and, similarly, if we change a character of the ciphertext, then several characters of the plaintext should change. 

        (2) Confusion: the key does not relate in a simple way to the ciphertext. In particular, each character of the ciphertext should depend on several parts of the key.

# 6.2 Hill Ciphers

    • Choose an integer 'n', for example n = 3.  The key is an n x n matrix M whose entries are integers (mod 26)

        - for example, let 

                  |1  2  3|
            M  =  |4  5  6|
                  |11 9  8|

    • The message is written as a series of row vectors 

        - e.g., "abc" -> [0, 1, 2]

    • To encrypt, right multiply the vector by the matrix (traditionally, the matrix appears on the right in the multiplication)

                   |1  2  3|
        [0, 1, 2]  |4  5  6| = [0, 23, 22] (mod 26)
                   |11 9  8|

        - therefore the ciphertext is AWX

    • In order to decrypt, we need the determinant of M to satisfy:

        gcd(det(M), 26) = 1
    
    • det(M) = -3, so we can find the inverse using the algorithm from MA322:

        |1  2  3 | 1  0  0|
        |4  5  6 | 0  1  0|     *R2 = r2 - 4r1
        |11 9  8 | 0  0  1|     *R3 = r3 - 11r1 

        |1  2   3 | 1  0  0|
        |0 -3  -6 |-4  1  0|    *R2 = -(1/3)r2
        |0 -13 -25|-11 0  1|    *R3 = -r3

        |1  2   3 | 1     0    0|
        |0  1   2 | 4/3 -1/3   0|     
        |0  13  25| 11    0   -1|   *R3 = r3 - 13r2

        |1  2   3 | 1     0     0|
        |0  1   2 | 4/3  -1/3   0|   
        |0  0  -1 | -19/3 13/3 -1|   *R3 = -r3

        |1  2   3 | 1     0     0|  *R1 = r1 - 3r3
        |0  1   2 | 4/3 -1/3    0|  *R2 = r2 - 2r3  
        |0  0   1 | 19/3 -13/3  1|  

        |1  2   0 | -18    13    -3|  *R1 = r1 - 2r2
        |0  1   0 | -34/3  25/3  -2|    
        |0  0   1 | 19/3  -13/3   1|

        |1  0   0 | 14/3  -11/3  1|  
        |0  1   0 | -34/3  25/3 -2|    
        |0  0   1 | 19/3  -13/3  1|

        *Thus we have we have obtained the inverse:

        | 14/3  -11/3  1|  
        |-34/3  25/3  -2|    
        | 19/3  -13/3  1|

        which can be rewritten cleanly as:

                |-14  11 -3|  
        -1/3 *  | 34 -25  6|    
                |-19  13 -3|

    • Since 17 is the inverse of -3 (mod 26) (which is found by using the Extended Euclidean Algorithm), we replace (-1/3) with 17 and reduce (mod 26) to obtain


             |-14  11 -3|  
        17 * | 34 -25  6| (mod 26) =    
             |-19  13 -3|

             |22 5  1|  
         N = |6 17 24|    
             |15 13 1|

    • Thus we check our value of N by ensuring that MN = I (identity matrix)
            
    • The decryption is accomplished by multiplying by N:

                      |22 5  1|  
        [0, 23, 22] * |6 17 24| = [0, 1, 2] (mod 26)  
                      |15 13 1|

        * AWX -> abc

    

    