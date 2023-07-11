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

int main()
{
    double num1, num2, calculo;
    char operador;

    printf("Ingrese un numero para realizar un calculo matematico: ");
    scanf("%lf", &num1);

    printf("Ingrese otro numero para realizar el calculo matematico: ");
    scanf("%lf", &num2);

    printf("Ingrese un operador (+, -, *, /): ");
    scanf(" %c", &operador);

    if (operador == '+')
    {
        calculo = num1 + num2;
        printf("El resultado de la suma es: %.2lf\n", calculo);
    }
    else if (operador == '-')
    {
        calculo = num1 - num2;
        printf("El resultado de la resta es: %.2lf\n", calculo);
    }
    else if (operador == '*')
    {
        calculo = num1 * num2;
        printf("El resultado de la multiplicacion es: %.2lf\n", calculo);
    }
    else if (operador == '/')
    {
        if (num2 != 0)
        {
            calculo = num1 / num2;
            printf("El resultado de la division es: %.2lf\n", calculo);
        }
        else
        {
            printf("No se puede dividir por cero.\n");
        }
    }
    else
    {
        printf("Operador invalido.\n");
    }

    return 0;
}
