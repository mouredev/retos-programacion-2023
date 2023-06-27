

int[] konamiCode = { (int)ConsoleKey.UpArrow,(int)ConsoleKey.UpArrow, (int)ConsoleKey.DownArrow, (int)ConsoleKey.DownArrow,
                             (int)ConsoleKey.LeftArrow, (int)ConsoleKey.RightArrow, (int)ConsoleKey.LeftArrow, (int)ConsoleKey.RightArrow,
                             (int)ConsoleKey.B, (int)ConsoleKey.A };

int[] userInput = new int[10];
int currentIndex = 0;

Console.WriteLine("Introduce el Código Konami:");

while (currentIndex < 10)
{
    ConsoleKeyInfo key = Console.ReadKey(true);
    userInput[currentIndex] = (int)key.Key;

    if (userInput[currentIndex] != konamiCode[currentIndex])
    {
        currentIndex = 0;
        Console.Clear();
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("Código incorrecto. Inténtalo de nuevo.");
        continue;
    }

    currentIndex++;

    if (currentIndex == 10)
    {
        Console.Clear();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("¡Código Konami introducido correctamente!");
    }
}

Console.ReadKey();
