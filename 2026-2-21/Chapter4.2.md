• In terms of security, it is one of the best possible systems, but implementation makes it unsuitable for most applications.

# 4.2 One Time Pads

    • Start by representing the message as a sequence of 0s and 1s (using ASCII, for example)

    • The key is a random sequence of 0s and 1s of the same length of the message
    
    • Encryption involves adding the key bitwise to the corresponding bits of message (mod 2)

        - in other words, the key is exclusive-ORed (⊕) with the message to obtain the ciphertext

        - decryption uses the same key; simply exclusive-OR the key with the ciphertext to obtain the original plaintext

    • For any ciphertext you see, there is always a key that would turn it into any plaintext of the same length

        - this is why ciphertext-only attacks are impossible with the one-time pad

    • A disadvantage of the one-time pad is that it requires a very long key:

        - for this reason various methods are often used in which a small input can generate a reasonably random sequence of 0s and 1s, hence an "approximation" to a one-time pad

        - two most common methods of pseudorandom bit generation are one-way functions and Blum-Blum-Shub (BBS) generators

    • A one-time pad has perfect secrecy iff the number of possible keys is greater than or equal to the number of possible plaintexts.