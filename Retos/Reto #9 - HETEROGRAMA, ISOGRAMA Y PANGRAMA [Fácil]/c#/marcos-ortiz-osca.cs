/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 * Un heterograma es una palabra o frase que no contiene ninguna letra repetida.
 * Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
 * Un pangrama es una frase en la que aparecen todas las letras del abecedario. 
 * 
 * 
 * Heterogramas: yuxtaponer (10), centrifugado (12), luteranismo (11), adulterinos (11), hiperblanduzcos (15)...
 * Isogramas con una repetición o de segundo orden: acondicionar (11), escritura (9), intestinos (10), papelera (8)...
 * Pangrama: Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.
 */



using System;
using System.Collections.Generic;
using System.Formats.Tar;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace Retos
{
    internal class Reto_08_2023
    {
        private static void Main(string[] args)
        {
            foreach (string test in ListaPruebas()) {
                Console.WriteLine(test);
                Console.WriteLine("---------------------------------------------------------------------");
                Console.WriteLine($"Heterograma: {IsHeterograma(test)}, Isograma:{IsIsograma(test)}, Panagrama: {IsPanagrama(test)}\n");
            }
            
            
        }

        private static bool IsPanagrama(string test)
        {
            //Normalizar cadena
            test=test.ToLower();
            var isEnye = test.Contains("ñ");
            test=test.Normalize(NormalizationForm.FormD);

            var caracteres = test.ToCharArray();
            var repeticiones = new HashSet<Int32>();
            if (isEnye) repeticiones.Add('ñ');

            foreach (char c in caracteres)
            {
               if(Char.IsAsciiLetter(c))
                {
                    repeticiones.Add(c);
                   
                }
            }

            if(repeticiones.Count >= 27) { return true; }

            return false;

        }

        private static bool IsHeterograma(string test)
        {
            var caracters = test.ToCharArray();
            var duplicados = new HashSet<Char>();
            foreach (char c in caracters)
            {
                var isDuplicate=duplicados.Add(c);
                if (isDuplicate==false)
                {
                    return false;
                }
            }
            return true;
        }

        private static bool IsIsograma(string test)
        {
            
            var caracteres=test.ToCharArray();
            var repeticiones=new HashSet<Int32>();
            foreach (char c in caracteres)
            {                
                repeticiones.Add(caracteres.AsQueryable().Count(p=> p == c));
            }

            if (repeticiones.Count == 2) return true;

            return false;
        }

        private static List<String> ListaPruebas()
        {
            var testList=new List<String>();
            testList.Add("yuxtaponer");
            testList.Add("centrifugado");
            testList.Add("adulterinos");
            testList.Add("acondicionar");
            testList.Add("escritura");
            testList.Add("intestinos");
            testList.Add("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.");
            return testList;
        }
    }
}
