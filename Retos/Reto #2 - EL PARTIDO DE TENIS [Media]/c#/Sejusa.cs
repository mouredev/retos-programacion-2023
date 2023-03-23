/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

namespace EL_PARTIDO_DE_TENIS
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Start.MatchGame();
        }
    }
}

//Creamos una clase con su método para ejecutarlo en el método principal "Main".
namespace EL_PARTIDO_DE_TENIS
{
    internal class Start
    {
        public static void  MatchGame()
        {
            Console.WriteLine("P1 = LOVE\t" +
                "P2 = LOVE");

            //Pedimos al usuario que pulse enter. Si no lo hace mostramos un mensaje de error.
            while (true)
            {
                Console.WriteLine("Pulse ENTER para continuar.");
                var input = Console.ReadLine();
                if (input != "")
                {
                    Console.WriteLine("¡Uepa, debes de pulsar ENTER!");
                }
                else
                {
                    //Creamos una matriz donde se guardan el orden de las anotaciones.
                    string[] points = { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };
                    int puntuacion1 = 0;
                    int puntuacion2 = 0;

                    foreach (string point in points)
                    {
                        /*Código lógico para evaluar si ha metido P1 o P2 según el orden de la matriz.
                        Una vez evaluado esto, se procede a evaluar los puntos del jugador anotador y 
                        dependiendo de los puntos que lleven, se ejecuta una acción o otra.*/

                        if (point == "P1")
                        {
                            if (puntuacion1 == 0)
                            {
                                puntuacion1 += 15;
                                Console.WriteLine("P1 = " + puntuacion1 + " P2 = " + puntuacion2);
                            }
                            else if (puntuacion1 == 15)
                            {
                                puntuacion1 += 15;
                                Console.WriteLine("P1 = " + puntuacion1 + " P2 = " + puntuacion2);
                            }
                            else if (puntuacion1 == 30)
                            {
                                puntuacion1 += 10;
                                Console.WriteLine("P1 = " + puntuacion1 + " P2 = " + puntuacion2);
                            }
                            else if (puntuacion1 == 40)
                            {
                                puntuacion1 += 5;
                                Console.WriteLine("Ventaja P1" + " P2 = " + puntuacion2);
                            }
                            else 
                            {
                                Console.WriteLine("¡Ha ganado P1!");
                            }
                        }

                        if (point == "P2")
                        {
                            if (puntuacion2 == 0)
                            {
                                puntuacion2 += 15;
                                Console.WriteLine("P1 = " + puntuacion1 + " P2 = " + puntuacion2);
                            }
                            else if (puntuacion2 == 15)
                            {
                                puntuacion2 += 15;
                                Console.WriteLine("P1 = " + puntuacion1 + " P2 = " + puntuacion2);
                            }
                            else if (puntuacion2 == 30)
                            {
                                puntuacion2 += 10;
                                Console.WriteLine("P1 = " + puntuacion1 + " P2 = " + puntuacion2);
                            }
                            else if (puntuacion2 == 40)
                            {
                                puntuacion2 += 5;
                                Console.WriteLine("P1 = " + puntuacion1 + " Ventaja P2");
                            }
                            else
                            {
                                Console.WriteLine("¡Ha ganado P2");
                            }
                        
                        //Si los dos jugadores llevan la misma cantidad de puntos, se ejecuta este código lógico.
                        if (puntuacion1 == puntuacion2)
                            {
                                Console.WriteLine("Deuce " + "P1 = " + puntuacion1 + " P2 = " + puntuacion2);
                            }
                        }
                    }
                }

            }
        }
    }
}
}
