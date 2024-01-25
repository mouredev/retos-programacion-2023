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

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reto__6
{
    internal class Program
    {

        static void Main(string[] args)
        {
            string jugador1 = "jugador1";
            string jugador2 = "jugador2";
     

            int victoriasJugador1 = 0;
            int victoriasJugador2 = 0;

            // Bucle para jugar múltiples rondas
            while (true)
            {
                Console.WriteLine("\nNueva ronda:");

                // Solicitar jugadas de los jugadores
                Console.Write("Jugador 1 elige: Piedra, Papel, Tijera, Lagarto o Spock: ");
                string jugadaJugador1 = Console.ReadLine().ToUpper();

                Console.Write("Jugador 2 elige: Piedra, Papel, Tijera, Lagarto o Spock: ");
                string jugadaJugador2 = Console.ReadLine().ToUpper();

                // Validar las jugadas y determinar el ganador
                string resultado = DeterminarGanador(jugadaJugador1, jugadaJugador2);

                // Mostrar el resultado de la ronda
                Console.WriteLine($"Resultado: {resultado}");

                // Actualizar el contador de victorias
                if (resultado == jugador1)
                    victoriasJugador1++;
                else if (resultado == jugador2)
                    victoriasJugador2++;

                // Preguntar si los jugadores quieren jugar otra ronda
                Console.Write("\n¿Quieren jugar otra ronda? (Sí/No): ");
                string respuesta = Console.ReadLine().ToUpper();

                if (respuesta != "SI")
                    break; // Salir del bucle si la respuesta no es "Sí"
            }

            // Mostrar el resultado final
            Console.WriteLine($"\nResultados finales:");
            Console.WriteLine($"Jugador 1: {victoriasJugador1} victorias");
            Console.WriteLine($"Jugador 2: {victoriasJugador2} victorias");

            if (victoriasJugador1 > victoriasJugador2)
                Console.WriteLine("Jugador 1 es el ganador!");
            else if (victoriasJugador2 > victoriasJugador1)
                Console.WriteLine("Jugador 2 es el ganador!");
            else
                Console.WriteLine("¡Empate!");

            // Esperar a que el usuario presione una tecla antes de salir
            Console.ReadKey();
        }

        // Función para determinar el ganador de una ronda
        static string DeterminarGanador(string jugada1, string jugada2)
        {
            if ((jugada1 == "PIEDRA" && (jugada2 == "LAGARTO" || jugada2 == "TIJERA")) ||
                (jugada1 == "PAPEL" && (jugada2 == "PIEDRA" || jugada2 == "SPOCK")) ||
                (jugada1 == "TIJERA" && (jugada2 == "PAPEL" || jugada2 == "LAGARTO")) ||
                (jugada1 == "LAGARTO" && (jugada2 == "PAPEL" || jugada2 == "SPOCK")) ||
                (jugada1 == "SPOCK" && (jugada2 == "PIEDRA" || jugada2 == "TIJERA")))
            {
                return "jugador1";
            } else if ((jugada2 == "PIEDRA" && (jugada1 == "LAGARTO" || jugada1 == "TIJERA")) ||
                (jugada2 == "PAPEL" && (jugada1 == "PIEDRA" || jugada1 == "SPOCK")) ||
                (jugada2 == "TIJERA" && (jugada1 == "PAPEL" || jugada1 == "LAGARTO")) ||
                (jugada2 == "LAGARTO" && (jugada1 == "PAPEL" || jugada1 == "SPOCK")) ||
                (jugada2 == "SPOCK" && (jugada1 == "PIEDRA" || jugada1 == "TIJERA")))

                {
                return "jugador2";
            } else {
                return "Empate";
            }
            }
    }

}