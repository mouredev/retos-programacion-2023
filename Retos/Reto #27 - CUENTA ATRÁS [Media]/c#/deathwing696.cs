/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

using System;
using System.Threading;

namespace reto27
{
    public class Reto27
    {
        static void Main(string[] args)
        {
            Cuenta_atras(10, 1);

            Cuenta_atras(5, 3);

            Console.ReadKey();
        }

        private static void Cuenta_atras(int numero, int segundos)
        {
            if (numero > 0)
            {
                if (segundos > 0)
                {
                    for (int i = numero; i >= 0; i--)
                    {
                        Console.WriteLine(i);
                        Thread.Sleep(segundos * 1000);
                    }
                }
                else
                {
                    Console.WriteLine("Los segundos entre cada número de la cuenta atrás deben de ser números enteros positivos");
                }
            }
            else
            {
                Console.WriteLine("El inicio de la cuentra atrás debe de ser un número entero positivo");
            }
        }
    }
}