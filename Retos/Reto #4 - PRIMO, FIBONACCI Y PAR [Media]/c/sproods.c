/* Reto #4 - PRIMO, FIBONACCI Y PAR - */

#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int Es_Primo(int, char *);          // Prototipos de funciones.
int Es_Fibonacci(int, char *);
int Es_Par(int, char *);

void main(void)
{
    int number;
    char sentencia[200] = "", op, snumber[50];

    while (true)
    {
        do
        {
            printf("\nEscriba, por favor, el número (entero positivo) que desea examinar: ");
            scanf("%d", &number);
            fflush(stdin);
        }
        while (number <= 0);

        sprintf(snumber, "%d", number);             // Función que convierte un entero a una cadena de caracteres el cual se almacena en la variable snumber.
        strcpy(sentencia, snumber);

        Es_Primo(number, sentencia);
        Es_Fibonacci(number, sentencia);
        Es_Par(number, sentencia);

        printf("\n");
        puts(sentencia);

        do
        {
            printf("¿Desea examinar otro números? (s/n): ");
            op = getchar();
            fflush(stdin);
        }
        while (op != 's' && op != 'n');

        if (op == 'n')
            break;
    }
}

int Es_Primo(int N, char *S)
{
    int i, div = 0;

    for (i = 1; i < N; i++)
        if (N % i == 0)
            div++;

    if (div == 1)
        strcat(S, " es primo, ");
    else
        strcat(S, " no es primo, ");

    return 0;
}

int Es_Fibonacci(int N, char S[])               // Función que determina si el número pertenece a la secuencia de Fibonacci.
{
    unsigned long long cuadrado1, cuadrado2;
    float raiz1, raiz2;

    // Si (5 * N^2 + 4) o (5 * N^2 - 4) es un cuadrado perfecto, entonces N es un número de Fibonacci.
    cuadrado1 = 5 * pow(N, 2) + 4;
    cuadrado2 = 5 * pow(N, 2) - 4;
    raiz1 = sqrt(cuadrado1);
    raiz2 = sqrt(cuadrado2);

    if ((pow(raiz1, 2) == cuadrado1) || (pow(raiz2, 2) == cuadrado2))
        strcat(S, "es fibonacci, ");
    else
        strcat(S, "no es fibonacci, ");

    return 0;
}

int Es_Par(int N, char S[])
{
    if (N % 2 == 0)
        strcat(S, "y es par.\n");
    else
        strcat(S, "y es impar.\n");

    return 0;
}