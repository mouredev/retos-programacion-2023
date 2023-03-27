class miguelex
{
    static string isFridayThe13th(int month, int year)
    {
        DateTime date = new DateTime(year, month, 13);
        if (date.DayOfWeek == DayOfWeek.Friday)
            return "True";
        else
            return "False";
    }

    static void Main(string[] args)
    {
        Console.WriteLine("¿Hay viernes 13 en marzo de 2023? " + isFridayThe13th(3, 2023));
        Console.WriteLine("¿Hay viernes 13 en octubre de 2023? " + isFridayThe13th(10, 2023));
    }
}
