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
            string[] puntuacion = { "love", "15", "30", "40"};
            int i = 0;
            int puntuacionP1, puntuacionP2;
            bool error, final;
            error= final =false;
            string tanto;
            puntuacionP1 = 0;
            puntuacionP2 = 0;
            while((error == false && final == false) && (i <partido.Length))
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
                    error = true;
                }
                if ((puntuacionP1 > 2 || puntuacionP2 > 2) && error == false)
                { 
                    if (puntuacionP1 > 2 && puntuacionP2 > 2)
                    {
                        if (Math.Abs(puntuacionP1 - puntuacionP2) == 2)
                        {
                            final = true;
                            if (i < (partido.Length - 2))
                            {
                                resultado += "**** ANOTACION ERRONEA MAS PUNTOS DE LOS PERMITIDOS ****";
                            }
                            else
                            { 
                                resultado += puntuacionP1 > puntuacionP2 ? "GANADOR JUGADOR 1" : "GANADOR JUGADOR 2";
                            }

                        }
                        else { 
                            resultado += (puntuacionP1 == puntuacionP2) ? "Deuces\n" : (puntuacionP1 > puntuacionP2) ? "Ventaja jugador 1\n" : "Ventaja jugador 2\n";
                        }
                    }
                    else if ((puntuacionP1 > 3 && puntuacionP2 < 3) || (puntuacionP1 < 3 && puntuacionP2 > 3))
                    {
                        final = true;
                        if (i < (partido.Length - 2))
                        {
                            resultado += "**** ANOTACION ERRONEA MAS PUNTOS DE LOS PERMITIDOS ****";
                        }else
                        { 
                            resultado += puntuacionP1 > puntuacionP2 ? "GANADOR JUGADOR 1" : "GANADOR JUGADOR 2";
                        }
                    }
                    else
                    {
                        resultado += puntuacion[puntuacionP1] + " - " + puntuacion[puntuacionP2] + "\n";
                    }
                }
                else
                {
                    resultado += error == false?puntuacion[puntuacionP1] + " - " + puntuacion[puntuacionP2] + "\n":"\n *** ERROR ***";
                }
                i +=2;
            }
            if (error==false && final == false) resultado += "**** PARDIDO INACABADO****";
            return resultado;
        }
    }
}