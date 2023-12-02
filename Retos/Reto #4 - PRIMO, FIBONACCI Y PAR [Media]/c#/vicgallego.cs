/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reto_4
{
    internal class Program
    {


        // Método principal donde comprueba los resultados y los muestra por pantalla
        static void Main()
        {
            Console.WriteLine("Introduce un numero: ");
            int numero = int.Parse(Console.ReadLine());

            string fibo = "";
            string paroimpar = "";
            string numeroprimo = "";


            if(EsFibonacci(numero) == true)
            {
                fibo = "es un numero fibonacci";
            }
            else
            {
                fibo = "no es un numero fibonacci";
            }


            if(numeropar(numero) == true)
            {
                paroimpar = "es un numero par";
            }
            else
            {
                paroimpar = "no es un numero par";
            }


            if (EsPrimo(numero) == true)
            {
                numeroprimo = "es un numero primo";
            }
            else
            {
                numeroprimo = "no es un numero primo";
            }

            Console.WriteLine($"El {numero}: {fibo}, {paroimpar} y {numeroprimo}");

        }




        static bool EsCuadradoPerfecto(int x)
        {
            // Calcula la raíz cuadrada del número y la convierte a entero
            int raizCuadrada = (int)Math.Sqrt(x);

            // Retorna verdadero si el cuadrado de la raíz cuadrada es igual al número original
            return raizCuadrada * raizCuadrada == x;
        }





        // formula para saber si es un numero fibonacci
        static bool EsFibonacci(int n)
        {
                       return EsCuadradoPerfecto(5 * n * n + 4) || EsCuadradoPerfecto(5 * n * n - 4);
        }




        // saber si el numero es par
        static bool numeropar(int numero)
        {
            if (numero % 2 == 0)
            {
                return true;
            }
            else
            {
                return false;
            }

        }

        //saber si el numero es primo
        static bool EsPrimo(int numero)
        {
            if (numero <= 1)
            {
                return false;
            }

            for (int i = 2; i <= Math.Sqrt(numero); i++)
            {
                if (numero % i == 0)
                {
                   
                    return false;
                }
            }

            return true;
        }

    }
}


