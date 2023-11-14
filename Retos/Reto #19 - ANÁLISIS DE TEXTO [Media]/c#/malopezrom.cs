// See https://aka.ms/new-console-template for more information
using System;
using System.Text.RegularExpressions;

namespace retosProgramacion2023
{

    /**
     * Función que analiza un texto y obtiene:
     * - Número total de palabras.
     * - Longitud media de las palabras.
     * - Número de oraciones del texto (cada vez que aparecen un punto).
     * - Palabra más larga.
     */
    class Program
    {
        static void AnalyzeText(string text)
        {
            Regex wordsRegex = new Regex(@"\p{L}+[\p{L}',@!.\-]*");
            Regex sentenceRegex = new Regex(@"\p{L}+[\p{L}',@!.\-]*\.+");
            string[] words = text.Replace("\n", " ").Split(' ');
            int sentences = 0;
            string longestWord = "";
            int length = 0;
            int size = 0;

            foreach (string word in words)
            {
                if (wordsRegex.IsMatch(word))
                {
                    size++;
                    if (sentenceRegex.IsMatch(word))
                    {
                        sentences++;
                    }
                }
                length += word.Length;
                if (word.Length > longestWord.Length)
                {
                    longestWord = word;
                }
            }

            int averageLength = length / size;

            Console.WriteLine("Total de palabras: " + size);
            Console.WriteLine("Longitud media: " + averageLength);
            Console.WriteLine("Numero de frases: " + sentences);
            Console.WriteLine("Palabra mas larga: " + longestWord + "(" + longestWord.Length + ")");
        }

        static void Main(string[] args)
        {
            string text = """
                    la luna asoma: federico garcía lorca
                       cuando sale la luna
                       se pierden las campanas
                       y aparecen las sendas
                       impenetrables.
                       cuando sale la luna,
                       el mar cubre la tierra
                       y el corazón se siente
                       isla en el infinito.
                       nadie come naranjas
                       bajo la luna llena.
                       es preciso comer
                       fruta verde y helada.
                       cuando sale la luna
                       de cien rostros iguales,
                       la moneda de plata
                       solloza en el bolsillo.
                    """.Trim();

            AnalyzeText(text);

        }
    }
}