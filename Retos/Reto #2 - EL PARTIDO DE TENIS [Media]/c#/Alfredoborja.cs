using System;
using System.Runtime.InteropServices.WindowsRuntime;
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

namespace PartidoTenis
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] secuencias = { "P1", "P2", "P2", "P1", "P1", "P2", "P2","P1","P1","P1"};
            Game game = new Game(secuencias);
        }
    }

    public class Game
    {
        public string[] Secuencia { get; set; }

        public Game(string[] secuencia)
        {
            Secuencia = secuencia;
            comenzar();
        }
        public void comenzar()
        {
            int unidadesP1 = 0;
            int unidadesP2 = 0;
            bool empate = false;
            for(int i = 0; i < Secuencia.Length; i++)
            {
                if(Secuencia[i].ToUpper() == "P1")
                {
                    if(unidadesP1 >= 30)
                    {
                        unidadesP1 += 10;                      
                    }
                    else
                    {
                        unidadesP1 += 15;
                    }
            
                }
                else if (Secuencia[i].ToUpper() == "P2")
                {
                    if (unidadesP2 >= 30)
                    {
                        unidadesP2 += 10;
                    }
                    else
                    {
                        unidadesP2 += 15;
                    }
                }
                else
                {
                    imprimir("Jugador invalido: " + Secuencia[i]);
                    break;
                }
               
                if(unidadesP1 == unidadesP2 && unidadesP1 >= 40)
                {
                    imprimir("Deuce");
                    empate = true;
                }
                else if(unidadesP1 >= unidadesP2 && empate)
                {   
                    if (Math.Abs(unidadesP1 - unidadesP2) == 20)
                    {
                        imprimir("Jugador 1 gano!");
                        break;
                    }
                    else 
                    {
                        imprimir("Jugador 1 lleva la ventaja");                      
                    }
                } 
                else if(unidadesP1 <= unidadesP2 && empate)
                {
                    if (Math.Abs(unidadesP1 - unidadesP2) == 20)
                    {
                        imprimir("Jugador 2 gano!");
                        break;
                    }
                    else
                    {
                        imprimir("Jugador 2 lleva la ventaja");
                    }
                }
                else if (unidadesP1 > 40)
                {
                    imprimir("Jugador 1 Gana!");
                    break;
                }
                else if (unidadesP2 > 40)
                {
                    imprimir("Jugador 2 Gana!");
                    break;
                }
                else
                {
                    imprimir( (unidadesP1 == 0 ? "Love" : ""+unidadesP1+"") + " - " + (unidadesP2 == 0 ? "Love" : ""+unidadesP2+""));

                }
            }
        }

        public void imprimir(string mensaje)
        {
            Console.WriteLine(mensaje);
        }
    }


}
