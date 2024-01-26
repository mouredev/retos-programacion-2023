/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres.
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 *
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

#include <stdio.h>
#include <stdlib.h>

static int string_length(char *str)
{
    int count = 0;
    while (str[count] != '\0')
    {
        count++;
    }
    return count;
}

void solve(char *msg1, char *msg2, const int len)
{
    if (string_length(msg1) != string_length(msg2))
    {
        return;
    }
    
    char *diff = (char *)malloc(sizeof(char) * len); // n * 1 Byte
    if (diff == NULL)
    {
        printf("Failed allocating memory in the Heap!\n");
        return;
    }
    int count = 0;

    for (int i = 0; i < len; i++)
    {
        if (msg1[i] != msg2[i])
        {
            diff[count++] = msg2[i];
        }
    }
    diff[count] = '\0';

    int j = 0;
    printf("[");
    while (diff[j] != '\0')
    {
        printf("%c ", diff[j]);
        j++;
    }
    printf("]\n");

    free(diff);
}

int main()
{
    int n = string_length("Me llamo mouredev");
    int n1 = string_length("Me llamo.Brais Moure");
    printf("n = %d | n1 = %d\n", n, n1);

    solve("Me llamo mouredev", "Me llemo mouredov", n);
    solve("Me llamo.Brais Moure", "Me llamo brais moure", n1);
    return 0;
}
