/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */

/*
    a^2 + b^2 = c^2

    a = m^2 - n^2    | m > n
    b = 2mn
    c = m^2 + n^2
*/

/*
    Informacion donde encontrar que es un triple pitagorico: https://euclides.org/triples-pitagoricos/#:~:text=Un%20triple%20pitag%C3%B3rico%20es%20un,a%2C%20byc%20son%20triples%20pitag%C3%B3ricos.
*/

#include <stdio.h>
#include <stdbool.h>

bool isCoprime(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }

    if (a == 1)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void solve(unsigned int limite)
{
    int m = 2;
    bool exit = false;

    while (!exit)
    {
        for (int n = 1; n < m; n++)
        {
            if (isCoprime(m, n) && (m - n) % 2 == 1)
            {
                int a = m * m - n * n;
                int b = 2 * m * n;
                int c = m * m + n * n;

                int k = 1;
                while (k * c <= limite)
                {
                    printf("(%d,%d,%d)\n", k*a, k*b, k*c);
                    k++;
                }

                if (c > limite)
                {
                    exit = !exit;
                    break;
                }
            }
        }
        m += 1;
    }
}

int main()
{
    solve(10); // (3, 4, 5) y (6, 8, 10)
    return 0;
}
