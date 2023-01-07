using System;

public class Program
{
	public static void Main(string[] args)
	{
		for (var i = 1; i <= 100; i++)
		{
			var mod = i % 15;
			if (mod == 0)
			{
				Console.WriteLine("fizzbuzz");
				continue;
			}

			mod = i % 5;
			if (mod == 0)
			{
				Console.WriteLine("buzz");
				continue;
			}

			mod = i % 3;
			if (mod == 0)
			{
				Console.WriteLine("fizz");
				continue;
			}

			Console.WriteLine(i);
		}
	}
}