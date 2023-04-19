/*  Statement:
 *  
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

using System.Text;

namespace Reto08
{
    internal class Guillermoqnk
    {
        static void Main(string[] args)
        {
            Console.WriteLine("   *Heterogram, Isogram and Pangram checker*");
            Console.Write("\n\nIntroduce the phrase to check: ");
            var input = Console.ReadLine();
            Console.WriteLine($"\nHexogram: {IsHeterogram(input)}\n\n");
            Console.WriteLine($"Isogram: {IsIsogram(input)}\n\n");
            Console.WriteLine($"Pangram: {IsPangram(input)}\n\n");
        }

        private static bool IsHeterogram(string input)
        {
            var letterList = input.ToList();

            foreach (var letter in letterList)
            {
                if(letterList.Where(x=>x==letter).Count() > 1)
                {
                    return false;
                }
            }

            return true;
        }

        private static bool IsIsogram(string input)
        {
            var letterList = input.ToList();

            int cuantity = 0;

            foreach (var letter in letterList)
            {
                int tempNumber = letterList.Where(x => x == letter).Count();

                if (cuantity == 0)
                {
                    cuantity = tempNumber;
                }
                else if (tempNumber != cuantity)
                    return false;

            }

            return true;
        }

        private static bool IsPangram(string input)
        {
            var letterList = input.ToList();

            for (int i = 97; i < 122; i++)
            {
                var change = (char)i;

                if (!letterList.Contains(change))
                {
                    return false;
                }
            }

            return true;
        }
    }
}