/*
 
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace reto9
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //string textoTry ="aabbccgg";
            //string textoTry ="noseriputa";
            string textoTry = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja";
            Console.WriteLine($"Heterograma: {CheckHeterograma(textoTry)}");
            Console.WriteLine($"Isograma: {CheckIsograma(textoTry)}");
            Console.WriteLine($"Pangrama: {CheckPangrama(textoTry)}");
            Console.ReadLine();
        }
        /// <summary>
        /// check ir text is Heterograma
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        public static bool CheckHeterograma(string data)
        {
            //frase que no contiene ninguna letra repetida.​
            HashSet<char> letrasEncontradas = new HashSet<char>();
            foreach (char letra in data)
            {
                if (letrasEncontradas.Contains(letra))
                    return false;
                letrasEncontradas.Add(letra);
            }
            return true;
        }

        /// <summary>
        /// Check if text is Isograma
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        public static bool CheckIsograma(string data)
        {
            //palabra o frase en la que cada letra aparece el mismo número de veces. ​
            Dictionary<Char, int> letrasEncontradas = new Dictionary<Char, int>();// HashSet<char>();
            foreach (char letra in data)
            {
               if (letrasEncontradas.ContainsKey(letra))
                    letrasEncontradas[letra]++;
                else
                    letrasEncontradas.Add(letra, 1);
            }
            int cantidad = letrasEncontradas.Values.First();
            
            foreach (int valor in letrasEncontradas.Values)
            {
                if (valor != cantidad)
                    return false;
            }
            return true; 
        }

        /// <summary>
        /// Check if text is Pangrama
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        public static bool CheckPangrama(string data)
        {
            //texto que usa todas las letras posibles del alfabeto de un idioma.
            HashSet<char> letras = new HashSet<char>();
            foreach (char c in data.ToLower())
            {
                char letra = Char.ToLower(c.ToString().Normalize(NormalizationForm.FormD)[0]);
                if (Char.IsLetter(letra))
                    letras.Add(letra);
            }
            return letras.Count == 26;
        }
    }
}
