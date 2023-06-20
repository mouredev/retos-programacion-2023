using System.Text;

namespace Reto2
{
    internal class Guillermoqnk
    {
        private static int player1 = 0;
        private static int player2 = 0;

        static void Main(string[] args)
        {
            while (((player1 < 4) && (player2 < 4)) || (Math.Abs(player1 - player2) < 2))
            {
                string input;

                input = Console.ReadLine();

                if (!input.Any())
                {
                    Console.WriteLine("You can't send empy input");
                }
                else if (input.Length > 2)
                {
                    Console.WriteLine("That's not a valid input, input must be compound be 2 characters");
                }
                else
                {
                    if (!Char.IsLetter(Convert.ToChar(input[0])))
                    {
                        Console.WriteLine("The first character must be a letter");
                    }
                    else
                    {
                        if (!Char.IsNumber(Convert.ToChar(input[1])))
                        {
                            Console.WriteLine("The second character must be a number");
                        }
                        else
                        {
                            if (input[0] is not 'P')
                            {
                                Console.WriteLine("Player identifier must be a P");
                            }
                            else
                            {
                                if (Convert.ToInt16(input[1]) is 1 || Convert.ToInt16(input[1]) is 2)
                                {
                                    Console.WriteLine("Player's number must be 1 or 2");
                                }
                                else
                                {
                                    if (input is "P1")
                                        player1++;
                                    else if (input is "P2")
                                        player2++;

                                    ShowPoints();
                                }
                            }
                        }
                    }
                }

            }
        }

        private static void ShowPoints()
        {
            Dictionary<int, string> keyValuePairsPoints = new Dictionary<int, string>()
            {
                {0, "Love" },
                {1, "15" },
                {2, "30" },
                {3, "40" },
            };

            StringBuilder output  = new StringBuilder();

            if(player1 < 4 && player2 < 4)
            {
                output.Append($"{keyValuePairsPoints[player1].ToString()} - {keyValuePairsPoints[player2].ToString()}");
            }
            else
            {
                if(player1 - player2 == 1)
                {
                    output.Clear().Append("Advantage P1");
                }
                else if(player2 - player1 == 1)
                {
                    output.Clear().Append("Advantage P2");
                }
                else if (player1 - player2 >= 2)
                {
                    output.Clear().Append("Player 1 wins!!");
                }
                else if (player2 - player1 >= 2)
                {
                    output.Clear().Append("Player 2 wins!!");
                }
                else if(player1 == player2)
                {
                    output.Clear().Append("Deuce");
                }
            }

            Console.WriteLine(output.ToString());
        }
    }
}