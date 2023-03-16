using System;
using System.Collections.Generic;

namespace RetrosProgramacionSemanales
{
    internal class TecAlvarez
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
        static void Main(string[] args)
        {
            var p1 = 0;
            var p2 = 0;

            var strText = Console.ReadLine();
            if (strText != null && strText != "" && strText.StartsWith("[") && strText.EndsWith("]"))
            {
                strText = strText.ToUpper();
                foreach (var item in strText.Replace("[", "").Replace("]", "").Split(','))
                {
                    if (item.Trim() == "P1")
                    {
                        p1 ++;
                    }
                    else if (item.Trim() == "P2")
                    {
                        p2 ++;
                    } else
                    {
                        Console.WriteLine("Cadena con formato incorrecto.");
                        Console.ReadLine();
                        return;
                    }
                    List<string> strlist = new List<string>() {"Love", "15", "30", "40" };
                    var strP1 = "";
                    if (p1 <= 2) {
                          strP1 = strlist[p1];
                    }

                    var strP2 = "";
                    if (p2 <= 2) {
                        strP2 = strlist[p2];
                    }

                    if (p1 >= 3 || p2 >= 3)
                    {
                        if (p1 == 3 && p2 < 3) {
                            strP1 = "40";
                        } 
                        else if (p2 == 3 && p1 < 3) {
                            strP2 = "40";
                        } 
                        else if (p1 == p2) {
                            strP1 = "Deuce";
                            strP2 = "";
                        }
                        else if (p1 >= 5)
                        {
                            strP1 = "Ha ganado el P1";
                            strP2 = "";
                        }
                        else if (p2 >= 5)
                        {
                            strP1 = "Ha ganado el P2";
                            strP2 = "";
                        }
                        else if (p1 > p2) {
                            strP1 = "Ventaja P1";
                            strP2 = "";
                        }
                        else if (p1 < p2) {
                            strP1 = "Ventaja P2";
                            strP2 = "";
                        }
                    }
                    Console.WriteLine(strP1 + (strP2 != "" ? " - " + strP2 : ""));
                    if (p1 >= 5 || p2 >= 5)
                    {
                        break;
                    }
                }
            }
            else
            {
                Console.WriteLine("Cadena con formato incorrecto.");
            }
            Console.ReadLine();
        }
    }
}
