/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace scaleraReto16
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("+ 5");
            DibujarEscalera(5);
            Console.WriteLine("- 5");
            DibujarEscalera(-5);
            Console.ReadKey();
        }
        public static void DibujarEscalera(int numeroEscalones)
        {
            if (numeroEscalones > 0)
            {
                // Escalera ascendente
                for (int i = 0; i < numeroEscalones; i++)
                {
                    for (int j = 0; j < numeroEscalones - i - 1; j++)
                    {
                        Console.Write("  ");
                    }
                    Console.WriteLine("_|");
                }
            }
            else if (numeroEscalones < 0)
            {
                // Escalera descendente
                for (int i = 0; i < -numeroEscalones; i++)
                {
                    for (int j = 0; j < i; j++)
                    {
                        Console.Write("  ");
                    }
                    Console.WriteLine("_|");
                }
            }
            else
            {
                // Caso especial
                Console.WriteLine("__");
            }
        }
    }
}
