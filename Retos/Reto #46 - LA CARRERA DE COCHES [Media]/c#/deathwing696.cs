/*
 * Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
 *   
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace reto46
{
    public class Reto46
    {        
        static void Main(string[] args)
        {
            List<List<string>> circuito;

            Configura_circuito(out circuito);

            Console.Write("Coche1:");
            Dibujar_circuito(circuito[0]);
            Console.Write("Coche2:");
            Dibujar_circuito(circuito[1]);

            while (!Ha_acabado(circuito))
            {
                Console.Write("Coche1:");
                Mover(circuito[0]);
                Console.Write("Coche2:");
                Mover(circuito[1]);
            }

            Console.ReadKey();
        }

        static private void Configura_circuito(out List<List<string>>circuito)
        {
            Random random = new Random();
            int largo_pista = random.Next(5, 15), num_arboles;
            List<string> list = new List<string>();

            circuito = new List<List<string>>()
            { 
                new List<string> {"M"},
                new List<string> {"M"}
            };

            for (int i = 0; i < 2; i++)
            {
                for (int j = 1; j < largo_pista; j++)
                {
                    circuito[i].Add("_");
                }
            }

            num_arboles = random.Next(0, 4);

            for (int i = 0; i < num_arboles; i++)
            {
                while (true)
                {
                    int num = random.Next(0, largo_pista);

                    if (circuito[0][num] != "A" && circuito[0][num] != "M")
                    {
                        circuito[0][num] = "A";
                        break;
                    }
                }
            }

            num_arboles = random.Next(0, 4);

            for (int i = 0; i < num_arboles; i++)
            {
                while (true)
                {
                    int num = random.Next(0, largo_pista);

                    if (circuito[1][num] != "A" && circuito[1][num] != "M")
                    {
                        circuito[1][num] = "A";
                        break;
                    }
                }
            }

            circuito[0][circuito[0].Count - 1] = "C";
            circuito[1][circuito[1].Count - 1] = "C";
        }

        static private void Dibujar_circuito(List<string> circuito)
        {
            foreach (var item in circuito)
            {
                Console.Write(item);
            }

            Console.WriteLine();
        
        }

        static private bool Ha_acabado(List<List<string>> circuito)
        {
            return (circuito[0][0] == "C" || circuito[1][0] == "C");
        }

        static void Mover(List<string> circuito)
        {
            Random random = new Random();
            int movimiento = random.Next(1, 4), posicion_coche = 0;
            bool modificar;

            for (int i = 0; i < circuito.Count; i++)
            {
                if (circuito[i] == "C")
                {
                    posicion_coche = i;
                    break;
                }
            }

            if (posicion_coche - movimiento < 0)
            {
                circuito[0] = "C";
                modificar = false;
            }
            else if (circuito[posicion_coche - movimiento] == "A")
            {
                circuito[posicion_coche - movimiento] = "O";
                modificar = true;
            }
            else 
            {
                circuito[posicion_coche - movimiento] = "C";
                modificar = false;
            }
            
            circuito[posicion_coche] = "_";            

            Dibujar_circuito(circuito);

            if (modificar)
            {
                circuito[posicion_coche - movimiento] = "A";
                circuito[posicion_coche] = "C";
            }

        }
    }
}