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

 public class TenisMarker
    {
        //                   0      1   2     3     4            5       
        string[] textos = { "Love ", "15 ", "30 ", "40 ", "Deuce ", "Ventaja " };
        int[] points = { 0, 0 };
        bool playing = true;

        public string CountPoint(Players player) // recibe un emum solo por comodidad al ingresar datos de prueba
        {
            
            if (playing)
            {
                if (player == Players.P1)
                {
                    points[0]++;
                    if (points[0] == 4 && points[1] < 3)
                    {
                        playing = false;
                        return "Ha ganado el Player 1";
                    }

                }
                else if (player == Players.P2)
                {
                    points[1]++;
                    if (points[1] == 4 && points[0] < 3)
                    {
                        playing = false;
                        return "Ha ganado el Player 2";
                    }

                }
                else
                {
                    return "Entrada no valida";
                }
                if (points[0] == 3 && points[1] == 3 || points[0] == 5 && points[1] == 5)
                {
                    points[0] = 4;
                    points[1] = 4;
                    return textos[4];
                }
                if (points[0] == 5) return textos[5] + "P1 ";
                if (points[1] == 5) return textos[5] + "P2 ";
                if (points[0] > 5 )
                {
                    playing = false;
                    return "Ha ganado el Player 1";
                }
                if (points[1] > 5)
                {
                    playing = false;
                    return "Ha ganado el Player 2";
                }
                return textos[points[0]] + " " + textos[points[1]];
            }
            return "juego terminado resete el contador";
            
             

        }
        public string CountPoint(Players[] players) //  recibe un emum solo por comodidad al ingresar datos de prueba
        {
            foreach (Players player in players)
            {
                 Console.WriteLine (CountPoint(player));
                
            }
            return "cadena terminada";
        }

        public enum Players
        {
            P1, P2
        }
        public string reseteGame (){
            points[0]=0;
            points[1]=0;
            playing = true;
            return "el marcador se ha reseteado";
        }
        

    }
