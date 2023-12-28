#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

int isPrime(int n) 
{
    if (n < 3 || n == 4)
        return 0;

    int max = sqrt(n) + 1;

    for (int i = 2; i < max; i++)
        if (n % i == 0)
            return 0;

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

    for (int i = 3; i <= rg; i = i + 2)
    {
        if (isPrime(i))
        {
            diff = i - ant;

            if (diff == 2)
                printf("%s(%d, %d)", (i != 5 ? ", " : ""), ant, i);
            
            ant = i;
        }
    }
    
    return 0;
}
