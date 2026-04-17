# 11.1 Hash Functions

    • A cryptographic hash function 'h' takes as input a message of arbitrary length and produces as output a message digest of fixed length.

    • Certain properties of a hash function should be satisfied:

        (1) given a message 'm', the message digest h(m) can be calculated very quickly

        (2) given a 'y', it is computationally infeasible to find a m' with h(m') = y (in other words, 'h' is preimage resistant)

        (3) it is computationally infeasible to find messages m₁ and m₂ such that h(m₁) = h(m₂) ('h' is strongly collision resistant)

    • A key distinction between 'strong' vs 'weak' collision resistance is summarized and simplified below:

        - weak: given a fixed x, find x != y such that h(x) = h(y); aka "if I give you a specific message x, you can’t find another y != x with the same hash”
       
        - strong: find any pair x != y such that h(x) = h(y); aka "you cannot find any pair x != y such that h(x) = h(y)
  
    • One of the main uses of hash functions is in digital signatures:
    
        - since the length of a digital signature is often at least as long as the document being signed, it is much more efficient to sign the hash of a document rather than the full document

    • Suppose a sender sends (m, h(m)) over the communications channel and it is received as (M, H); to check whether errors might have occurred, the recipient computes h(M) and ensures it equals 'H'. 
    
        - if any errors occurred, it is likely that h(M) != H because of the collision-resistance properties of 'h'
  
    • It is important to note that this scheme only protects against accidental corruption (noise, transmission errors), NOT active attackers;

        - if an active attacker intercepts the message, they can intercept (m, h(m)), change m to a malicious message m', calculate a new hash h(m') and send (m', h(m')) to the receiver
         
        - the receiver will calculate h(m'), see that it matches the 'H' they received, and wrongly assume the message is valid

# 11.2 Simple Hash Examples

    • The hash functions described in this section and the next are easily seen to involve only very basic operations on bits and therefore can be carried out much faster than procedures such as modular exponentiation.

    • Suppose we start with a message 'm' of arbitrary length 'L' and break 'm' into 'n' bit blocks (these blocks are denoted mⱼ)

        - thus we have m = [m₁, m₂, . . ., mₖ]

        * here 'k' = ceil(L/n), so the last block mₖ is padded with zeroes to ensure it has 'n' bits
  
        (1) write the jth block mⱼ as a row vector

            mⱼ = [mⱼ₁, mⱼ₂, ..., mⱼₙ]   *each mⱼᵢ is a bit

            * pause here:  make sure you understand that each block mⱼ is a sequence of 'n' bits (011001011...)
                           mⱼᵢ is just ONE of these bits of mⱼ

        (2) stack these row vectors (mⱼ) to form a 2D array (a matrix):

            +-----------------------------+
            |  m11    m12   ...    m1n    |
            |                             |
            |  m21    m22   ...    m2n    |
            |   .      .    .        .    |
            |   .      .      .      .    |
            |   .      .        .    .    | 
            |  mk1    mk2   ...    mkn    |    
            +-----------------------------+
                ║      ║     ║      ║
                ▼      ▼     ▼      ▼
                ⊕     ⊕    ⊕     ⊕
                ║      ║     ║      ║
                ▼      ▼     ▼      ▼
            [ c₁     c₂   ...     cₙ ]  =  h(m)

            * here we are calculating the ith bit of the hash as the XOR along the ith column of the matrix (e.g., hᵢ = m₁ᵢ ⊕ m₂ᵢ ⊕ ..., ⊕ mₖᵢ)

        • It is important to note that the above example is not cryptographically secure as it is easy to find to messages to hash to same value:
        
            - practical cryptographic hash functions typically make use of several other bit-level operations in order to make it more difficult to find collisions

        • Another operation used in hash functions is bit rotation. For example, for every j = 1, 2, . . . , k shift the row j of the matrix by j − 1 positions to the left. 

            - however, building a cryptographic hash requires considerably more tricks than just rotating as we'll see in chapter 12