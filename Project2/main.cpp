#include <pari/pari.h>
#include <iostream>

int main() 
{
    pari_init(1000000, 2);

    GEN x = stoi(2);
    GEN y = stoi(6);
    GEN z = gmul(x, y);

    std::cout << gtolong(z) << std::endl;
}

