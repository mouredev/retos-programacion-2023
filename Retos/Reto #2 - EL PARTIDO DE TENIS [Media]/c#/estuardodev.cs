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

using System;

class estuardodev
{
   public static void Main(String[] args)
    {
        string[] Plays = { "P1", "P1", "P2", "P1", "P2", "P2", "P2"};
        GameTennis(Plays);

    }

    public static void GameTennis(string[] Plays)
    {
        Dictionary<int, string> points = new Dictionary<int, string>
        {
            {0, "Love" },
            {1, "Deuce" }
        };

        int points_P1 = 0;
        int points_P2 = 0;

        foreach (string p in Plays)
        {

            switch (p)
            {
                case "P1":
                    if (points_P1 < 30)
                    {
                        points_P1 = points_P1 + 15;
                    }
                    else
                    {
                        points_P1 = points_P1 + 10;
                    }
                    break;
                case "P2":
                    if (points_P2 < 30)
                    {
                        points_P2 = points_P2 + 15;
                    }
                    else
                    {
                        points_P2 = points_P2 + 10;
                    }
                    break;
            }

           
            if(points_P1 == 0)
            {
                Console.WriteLine(points[0] + " - " + points_P2 + " - (Ventaja P2)");
            } else if (points_P2 == 0)
            {
                Console.WriteLine(points_P1 + " - " + points[0] + " - (Ventaja P1)");
            } else if (points_P1 == points_P2)
            {
                Console.WriteLine(points[1]);
            } else
            {
                if(points_P1 < points_P2)
                {
                    Console.WriteLine(points_P1 + " - " + points_P2 + " - (Ventaja P2)");
                }
                else
                {
                    Console.WriteLine(points_P1 + " - " + points_P2 + " - (Ventaja P1)");
                }
                
            }
        }

        if(points_P1 > points_P2)
        {
            Console.WriteLine("Ganador P1");
        } else if(points_P2 < points_P1)
        {
            Console.WriteLine("Ganador P2");
        }
        else
        {
            Console.WriteLine(points[1]);
        }

    }
}
