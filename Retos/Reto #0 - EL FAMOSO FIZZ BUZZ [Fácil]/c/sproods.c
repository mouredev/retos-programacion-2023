/* Solución del "Reto #0: EL FAMOSO FIZZ-BUZZ" */

#include <stdio.h>

void main(void)
{
    int i = 0;

    while (i < 100)
    {
        i++;

        if (i % 15 == 0)
            printf("fizzbuzz\n");
        else if (i % 3 == 0)
            printf("fizz\n");
        else if (i % 5 == 0)
            printf("buzz\n");
        else
            printf("%d\n", i);
    }
}
