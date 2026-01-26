• The letters of the alphabet are assigned numbers 0 - 25 for a-z, respectively

# 2.1 Shift Ciphers

    • The earliest cryptosystem was attributed to Julius Caesar's shift cipher that shfited each letter back by three places

        - e.g., 'd' became 'a' and 'g' became 'd'

    • Decryption was accomplished by shifting forward by three spaces (and trying to figure out how to put the spaces back in)

    • The general situation is thus x -> y ≡ x + k (mod 26) for encryption, and y -> x ≡ y - k (mod 26) for decryption

        - the key 'k' must be selected from {0, 1, . . . , 25}, and in this case k = -3

    • For example, since A = 0 and D = 3, the encryption process went as follows:
    
        - A ≡ D - 3 (mod 26)

    • Decryption followed the same logic:

        - D ≡ A + 3 (mod 26)

    • Now we can see how the four types of attack work:
    
        (1) Ciphertext only: since there are only 26 possibilities, if a message is longer than just a few letters, it is very likely that for only one value of k, a meaningful message will emerge. 

            - exceptions do exist, however such as the words ‘river’ and ‘arena’ which are shifts of each other with the shift of k = 9

        (2) Known plaintext: if you know just one letter of the plaintext along with the corresponding letter of the ciphertext, you can deduce the key.

            - e.g., if we know that 't' encrypts to 'd', then using the decryption formula above we fill in known values and solve for 'k':

                t ≡ d - k (mod 26)     ->      19 ≡ 3 - k (mod 26)

                19 ≡ 3 - k (mod 26)    ->      16 ≡ -k (mod 26)        

                -16 ≡ k (mod 26)       ->      10 ≡ k (mod 26)

                *thus to decrypt, we can either shift backward by 10 (d - 10) or equivalently forward by 16 (d - (-16)) as both give the same result mod (26)

        (3) Chosen plaintext: here we pick the plaintext and see what it encrypts to, so we use the encryption formula:

            - for example, if we choose 'a' as the plaintext and the ciphertext is 'h', then we use the formula ciphertext ≡ plaintext + key:
            
                -- 7 ≡ 0 + k (mod 26), k = 7

        (4) Chosen ciphertext: here we pick the cyphertext and see what it decrypts to, so we use the decryption formula: 
        
            - if we can choose 'a' as the ciphertext and the plaintext is 'h', the we use the formula plaintext ≡ ciphertext - key:
            
                -- 7 ≡ 0 - k (mod 26), k = -7

            
    

    