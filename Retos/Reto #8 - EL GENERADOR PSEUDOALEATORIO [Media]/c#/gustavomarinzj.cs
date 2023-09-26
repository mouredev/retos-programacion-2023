using System;

namespace GeneradorPseudoaleatorio
{
    class Program
    {
        static void Main(string[] args)
        {
            // Las centésimas de segundo de un valor de fecha y hora.
            string ahora = DateTime.Now.ToString("ff");
            int semilla = Convert.ToInt32(ahora);
            int miNumero;

            for (int i = 1; i < 11; i++)
            {
                // es.wikipedia.org/wiki/Generador_de_números_aleatorios
                miNumero = ((1664525 * (semilla - i)) + 1013904223) % (2^99);
                Console.WriteLine(miNumero);
            }

            Console.Read();
        }
    }
}