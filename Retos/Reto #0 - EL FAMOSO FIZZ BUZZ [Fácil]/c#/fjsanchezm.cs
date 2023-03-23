for (int i = 1; i <= 100; i++)
{
    if (i % 3 == 0 && i % 5 == 0)
    {
        Console.WriteLine(String.Format("Numero: {0} fizzbuzz", i));
    }
    else if (i % 3 == 0)
    {
        Console.WriteLine(String.Format("Numero: {0} fizz", i));
    }
    else if (i % 5 == 0)
    {
        Console.WriteLine(String.Format("Numero: {0} buzz", i));
    }
    else
    {
        Console.WriteLine("Numero: " + i);
    }
}