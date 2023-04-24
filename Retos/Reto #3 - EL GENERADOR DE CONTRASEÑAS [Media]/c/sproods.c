/* Reto #3 - EL GENERADOR DE CONTRASEÑAS [Media] */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define MAX 16

void Minus(int *, int);          // Prototipos de funciones.
void MinusMayus(int *, int);
void MinusNums(int *, int);
void MinusSimb(int *, int);
void MinusMayusNums(int *, int);
void MinusMayusSimb(int *, int);
void MinusNumsSimb(int *, int);
void MinusMayusNumsSimb(int *, int);
void Imprime(int *, int);

void main(void)
{
    int tam, letras[MAX], op;
    char res;

    while (true)
    {
        do
        {
            printf("\nDetermine el número de caracteres de su contraseña (entre 8 y 16): ");
            scanf("%d", &tam);
            fflush(stdin);
        }
        while (tam < 8 || tam > 16);

        do
        {
            printf("Elija, entre las siguientes alternativas, el tipo de caracteres que desea tener en su contraseña:\n");
            printf("\n1. Solo minúsculas\n2. Minúsculas y mayúsculas\n3. Minúsculas y números\n4. Minúsculas y símbolos\n5. Minúsculas, mayúsculas y números\n6. Minúsculas, mayúsculas y símbolos\n7. Minúsculas, números y símbolos\n8. Todos combinados...\n");
            scanf("%d", &op);
            fflush(stdin);
        }
        while (op < 1 || op > 8);

        switch (op)
        {
            case 1: Minus(letras, tam);
                break;
            case 2: MinusMayus(letras, tam);
                break;
            case 3: MinusNums(letras, tam);
                break;
            case 4: MinusSimb(letras, tam);
                break;
            case 5: MinusMayusNums(letras, tam);
                break;
            case 6: MinusMayusSimb(letras, tam);
                break;
            case 7: MinusNumsSimb(letras, tam);
                break;
            case 8: MinusMayusNumsSimb(letras, tam);
                break;
        }

        Imprime(letras, tam);

        do
        {
            printf("\n¿Desea generar otra contraseña? (s/n): ");
            res = getchar();
            fflush(stdin);
        }
        while (res != 's' && res != 'n');

        if (res == 'n')
            break;
    }

    printf("\nGracias por usar el generador aleatorio de contraseñas...\n");
}

void Minus(int A[], int T)
{
    int num, i;

    srand(time(NULL));

    for (i = 0; i < T; i++)
    {
        num = rand() % 26 + 97;
        A[i] = num;
    }
}

void MinusMayus(int A[], int T)
{
    int num, i;

    srand(time(NULL));

    for (i = 0; i < T; i++)
    {
        do
        {
            num = rand() % 58 + 65;
        }
        while (num > 90 && num < 97);

        A[i] = num;
    }
}

void MinusNums(int A[], int T)
{
    int num, i;

    srand(time(NULL));

    for (i = 0; i < T; i++)
    {
        do
        {
            num = rand() % 75 + 48;
        }
        while (num > 57 && num < 97);

        A[i] = num;
    }
}

void MinusSimb(int A[], int T)
{
    int num, i;

    srand(time(NULL));

    for (i = 0; i < T; i++)
    {
        do
        {
            num = rand() % 94 + 33;
        }
        while ((num > 47 &&  num < 58) || (num > 64 && num < 91));

        A[i] = num;
    }
}

void MinusMayusNums(int A[], int T)
{
    int num, i;

    srand(time(NULL));

    for (i = 0; i < T; i++)
    {
        do
        {
            num = rand() % 75 + 48;
        }
        while ((num > 57 && num < 65) || (num > 90 && num < 97));

        A[i] = num;
    }
}

void MinusMayusSimb(int A[], int T)
{
    int num, i;

    srand(time(NULL));

    for (i = 0; i < T; i++)
    {
        do
        {
            num = rand() % 94 + 33;
        }
        while (num > 47 && num < 58);

        A[i] = num;
    }
}

void MinusNumsSimb(int A[], int T)
{
    int num, i;

    srand(time(NULL));

    for (i = 0; i < T; i++)
    {
        do
        {
            num = rand() % 94 + 33;
        }
        while (num > 64 && num < 91);

        A[i] = num;
    }
}

void MinusMayusNumsSimb(int A[], int T)
{
    int num, i;

    srand(time(NULL));

    for (i = 0; i < T; i++)
    {
        num = rand() % 94 + 33;
        A[i] = num;
    }
}

void Imprime(int A[], int T)
{
    int i;

    printf("\nSu contraseña es:\n");
    for (i = 0; i < T; i++)
    {
        //printf("%d\t- %d\t - %c\n", i + 1, A[i], A[i]);       // Impresión de los caracteres con su correspondiente códgigo ASCI.
        printf("%c", A[i]);
    }

    printf("\n");
}