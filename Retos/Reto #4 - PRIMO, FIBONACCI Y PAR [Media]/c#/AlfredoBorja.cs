using System;
using System.Collections;

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

namespace PrimoFibonacciPar
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Utility.imprimir("Introduce tu numero a evaluar: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Numeros numeros = new Numeros(n);
            Utility.imprimir($"El numero {n}" +(numeros.IsPrimo() == true ? " es primo":" no es primo" ) +"," + (numeros.IsFibonacci() == true ? " fibonacci ":" no es fibonacci ") +"y "+(numeros.IsPar() == true ? "es par":"es impar" ) );
        }
    }

    public class Numeros
    {
        public int Numero { get; set; }

        public Numeros(int numero)
        {
            Numero = numero;
        }

        public bool IsFibonacci()
        {
            bool response = false;
            ArrayList lista = new ArrayList();
            int x = 0;
            int y = 1;
            int result = 0;

            for (int i = 0; i <= Numero; i++)
            {
                lista.Add(x);
                result = x + y;
                x = y;
                y = result;
            }
            int index = lista.IndexOf(Numero);
            if (index > -1) response = true;
            return response;
        }

        public bool IsPrimo()
        {   
            int divisible = 0;
            bool response = false;
            for (decimal j = 1; j <= Numero; j++)
            {
                if (Numero % j == 0) divisible++;
            }
            if (divisible <= 2) response = true;
            return response;
        }

        public bool IsPar()
        {
            bool response = false;
            if(Numero % 2 == 0) response = true;
            return response;
        }

    }

    public static class Utility
    {
        public static void imprimir(string str)
        {
            Console.WriteLine(str);
        }
    }
}

