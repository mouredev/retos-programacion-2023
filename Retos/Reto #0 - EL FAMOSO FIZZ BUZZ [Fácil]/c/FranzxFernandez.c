/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

#include <stdio.h>

void solve()
{
    for (int i = 1; i <= 100; i++)
    {
        if ((i % 3 == 0) && (i % 5 == 0))
        {
            printf("fizzbuzz\n");
        }
        else if (i % 3 == 0)
        {
            printf("fizz\n");
        }
        else if (i % 5 == 0)
        {
            printf("buzz\n");
        }
        else
        {
            printf("%d\n", i);
        }
    }
}

int main()
{
    solve();

    return 0;
}
