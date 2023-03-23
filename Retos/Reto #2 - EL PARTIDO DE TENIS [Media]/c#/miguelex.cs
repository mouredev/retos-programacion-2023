using System;
using System.Collections.Generic;

namespace miguelex
{
    internal class Program
    {
        static void Main(string[] args)
        {
            TennisMatch(new List<string>() { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" });
            TennisMatch(new List<string>() { "P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2" });
        }

        private static void TennisMatch(List<String> players)
        {
            int p1Points = 0;
            int p2Points = 0;

            foreach (var player in players)

            {
                if (player.ToUpper() == "P1")
                {
                    p1Points++;
                }
                else if (player.ToUpper() == "P2")
                {
                    p2Points++;
                }
                else
                {
                    Console.WriteLine("Tanteo incorrecto");
                }

                if (p1Points == 4 && p2Points == 4)
                {
                    p1Points = 3;
                    p2Points = 3;
                }

                PrintScore(p1Points, p2Points);
            }
        }

        private static void PrintScore(int P1, int P2)
        {
            List<string> score = new List<string> { "Love", "15", "30", "40" };

            if (P1 == P2 && P1 == 3)
            {
                Console.WriteLine("\tDeuce");
            }
            else if (P1 == 4 && P2 == 3)
            {
                Console.WriteLine("\tVentaja P1");
            }
            else if (P2 == 4 && P1 == 3)
            {
                Console.WriteLine("\tVentaja P2");
            }
            else if (P1 == 5 && P1 - P2 == 2)
            {
                Console.WriteLine("\tGana P1");
            }
            else if (P2 == 5 && P2 - P1 == 2)
            {
                Console.WriteLine("\tGana P2");
            }
            else
            {
                Console.WriteLine("P1:\t {0} - {1} \t:P2", score[P1], score[P2]);
            }
        }
    }

}