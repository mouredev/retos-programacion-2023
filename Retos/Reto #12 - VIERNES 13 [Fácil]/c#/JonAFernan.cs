namespace reto12;

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine(IsFriday13(2,2023));//False
        Console.WriteLine(IsFriday13(5,2022));//True
    }

    static bool IsFriday13(int month, int year)
    {
        DateTime dateToCheck = new DateTime(year, month, 13);

        return dateToCheck.DayOfWeek == DayOfWeek.Friday;
    }
}
