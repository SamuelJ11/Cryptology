/*
 * File: Helper.cpp
 * Project: Implementing RSA
 * Purpose: Provide the implementation of the Helper class
 */

#define FERMAT_TRIALS 20

#include "Helper.h"

using namespace std;

GEN Helper::generate_randint() 
{
    // TBD
}

GEN Helper::modular_exponentiation(const GEN &base, const GEN &exp, const GEN &mod)
{
    /* 
        This function uses sucessive squaring of the base until we reach the highest power 
        of the base that is less than or equal to the target exponent    
    */

    pari_sp ltop = avma; // declare a stack top pointer for garbage collection

    GEN current_exp = stoi(2);
    while (current_exp <= exp)
    {
        GEN result = gpow(base, current_exp, 0);  // third argument is ignored for integer exponents
    }


    
    pari_sp lbot = avma; // declare a stack bottom pointer for garbage collection

}

bool Helper::is_prime(const GEN &num) 
{
    GEN N = num;
    for (int i = 0; i < FERMAT_TRIALS - 1; i++)
    {
        /* Generate a random integer x such that 1 < x < n - 1 */
        /* 
            The random(N) function from PARI generates a random number ∈ [0: n - 1]*
            Since we want x ∈ [2: n - 2], we define the argument to random() to be 
            N - 3, instead of N.  This gives us x ∈ [0: n - 4]
            Then we simply shift the range by +2 so that x ∈ [2: n - 2]
        */

        GEN x = randomi(N - 3);
        gaddgs(x, 2);
    }
    
}