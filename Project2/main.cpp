#include <pari/pari.h>
#include <iostream>
#include <vector>

using namespace std;

int main() 
{
    /*
        the first argument is the number of bytes given to PARI to work with, and the second is the upper
        limit on a precomputed prime number table
    */
    pari_init(1000000, 0);

    GEN v = stoi(15);

    int flag = 1;
    vector<int> bits;
    int size = bits.size();

    while (cmpsi(flag, v) <= 0)
    {
        int i = 0;
        if (bittest(v, i))
        {
            bits[size - (i + 1)] = 1;
        }
        else
        {
            bits[size - (i + 1)] = 0;
        }

        i ++;
        flag *= 2;
    }

    for (int i = 0; i < size; i++)
    {
        cout << bits[i] << " ";
    }
    
    return 0;
}
