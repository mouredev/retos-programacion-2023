#include <stdio.h>

int main (void)
{
    unsigned int value;
    unsigned int i;

    printf("TABLA DE MULTIPLICAR\nDime un numero... ");
    scanf("%d", &value);

    i = 1;
    while (i <= 10 && value != 0)
    {
        printf("%d x %d = %d\n", value, i, i * value);
        i++;
    }
    return (0);
}
