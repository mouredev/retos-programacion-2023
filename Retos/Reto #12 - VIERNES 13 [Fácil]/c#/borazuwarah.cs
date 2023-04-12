/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

Console.WriteLine("Hello, World!");

Console.WriteLine(IsViernesTrece(2010, 1));
Console.WriteLine(IsViernesTrece(2010, 2));
Console.WriteLine(IsViernesTrece(2010, 3));
Console.WriteLine(IsViernesTrece(2010, 4));
Console.WriteLine(IsViernesTrece(2010, 5));
Console.WriteLine(IsViernesTrece(2010, 6));
Console.WriteLine(IsViernesTrece(2010, 7));
Console.WriteLine(IsViernesTrece(2010, 8));
Console.WriteLine(IsViernesTrece(2010, 9));
Console.WriteLine(IsViernesTrece(2010, 10));
Console.WriteLine(IsViernesTrece(2010, 11));
Console.WriteLine(IsViernesTrece(2010, 12));
Console.ReadLine();


static bool IsViernesTrece(int year, int month)
{
    DateOnly dt = new DateOnly(year, month, 13);
    
    if ((int)dt.DayOfWeek == 5)
        return true;
    else
        return false;
}