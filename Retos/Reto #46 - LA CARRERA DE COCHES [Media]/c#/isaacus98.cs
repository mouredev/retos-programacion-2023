using System.IO;

namespace RetosProgramacion
{
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
     */

    internal class Program
    {
        static string[] iconoCoche = { "1", "2" };

        static void Main(string[] args)
        {
            /*
             * M = Meta
             * A = Arbol
             * E = Choque con arbol
             * 1 = Coche 1
             * 2 = Coche 2
             */

            Console.WriteLine("Introduzca la longitud del circuito: ");
            int longitud = int.Parse(Console.ReadLine());
            int posmover;
            int[] posicionesCoches = { longitud - 1, longitud - 1 };
            bool[] saltarTurno = { false, false };
            string[,] circuito = GenerarCircuito(longitud);
            
            ImprimirCircuito(circuito);

            Thread.Sleep(5000);
            
            Random rnd = new Random();
            while (!CarreraFinalizada(posicionesCoches))
            {
                for (int i = 0; i < circuito.GetLength(0); i++)
                {
                    if (!saltarTurno[i])
                    {
                        if (posicionesCoches[i] != 0)
                        {
                            posmover = rnd.Next(1, 4);

                            if ((posicionesCoches[i] - posmover) <= 0)
                            {
                            // Meta
                                if (circuito[i, posicionesCoches[i]] == "E")
                                    circuito[i, posicionesCoches[i]] = "A";
                                else
                                    circuito[i, posicionesCoches[i]] = "_";

                                if ((posicionesCoches[i] - posmover) == 0)
                                {
                                    posicionesCoches[i] -= posmover;
                                    circuito[i, posicionesCoches[i]] = iconoCoche[i];
                                }
                                else
                                {
                                    posicionesCoches[i] -= posicionesCoches[i];
                                    circuito[i, posicionesCoches[i]] = iconoCoche[i];
                                }

                            } 
                            else if (circuito[i, posicionesCoches[i] - posmover] == "A")
                            {
                            // Choque arbol
                                saltarTurno[i] = true;
                                if (circuito[i, posicionesCoches[i]] == "E")
                                    circuito[i, posicionesCoches[i]] = "A";
                                else
                                    circuito[i, posicionesCoches[i]] = "_";

                                posicionesCoches[i] -= posmover;
                                circuito[i, posicionesCoches[i]] = "E";
                            }
                            else if (circuito[i, posicionesCoches[i] - posmover] == "_")
                            {
                            // Avance coche
                                if (circuito[i, posicionesCoches[i]] == "E")
                                    circuito[i, posicionesCoches[i]] = "A";
                                else
                                    circuito[i, posicionesCoches[i]] = "_";

                                posicionesCoches[i] -= posmover;
                                circuito[i, posicionesCoches[i]] = iconoCoche[i];
                            }
                        }
                    }
                    else
                    {
                        saltarTurno[i] = false;
                    }
                }

                ImprimirCircuito(circuito);

                if (posicionesCoches[0] == 0 && posicionesCoches[1] == 0)
                    Console.WriteLine("Empate!!!");

                if (posicionesCoches[0] == 0)
                    Console.WriteLine("Ganador coche 1");

                if (posicionesCoches[1] == 0)
                    Console.WriteLine("Ganador coche 2");

                Thread.Sleep(1000);
            }
            
        }

        static string[,] GenerarCircuito(int longitud)
        {
            Random rnd = new Random();
            string[,] circuito = new string[2, longitud];
            int probabilidadArbol = 20;
            
            for (int i = 0; i < circuito.GetLength(0); i++)
            {
                for (int j = 0; j < circuito.GetLength(1); j++)
                {
                    if (j == 0)
                    {
                        circuito[i, j] = "M";
                    } 
                    else
                    {
                        int probalidad = rnd.Next(0, 101);
                        if (probalidad >= 0 && probalidad <= probabilidadArbol)
                            circuito[i, j] = "A";
                        else
                            circuito[i, j] = "_";
                    }
                }

                circuito[i, circuito.GetUpperBound(1)] = iconoCoche[i];
            }

            return circuito;
        }

        static void ImprimirCircuito(string[,] circuito)
        {
            for(int i = 0;i < circuito.GetLength(0); i++)
            {
                Console.WriteLine("Pista del jugador " + (i+1));
                for(int j = 0;j < circuito.GetLength(1); j++)
                {
                    Console.Write(circuito[i,j]);
                }
                Console.WriteLine();
                Console.WriteLine();
            }
        }

        static bool CarreraFinalizada(int[] posicionesCoche)
        {
            return posicionesCoche[0] == 0 || posicionesCoche[1] == 0;
        }
    }
}