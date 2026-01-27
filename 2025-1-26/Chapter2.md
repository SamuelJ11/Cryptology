• The letters of the alphabet are assigned numbers 0 - 25 for a-z, respectively.

# 2.1 Shift Ciphers

    • The earliest cryptosystem was attributed to Julius Caesar's shift cipher that shfited each letter back by three places.

        - e.g., 'd' became 'a' and 'g' became 'd'

    • Decryption was accomplished by shifting forward by three spaces (and trying to figure out how to put the spaces back in).

    • The general situation is thus x -> y ≡ x + k (mod 26) for encryption, and y -> x ≡ y - k (mod 26) for decryption.

        - the key 'k' must be selected from {0, 1, . . . , 25}, and in this case k = -3

    • For example, since A = 0 and D = 3, the encryption process went as follows:
    
        - A ≡ D - 3 (mod 26)

    • Decryption followed the same logic:

        - D ≡ A + 3 (mod 26)

    • Now we can see how the four types of attack work:
    
        (1) ciphertext only: since there are only 26 possibilities, if a message is longer than just a few letters, it is very likely that for only one value of k, a meaningful message will emerge. 

            - exceptions do exist, however such as the words ‘river’ and ‘arena’ which are shifts of each other with the shift of k = 9

        (2) known plaintext: if you know just one letter of the plaintext along with the corresponding letter of the ciphertext, you can deduce the key.

            - e.g., if we know that 't' encrypts to 'd', then using the decryption formula above we fill in known values and solve for 'k':

                t ≡ d - k (mod 26)     ->      19 ≡ 3 - k (mod 26)

                19 ≡ 3 - k (mod 26)    ->      16 ≡ -k (mod 26)        

                -16 ≡ k (mod 26)       ->      10 ≡ k (mod 26)

                *thus to decrypt, we can either shift backward by 10 (d - 10) or equivalently forward by 16 (d - (-16)) as both give the same result mod (26)

        (3) chosen plaintext: here we pick the plaintext and see what it encrypts to, so we use the encryption formula:

            - for example, if we choose 'a' as the plaintext and the ciphertext is 'h', then we use the formula ciphertext ≡ plaintext + key:
            
                -- 7 ≡ 0 + k (mod 26), k = 7

        (4) chosen ciphertext: here we pick the cyphertext and see what it decrypts to, so we use the decryption formula: 
        
            - if we can choose 'a' as the ciphertext and the plaintext is 'h', the we use the formula plaintext ≡ ciphertext - key:
            
                -- 7 ≡ 0 - k (mod 26), k = -7

# 2.2 Affine Ciphers

    • Recall that an integer 's' is a multiplicative inverse (mod n) of 'a' iff as ≡ 1 (mod n).

        - s.a gives a remainder of 1 when divided by n, therefore 's' is the multiplicative inverse of a (mod n)

        - 'a' has a multiplicative inverse (mod n) if and only if gcd(a, n) = 1

    • Now consider an encryption method involving two integers α and β, with gcd(α, β) = 1, that uses the affine function defined below:

        - f(x) = αx + β (mod 26)    *equivalently written as y ≡ αx + β (mod 26)

    • If for example we consider the case where (α, β) = (9, 2), the we are working with 9x + 2.

        - now we can take a plaintext letter such as 'h' and encrypt it via 9(7) + 2 = 65 ≡ 13 (mod 26), which is the letter 'n'

    • So how do we decrypt? 

        - in normal arthithmetic we could take the encryption function y = 9x + 2 and simply solve for x instead via x = 1/9(y - 2)

        - however, since we are working with (mod 26) the fractional 1/9 needs to be reinterpreted

            *recall from chapter 3 that a fraction (b/a) can be used (mod n) if gcd (a, n) = 1

            *in other words, b/a (mod n) really means a⁻¹(b) (mod n), where a⁻¹(a) ≡ 1 (mod n)

        - now we set up an equation to solve for the inverse of 1/9 (mod 26) using the procedure outline in chapter 3:
        
            -- our general form is a.x ≡ c (mod n), where specifically we are working with 9x ≡ 1 (mod 26)

            (1) use the extended Euclidean algorithm to find integers s and t such that a.s + n.t = 1

                +-------------------+-----------------+-------------------------------------------------+
                |     Euclidean     |    Rewrite      |                Build Solution                   |
                +-------------------+-----------------+-------------------------------------------------+
                |  26 = 9(2) + 8    | 26 - 9(2) = 8   |  9 - (26 - 9(2)) = 1  -->  (3)9 + (-1)26 = 1    |
                +-------------------+-----------------+-------------------------------------------------+
                |  9 = 8(1) + 1     | 9 - 8(1) = 1    |                  9 - [8] = 1                    |
                +-------------------+-----------------+-------------------------------------------------+

                *s = 3, t = -1

            (2) x ≡ c.s (mod n), but in this case we replace the fraction c/a with c.s

                1/9 -> 1(3) = 3

                now we have the inverse of 1/9 (mod 26), so we can replace 1/9 in the original equation:

                x ≡ 3(y - 2) (mod 26)    *notice we are using '≡' here instead of '=' from x = 1/9(y - 2)

                x ≡ 3y - 6 (mod 26)     ->      x ≡ 3y + 20 (mod 26)

        - thus we have obtained the decryption function x ≡ 3y + 20 (mod 26) from the encryption function y ≡ 9x + 2 (mod 26)

    • Note that if y ≡ αx + β (mod 26) is the encryption function, then decryption is only one-to-one if gcd (a, n) = 1.

        - for example, the encryption function y ≡ 13x + 4 (mod 26) is not one-to-one because gcd(26, 13) = 13 ≠ 1, therefore decryption is impossible

    • Given the constraint defined above, there are 12 choices for 'α' (ϕ(26) = 12) and 26 choices for 'β'.

        * see Euler's totient function which counts the number of positive integers less than 'n' that are relatively prime to it, in this case ϕ(26) = 12

        - therefore there are 12 . 26 = 312 possible choices for the key

    • Lets look at the possible attacks:

        (1) ciphertext only: an exhaustive search through all 312 keys would be very easy to do on a computer

        (2) known plaintext: knowing two letters of the plaintext and the corresponding letters of the ciphertext suffices to find the key:

            - suppose we know that plaintext 'if' -> ciphertext 'pq', then we have two equations with two unknowns:

                * recall that 'i' = 8, 'f' = 5, 'p' = 15, 'q' = 16

                8α + β ≡ 15 (mod 26)
                5α + β ≡ 16 (mod 26)

                * now we can solve for (α, β) by subtracting equation 2 from equation 1

                3α ≡ -1 (mod 26)    -> 3α ≡ 25 (mod 26)     *general form a.x ≡ c (mod n) 

                * use the extended Euclidean algorithm to find integers s and t such that a.s + n.t = 1

                +-------------------+-----------------+-------------------------------------------------+
                |     Euclidean     |    Rewrite      |                Build Solution                   |
                +-------------------+-----------------+-------------------------------------------------+
                |  26 = 3(8) + 2    |  26 - 3(8) = 2  |  3 - (26 - 3(8)) = 1  -->  (9)3 + (-1)26 = 1    |
                +-------------------+-----------------+-------------------------------------------------+
                |  3 = 2(1) + 1     |    3 - 2 = 1    |                  3 - [2] = 1                    |
                +-------------------+-----------------+-------------------------------------------------+

                *s = 9, t = -1

                *x = α ≡ c.s (mod n) -> α ≡ 225 (mod 26) -> α ≡ 17 (mod 26)

            - now we know that α = 17, so we can easily solve for β using the first equation:

                8(17) + β ≡ 15 (mod 26)  ->  136 + β ≡ 15 (mod 26)  ->  6 + β ≡ 15 (mod 26)  -> β ≡ 9 (mod 26)

            - thus we have obtained (α, β) = (17, 9) and the resulting ENCRYPTION function y ≡ 17x + 9 (mod 26)

            - aside from the encryption function, we can find the DECRYPTION function via x ≡ α⁻¹(y - β) 

                - here we will skip the process of finding inverse of 17 (mod 26) and obtain 23

                    *verify this, (23)17 - 26(15) = 1

            - now we finally arrive at the decryption function, x ≡ 23y - 207 (mod 26)  ->  x ≡ 23y + 1 (mod 26)

        (3) chosen plaintext: recall that an attacker can choose some plaintexts to be encrypted and then observe the resulting ciphertext

            - we can choose 'ab' to be encyrpted as a good choice, as 'a' = 0 and 'b' = 1.  Let the resulting ciphertext be 'jq', for example:

            - recalling the encryption algorithm y ≡ αx + β (mod 26), we see that the ciphertext for 'a' is just β:

                -- y ≡ α(0) + β (mod 26)  ->  y ≡ β (mod 26)       

                * this gives the additive part of the key

                * for example, if we know that 'a' encrypts to 'j', then we see immediately that β = 9

            - similarly for encrypting 'b' we see:
                
                y ≡ α(1) + β (mod 26)  ->  y ≡ α + β (mod 26)

                * this allows us to solve for the multiplicative part of the key (α)

                -- since we know that 'b' encrypts to 'q'(16), and we already know that 16 ≡ α + β

                -- from earlier we obtained β = 9, so we can set up an equation and solve for α via 16 ≡ α + 9  ->  α = 7

            - now we have the encryption function y ≡ 8x + 9 (mod), from which can deduce the decryption function via x ≡ α⁻¹(y - β):

                -- x ≡ 15y - 135 (mod 26)  ->  x ≡ 15y + 21 (mod 26)

        (4) chosen ciphertext: recall that an attacker can choose some ciphertexts to be decrypted and then observe the resulting plaintext

            - if we choose 'AB' as the chosen ciphertext, then we can immediately deduce the decryption algorithm via x ≡ α⁻¹(y - β)

            - the goal of this attack is to pick the easiest possible values for 'y' (the ciphertext letter) to make the algebra as simple as possible

            - here we have chosen y₁ = 'A' and y₂ = 'B', such that x₁ ≡ α⁻¹(y₁ - β) and x₂ ≡ α⁻¹(y₂ - β)

                * y₁ = 0 (Letter 'A') and y₂ = 1 (Letter 'B')

            - we can begin by decrypting 'A' by plugging y₁ = 0 into the decryption function

                x₁ ≡ α⁻¹(0 - β)  ->  x₁ ≡ α⁻¹(-β) (mod 26)

            - now we decrypt 'B' by plugging y₂ = 1 into the decrytpion function

                x₂ ≡ α⁻¹(1 - β) (mod 26)  ->  x₂ ≡ α⁻¹ - β(α⁻¹) (mod 26)  ->  x₂ ≡ α⁻¹ + α⁻¹(-β)    

            - lets put those two equations directly op top of each other and maybe we'll notice something:

                x₁ ≡ α⁻¹(-β)         (mod 26)
                x₂ ≡ α⁻¹ + α⁻¹(-β) (mod 26)

                * notice the second part of the equation for x₂ is exactly x₁:

                x₁ ≡ α⁻¹(-β)  (mod 26)
                x₂ ≡ α⁻¹ + x₁ (mod 26)

                * subtracting x1 from both sides of the second equation lets us solve for α⁻¹:

                α⁻¹ = x₂ - x₁ (mod 26)

                * the above equation shows that α⁻¹ is simply the "distance" between the two plaintext values (mod 26)

            - now that we obtained α⁻¹, we can find β directly from the equation for x₁ with minimal algebraic manipulation:

                x₁ ≡ α⁻¹(-β) (mod 26)

                * multiply both sides by α (note that α is found by finding the multiplicative inverse of the multiplicative inverse α⁻¹ (mod 26)):

                αx₁ ≡ -β  ->  β ≡ -αx₁ (mod 26)

            - thus we have obtained the keys for the decryption function

# 2.3 The Vigenère Cipher



               



    

    