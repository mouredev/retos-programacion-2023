using System;
using System.Collections.Generic;
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

namespace PierdraPapelTijera
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Jugadores> jugadores = new List<Jugadores>();
            jugadores.Add(new Jugadores { Jugador1 = "piedra", Jugador2 = "papel"});
            jugadores.Add(new Jugadores { Jugador1 = "spock", Jugador2 = "tijera" });
            jugadores.Add(new Jugadores { Jugador1 = "spock", Jugador2 = "lagarto" });

            Partida partida = new Partida(jugadores);
            partida.StartGame();
            Console.WriteLine(partida.ChooseWinner());
        }
    }

    public class Jugadores
    {
        public string Jugador1 { get; set; }
        public string Jugador2 { get; set; }
    }

    public class Partida
    {
        public List<Jugadores> _jugadores { get; set; }
        private int Player1Wins { get; set; }
        private int Player2Wins { get; set; }
        public Partida(List<Jugadores> jugadores)
        {
            _jugadores = jugadores;  
        }
        public enum tipos
        {
            piedra = 1,
            papel = 2,
            tijera = 3,
            lagarto = 4,
            spock = 5
        }

        public void StartGame()
        {   
            foreach (var jugador in _jugadores)
            {
                var a = jugador.Jugador1;
                var b = tipos.piedra;
                if ( jugador.Jugador1 == tipos.piedra.ToString())
                {
                    WithPiedra(jugador);
                }
                else if (jugador.Jugador1 == tipos.papel.ToString())
                {
                    WithPapel(jugador);
                }
                else if (jugador.Jugador1 == tipos.tijera.ToString())
                {
                    WithTijera(jugador);
                }
                else if(jugador.Jugador1 == tipos.lagarto.ToString())
                {
                    WithLagartija(jugador);
                }
                else if(jugador.Jugador1 == tipos.spock.ToString())
                {
                    WithSpock(jugador);
                }
            }
        }

        private void WithPiedra(Jugadores jugador)
        {
            var a = jugador.Jugador1;
            var b = (int)tipos.piedra;
            if (jugador.Jugador2 == tipos.tijera.ToString() || jugador.Jugador2 == tipos.lagarto.ToString())
            {
                Player1Wins++;
            }
            else if (jugador.Jugador2 == tipos.spock.ToString() || jugador.Jugador2 == tipos.papel.ToString())
            {
                Player2Wins++;
            }
        }
        private void WithPapel(Jugadores jugador)
        {
            if (jugador.Jugador2 == tipos.piedra.ToString() || jugador.Jugador2 == tipos.spock.ToString())
            {
                Player1Wins++;
            }
            else if (jugador.Jugador2 == tipos.tijera.ToString() || jugador.Jugador2 == tipos.lagarto.ToString())
            {
                Player2Wins++;
            }
        }
        private void WithTijera(Jugadores jugador)
        {
            if (jugador.Jugador2 == tipos.papel.ToString() || jugador.Jugador2 == tipos.lagarto.ToString())
            {
                Player1Wins++;
            }
            else if (jugador.Jugador2 == tipos.spock.ToString() || jugador.Jugador2 == tipos.piedra.ToString())
            {
                Player2Wins++;
            }
        }
        private void WithLagartija(Jugadores jugador)
        {
            if (jugador.Jugador2 == tipos.papel.ToString() || jugador.Jugador2 == tipos.spock.ToString())
            {
                Player1Wins++;
            }
            else if (jugador.Jugador2 == tipos.piedra.ToString() || jugador.Jugador2 == tipos.tijera.ToString())
            {
                Player2Wins++;
            }
        }
        private void WithSpock(Jugadores jugador)
        {
            if (jugador.Jugador2 == tipos.tijera.ToString() || jugador.Jugador2 == tipos.piedra.ToString())
            {
                Player1Wins++;
            }
            else if (jugador.Jugador2 == tipos.lagarto.ToString() || jugador.Jugador2== tipos.papel.ToString())
            {
                Player2Wins++;
            }
        }

        public string ChooseWinner()
        {
            if(Player1Wins > Player2Wins)
            {
                return "Jugador 1 gana";
            }
            else if (Player1Wins < Player2Wins)
            {
                return "Jugador 2 gana";
            }
            else
            {
                return "Tie";
            }
        }

    }
}
