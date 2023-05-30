#include <stdio.h>
#include <stdlib.h>

int isPrime(int n) 
{
    if (n < 3 || n == 4)
    {
        return 0;
    }

    int max = n / 2;

    for (int i=2; i < max; i++)
    {
        if (n % i == 0)
            return 0;
    }

    return 1;
}

int main(int args, char** argv)
{
    int rg, diff, ant = 0;

    if (args != 2) 
    {
        printf("Debe introducir el rango máximo.");
        return 1;
    }

    rg = atoi(argv[1]);

    if (rg > 4) {
        printf("(3, 5)");
    } else 
        return 0;

    for (int i=4; i <= rg; i++) {
        if (isPrime(i)) {
            diff = i - ant;

            if (diff == 2) {
                printf(", (%d, %d)", ant, i);                
            }
            
            ant = i;
        }
    }
    
    return 0;
}
