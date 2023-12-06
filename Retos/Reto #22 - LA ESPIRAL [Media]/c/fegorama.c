#include <stdio.h>
#include <stdlib.h>

/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */

void build_spiral(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (j == (n + 1) - i && i < ((n + 1) / 2) + 1)
                printf("%c", 187); // ╗
            else if (j == (i - 1) && (i > 1 && i <= (n + 1) / 2))
                printf("%c", 201); // ╔
            else if (j == i && (i > (n / 2) + 1))
                printf("%c", 188); // ╝
            else if ((j == (n + 1) - i) && (i > (n / 2) + 1))
                printf("%c", 200); // ╚
            else if ((j < i - 1 && j < n - (i - 2)) || (j > n - i && j > i - 1))
                printf("%c", 186); // ║
            else if (j <= n - i || j > n - (i - 1))
                printf("%c", 205);
            else
                printf(" ");
        }
        printf("\n");
    }
}

int main(int args, char **argv)
{
    int n;

    if (args != 2)
    {
        printf("Indique el total de lados.");
        return 1;
    }
    else
        n = atoi(argv[1]);

    build_spiral(n);
    return 0;
}
