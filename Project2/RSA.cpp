/*
 * File: RSA.cpp
 * Project: Implementing RSA
 * Purpose: Provide the implementation of the RSA class
 */

#include "RSA.h"

using namespace std;

RSA::RSA() 
{

}

GEN RSA::computeN() 
{
    return gmul(p, q);
}

