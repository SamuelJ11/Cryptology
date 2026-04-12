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

using namespace std;

class Helper

{
public:

    static GEN modular_exponentiation(GEN base, GEN exponent, GEN modulus);

    static GEN generate_randint();  // method that uses the Blum Blum Shub algorithm to generate a random integer

    static bool is_prime(const GEN &num);  // method to check if a number is prime using Fermat's primality test and the Miller-Rabin primality test

};

#endif // HELPER_H