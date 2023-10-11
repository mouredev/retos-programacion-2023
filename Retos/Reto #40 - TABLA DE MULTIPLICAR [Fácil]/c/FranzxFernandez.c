/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ...
 */

#include <stdio.h>

void solve()
{
    int num;
    (void)scanf("%d", &num);

    for (int i = 1; i < 11; i++)
    {
        printf("%d x %d = %d\n", num, i, num * i);
    }
}

int main()
{
    solve();
    return 0;
}
