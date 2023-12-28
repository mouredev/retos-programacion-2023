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
    * - Consulta las reglas del juego si tienes dudas sobre el sistema de unidades.   
*/

namespace challenge_2
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] points = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
            Console.WriteLine(game(points));
        }

        static string game(string[] points)
        {
            if (points.Length != 8 && points.Length % 2 != 0)
            {
                return "Faltan puntos";
            }

            foreach (var point in points)
            {
                if (point != "P1" && point != "P2")
                {
                    return "Uno o más de los valores de entrada son incorrectos";
                }
            }

            int p1_points = 0, p2_points = 0;
            var system_points = new Dictionary<int, string>()
            {
                {0, "Love"},
                {1, "15"},
                {2, "30"},
                {3, "40"}
            };

            foreach (var point in points)
            {
                var x = (point == "P1") ? p1_points++ : p2_points++;

                if ((p1_points + p2_points) < 6)
                {
                    Console.WriteLine($"{system_points[p1_points]} - {system_points[p2_points]}");
                }
                else if (p1_points == p2_points)
                {
                    Console.WriteLine("Deuce");
                }
                else if (Math.Max(p1_points, p2_points) - Math.Min(p1_points, p2_points) == 2)
                {
                    Console.WriteLine($"Ha ganado el {point}");
                }
                else
                {
                    Console.WriteLine($"Ventaja {point}");
                }
            }

            return "---------------";
        }
    }
}