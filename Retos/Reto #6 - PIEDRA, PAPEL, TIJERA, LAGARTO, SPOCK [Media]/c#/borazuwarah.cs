/*

 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
/*
 Las tijeras cortan el papel.
El papel cubre la piedra.
La piedra aplasta el lagarto.
El lagarto envenena a Spock.
Spock aplasta las tijeras.
Las tijeras decapitan el lagarto.
El lagarto se come el papel.
El papel refuta a Spock.
Spock vaporiza la piedra.
La piedra aplasta a las tijeras.
 */


using System;


namespace Reto6
{
    internal class Program
    {
        public enum gameOption
        {
            Piedra,
            Papel,
            Tijera,
            Lagarto,
            Spok
        }
        public static int player1count = 0;
        public static int player2count = 0;
        static void Main(string[] args)
        {
            Game(gameOption.Piedra, gameOption.Tijera);
            Game(gameOption.Lagarto, gameOption.Spok);
            Game(gameOption.Piedra, gameOption.Spok);
            Game(gameOption.Tijera, gameOption.Spok);
            Game(gameOption.Papel, gameOption.Tijera);
            Game(gameOption.Piedra, gameOption.Lagarto);
            Game(gameOption.Piedra, gameOption.Tijera);
            Game(gameOption.Tijera, gameOption.Piedra);




            Console.WriteLine("Resultado:");
            if (player1count!=player2count)
                Console.WriteLine($"Player 1   {player1count} - {player2count}   player 2");
            else
                Console.WriteLine($"Player 1   EMPATA   player 2");
            Console.ReadKey();
        }

        /// <summary>
        /// Game
        /// </summary>
        /// <param name="player1"></param>
        /// <param name="player2"></param>
        public static void Game(gameOption player1, gameOption player2)
        { 
            switch (player1) 
            {
                case    gameOption.Piedra:
                    if (player2 == gameOption.Piedra)
                      //  Console.WriteLine("Empate");
                    if (player2 == gameOption.Tijera)
                        player1count++;
                    if (player2 ==gameOption.Papel)
                        player2count++;
                    if (player2 == gameOption.Lagarto)//La piedra aplasta el lagarto.
                        player1count++;
                    if (player2 == gameOption.Spok)//Spock vaporiza la piedra.
                        player2count++;
                    break;
                case gameOption.Tijera:
                    if (player2 == gameOption.Tijera)
                     //   Console.WriteLine("Empate");
                    if (player2 == gameOption.Piedra)
                        player2count++;
                    if (player2 == gameOption.Papel)
                        player1count++;
                    if (player2 == gameOption.Lagarto)//Las tijeras decapitan el lagarto.
                        player1count++;
                    if (player2 == gameOption.Spok) //Spock aplasta las tijeras.
                        player2count++;
                    break;
                case gameOption.Papel:
                    if (player2 == gameOption.Papel)
                    //    Console.WriteLine("Empate");
                    if (player2 == gameOption.Tijera)
                        player2count++;
                    if (player2 == gameOption.Piedra)
                        player1count++;
                    if (player2 == gameOption.Lagarto)//El lagarto se come el papel.
                        player2count++;
                    if (player2 == gameOption.Spok)//El papel refuta a Spock.
                        player1count++;
                    break;
                case gameOption.Lagarto:
                    if (player2 == gameOption.Lagarto)
                    //    Console.WriteLine("Empate");
                    if (player2 == gameOption.Tijera)//Las tijeras decapitan el lagarto.
                        player2count++;
                    if (player2 == gameOption.Piedra)//La piedra aplasta el lagarto.
                        player2count++;
                    if (player2 == gameOption.Papel)//El lagarto se come el papel.
                        player1count++;
                    if (player2 == gameOption.Spok)//El lagarto envenena a Spock.
                        player1count++;
                    break;
                case gameOption.Spok:
                    if (player2 == gameOption.Spok)
                    //    Console.WriteLine("Empate");
                    if (player2 == gameOption.Lagarto)//El lagarto envenena a Spock.
                        player2count++;
                    if (player2 == gameOption.Piedra)//Spock vaporiza la piedra.
                        player1count++;
                    if (player2 == gameOption.Papel)//El papel refuta a Spock.
                        player1count++;
                    if (player2 == gameOption.Tijera)//Spock aplasta las tijeras.
                        player1count++;
                    break;
                default:
                    Console.WriteLine("");
                    break;

            }
        }
    }
}
