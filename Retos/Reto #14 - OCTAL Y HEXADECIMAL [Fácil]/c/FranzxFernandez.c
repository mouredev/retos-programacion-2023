/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

#include <stdio.h>

static void decimal_to_octal_and_hex(int number);
static void test_decimal_to_octal_and_hex();

int main(int argc, char const *argv[])
{
    test_decimal_to_octal_and_hex();
    return 0;
}
static void decimal_to_octal_and_hex(int number)
{
    printf("Decimal: %d\n", number);
    if (number < 0)
    {
        return;
    }

    int array_octal[10] = {0}, j = 0; 
    char array_hex[10] = {0};
    int guardar = number;
    while (number != 0)
    {
        array_octal[j++] = number % 8;
        number /= 8;
    }

    printf("Octal: ");
    for (int i = j; i >= 0; i--)
    {
        printf("%d", array_octal[i]);
    }
    printf("\n");

    j = 0; 

    while (guardar != 0)
    {
        int temp = guardar % 16;
        if (temp < 10)
        {
            array_hex[j++] = 48 + temp;
        }
        else
        {
            array_hex[j++] = 55 + temp;
        }
        guardar /= 16;
    }

    printf("Hex: ");
    for (int i = j; i >= 0; i--)
    {
        printf("%c", array_hex[i]);
    }
    printf("\n");
}
static void test_decimal_to_octal_and_hex()
{
    int test_cases[] = {192, 0, 255, 93, 125, 10, 16};
    int num_cases = sizeof(test_cases) / sizeof(test_cases[0]);

    for (int i = 0; i < num_cases; i++)
    {
        printf("Test Case %d:\n", i + 1);
        decimal_to_octal_and_hex(test_cases[i]);
        printf("\n");
    }
}
