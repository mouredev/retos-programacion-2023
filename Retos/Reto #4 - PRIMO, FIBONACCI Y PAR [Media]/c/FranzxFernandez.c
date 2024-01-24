/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

static bool esPar(const int n);
static bool esPrimo(const int n);
static bool esFibonacci(const int n);

int main(int argc, char const *argv[])
{
    printf("Enter a number: ");
    int n;
    (void)scanf("%d", &n);

    bool temp = esPar(n);
    printf("%d %s", n, (temp == true) ? "es par" : "es impar");

    temp = esPrimo(n);
    printf("%s", (temp == true) ? ", primo" : ", no es primo");

    temp = esFibonacci(n);
    printf("%s", (temp == true) ? " y Fibonacci" : " y no es Fibonacci");
    
    return 0;
}
static bool esPar(const int n)
{
    return (n % 2) == 0;
}
static bool esPrimo(const int n)
{
    if (n < 2)
    {
        return false;
    }
    for (int i = 2; i < sqrt(n); i++)
    {
        if (n % i == 0)
        {   
            return false;
        }
        
    }
    return true;
}
static bool esFibonacci(const int n)
{
    int a = 0;
    int b = 1;

    if (n == a || n == b)
    {
        return true;
    }

    while (b <= n)
    {
        int temp = a + b;
        a = b;
        b = temp;

        if (n == b)
        {
            return true;
        }
    }

    return false;
}
