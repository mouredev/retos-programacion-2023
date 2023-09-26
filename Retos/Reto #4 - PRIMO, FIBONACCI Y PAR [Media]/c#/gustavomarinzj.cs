/*
* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
* Ejemplos:
* - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
* - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*/
using System;
using System.Collections.Generic;

namespace PrimoFibonacciPar
{
    class Program
    {
        static void Main(string[] args)
        {
            // Se probó con números aleatorios
            // Random aleatorio = new Random();
            // int numero = aleatorio.Next(0, 6765);
            int numero = 7;

            Console.WriteLine("El número " + numero + " " + esPrimo(numero) + ", " + esFibonacci(numero) + " " + esPar(numero));
            Console.Read();
        }
        public static string esFibonacci(int num)
        {
            // sucesion de Fibonacci hasta n = 20
            List<int> sucesionFibonacci = new List<int>() { 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765 };
            string resultado = "no es Fibonacci";
            // recorrer la sucesión buscando el número
            for (int i = 0; i < sucesionFibonacci.Count; i++)
            {
                if (num == sucesionFibonacci[i])
                {
                    resultado = "es Fibonacci";
                    break;
                }
            }
            return resultado;
        }

        public static string esPrimo(int num)
        {
            string resultado = "es primo";
            // dividir el número, comprobando que el residuo no sea cero
            for (int i = 2; i < num; i++)
            {
                if ((num % i) == 0)
                {
                    // no es primo 
                    resultado = "no es primo";
                }
            }
            return resultado;
        }

        public static string esPar(int num)
        {
            string resultado = "y es impar";
            if (num % 2 == 0)
            {
                resultado = "y es par";
            }
            return resultado;
        }

    }
}