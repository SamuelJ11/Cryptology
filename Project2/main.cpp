#include <pari/pari.h>
#include <iostream>

int main() 
{
    /*
        the first argument is the number of bytes given to PARI to work with, and the second is the upper
        limit on a precomputed prime number table
    */
    pari_init(1000000, 0);

    GEN v = cgetg(4, t_VEC);

    /* 
        gel(x,i) is used to access elements of a GEN object
        where we access component number i of the GEN object x
    */
    gel(v, 1) = stoi(1);
    gel(v, 2) = stoi(2);
    gel(v, 3) = stoi(3);

    output(v);

    return 0;
}

