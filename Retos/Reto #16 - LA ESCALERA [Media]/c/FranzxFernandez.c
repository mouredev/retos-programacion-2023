/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 */

#include <stdio.h>

void solve()
{
    int n;
    printf("Introduce un numero para dibujar una escalera: ");
    (void)scanf("%d", &n);

    if (n > 0)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int space = 1; space <= (n + 1) - i; space++) 
            {
                printf(" ");
            }
            for (int j = 1; j <= 1; j++)
            {
                printf("_|");
            }
            printf("\n");
        }
    }else if (n < 0)
    {
        for (int i = 1; i <= (n * -1); i++)
        {
            for (int space = 1; space <= i; space++)
            {
                printf(" ");
            }
            for (int j = 1; j <= 1; j++)
            {
                printf("|_");
            }
            printf("\n");
        }
    }else
    {
        printf("(__)");
    }
}

int main()
{
    solve();
    return 0;
}
