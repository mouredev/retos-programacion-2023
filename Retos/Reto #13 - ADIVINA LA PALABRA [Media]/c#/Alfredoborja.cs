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
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

using System;
using System.Collections.Generic;
using System.Net.Http;

namespace AdivinaPalabra
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Game game = new Game("parangacutiminicuaro");
            game.iniciar();
        }
    }

    public class Game
    {
        public string PalabraRespuesta { get; set; }
        public String PalabraConGuiones { get; set; }
        public char[] Letras { get; set; }
        public int Intentos { get; set; }

        public Game(string palabra)
        {
            PalabraRespuesta = palabra.ToLower();
            Intentos = 3;
            splitString();
        }

        public void iniciar()
        {
            while (Intentos > 0)
            {
                Console.WriteLine("Escribe una letra: ");
                string respuesta = Console.ReadLine();
                if(respuesta != "") sustituirLetras(respuesta.ToLower());
                if (PalabraRespuesta == PalabraConGuiones)
                {
                    Console.WriteLine("Fin del juego, tu ganaste!");
                    return;
                }
            }
            Console.WriteLine("Fin del juego, perdiste!");
        }
        public void splitString()
        {
            Letras = PalabraRespuesta.ToCharArray();
            int letrasOcultas = (int)(Letras.Length * 0.60);
            for (int i = 1; letrasOcultas >= i; i++)
            {
                Random ran = new Random();
                int posicionAleatoria = ran.Next(0, Letras.Length-1);
                Letras[posicionAleatoria] = '_';
            }
            mostrarScore();
        }

        public void mostrarScore()
        {
            PalabraConGuiones = new String(Letras);
            Console.WriteLine(PalabraConGuiones);      
            Console.WriteLine("Intentos restantes: " + Intentos);
        }

        public void sustituirLetras(string letra)
        {
            var posiciones = encontrarLetras(letra);   
            foreach(var posicion in posiciones)
            {
                Letras[posicion] = Convert.ToChar(letra);
            }
            mostrarScore();
        }

        public List<int> encontrarLetras(string letra)
        {
            List<int> posiciones = new List<int>();
            int posicion = PalabraRespuesta.IndexOf(letra);
            if (posicion == -1) restarIntentos();
            while (posicion != -1)
            {
                posiciones.Add(posicion);
                posicion = PalabraRespuesta.IndexOf(letra, posicion + 1);
            }
            return posiciones;
        }

        public void restarIntentos()
        {
            Intentos--;
        }


    }


}
