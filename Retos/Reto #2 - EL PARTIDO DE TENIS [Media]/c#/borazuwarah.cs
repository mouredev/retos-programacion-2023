using System;
using System.Collections.Generic;


namespace Reto2CSharp
{
    internal class Program
    {
        public static string _player1Mark = "Love";
        public static string _player2Mark = "Love";
        public static int _ventaje = 0;

        static void Main(string[] args)
        {
            List<string> points = new List<string> { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };

            foreach (var x in points)
            {
                ProccessPoint(x);
            }
            Console.ReadLine();
        }
        /// <summary>
        /// proccess point
        /// </summary>
        /// <param name="point"></param>
        public static void ProccessPoint(string point)
        {
            if (point.Contains("1"))
            {
                if (_player1Mark == "Love")
                    _player1Mark = "15";
                else if (_player1Mark == "15")
                    _player1Mark = "30";
                else if (_player1Mark == "30")
                    _player1Mark = "40";
                else if (_player1Mark == "40")
                {
                    if (_player2Mark == "40")
                        _player1Mark = "Ventaja";
                    else
                        _player1Mark = "Victoria";
                }
            }
            else
            {
                if (_player2Mark == "Love")
                    _player2Mark = "15";
                else if (_player2Mark == "15")
                    _player2Mark = "30";
                else if (_player2Mark == "30")
                    _player2Mark = "40";
                else if (_player2Mark == "40")
                {
                    if (_player1Mark == "40")
                        _player2Mark = "Ventaja";
                    else
                        _player2Mark = "Victoria";
                }
            }
            ShowResult();
        }


        /// <summary>
        /// Show results
        /// </summary>
        public static void ShowResult()
        {
            if (_player1Mark == "40" && _player2Mark == "40")
            {
                _ventaje = 0;
                Console.WriteLine($"Deuce");
            }
            else if (_player1Mark == "Ventaja" && _ventaje == 0)
            {
                Console.WriteLine($"Ventaja Player 1");
                _ventaje++;
            }
            else if (_player2Mark == "Ventaja" && _ventaje == 0)
            {
                Console.WriteLine($"Ventaja `player 2");
                _ventaje++;
            }
            else if (_player1Mark == "Ventaja" && _ventaje == 1)
                Console.WriteLine($"Player 1 win");
            else if (_player2Mark == "Ventaja" && _ventaje == 1)
                Console.WriteLine($"Player 2 win");
            else
                Console.WriteLine($"{_player1Mark} - {_player2Mark}");
        }
    }
}
