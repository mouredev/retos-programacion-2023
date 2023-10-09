/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

using System;
using System.Globalization;
using System.Text;

namespace deathwing696
{
    public class Deathwing696
    {

        private static string Oculta_letras(string palabra)
        {
            StringBuilder palabra_oculta = new StringBuilder(palabra);
            int num_caracteres_ocultos = Convert.ToInt32(Math.Floor(palabra.Length * 0.6));
            Random rnd = new Random();            

            for (int i = 0; i < num_caracteres_ocultos; i++)
            {
                palabra_oculta[rnd.Next(0, palabra.Length)] = '_';
            }

            return palabra_oculta.ToString();
        }

        private static void Muestra_letras(ref string palabra_oculta, string palabra, string letra)
        {
            StringBuilder pista = new StringBuilder(palabra_oculta.ToLower());

            for (int i = 0; i < palabra.Length; i++)
            {
                if (palabra[i] == Convert.ToChar(letra))
                    pista[i] = palabra[i];
            }

            pista[0] = char.ToUpper(pista[0]);
            palabra_oculta = pista.ToString();
            
        }

        private static bool Estan_todas_mostradas(string palabra_oculta)
        {
            int faltan_adivinar = palabra_oculta.Split('_').Length - 1;

            return faltan_adivinar == 0;
        }

        public static void Main(string[] args)
        {
            string[] palabras = {"Quema", "Recordad", "Idiota", "Manada", "Parsimonioso", "Incapaz", "Absurdamente", "Purificar", "Vagabundo", "Comportamiento"};
            Random rnd = new Random();
            string palabra = palabras[rnd.Next(0, palabras.Length)], palabra_oculta, input;            
            int intentos = 3;           

            palabra_oculta = Oculta_letras(palabra);            

            while(intentos > 0 && !Estan_todas_mostradas(palabra_oculta))
            {
                Console.WriteLine("{0}   intentos:{1}", palabra_oculta, intentos);

                Console.Write("Introduce una letra o resuelve la palabra:");
                input =  Console.ReadLine();

                if (input.Length == 1)
                {
                    if (palabra.ToLower().Contains(input.ToLower()))
                    {
                        Muestra_letras(ref palabra_oculta, palabra.ToLower(), input.ToLower());
                    }
                    else
                    {
                        Console.WriteLine("Lo siento la palabra no contiene la letra {0}, vuelve a intentarlo", input);
                        intentos--;
                    }
                }
                else
                {
                    if (palabra.ToLower().Equals(input.ToLower()))
                    {
                        Console.WriteLine("ENHORABUENA! Has adivinado la palabra {0} en {1} intentos", palabra, (3 - intentos) + 1);
                        intentos = 0;
                    }
                    else
                    {
                        Console.WriteLine("Lo siento, la palabra que buscamos no es {0}, vuelve a intentarlo", input);
                        intentos--;
                    }
                }
            }

            if (Estan_todas_mostradas(palabra_oculta))
                Console.WriteLine("ENHORABUENA! Has adivinado la palabra {0} en {1} intentos", palabra, (3 - intentos) + 1);

            Console.ReadKey();
        }
    }
}