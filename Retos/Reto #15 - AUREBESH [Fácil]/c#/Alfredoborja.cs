using System;
using System.Collections.Generic;
using System.Linq;

/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico 
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

namespace Aurebesh
{
    internal class Program
    {
        static void Main(string[] args)
        {
           Traductor lenguaje = new Traductor();
            lenguaje.leerEspañol("alfredo");
            lenguaje.leerAurebesh("Aurek Leth Forn Resh Esk Dorn Osk");
        }
    }

    public class Traductor
    {
        List<Diccionario> diccionario = new List<Diccionario>();
        public Traductor()
        {
            diccionario.Add(new Diccionario("a", "Aurek"));
            diccionario.Add(new Diccionario("b", "Besh"));
            diccionario.Add(new Diccionario("c", "Cresh"));
            diccionario.Add(new Diccionario("d", "Dorn"));
            diccionario.Add(new Diccionario("e", "Esk"));
            diccionario.Add(new Diccionario("f", "Forn"));
            diccionario.Add(new Diccionario("g", "Grek"));
            diccionario.Add(new Diccionario("h", "Herf"));
            diccionario.Add(new Diccionario("i", "Isk"));
            diccionario.Add(new Diccionario("j", "Jenth"));
            diccionario.Add(new Diccionario("k", "Krill"));
            diccionario.Add(new Diccionario("l", "Leth"));
            diccionario.Add(new Diccionario("m", "Mern"));
            diccionario.Add(new Diccionario("n", "Nern"));
            diccionario.Add(new Diccionario("o", "Osk"));
            diccionario.Add(new Diccionario("p", "Peth"));
            diccionario.Add(new Diccionario("q", "Qek"));
            diccionario.Add(new Diccionario("r", "Resh"));
            diccionario.Add(new Diccionario("s", "Senth"));
            diccionario.Add(new Diccionario("t", "Trill"));
            diccionario.Add(new Diccionario("u", "Usk"));
            diccionario.Add(new Diccionario("v", "Vev"));
            diccionario.Add(new Diccionario("w", "Wesk"));
            diccionario.Add(new Diccionario("x", "Xesh"));
            diccionario.Add(new Diccionario("y", "Yirt"));
            diccionario.Add(new Diccionario("z", "Zerek"));
        }


        public void leerEspañol(string palabra)
        {
            char[] charArray = palabra.ToCharArray();
            Console.WriteLine($"La palabra {palabra} en Aurebesh significa: ");
            for(int i = 0; i < charArray.Length; i++)
            {
                char c = charArray[i];
                Console.Write(convertirEspañol(c) + " ");
            }
            Console.WriteLine();
        }

        public string convertirEspañol(char letra)
        {
            string letraAurebesh = diccionario.Where(x => x.LetraEspañol == letra.ToString()).Select(x => x.LetraAurebesh).FirstOrDefault();
            return String.IsNullOrEmpty(letraAurebesh) == false ? letraAurebesh : letra.ToString(); 
        }

        public void leerAurebesh(string palabra)
        {
            string[] letrasAurebesh = palabra.Split(" ");
            Console.WriteLine($"La palabra {palabra} en español significa: ");
            for(int i = 0; i < letrasAurebesh.Length; i++)
            {
                string c = letrasAurebesh[i];
                Console.Write(convertirAurebesh(c));
            }
            Console.WriteLine();

        }
        public string convertirAurebesh(string palabra)
        {
            string letraEspañol = diccionario.Where(x => x.LetraAurebesh == palabra.ToString()).Select(x => x.LetraEspañol).FirstOrDefault();
            return String.IsNullOrEmpty(letraEspañol) == false ? letraEspañol : palabra.ToString();

        }
    }

    public class Diccionario
    {
        public string LetraEspañol { get; set; }
        public string LetraAurebesh { get; set; }

        public Diccionario(string letraEspañol, string letraAurebesh)
        {
            LetraEspañol = letraEspañol;
            LetraAurebesh = letraAurebesh;
        }
    }
}
