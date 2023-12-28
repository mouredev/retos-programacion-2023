namespace Reto13
{
    internal class Guillermoqnk
    {
        private static int regardingTries = 4;

        private static string? wordToShow;

        private static string? wordToGuess;

        private static char hiddenWordSymbol = '_';

        private static List<char> usedLetters = new List<char>();

        static void Main(string[] args)
        {
            PlayGame();
        }
        private static void DrawGame()
        {
            Console.Clear();

            DrawHangman();

            Console.WriteLine($"\n\nWord To Guess: {wordToShow}\n\n\n");

            Console.Write("Used letters: ");

            foreach(char letter in usedLetters)
            {
                Console.Write($"{letter}, ");
            }
        }

        private static void DrawHangman()
        {
            switch (regardingTries)
            {
                case 4:
                    Console.WriteLine("_________");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("_|_");
                    break;

                case 3:
                    Console.WriteLine("_________");
                    Console.WriteLine(" |     | ");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("_|_");
                    break;

                case 2:
                    Console.WriteLine("_________");
                    Console.WriteLine(" |     | ");
                    Console.WriteLine(" |     O ");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("_|_");
                    break;

                case 1:
                    Console.WriteLine("_________");
                    Console.WriteLine(" |     | ");
                    Console.WriteLine(" |     O ");
                    Console.WriteLine(" |    /|\\");
                    Console.WriteLine(" |");
                    Console.WriteLine("_|_");
                    break;

                case 0:
                    Console.WriteLine("_________");
                    Console.WriteLine(" |     | ");
                    Console.WriteLine(" |     O ");
                    Console.WriteLine(" |    /|\\");
                    Console.WriteLine(" |    / \\ ");
                    Console.WriteLine("_|_");
                    Console.WriteLine(" GAME OVER ");
                    break;

                default:
                    break;

            }
        }

        private static void GenerateWord()
        {
            int wordIndex = new Random().Next(0, words.Length);

            string word = words[wordIndex];

            wordToGuess = word;
            wordToShow = word;

            float hiddenWordPercentage = new Random().Next(4, 6);

            int hiddenWords = (int)Math.Round((double)((float)word.Length / 100) * (hiddenWordPercentage * 10), 0);

            bool generated = false;

            while (!generated)
            {
                int position = new Random().Next(0, word.Length);

                if (wordToShow[position] != hiddenWordSymbol)
                {
                    wordToShow = wordToShow.Remove(position,1).Insert(position, Convert.ToString(hiddenWordSymbol));

                    hiddenWords--;

                    if(hiddenWords == 0)
                    {
                        generated = true;
                    }
                }
            }
        }

        private static void CheckWord(char guessedLetter)

        {
            bool result = wordToGuess.Any(x => x == guessedLetter) ? true : false;

            bool keepChecking = true;

            int positionToStartChecking = 0;

            if (wordToGuess.IndexOf(guessedLetter) == -1)
            {
                Console.WriteLine("\n\nOps! That letter isn't in the word, someone is going to dead if you keep doing that...");

                Thread.Sleep(1500);

                regardingTries--;
            }
            else
            {
                while (keepChecking)
                {
                    int indexToChange = wordToGuess.IndexOf(guessedLetter, positionToStartChecking);

                    if (indexToChange != -1)
                    {
                        wordToShow = wordToShow!.Remove(indexToChange, 1).Insert(indexToChange, Convert.ToString(guessedLetter));

                        positionToStartChecking = indexToChange+1;
                    }
                    else
                    {
                        keepChecking = false;
                    }
                }

                Console.WriteLine("\nCorrect letter!!! :D");

                Thread.Sleep(1500);

            }

            usedLetters.Add(guessedLetter);
        }

        private static void Charging()
        {
            Thread.Sleep(500);

            Console.Write("\n.");

            Thread.Sleep(500);

            Console.Write(".");

            Thread.Sleep(500);

            Console.Write(".");

            Thread.Sleep(500);
        }

        private static void PlayGame()
        {
            bool win = false;
            bool startGame = false;

            Console.WriteLine(" WELCOME TO THE HANGMAN GAME \n\n");

            DrawHangman();

            string response = String.Empty;

            while(startGame == false)
            {
                Console.Clear();

                DrawHangman();


                Console.WriteLine("\n\nStart game? (Y/N)");

                response = Console.ReadLine();

                Charging();

                if(response?.ToUpper() == "Y" || response?.ToUpper() == "N")
                {
                    startGame= true;

                    Console.WriteLine("\n\nStarting game");

                    Thread.Sleep(1000);
                }
                else
                {
                    Console.WriteLine("\n\nThat's not a valid response try again with Y or N");

                    Thread.Sleep(1000);
                }
            }

            if(response.ToUpper() == "Y")
            {
                GenerateWord();

                while(win == false || regardingTries != 0)
                {
                    DrawGame();

                    Console.Write("\n\nType a letter: ");

                    Console.WriteLine(wordToGuess);

                    string input = Console.ReadLine();

                    try
                    {
                        char res = Convert.ToChar(input.ToLower());
                         
                        if (Char.IsLetter(res))
                        {
                            if (!usedLetters.Contains(Convert.ToChar(res)))
                            {
                                Charging();

                                CheckWord(Convert.ToChar(res));
                            }
                            else
                            {
                                Charging();

                                Console.WriteLine("\nYou've already used that word, but hangman keeps there...");

                                Thread.Sleep(1500);

                                regardingTries--;

                            }
                        }
                    }

                    catch(Exception ex)
                    {
                        Charging();

                        if(input != wordToGuess)
                        {
                            Console.WriteLine("\nThat's not the word, you've condemned the hangman :v");

                            Thread.Sleep(1500);

                            regardingTries--;
                        }
                        else
                        {
                            wordToShow = wordToGuess;
                        }

                    };

                    if(wordToGuess == wordToShow)
                    {
                        win= true;

                        Console.Clear();

                        Console.WriteLine($"\nHey!!! You guessed the word, that's amazing\n\nThe word was: {wordToGuess}");

                        Thread.Sleep(5000);

                        Console.WriteLine("\nSee ya!");

                        Environment.Exit(0);
                    }
                }
            }
            else
            {
                Console.WriteLine(" You are a bad guy :( ");

                Thread.Sleep(2000);

                Environment.Exit(0);
            }
        }

        static string[] words = { "apple", "bread", "chair", "drink", "empty", "field", "grape", "house", "iguana", "jelly", "kite", "lemon", "money", "night", "orange", "party", "queen", "river", "spoon", "table", "uncle", "voice", "water", "xerox", "yacht", "zebra", "amber", "beach", "candy", "denim", "elbow", "fossil", "ghost", "happy", "igloo", "jolly", "kitten", "laptop", "melon", "napkin", "oyster", "peanut", "quack", "rabbit", "salmon", "turtle", "umbrella", "valley", "window", "xyloid", "yogurt", "zipper", "apron", "banner", "carrot", "dragon", "effort", "feather", "goblin", "harvest", "insect", "jester", "kitten", "lizard", "mustard", "necklace", "oxygen", "potato", "quiver", "raptor", "saddle", "thunder", "unicorn", "vampire", "walnut", "xylene", "yellow", "zodiac", "anchor", "bonnet", "cricket", "diamond", "elephant", "feather", "goggles", "hammock", "island" };

    }
}
