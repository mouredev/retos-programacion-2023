/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 * 
 * Un heterograma es una palabra o frase que no contiene ninguna letra repetida
 * 
 * Un isograma (del griego isos  : "igual" y grama  : "letra") es una oración que contiene
 * cada letra del alfabeto el mismo número de veces, por lo tanto, un heterograma es un isograma
 * en el que cada letra está presente solo una vez.
 * 
 * Un pangrama (del griego: παν γραμμα, 'todas las letras') o frase 
 * holoalfabética es un texto que usa todas las letras posibles del alfabeto de un idioma.
 * 
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace HETEROGRAMA
{
    class Program
    {
        static void Main(string[] args)
        {
            string cadena = "noserituya";
            TiposTexto tiposTexto = new TiposTexto(cadena);
            Console.WriteLine(tiposTexto.isHeterograma() == true ? "Es heterograma" : "No es heterograma");
            Console.WriteLine(tiposTexto.isIsograma() == true ? "Es Isograma" : "No es Isograma");
            Console.WriteLine(tiposTexto.isPangrama() == true ? "Es un pangrama" : "No es un pangrama");
        }
    }

    public class TiposTexto
    {
        Dictionary<string, int> letras;
        public TiposTexto(string cadena)
        {
            letras = guardarCadenaEnDiccionario(cadena);
        }
        public bool isHeterograma()
        {
            List<int> valores = letras.Values.ToList();
            valores.Sort();
            var response = valores.LastOrDefault() == 1 ? true : false;
            return response;
        }

        public bool isIsograma()
        {
            List<int> valores = letras.Values.ToList();
            var response = valores.Distinct().Count() == 1 ? true : false;
            return response;
        }

        public bool isPangrama()
        {
            List<string> keys = letras.Keys.ToList();
            var response = keys.Distinct().Count() == 26 ? true : false;
            return response;
        }

        private static Dictionary<string, int> guardarCadenaEnDiccionario(string cadena)
        {
            Dictionary<string, int> letras = new Dictionary<string, int>();
            foreach (var letra in cadena)
            {
                if (letras.Keys.Contains(letra.ToString()))
                {
                    letras[letra.ToString()]++;
                }
                else
                {
                    letras.Add(letra.ToString(), 1);
                }
            }

            return letras;
        }

    }
}
