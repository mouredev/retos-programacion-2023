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

using System;

namespace deathwing696
{
    public class deathwing696
    {
        public void Modifica_marcador(ref string marcador, bool es_p1)
        {
            string[] tanteo = marcador.Split('-');
            string punto;

            if (es_p1 == true)
                punto = tanteo[0].Trim();
            else
                punto = tanteo[1].Trim();

            switch (punto)
            {
                case "Love":
                    if (es_p1 == true)
                        marcador = String.Format("15 - {0}", tanteo[1]);
                    else
                        marcador = String.Format("{0} - 15", tanteo[0]);
                    break;

                case "15":
                    if (es_p1 == true)
                        marcador = String.Format("30 - {0}", tanteo[1]);
                    else
                        marcador = String.Format("{0} - 30", tanteo[0]);
                    break;

                case "30":
                    if (es_p1 == true)
                    {
                        if (tanteo[1].Trim() == "40")
                            marcador = "Deuce";
                        else
                            marcador = String.Format("40 - {0}", tanteo[1]);
                    }
                    else
                    {
                        if (tanteo[0].Trim() == "40")
                            marcador = "Deuce";
                        else
                            marcador = String.Format("{0} - 40", tanteo[0]);
                    }
                    break;

                case "40":
                    if (es_p1 == true)
                        marcador = "Ha ganado P1";
                    else
                        marcador = "Ha ganado P2";
                    break;
                case "Deuce":
                    if (es_p1 == true)
                        marcador = "Ventaja P1";
                    else
                        marcador = "Ventaja P2";
                    break;

                case "Ventaja P1":
                    if (es_p1 == true)
                        marcador = "Ha ganado P1";
                    else
                        marcador = "Deuce";
                    break;

                case "Ventaja P2":
                    if (es_p1 == false)
                        marcador = "Ha ganado P2";
                    else
                        marcador = "Deuce";
                    break;

                default:
                    break;
            }
        }

        public static void Main(string[] args)
        {
            deathwing696 clase = new deathwing696();
            string cadena = "[P1, P1, P2, P2, P1, P2, P1, P1]";
            cadena = cadena.Replace("[", "");
            cadena = cadena.Replace("]", "");
            cadena = cadena.Replace(",", "");
            string[] array = cadena.Split(' ');
            string marcador = "Love - Love";

            for (int i = 0; i < array.Length; i++)
            {
                if (array[i] == "P1")
                    clase.Modifica_marcador(ref marcador, true);
                else if (array[i] == "P2")
                    clase.Modifica_marcador(ref marcador, false);

                Console.WriteLine(marcador);

            }

            Console.ReadKey();
        }
    }