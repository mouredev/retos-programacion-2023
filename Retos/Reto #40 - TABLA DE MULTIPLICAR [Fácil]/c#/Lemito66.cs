// See https://aka.ms/new-console-template for more information

void multiplicationTable(int number, int stop)
{
    for (int i = 0; i <= stop; i++)
    {
        Console.WriteLine($"{number} x {i} = {number * i}");
    }
}

multiplicationTable(5, 10);