/* Reto #3 - EL GENERADOR DE CONTRASEÑAS [Media] */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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
    int tam, letras[MAX];

    do
    {
        printf("\nDetermine el número de caracteres de su contraseña (entre 8 y 16): ");
        scanf("%d", &tam);
    }
    while (tam < 8 || tam > 16);

    MinusMayusNumsSimb(letras, tam);
    Imprime(letras, tam);
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

    for (i = 0; i < T; i++)
        printf("%d\t- %d\t - %c\n", i + 1, A[i], A[i]);
}