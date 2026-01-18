# 1.1 Secure Communications

    • The plaintext is the message, the key is the cipher used to decrypt the message, and the ciphertext is the encyrpted message itself

## 1.1.1 Possible Attacks

    • There are four main types of attack that Eve might be able to use:

        (1) Ciphertext only: Eve has only a copy of the ciphertext

        (2) Known plaintext: Eve ahs a copy of a ciphertext and the corresponding plaintext

        (3) Chosen plaintext: Eve gains temporary access to the encryption machine allowing her to encrypt a large number of suitably chosen plaintexts to deduce the key

        (4) Chosen ciphertext: Eve obtains temporary access to the decryption machine, uses it to decrypt several strings of symbols, and treis to use the results to deduce the key

    • One of the most important assumptions in modern cryptography is Kerckhoffs’s principle: In assessing the security of a cryptosystem, one should always assume the enemy knows the method being used. 

## 1.1.2 Symmetric and Public Key Algorithms

    • Encryption/decryption methods fall into two categories: symmetric key and public key

        - in symmetric key algorithms, the encryption and decryption keys are known to both Alice and Bob (in many cases both keys are the same)

    • In public key algorithms the encryption key is made public, but it is computationally infeasible to find the decryption key without information known only to Bob

        - a non-mathematical examlple of this is as follows: 
        
            (1) Bob sends Alice a message box and an unlocked padlock 
            (2) Alice puts her message in the box, locks the padlock and sends the box back to Bob
        
            however, this raises the authentication problem: Eve can intercept Bob’s original message box and replace Bob’s lock with her own

    • In public key cryptography, the method and the encryption key are made public, and everyone knows what must be done to find the decryption key.

        - the security rests on the fact that this is computationally infeasible

    • Public key cryptosystems seem a step beyond the symmetric-key ones, but they are computationally much more expensive. 
    
        - they are therefore used only in communicating small amounts of data such as digital signatures and keys for symmetric key cryptosystems

    • Symmetric encryption directly processes the data itself, so we can choose to process it continuously (stream) or in chunks (blocks). The design decision is about efficiency vs. structure.
    
    • Within symmetric key cryptography, there are two types of ciphers: stream ciphers and block ciphers

        - in stream ciphers, the data are fed into the algorithm in small pieces (bits or characters), and the output is produced in corresponding small pieces

        - in block ciphers, a block of input bits is collected and fed into the algorithm all at once, and the output is a block of bits

## 1.1.3 Key Length

    • In a brute force attack, the length of the ky is directly related to how long it will take to search the entire keyspace

    • Longer keys are advantageous but are not guaranteed to amke an adversary's task difficult

    • One-time pad systesm are unbreakable but the expense of using a one-time pad is enormous as it requires exchanging a key that is as long as the plaintext itself, and the key can only be used once

# 1.2 Crytographic Applications
   
    

