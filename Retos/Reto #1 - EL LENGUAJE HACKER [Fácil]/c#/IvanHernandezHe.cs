/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

// version .NET 7.0

namespace Retos_2023.retos
{
    class Reto_1
    {

        static void Main()
        {

            Console.WriteLine("Reto #1: EL 'LENGUAJE HACKER'");

            Imprimir_TextoLeet(Convertir_Caracteres(Extraer_Caracteres(Leer())));

        }

        private static string Leer()    // Función que lee y valida el ingreso de un texto en consola
        {
            string text;

            do
            {
                Console.WriteLine("Ingresa el texto que quieres convertir a LEET");
                text = Console.ReadLine()!;

            } while (String.IsNullOrEmpty(text));

            return text;
        }

        private static char[] Extraer_Caracteres(string texto)  //Función que recibe un string y regresa una cadena de caracteres
        {
            char[] arrayChars = texto.ToCharArray();

            return arrayChars;
        }

        private static string[] Convertir_Caracteres(char[] caracteres) // Función que recibe arreglo de caracteres y regresa arreglo string convertido
        {
            string[] arrayConvert = new string[caracteres.Length];

            for (int c = 0; c < caracteres.Length; c++)
            {

                switch (caracteres[c])
                {
                    case ' ':
                        arrayConvert[c] = " ";
                        break;

                    case 'A' or 'a':
                        arrayConvert[c] = "4";
                        break;

                    case 'B' or 'b':
                        arrayConvert[c] = "I3";
                        break;

                    case 'C' or 'c':
                        arrayConvert[c] = "[";
                        break;

                    case 'D' or 'd':
                        arrayConvert[c] = ")";
                        break;

                    case 'E' or 'e':
                        arrayConvert[c] = "3";
                        break;

                    case 'F' or 'f':
                        arrayConvert[c] = "|=";
                        break;

                    case 'G' or 'g':
                        arrayConvert[c] = "&";
                        break;

                    case 'H' or 'h':
                        arrayConvert[c] = "#";
                        break;

                    case 'I' or 'i':
                        arrayConvert[c] = "1";
                        break;

                    case 'J' or 'j':
                        arrayConvert[c] = ",_|";
                        break;

                    case 'K' or 'k':
                        arrayConvert[c] = ">|";
                        break;

                    case 'L' or 'l':
                        arrayConvert[c] = "1";
                        break;

                    case 'M' or 'm':
                        arrayConvert[c] = "/\\/\\";
                        break;

                    case 'N' or 'n':
                        arrayConvert[c] = "^/";
                        break;

                    case 'O' or 'o':
                        arrayConvert[c] = "0";
                        break;

                    case 'P' or 'p':
                        arrayConvert[c] = "|*";
                        break;

                    case 'Q' or 'q':
                        arrayConvert[c] = "(_,)";
                        break;

                    case 'R' or 'r':
                        arrayConvert[c] = "I2";
                        break;

                    case 'S' or 's':
                        arrayConvert[c] = "5";
                        break;

                    case 'T' or 't':
                        arrayConvert[c] = "7";
                        break;

                    case 'U' or 'u':
                        arrayConvert[c] = "(_)";
                        break;

                    case 'V' or 'v':
                        arrayConvert[c] = "\\/";
                        break;

                    case 'W' or 'w':
                        arrayConvert[c] = "\\/\\/";
                        break;

                    case 'X' or 'x':
                        arrayConvert[c] = "><";
                        break;

                    case 'Y' or 'y':
                        arrayConvert[c] = "j";
                        break;

                    case 'Z' or 'z':
                        arrayConvert[c] = "2";
                        break;

                    case '1':
                        arrayConvert[c] = "L";
                        break;

                    case '2':
                        arrayConvert[c] = "R";
                        break;

                    case '3':
                        arrayConvert[c] = "E";
                        break;

                    case '4':
                        arrayConvert[c] = "A";
                        break;

                    case '5':
                        arrayConvert[c] = "S";
                        break;

                    case '6':
                        arrayConvert[c] = "b";
                        break;

                    case '7':
                        arrayConvert[c] = "T";
                        break;

                    case '8':
                        arrayConvert[c] = "B";
                        break;

                    case '9':
                        arrayConvert[c] = "g";
                        break;

                    case '0':
                        arrayConvert[c] = "o";
                        break;

                    default:
                        arrayConvert[c] = caracteres[c].ToString();
                        break;
                }
            }

            return arrayConvert;
        }

        private static void Imprimir_TextoLeet(string[] cadena_Convertida)  //Función que imprime un arreglo de strings
        {

            for (int s = 0; s < cadena_Convertida.Length; s++)
            {
                Console.Write(cadena_Convertida[s]);
            }

            Console.Write("\n");
        }
    }
}