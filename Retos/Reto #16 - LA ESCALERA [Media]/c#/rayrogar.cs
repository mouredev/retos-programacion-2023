using System;
using System.Collections.Generic;
using System.Linq;


namespace Reto_Semanal
{

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
    public class Reto_16
    {

        static void Main(string[] args)
        { 
            try
            {
                while (true)
                {


                    int niv = int.Parse(Console.ReadLine());

                    if (niv == 0)
                        Console.WriteLine("__");
                    for (int i = 0; i < Math.Abs(niv) + 1; i++)
                    {
                        if (i == 0)
                            Console.WriteLine("_".PadLeft(niv > 0 ? niv * 2 + 1 : 0));
                        else
                        {
                            Console.WriteLine(niv < 0 ? "|_".PadLeft((i * 2) + 1) : "_|".PadLeft(Math.Abs(niv) * 2 - (i - 1) * 2));
                        }
                    }

                }
            }
            catch (System.Exception)
            {

                Console.WriteLine("See You Latter Babe!!!!");
            }
            

        }

    }
}