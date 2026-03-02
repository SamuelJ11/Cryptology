# 7.6: Password Security

    • Let f(x) be a one-way function; a password 'x' can then be stored as f(x), along with the user's name

        - when the user logs in and enters thier password, the computer calculates f(x) for each user

        - to access someone's account, the intruder needs to know 'x', which is hard to compute since f(x) is a one-way function

    • In many systems, the encrypted passwords are stored in a public file, therefore anyone with access to the system can obtain this file

        - if f(x) is known, then all the words in a dictionary, and various modifications of these words can be fed into f(x)

        - comparing the results with the password file will often yield the passwords of several users

    • The dictionary attack described above can be partially prevented by making the password file not publicly available, but this alone is not enough

    • One way to hinder a dictionary attack is with a 'salt':

        - each password is randomly padded with an additional 12 bits

        - these 12 bits are then used to modify the function f(x)

        - the result is stored in the password file, along with the user's name and the values of the 12-bit salt

    • You might be thinking that if the attacker has the file and the file contains the salt, they could just "add the salt" to their dictionary words and proceed as usual.

        - however, the goal of a salt isn't to make the password impossible to crack; its to make it mathematically expensive and slow to crack many passwords at once

        - without a salt, an attacker can calculate f(x) for every word in the dictionary once and save the results in a massive list (called a Rainbow Table) 
        
            - they can then use that single list to crack passwords on any system in the world

        - but with a salt, the "target" changes for every user:

            - even if both users use the same password, thier stored hashes will be completely different because the function f(x) is modified by that 12-bit salt

        - the attacker can no longer use a pre-made list; they have to start their calculations from scratch for every single user on the system

    • With salt, the storage requirements for this "rainbow table"  increase by a factor of 2¹² = 4096 since each word needs to be stored 4096 times

    • Historically, the one-way function was based on DES. The first eight characters of the password are converted to seven-bit ASCII, and those 56 bits became the DES key.

        - if the password is shorter than eight symbols, it is padded with zeros to obtain the 56 bits

        - the "plaintext" of all zeroes is then encrypted using 25 rounds of DES with this key, and the output is stored in the password file

    • In this antiquated system, passwords need not be longer than 8 characters as subsequent characters were ignored by the DES function.

        - this makes the system vulnerable to brute force attacks today

    • In order to increase security, salt is added as follows:

        (1) a random 12-bit number is generated as the salt

        (2) the expansion function from DES that generates the 48-bit E(R) is modified as follows:
            
            - if the first bit of the salt is 1, the first and 25th bits of E(R) are swapped;

            - if the second bit of the salt is 1, the second and 26th bits of E(R) are swapped;

            .
            .
            .

            - if the twelth bit of the salt is 1, the twelth and 32nd bits of E(R) are swapped

            * note that when a bit of the salt is 0, it causes no swap

    • In this way, the salt means that 4096 variations of DES are possible