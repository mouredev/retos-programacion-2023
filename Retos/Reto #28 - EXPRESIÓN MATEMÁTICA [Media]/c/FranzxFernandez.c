/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / %
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */

#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

static bool isValid(const char *expression);

int main(int argc, char const *argv[])
{
    // Test case 1
    const char *temp = "5 + 4 / 7 - 4";
    printf("It is the expression valid? -> %d\n", isValid(temp));

    // Test case 2
    const char *temp_1 = "5 a 6";
    printf("It is the expression valid? -> %d\n", isValid(temp_1));

    // Test case 3
    const char *temp_2 = "5 + 4 / 7 - 4 + 3 * 6 / 9";
    printf("It is the expression valid? -> %d\n", isValid(temp_2));

    // Test case 4
    const char *temp_3 = "5 + 4 / 7 . 4 + 3 * 6 / 9";
    printf("It is the expression valid? -> %d\n", isValid(temp_3));

    return 0;
}
static bool isValid(const char *expression)
{
    char op[] = "+-*/%";

    for (int i = 0; expression[i] != '\0'; i++) // recorriendo el string
    {
        if (isalpha(expression[i]) != 0) // Si contiene alguna letra del alfabeto
        {
            return false;
        }
    }
    int n = strlen(expression);
    char *short_expression = (char *)malloc((n + 1) * sizeof(char)); // (n + 1) * 1B

    if (short_expression == NULL)
    {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    int count = 0;
    for (int j = 0; expression[j] != '\0'; j++)
    {
        if (expression[j] == ' ')
        {
            continue;
        }
        else
        {
            short_expression[count++] = expression[j]; // copiando la expresion sin espcios.
        }
    }
    short_expression[count] = '\0';

    //printf("%s\n", short_expression);

    // printf("%c\n", short_expression[0]);
    bool isaNumber = false;
    for (int z = 0; short_expression[z] != '\0'; z++)
    {
        if (z % 2 == 0) // pares
        {
            if (!isdigit(short_expression[z])) // Si en la posicion par no hay numeros...
            {
                return false;
            }
        }
        else // Si son impares deberian ser solo los 4 operadores
        {
            if (short_expression[z] == op[0] || short_expression[z] == op[1] || short_expression[z] == op[2] || short_expression[z] == op[3] || short_expression[z] == op[4])
            {
                isaNumber = true;
            }
            else
            {
                isaNumber = false;
                return false;
            }
        }
    }

    free(short_expression);
    return true;
}