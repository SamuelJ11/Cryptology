/* File: Helper.h
 * Project: Implementing RSA
 * Purpose: This file contains the declaration of the Helper class, which provides utility functions for RSA implementation.
 * Author: Samuel Aboud
 * Date: 4/11/2026
 */

#ifndef HELPER_H
#define HELPER_H

#include <pari/pari.h>
#include <string>
#include <vector>

using namespace std;

class Helper

{
public:

    static GEN modular_exponentiation(const GEN &base, const GEN &exponent, const GEN &modulus);

    static GEN generate_randint();  // method that uses the Blum Blum Shub algorithm to generate a random integer

    static vector<int> to_binary(const GEN &num);

    static bool is_prime(const GEN &num);  // method to check if a number is prime using Fermat's primality test and the Miller-Rabin primality test

    static void export_keys(const string &keyname);  // method to export the public and private keys to files

};

#endif // HELPER_H