// See https://aka.ms/new-console-template for more information



namespace reto0;
public class Reto0
{

    public static void Main(string[] args)
    {
        Enumerable.Range(1, 100).ToList().ForEach(x => { var fiz = x % 3 == 0 ? "Fizz" : null; var buzz = x % 5 == 0 ? "Buzz" : null; Console.WriteLine($"{fiz}{buzz}".Length == 0 ? x.ToString() : $"{fiz}{buzz}"); });
    }

}