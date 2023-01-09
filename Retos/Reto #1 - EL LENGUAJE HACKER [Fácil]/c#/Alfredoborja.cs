using System;
using System.Security.Cryptography.X509Certificates;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

namespace LENGUAJEHACKER
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var cadena = new Leet();
            cadena.texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum";
            imprimirTexto("Cadena original: ",ref cadena);
            convertirCadena(ref cadena);
            imprimirTexto("Lenguaje hacker: ",ref cadena);

             void convertirCadena(ref Leet cadena)
            {
                cadena.texto = cadena.texto.ToLower().Replace("a", "4").Replace("b", "I3").Replace("c", "[").Replace("d", ")").Replace("e", "3").Replace("f", "|=").Replace("g", "&").Replace("h", "#")
                .Replace("i", "1").Replace("j", ",_|").Replace("k", ">|").Replace("l", "1").Replace("m", "/\\/\\").Replace("n", "^/").Replace("o", "0").Replace("p", "|*").Replace("q", "(_,)")
                .Replace("r", "I2").Replace("s", "5").Replace("t", "7").Replace("u", "(_)").Replace("v", "\\/").Replace("w", "\\/\\/").Replace("x", "><").Replace("y", "j").Replace("z", "2").Replace("0", "o")
                .Replace("1", "L").Replace("2", "R").Replace("3", "E").Replace("4", "A").Replace("5", "S").Replace("6", "b").Replace("7", "T").Replace("8", "B").Replace("9", "g");
            }

             void imprimirTexto(string titulo,ref Leet cadena)
            {

                Console.WriteLine(titulo + cadena.texto);
            }
        }
    }

    public class Leet
    {
        public string texto { get; set; }
    }
}
