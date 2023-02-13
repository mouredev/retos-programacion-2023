/* Reto #5 -HOLA MUNDO [FÁCIL] - */

#include <stdio.h>

void hola(void);            // Prototipos de funciones.
void x(int, int);
void s(void);

void main(void)
{
    hola();
}

void hola(void)
{
    s();
    x(1, 2);
    x(1, 5);
    x(1, 24);
    x(1, 6);
    x(1, 0);
    s();
    x(1, 2);
    x(1, 5);
    x(1, 24);
    x(1, 6);
    x(1, 0);
    s();
    x(4, 1);
    x(3, 1);
    x(1, 1);
    x(3, 4);
    x(5, 1);
    x(1, 1);
    x(1, 1);
    x(3, 1);
    x(3, 1);
    x(3, 2);
    x(1, 0);
    s();
    x(1, 2);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 4);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(1, 2);
    x(0, 0);
    s();
    x(1, 2);
    x(1, 1);
    x(3, 1);
    x(1, 1);
    x(4, 3);
    x(1, 1);
    x(1, 1);
    x(1, 1);
    x(3, 1);
    x(1, 1);
    x(1, 1);
    x(3, 1);
    x(3, 2);
    x(1, 0);
    s();
}

void x(int m, int n)
{
    int i, j;

    for (i = 0; i < m; i++)
        printf("#");

    for (j = 0; j < n; j++)
        printf(" ");
}

void s(void)
{
    printf("\n");
}
