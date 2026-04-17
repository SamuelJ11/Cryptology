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

    