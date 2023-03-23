using System;
					
public class Program
{
	public static void Main()
	{
		for (int numero = 1; numero <= 100; numero++) {
            if (numero % 3 == 0 && numero % 5 == 0) {
               Console.WriteLine("FizzBuzz");
            } else if (numero % 3 == 0) {
               Console.WriteLine("Fizz");
            } else if (numero % 5 == 0) {
               Console.WriteLine("Buzz");
            } else {
               Console.WriteLine(numero);
            }
		}
	}
}