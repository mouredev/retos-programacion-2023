using System;
using System.Linq;

namespace Reto40
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.Write("Introduce un número:");

            if (int.TryParse(Console.ReadLine(), out int numero))
            {
                var tabla = Enumerable.Range(1, 10)
                    .Select(i => $"{numero} x {i} = {i * numero}").ToList();

                foreach (var linea in tabla)
                {
                    Console.WriteLine(linea);
                }
            }
            else
            {
                Console.WriteLine("Entrada inválida");
            }

            Console.ReadKey();
        }
    }
}