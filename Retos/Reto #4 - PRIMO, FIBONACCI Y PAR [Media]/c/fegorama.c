/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
 * Devuelve 1 si es primo, usando iteratividad
 */
int isPrime(unsigned long n) 
{
    if (n < 3 || n == 4)
        return 0;

    int max = sqrt(n) + 1;

    for (int i = 2; i < max; i++)
        if (n % i == 0)
            return 0;

    return 1;
}

/*
 * Devuelve 1 si está dentro de los valores de la suceción de Fibonacci, usando iteratividad
 */
int isFibonacci(unsigned long n)
{
    // 0, 1, 2 y 3 son números de la sucesión de Fibonacci
    if (n < 4)
        return 1;

    unsigned long current = 2;
    unsigned long temporal = 0;
    unsigned long next = 3;

    // Se realiza un recorrido para localizar si está dentro de la sucesión 
    // y si coincide se devuelve 1, pero si el valor siguiente se pasa de 
    // n, se sale del bucle porque no es de la sucesión
    while (next < n)
    {
        temporal = current;
        current = next;
        next += temporal;
        if (next == n)
            return 1;
    }

    // Si llega al final y no se ha localizado, no está en la sucesión 
    // y se devuelve 0
    return 0;
}

/*
 * Función principal
 */
int main()
{
    unsigned char s[11];    // Cadena de texto entrada por teclado
    unsigned long n;        // Número a verificar

    // Se solicita entrada por teclado
    printf("Introduzca un número: ");
    fgets(s, 5, stdin);

    // Limpieza de la cadena entrada por teclado
    s[strcspn(s, "\r\n")] = 0;

    // Se transforma a largo sin signo
    if ((n = strtoul(s, NULL, 10)) == 0)
    {
        fprintf (stderr, "Error en la conversión del número introducido.\n");
        return 1;
    }

    // Verificación e impresión de los resultados
    printf("%d ", n);

    if (isPrime(n))
        printf ("es primo");
    else 
        printf ("no es primo");

    if (isFibonacci(n))
        printf (", es fibonnacci");
    else
        printf (", no es fibonnacci");

    if ((n % 2) == 0)
        printf (" y es par\n");
    else
        printf (" y es impar\n");

    return 0;
}