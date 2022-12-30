internal class Program
{
	static void Main(string[] args)
	{
		for (int i = 0; i < 100; i++)
		{
			int num = i + 1;

			if (num % 3 == 0 && num % 5 == 0)
			{
				Console.WriteLine("FizzBuzz");

			}
			else if (num % 5 == 0)
			{

				Console.WriteLine("Buzz");

			}
			else if (num % 3 == 0)
			{

				Console.WriteLine("Fizz");

			}
			else
			{
				Console.WriteLine(num);
			}
		}
	}
}
}