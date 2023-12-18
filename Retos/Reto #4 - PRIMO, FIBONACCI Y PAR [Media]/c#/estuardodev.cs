/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

using System;

class Program
{
    public static void Main(String[] args)
    {
        Console.Write("Ingesa un número para verificar si es primo, fibonacci y par: ");
        try { 
            int valor = Convert.ToInt32(Console.ReadLine());
            verificar(valor);
        } catch (Exception ex) { 
            Console.WriteLine("Ingresa valores válidos."); 
        }
    }

    public static void verificar(int dato)
    {
        Console.WriteLine($"{dato} {EsPrimo(dato)}, {EsFibonacci(dato)} y {par_impar(dato)}");
    }

    public static string par_impar(int dato)
    {
        if (dato % 2 == 0)
        {
            return "es par";
        }
        else
        {
            return "es impar";
        }
    }

    public static string EsPrimo(int numero)
    {
        if (numero <= 1)
            return "no es primo";

        for (int i = 2; i <= Math.Sqrt(numero); i++)
        {
            if (numero % i == 0)
                return "no es primo"; 
        }

        return "es primo"; 
    }

    public static string EsFibonacci(int dato)
    {
        int a = 0;
        int b = 1;
        int contador = 0;

        while (contador < 1000)
        {
            int temp = a + b;
            a = b;
            b = temp;

            if (a == dato)
            {
                return "fibonacci";
            }
            contador++;
        }

        return "no es fibonacci";
    }
}
