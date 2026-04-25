# 12.1 Birthday Attacks

    • If there are 23 people in a room, the probability is slightly more than 50% that two of them have the same birthday:

        - if there are 30, the probability is around 70%

    • This phenomenon is called the birthday paradox, and be explained using a method from discrete math:

        (1) the first person uses up one day, so the second person has a (1 - 1/365) chance of having a different birthday

        (2) the third person has a (1 - 2/365) chance of differing from the first two, so the probabilty of all three people having different birthdays is (1 - 1/365)(1 - 2/365)

        (3) continuing this process for the 23rd person, we have:

            (1 - 1/365)(1 - 2/365)(1 - 3/365) ... = ∏ x: 1, 23 (1-x/365) = 0.493

        (4) therefore, the probability of at least 2 people having the same birthday is 

            1 - 0.493 = 0.507

    • More generally, suppose we have 'N' objects, where 'N' is large, and there 'r' people that each choose an object with replacement:

        - then the probability that there is a match is 1 - e^(-r²/2N)

    • Note the above was an approximation for a large 'N', but for smaller values it is better to use the product formula.

    • Suppose now that there are 'N' objects and TWO groups of people, and we want to find the probability that someone from the first group chooses the same object as someone from the second group:

        - in this case, we use 1 - e^(-λ), where λ = -r²/N

    • For example, there is a 1 - e^(-30²/365) = 1 - e^(-2.446) = 91.5% probability that one person in one group of 30 people has the same birthday as someone in a second group of 30 people

    • The birthday attack can be used to find collisions for hash functions if the output of the hash function is not sufficiently large:

        - if 'h' is an n-bit hash, then there are N = 2ⁿ possible outputs

        - if we make a list h(x) for approximately sqrt(N) = 2⁰˙⁵ⁿ random choices of 'x', then there is a good chance of having two values x₁ and x₂ such that h(x₁) = h(x₂)

    • Similarly, suppose we have two sets of inputs, 'S' and 'T'.  If we compute h(s) for approximately sqrt(N) randomly chosen values of s ∈ S, and do the same for 'T':

        - then we expect some value h(s) to be equal to some value h(t) 

        - this situation will arise in attack signature schemes, where 'S' is a set of good documents and 'T' is a set of fraudulent documents

    • The above scenario demonstrates why it is important for modern-day hash functions to have outputs of 256-bits, requiring such lists to be have a length of roughly 2¹²⁸ bits, which is roughly 10³⁸ digits - far too large, both in time and memory.