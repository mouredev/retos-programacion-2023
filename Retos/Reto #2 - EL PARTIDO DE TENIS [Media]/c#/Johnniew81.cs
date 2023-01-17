namespace Reto_Tenis
{
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
    class Program
    {
        static void Main(string[] args)
        {

            string partido, resultado;
            Console.WriteLine("");
            partido = Console.ReadLine();
            partido = partido.Replace(", ", string.Empty);
            partido = partido.Replace(",", string.Empty);
            resultado = machtennis(partido);
            Console.WriteLine(resultado);
        }
        static string machtennis(string partido)
        {
            string resultado = "";
            string[] puntuacion = { "love", "15", "30", "40", "40", "Ventaja" };
            int puntuacionP1, puntuacionP2;
            string tanto;
            puntuacionP1 = 0;
            puntuacionP2 = 0;
            for (int i = 0; i < partido.Length; i++)
            {
                tanto = partido.Substring(i, 2);
                if (tanto == "p1" || tanto == "P1")
                {
                    puntuacionP1++;
                }
                else if (tanto == "p2" || tanto == "P2")
                {
                    puntuacionP2++;
                }
                else
                {
                    resultado = "Meter los datos correctos \n ejemplo: p1,p2,p1,p2";
                    return resultado;
                }
                if ((puntuacionP1 == 3 && puntuacionP2 == 3) || (puntuacionP1 == 5 && puntuacionP2 == 5))
                {

                    puntuacionP1 = 4;
                    puntuacionP2 = 4;
                    resultado += "Deuce\n";
                }
                else if ((puntuacionP1 == 6) || (puntuacionP1 == 4 && puntuacionP2 < 3))
                {
                    resultado += "GANADOR JUGADOR 1";
                    return resultado;
                }
                else if ((puntuacionP2 == 6) || (puntuacionP2 == 4 && puntuacionP1 < 3))
                {
                    resultado += "GANADOR JUGADOR 2";
                    return resultado;
                }
                else
                {
                    resultado += puntuacion[puntuacionP1] + " - " + puntuacion[puntuacionP2] + "\n";
                }
                i++;
            }
            resultado += "**** PARDIDO INACABADO****";
            return resultado;
        }
    }
}