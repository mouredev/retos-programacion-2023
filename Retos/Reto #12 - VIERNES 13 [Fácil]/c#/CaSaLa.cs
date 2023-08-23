// See https://aka.ms/new-console-template for more information



using System.Text.RegularExpressions;

namespace reto12;
public class reto12
{
    
    public static void Main(string[] args)
    {
        TieneViernes13(1, 2023);
        TieneViernes13(10, 2023);
    }

    public static bool TieneViernes13(int mes, int año)
    {
        return new DateTime(año, mes, 13).DayOfWeek == DayOfWeek.Friday;
    }

}