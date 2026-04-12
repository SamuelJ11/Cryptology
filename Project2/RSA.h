/* File: RSA.h
 * Project: Implementing RSA
 * Purpose: This file contains the declaration of the RSA class, which implements the RSA encryption and decryption algorithm.
 *          The class includes methods for generating public and private keys, as well as encrypting and decrypting messages.
 * Author: Samuel Aboud
 * Date: 4/11/2026
 */

#ifndef RSA_H
#define RSA_H

#include <pari/pari.h>
#include <string>

#include "Helper.h"

using namespace std;

class RSA

{
public:

    RSA();  // default constructor

    GEN computeN();  // method to compute the modulus n = p * q

    GEN generate_keys();  // method to compute the public and private keys

    void export_keys(const string &keyname);  // method to export the public and private keys to files

    void encrypt(const string &message, const string &keyname);  // method to encrypt a message using the public key

    void decrypt(const string &ciphertext, const string &keyname);  // method to decrypt a message using the private key

private:

    GEN computeD();  // method to compute the private exponent d

    GEN p;  // prime number p
    GEN q;  // prime number q 
    GEN d;  // private exponent (key) d
};

#endif // RSA_H