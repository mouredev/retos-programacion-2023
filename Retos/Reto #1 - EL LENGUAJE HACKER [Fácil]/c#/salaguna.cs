/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

namespace Reto_1
{
    internal class salaguna
    {
        public static void Main()
        {
            PideTexto();
        }

        private static string? PideTexto()
        {
            Console.Write("Escribe un texto y luego pulsa enter: ");
            string? miTexto = Console.ReadLine();
            if (miTexto == null)
            {
                Console.WriteLine("No me engañes, no has escrito nada!!!");
                PideTexto();
            }
            else
            {
                Console.WriteLine(TransformaTexto(miTexto));
            }
            return miTexto;
        }

        private static string TransformaTexto(string? textoEntrada)
        {
            if (textoEntrada == null)
                return string.Empty;
            string miCodificacion = string.Empty;
            for (int i = 0; i < textoEntrada.Length; i++)
            {
                miCodificacion += DameCodificacion(textoEntrada.Substring(i, 1));
            }
            return miCodificacion;
        }

        private static string DameCodificacion(string miLetra)
        {
            string miCodigo = string.Empty;
            switch (miLetra.ToUpper())
            {
                case "A":
                    miCodigo = "4";
                    break;
                case "B":
                    miCodigo = "I3";
                    break;
                case "C":
                    miCodigo = "[";
                    break;
                case "D":
                    miCodigo = ")";
                    break;
                case "E":
                    miCodigo = "3";
                    break;
                case "F":
                    miCodigo = "|=";
                    break;
                case "G":
                    miCodigo = "&";
                    break;
                case "H":
                    miCodigo = "#";
                    break;
                case "I":
                    miCodigo = "1";
                    break;
                case "J":
                    miCodigo = ",_|";
                    break;
                case "K":
                    miCodigo = ">|";
                    break;
                case "L":
                    miCodigo = "1";
                    break;
                case "M":
                    miCodigo = @"/\/\";
                    break;
                case "N":
                    miCodigo = "^/";
                    break;
                case "O":
                    miCodigo = "0";
                    break;
                case "P":
                    miCodigo = "|*";
                    break;
                case "Q":
                    miCodigo = "(_,)";
                    break;
                case "R":
                    miCodigo = "I2";
                    break;
                case "S":
                    miCodigo = "5";
                    break;
                case "T":
                    miCodigo = "7";
                    break;
                case "U":
                    miCodigo = "(_)";
                    break;
                case "V":
                    miCodigo = @"\/";
                    break;
                case "W":
                    miCodigo = @"\/\/";
                    break;
                case "X":
                    miCodigo = "><";
                    break;
                case "Y":
                    miCodigo = "j";
                    break;
                case "Z":
                    miCodigo = "2";
                    break;
                case " ":
                    miCodigo = " ";
                    break;
                default:
                    break;
            }
            return miCodigo;
        }
    }
}
