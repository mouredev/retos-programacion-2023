using System;

public class Program
{
	public static void Main()
	{
		Console.WriteLine($"Numero aleatorio: {Program.Random(50)}");
	}
	
	public static double Random(int limit){
		double rnd = DateTime.Now.Ticks%limit;
		return rnd;
	}
}