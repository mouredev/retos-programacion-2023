/*

# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

## Enunciado

*/

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

Console.WriteLine("Ingrese un número: ");
int number = Convert.ToInt32(Console.ReadLine());

Console.WriteLine($"{number} {(IsPrimo(number) ? "" : "no ")}" +
    $"es primo, {(IsFibonacci(number) ? "" : "no es ")}fibonacci y es {(IsPar(number) ? "par" : "impar")}");

bool IsFibonacci(int number)
{
    if (number <= 3) return true;
    
    int n = 2, tmp;
    int sum = 3;

    // Generar Fibonacci
    while (sum < number)
    {
        tmp = sum;
        sum += n;
        n = tmp;
    }
    return sum == number;
}

bool IsPrimo(int number)
{
    if(number <= 1) return false;
    int num = 2;
    while(num * num <= number)
    {
        if(number % num == 0) return false;
        num++;
    }
    return true;
}

bool IsPar(int number)
{
    return number % 2 == 0;
}