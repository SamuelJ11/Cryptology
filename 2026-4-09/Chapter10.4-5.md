# 10.4 Diffie-Hellman Key Exchange

    • Suppose Alice is sending a message to bob; this key exchange method has the following scheme:

        (1) either Alice or Bob selects a large prime 'p' for which the DLP is hard, along with a primitive root 'α' (mod p). both 'p' and 'α' are made public

        (2) Alice chooses a secret random 'x' with 1 <= x <= p-2, and Bob selects a secret random 'y' with 1 <= y <= p-2

        (3) Alice sends αˣ (mod p) to Bob, and Bob sends αʸ (mod p) to Alice

        (4) Using the messages that they each have recieved, they can each calculate the session key 'K':

            - Alice calculates 'K' via K ≡ (αʸ)ˣ (mod p)

            - Bob caculates 'K' via K ≡ (αˣ)ʸ (mod p)

    • Now that Alice and BOb have the same number 'K', they can use some prearranged procedure to produce a key:

        - for example, they could use the middle 56 bits of 'K' to obtain a DES key

    • If Eve is listening to all the communications between Alice and Bob, she will know αˣ and αʸ:

        - Eve could then potentially calculate x = 𝓛ₐ(K) (the discrete log of αˣ), then raise αʸ to to the power of 'x' to obtain αˣʸ ≡ K

        - Once EVE has 'K', she can use the same procedure (assuming she knows this) as Alice and Bob to extract a communication key
  
    • However, Eve does nto necessarily have to compute 'x' or 'y' to find 'K'; what she needs to do is solve either the Computational Diffie-Hellman Problem or the Decision Diffie-Hellman Problem: 

        (1) Computational Diffie-Hellman Problem: given αˣ (mod p) and αʸ (mod p), find αˣʸ (mod p)

        (2) Decision Diffie-Hellman Problem: given αˣ (mod p) and αʸ (mod p), and c /≡ 0 (mod p), decide whether or not c ≡ αˣʸ (mod p)

    • It is currently unknown whetehr a method for solving the decision Diffie-Hellman problem yield a solution to the computational Diffie-Hellman problem.

# 10.5 The ElGamal Public Key Cryptosystem

    • This system does not quite fit the definition of a public key cryptosystem given in Chapter 9, since the set of possible plaintexts (integers mod p) is not the same as the set of possible ciphertexts (pairs of integers (r, t) mod p):

        - as we will see shortly, in this scheme a plaintext is a single number 'm' such that m ∈ Zₚ 

        - the ciphertext outputs a pair of numbers (r, t) such that the ciphertext ∈ Zₚ x Zₚ

    • Suppose Alice wants to send a message 'm' to Bob (Assume 'm' is an integer with 0 <= m < p; if 'm' is larger, break it into smaller blocks):

        (1) Bob chooses a large prime 'p' and a primitive root 'α' (mod p)

        (2) Bob also chooses a secret integer 'b' and computes β ≡ αᵇ (mod p); this information (p, α, β) is made public and is Bob's public key

        (3) Alice does the following:

            1. downloads (p, α, β)
            2. chooses a random integer 'k' and comptutes r ≡ αᵏ (mod p)
            3. computes t ≡ βᵏm (mod p)
            4. sends the pair (r, t) to Bob

        (4) Bob decrypts by computing tr⁻ᵇ ≡ m (mod p)

    • Bob's decryption works because tr⁻ᵇ ≡ βᵏm(αᵏ)⁻ᵇ ≡ (αᵇ)ᵏm(α⁻ᵇᵏ) ≡ (αᵇᵏ)(α⁻ᵇᵏ)m ≡ m (mod p)

        * remember our alegebra rules that state that (αᵇᵏ)(α⁻ᵇᵏ) = 1

    • If Eve determines 'b', then she can decrypt by the same procedure that Bob uses, therefore it is important for Bob to keep 'b' secret.

        - additionally, since 'k' is a random integer, 't' gives Eve no information about 'm', and knowing 'r' is similarly unhelpful
  
        - 'k' is difficult to determine from 'r', since this is again a DLP; however if Eve finds 'k', she can then calculate tβ⁻ᵏ, which of course is 'm'

        - the previous fact is why its so important for a different random 'k' to be uses for each message

    • Suppose Alice encrypts messages m₁ and m₂ for Bob and uses the same value of 'k' for each message:

        - this means that 'r' will be the same for both messages, so the ciphertexts will be (r, t₁) and (r, t₂)

        - if Eve finds out the plaintext m₁, she can also determine m₂, as follows:

            1. note that t₁/m₁ ≡ βᵏ ≡ t₂/m₂ (mod p)
            2. since Eve knows t₁ and t₂, she computes m₂ ≡ t₂(t₁/m₁) (mod p)