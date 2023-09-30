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

namespace deathwing696
{
    public class Deathwing696
    {
        private static void Dibuja_ascendente(int num_escalones)
        {          
            for (int i = 0; i <= num_escalones; i++)
            {
                int num_espacios = ((num_escalones - i) * 2);

                for (int j = 0; j < num_espacios; j++)
                {
                    Console.Write(" ");
                }

                if (i == 0)
                    Console.WriteLine("_");
                else
                    Console.WriteLine("_|");
            }
        }

        private static void Dibuja_descendente(int num_escalones)
        {
            for (int i = 0; i <= num_escalones; i++)
            {
                int num_espacios;

                num_espacios = (i * 2) - 1;

                for (int j = 0; j < num_espacios; j++)
                {
                    Console.Write(" ");
                }

                if (i == 0)
                    Console.WriteLine("_");
                else
                    Console.WriteLine("|_");
            }
        }

        public static void Main(string[] args)
        {
            int num_escalones;

            Console.Write("Introduce el número de escalones que quieres que tenga la escalera:");
            num_escalones = Convert.ToInt32(Console.ReadLine());

            if (num_escalones > 0)
            {
                Dibuja_ascendente(num_escalones);
            }
            else if (num_escalones < 0)
            {
                Dibuja_descendente(num_escalones * -1);
            }
            else
            {
                Console.WriteLine("__");
            }

            Console.ReadKey();
        }
    }
}