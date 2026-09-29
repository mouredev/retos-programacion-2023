/**
 * El Famoso Fizz Buzz, en una función reutilizable
 * @Metalex84
 *
**/

class Program
{
    static void Main()
    {
		for (int i = 1; i <= 100; i++)
		{
			Console.WriteLine(FizzBuzz(i));
		}
    }

    static string FizzBuzz(int n)
    {
		if (n % 3 == 0 && n % 5 == 0)
		{
			return "fizzbuzz";
		}
		else if (n % 3 == 0)
		{
			return "fizz";
		}
		else if (n % 5 == 0)
		{
			return "buzz";
		}
		else
		{
			return n.ToString();
		}
    }
}
